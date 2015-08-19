# Running from the terminal #
This is the first step towards understanding what is the problem. For example, if Specto crashes, you will usually have information related to the crash sent to your terminal window before Specto quits. Without a terminal, applications do not output as much information as they can when problems occur. If you don't know how to open a terminal window... Well I suggest you talk with your system administrator.

# Activating the debug mode #
Normally, Specto does not output a lot information to the user. When this mode is activated, you will receive a tsunami of information when you run Specto from a terminal.
  1. Start Specto
  1. Open the preferences window (either using the notifier window's **Edit** menu, or by right clicking the tray icon and choosing **Preferences**)
  1. Activate the checkbox "Enable Debug Mode"

## Activating the debug mode manually ##
If, for some reason, you cannot access the preferences window or Specto refuses to start, you can activate the debug mode with this command:
```
gconftool-2 --set --type boolean /apps/specto/preferences/debug_mode true
```

# Getting logs #
While the debug mode is active, Specto outputs a lot of information into a debugging log, in the ~/.specto/ folder. This log is called specto.log, but you do not need to go fetch it manually everytime. Specto has a log viewer window. Just open the **notifier window**, click the **View menu**, and select **Error Log**. You will have the ability to save that log.

# Providing information #
Here is a small non-exhaustive list of infos that you can provide about your system when contacting us for help:
  * Your specto.log and error.log, found in ~/.config/specto
  * Linux distribution
  * Python and PyGTK version
  * Your watches.list in ~/.config/specto/ ; however, do **not** ever provide your watches.list if you are not using GNOME keyring encryption (Specto 0.3 and newer), otherwise this file can contain passwords. In all cases, we recommend that you check this file before submitting it. Be careful when pasting information to public places (such as [pastebin](http://www.pastebin.ca)), make sure there are no passwords in there.
  * Anything else you find relevant

# Filing bugs #
Reporting software bugs is an important process of making it better. Free and Open Source software depends on the fact that the community can help (not replace ;) the developers finding bugs in the software. If you notice a strange behavior or experience a crash, please take a few minutes of your time to tell us about it. To do that, you should
  1. Create a google/gmail account if you don't have one already (it's free and easy)
  1. Check the [bug list](http://code.google.com/p/specto/issues/list)
  1. Search and see if your bug has already been reported, including in the [already fixed bugs](http://code.google.com/p/specto/issues/list?can=1&q=&colspec=ID+Type+Status+Priority+Summary+Milestone+Stars+DevBranch&cells=tiles) using the search feature
  1. If not, file a [new bug](http://code.google.com/p/specto/issues/entry)