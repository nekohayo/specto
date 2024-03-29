# -*- coding: UTF8 -*-

# Specto , Unobtrusive event notifier
#
#       balloons.py
#
# Copyright (c) 2005-2007, Jean-François Fortin Tam

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

import pygtk
pygtk.require('2.0')
import pynotify
import sys
import gtk
import spectlib.util

from spectlib import logger
from spectlib.i18n import _

notifyInitialized = False

class NotificationToast:
    _notifyRealm = 'Specto'
    _Urgencies = {
        'low': pynotify.URGENCY_LOW,
        'critical': pynotify.URGENCY_CRITICAL,
        'normal': pynotify.URGENCY_NORMAL
        }

    def __open_watch(self, n, action, id):
        if self.specto.notifier.open_watch(id):
            self.specto.notifier.clear_watch('',id)

    # I'd love to have a default icon. #Kiddo: which one? Not sure this is a really good thing. Unless we show the Specto logo?
    def __init__(self, specto, body, icon=None, x=0, y=0, urgency="low", summary=_notifyRealm, name=None):
        global notifyInitialized

        if not notifyInitialized:
           pynotify.init(self._notifyRealm)
           notifyInitialized = True

        self.specto=specto
        self.toast = pynotify.Notification(summary, body)
        self.timeout = specto.specto_gconf.get_entry("pop_toast_duration")*1000
        if self.timeout:
            self.toast.set_timeout(self.timeout)
        if name:
            #If name is not None and exists in specto.watch_db, a button is added to the notification
            w = self.specto.find_watch(name)
            if w != -1:
                self.toast.add_action("clicked", gtk.stock_lookup(gtk.STOCK_JUMP_TO)[1].replace('_', ''), self.__open_watch, w)
        self.toast.set_urgency(self._Urgencies[urgency])
        if icon:
            #self.toast.set_property('icon-name', icon)#we now use a pixbuf in the line below to allow themable icons
            self.toast.set_icon_from_pixbuf(icon)
            
        if x!=0 and y!=0:#grab the x and y position of the tray icon and make the balloon emerge from it
            self.toast.set_hint("x", x)
            self.toast.set_hint("y", y)
        
        if not self.toast.show():
            specto.logger.log("Can't send Notification message. Check your DBUS!", "error", self.__class__)
