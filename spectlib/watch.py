#!/usr/bin/env python
# -*- coding: UTF8 -*-

# Specto , Unobtrusive event notifier
#
#       watch.py
#
# Copyright (c) 2005-2007, Jean-François Fortin Tam
# This module code is maintained by : Pascal Potvin, Jean-François Fortin and Wout Clymans

# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public
# License along with this program; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place - Suite 330,
# Boston, MA 02111-1307, USA.

# The Watcher : this file should give a class intended for subclassing. It should give all the basic methods.
import os, sys
import gobject
import gnome

#specto imports
from spectlib.specto_gconf import GConfClient
from spectlib.iniparser import ini_namespace
from ConfigParser import ConfigParser
from spectlib import i18n
from spectlib.i18n import _

def gettext_noop(s):
   return s

class Watch:
    """
    The watch superclass. All the base functions are written here.
    """
    def __init__(self, specto):
        self.refresh = int(5000)
        self.name = "default"
        self.specto = specto
        self.timer_id = -1
        gnome.sound_init('localhost')
        global _
        
    def update(self):
        """
        Check if an error sound has to be played or if a watch has to be flagged updated.
        """
        #play error sound
        conf = GConfClient("/apps/specto/preferences")
        if self.error == True and conf.get_entry("/use_problem_sound", "boolean"):
            problem_sound = conf.get_entry("/problem_sound", "string")
            gnome.sound_play(problem_sound)
        
        #call update function if watch was updated
        if self.updated == True:
            self.notify()
            self.specto.toggle_updated(self.id) #call the main function to update the notifier entrie
        self.timer_id = gobject.timeout_add(self.refresh, self.update)

    def notify(self):
        """
        Notify the user when a watch was updated.
        """
        global _
        if self.specto.DEBUG or not self.specto.GTK:
            self.specto.logger.log(_("Watch \"%s\" updated!") % self.name, "info", self.__class__)

        #determine if libnotify and/or sound support is to be used
        conf = GConfClient("/apps/specto/preferences")
        pop_toast = conf.get_entry("/pop_toast", "boolean")
        
        #play a sound   
        update_sound = conf.get_entry("/update_sound", "string")
        if conf.get_entry("/use_update_sound", "boolean"):
            gnome.sound_play(update_sound)
        
        if (pop_toast == True) and (self.specto.GTK):
            from spectlib.balloons import NotificationToast

            if self.type==0:#web
                NotificationToast(self.specto, _("The website, <b>%s</b>, has been updated.") % str(self.name), self.specto.PATH + "icons/notifier/big/web.png" )
            elif self.type==1:#email

                if self.prot!=2:#other account than gmail
                    notification_toast = _("Your email account, <b>%s</b>, has new mail.") % str(self.name)
                elif self.prot==2:#gmail
                    gettext = _
                    _ = gettext_noop
                    notification_toast = i18n._translation.ungettext(\
                        # English singular form:
                        _("Your email account, <b>%s</b>, has <b>%d</b> new mail.") % (self.name, self.newMsg-self.oldMsg),\
                        # English plural form:
                        _("Your email account, <b>%s</b>, has <b>%d</b> new unread mails, totalling %s") % (self.name, self.newMsg-self.oldMsg, self.newMsg),\
                        self.newMsg-self.oldMsg)
                    _ = gettext
                    
                    if (self.newMsg - self.oldMsg >1):
                        self.oldMsg = self.newMsg#store temporarily the number of old messages to prevent false alerts
                    elif (self.newMsg - self.oldMsg == 1):
                        self.oldMsg = self.newMsg#store temporarily the number of old messages to prevent false alerts
                    else:
                        notification_toast = None#nothing to notify the user about.

                if notification_toast:
                    NotificationToast(self.specto, notification_toast, self.specto.PATH + "icons/notifier/big/mail.png" )

            elif self.type==2:#folder
                NotificationToast(self.specto, _("The file/folder, <b>%s</b>, has been updated.") % self.name, self.specto.PATH + "icons/notifier/big/folder.png" )
            else:
                self.specto.logger.log(_("Not implemented yet"), "warning", self.__class__)#TODO: implement other notifications
            #end of the libnotify madness

    def stop_watch(self):
        """ Stop the watch. """
        gobject.source_remove(self.timer_id)

    def set_name(self, name):
        """ Set the name. """
        self.name = name

    def get_name(self):
        """ Return the name. """
        return self.name

    def get_type(self):
        """ Return the type. """
        return self.type
    
    def set_refresh(self, refresh):
        """ Set the refresh value. """
        self.refresh = refresh
        

