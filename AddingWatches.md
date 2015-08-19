In order to add a watch, you need to start Specto and open the notifier window. If there is no window called "notifications" open already, you can open it by clicking the Specto tray icon.

Once this window is open, you can click the "add" button in the toolbar, or in the "Edit" menu. A submenu will appear, allowing you to choose what type of watch you want to add:

  * Email: checks for unread mail
  * System
    * Folder: notifies when the folder has new/modified/deleted contents
    * File: notifies when the file is modified
    * Port: notifies when an application starts/stop using a socket
    * Process: notifies when the process with a matching name starts or stop
  * Version control
    * Bazaar: checks a Bazaar-controlled folder on your system and compares it to itself and to its parent (remote) branch. This is useful if you want to know when your local copy of a branch is outdated, or when you have a local repository into which others "push". This watch's behavior is roughly equal to the command "bzr missing".
  * Social networks
    * Facebook: notifies you of private messages, wall posts, notifications and requests in your Facebook account
  * Internet
    * Google Reader: checks for unread items in your Google Reader account
    * Website or RSS feed: Specto will watch a web page or web feed, and notify you when it has been updated

When you select the desired watch type, a new dialog will appear, allowing you to configure the watch you want to create.

# Name #
This is only a unique name that you must give to your "watch", in order to identify it easily. Specto will often refer to this watch with that name. Try to keep it short.

# Refresh Interval #
The amount of time Specto must wait before checking for updates on the watch. In addition to the refresh "number", you must specify which time unit the watch must use (seconds, minutes, hours, days).

It is strongly recommended to **set the refresh interval to a reasonably high value**. There are a few good reasons to do this:
  * Save processing power and network bandwidth
  * Prevent from being [blacklisted](http://en.wikipedia.org/wiki/Blacklist) by content providers, which could consider your requests as a [DoS attack](http://en.wikipedia.org/wiki/Denial_of_Service).
  * Keeps you concentrated on working instead of staring at Specto all the time :)

# Error Margin #
Certain watch types (such as websites) have a special mechanism we call the Mighty **Error Margin**. What it does is that it sets the minimum filesize difference (in percentage) before a watch will be considered as "updated". This feature is important for websites for example, because a lot of them use advertising content, fooling Specto into thinking they were updated. Usually, a 2% error margin seems correct, but you can fine-tune it later using the watch editing dialog.

# Finishing the process #
When you click the "add" button, the watch will be added to Specto's watch list, shown in the notifier window, and will start checking for updates. To remove it from the database, see RemovingWatches.

## How do I know it works? ##
If you want to make sure that Specto works for watching websites, you can use this test page that changes randomly: randize.com

# Hidden watch settings #
Some watches have special settings that can only be set by editing the ~/.config/specto/watches.list file manually. These are settings that most users would not need or that are not practical to implement in the user interface.
  * Setting a port for mail watches ([issue #128](https://code.google.com/p/specto/issues/detail?id=#128)): add 'port = 323' to your watch config
  * Allow checking a specific IMAP folder ([issue #136](https://code.google.com/p/specto/issues/detail?id=#136)): add 'folder = something' to your watch config
  * To (dis)allow URL redirects on a per-watch basis ([issue #146](https://code.google.com/p/specto/issues/detail?id=#146)): add "redirect = True". This overrides the gconf key "follow\_website\_redirects".

It is possible to reuse some of Specto's variables inside your custom commands. If you add the following variables in the "custom open command" or "custom changed command" fields in a watch's settings, they will be replaced by the value in Specto:
  * %information = the information that is displayed in the balloon message
  * %extra\_information = the information displayed in the "extra information" tab
  * %name = the name from the watch
  * %last\_changed = the date and time the watch was last changed

An example would be: "/usr/bin/mycommand %name %last\_changed"

# Hidden global settings #
You can use gconf-editor and navigate to /apps/specto to reveal some more settings, such as the hidden gconf key, "follow\_website\_redirects" ([Issue #58](https://code.google.com/p/specto/issues/detail?id=#58)).

# Does Specto support proxies? #
Yes. Watches that use the network will (normally) use your GNOME proxy settings automatically.