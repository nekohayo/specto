# Who you are dealing with #
Specto is a project based on volunteering (until we get rich by world domination because of the widespread use of Specto). That means that when contributing, you must be willing to make that will be readable by others, by following these few guidelines to keep things smooth.
## Communicating ##
There are some ways you can use to communicate: the primary means of communicating is by the mailing list: http://groups.google.com/group/specto

## The importance of knowing what each other does ##
As a project progresses, things can get pretty sticky. Kind of like the random (/b/) board on 4chan, without the sauce. In order to minimize confusion, everytime you wish to start hacking on a specific part of Specto, assign it to yourself if it's a [bug or feature request](http://code.google.com/p/specto/issues/list). This way, everyone knows what you are up to, and can avoid touching a particular module if the changes are too significant, or, if you request help, may come over and help. We recommend a rainy Saturday night and good music.

In addition to assigning the task to yourself, you should ask the other developpers on jabber or in the google group.

# Ways of contributing #
  * Hacking code
  * Filing bug reports ("issues")
  * Writing documentation and keeping this wiki up to date for developers
  * [Translating](Translating.md) Specto into your language
  * Suggesting brilliant cracktastic ideas

## How to contribute code with a patch ##
You modified your bzr version of Specto and want to send us the changes? Great, here is how you can make a simple patch. In the root folder of your Specto branch:
`bzr diff > my_changes.patch`
You can then attach this patch to an [issue](http://code.google.com/p/specto/issues/list) or email it, or print it out on paper and come running at our doorstep early in the morning!

To merge a patch with your working branch of Specto, most of the time, a simple
`bzr patch his_changes.patch`
...will do. If you are not using bazaar or if you like pain, you can also use the "patch" command:
`patch -p0 < his_changes.patch`
Note that p0 is an indicator of the _directory level_. For example, "_patch -p1 < foo.patch_": the number behind "p" might vary, depending on the patch, and the directory you are in when you are applying the patch. So, to figure out what the number must be, you must actually look at the patch. The "p" number strips X directories from the path listed in the patch.


# Tools of the Trade #
Of course, you are absolutely free to use whatever you want to help Specto, but here are just a few hints of software we recommend if you have no idea what you should use.
  * A computer running Linux, with all the dependencies satisfied
  * bzr (Bazaar) for access to the latest version at any time
  * A text editor for coding (Gedit, Bluefish, SPE, whatever)
  * Meld for viewing changes between files of different versions. Very useful, and has a feature to work with bzr.
  * A Google account if you want to manage bugs in the issue tracker
  * A Launchpad account if you want to host your own bazaar branch of the code on https://code.launchpad.net/specto