class Watch_io:
    """
    A class for managing watches.
    """
    
    def __init__(self):
        #read the watch from ~/.specto/watches.list using the iniparser module
        self.file_name = os.environ['HOME'] + "/.specto/" + "watches.list"
        if not os.path.exists(self.file_name):
            f = open(self.file_name, "w")
            f.close()
        os.chmod(self.file_name, 0600)#This is important for security purposes, we make the file read-write to the owner only, otherwise everyone can read passwords.
        self.cfg = ini_namespace(file(self.file_name))

    def read_options(self):
        """
        Read the watch options from the config file ( ~/.specto/watches.list ),
        and return a dictionary containing the info needed to start the watches.
        """
        watch_value_db = {}
        options = {}

        names = self.cfg._sections.keys()
        i = 0
        for name_ in names:
            watch_options = {}
            options = {}
            options = self.cfg._sections[name_]._options.keys()

            for options_ in options:
                watch_options_ = { options_: self.cfg[name_][options_] }
                watch_options.update(watch_options_)
            values = {}
            values['name'] = name_
            values['type'] = int(watch_options['type'])
            del watch_options['type'] #delete the standard options from the dictionary with extra arguments because we allready saved them in the line above
            values['refresh'] = int(watch_options['refresh'])
            del watch_options['refresh']

            if int(values['type']) == 0:
                values['uri'] = watch_options['uri']
                values['error_margin'] = watch_options['error_margin']

            elif int(values['type']) == 1:
                values['prot'] = watch_options['prot']
                if int(values['prot']) != 2:
                    values['host'] = watch_options['host']
                    values['ssl'] = watch_options['ssl']
                values['username'] = watch_options['username']
                values['password'] = watch_options['password']
            elif int(values['type']) == 2:
                values['file'] = watch_options['file']
                values['mode'] = watch_options['mode']
                
            try:
                if watch_options['updated'] == "True":
                    values['updated'] = True
                else:
                    values['updated'] = False
            except:
                values['updated'] = False
                
            try:
                if watch_options['active'] == "True":
                    values['active'] = True
                else:
                    values['active'] = False
            except:
                values['active'] = True
                
            try:
                if watch_options['last_updated']:
                    values['last_updated'] = watch_options['last_updated']
            except:
                values['last_updated'] = _("No updates yet.")

            #if we want to create a watch, set create to True
            watch_value_db[i] = values
            del values
            i += 1
        return watch_value_db

    def read_option(self, name, option):
        """ Read one option from a watch. """
        try:
            return self.cfg[name][option]
        except:
            return 0

    def write_options(self, values):
        """
        Write or change the watch options in a configuration file.
        Values has to be a dictionary with the name from the options and the value. example: { 'name':'value', 'name':'value' }
        If the name is not found, a new watch will be added, else the excisting watch will be changed.
        """
        self.cfg = ini_namespace(file(self.file_name))
        name = values['name']

        if not self.cfg._sections.has_key(name):
            self.cfg.new_namespace(name) #add a new watch

        del values['name']
        for option, value  in values.iteritems():
            self.cfg[name][option] = value

        f = open(self.file_name, "w")
        f.write(str(self.cfg).strip()) #write the new configuration file
        f.close()

    def remove_watch(self, name):
        """ Remove a watch from the configuration file. """
        cfgpr = ConfigParser()
        cfgpr.read(self.file_name)
        cfgpr.remove_section(name)
        f = open(self.file_name, "w")
        cfgpr.write(f)
        f.close()
        
    def search_watch(self, name):
        """
        Returns True if the watch is found in ~/.specto/watches.list.
        """
        self.cfg = ini_namespace(file(self.file_name))
        if not self.cfg._sections.has_key(name):
            return False
        else:
            return True
        
    def replace_name(self, orig, new):
        """ Replace a watch name (rename). """
        #read the file
        f = open(self.file_name, "r")
        text = f.read()
        f.close
        text = text.replace("[" + orig + "]", "[" + new + "]")
        
        #replace and write file
        f = open(self.file_name, "w")
        f.write(text)
        f.close()
        
