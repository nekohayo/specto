If you see a missing word and would like it to be included, please add it at the end, in the "unknown terms" section.

# Generic terms #
  * Watch: This is the "object" that checks a target for updates at a regular time interval. In the case of a "mail watch", for example, a watch could check for new emails every hour.
  * Refresh Interval: Time span between each watch checks. For example, a refresh interval of 3600 (60 minutes) means that the watch will check the content for updates, wait 60 minutes, and check again. It is recommended that you set a reasonable amount of time between watch checks, in order to save bandwidth and prevent content providers from saying nasty words.
  * Error Margin: The maximum filesize difference (in percent) that a webpage can have until it is considered as "updated"
  * URL: A Uniform Resource Locator (URL) is a string of characters conforming to a standardized format, which refers to a resource on the Internet (such as a document or an image) by its location. For example, the URL of this page is [Terminology](Terminology.md). An HTTP URL, commonly called a web address, is usually shown in the address bar of a web browser. **In the notifier window's watch information pane, we refer to it as _location_.**
  * Notifier: Specto's main window, that is, the one that contains the list of the watches and allows managing them.
  * Debug Mode: A special operation mode of Specto that allows getting more information in order to help detecting bugs.
  * Bug: A software bug is an error, flaw, mistake, failure, or fault in a computer program that prevents it from working as intended, or produces an incorrect result. As a user, if you experience weird behavior from Specto, it may be that you found a bug. You should [report it](http://code.google.com/p/specto/issues/list) so that we know of its existence, if it has not already been reported by someone else.
  * Notification icon: the icon that shows in the panel's notification area. This is not called a "tray icon".
  * Balloons: the notification bubbles/toasts that appear, attached to the notification icon in the panel's notification area


# Watch statuses #
  * idle: the watch is not marked as having unread items, and is not doing anything (translator hint synonyms: idle/sleep/ready)
  * checking: the watch is busy checking for updates (translator hint synonyms: checking/refreshing). This was previously called "updating".
  * changed: the watch has new unread items that have not yet been "marked as read" by the user.
  * error: the watch encountered an error?

## Additional notes ##
"checking" was previously called "updating", and "changed" was previously called "updated". These previous terms were terribly confusing, because they ended up creating messages where you are not 100% sure if it means the watch has "finished checking" or if it means that it "finished checking and has detected changes". It also made the code much harder to understand, since you're never entirely sure that the ones who wrote it were not drunk that day :)

When a watch goes through the checking process successfully (status != "error") but does not have new unread items (status != "changed"), do NOT use the wording "updated" or "finished updating" or anything like that, because it induces confusion. Instead, say that the watch is now "idle".
Basically, these are the possible paths a watch can take:
  * idle --> checking --> idle.
  * idle --> checking --> changed --> [marks the watch as read](user.md) --> idle.

# Unknown terms #
None