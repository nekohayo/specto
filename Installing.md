Installing Specto is usually an easy process if you have a Ph.D in rocket science, but this can vary wildly depending on a range of factors such as your Linux distribution, the availability of Specto for your distribution, and the number of cats in 4chan.

# Official packages and tarballs #
These are the "release" packages. You can find them in our [download section](http://code.google.com/p/specto/downloads/list). Useful if your distribution provides no packages for Specto, or if their packages are too old for your taste.

# Linux Distributions that provide Specto #
Take note that distribution packages might not always be up to date, and may contain bugs that are fixed in newer versions (or development versions).
If you are a package maintainer and would like to package Specto, please edit this page (if you are a project member) or send an email to the Group to add your distribution to this list.
  * [Fedora](http://fedora.redhat.com)
  * [Frugalware Linux](http://frugalware.org)
  * [Debian GNU/Linux](http://debian.org) (in testing and unstable)
  * [Ubuntu Linux](http://www.ubuntu.com) (in universe since 7.04)
  * [OpenSuse](http://opensuse.org)

# Getting Specto from Bazaar (bzr) #
If you want to take a look at all the branches related to Specto (some of which could be made by third parties), visit our [launchpad bazaar branches page](https://code.launchpad.net/specto).

To get the official main development branch (named specto-main), grab it with this command:
```
bzr branch lp:specto
```

Note that **the SVN version of Specto on google code hosting is deprecated** and should not be used.

You may want to **keep your bzr version of Specto updated** from time to time. Assuming you are in the directory where you keep the Specto bzr trunk (specto-main):
```
bzr pull
```

# Running or installing from a tarball or a bzr branch #
After extracting the contents of a tarball, you will notice Specto has a bunch of files and folders. Before doing anything remotely productive, you need to make sure you fill the dependencies to make Specto work.

## Dependencies ##
This is the most current list of required software packages needed to compile Specto. The items in bold are the ones you are most likely to need to install, the rest is usually already present in most distributions. These dependencies are only relevant to the development version of Specto (older versions may have different dependencies).
  * bzr (for the bazaar watch plugin, or if you want to grab Specto from a bazaar branch)
  * gnome-icon-theme?
  * libgnome-keyring0
  * librsvg2-common
  * python
  * python-central
  * python-dbus (optional, for DBUS-dependent watches)
  * python-dev (if you run the development version with setup.py)
  * python-gconf
  * python-gst0.10 (optional, for sounds)
  * python-gtk2 (_version 2.10 or higher;_ this also means you need GTK+2.10 or newer)
  * python-indicate (optional, for integration with Ubuntu's "indicator applet")
  * python-numpy (recent versions of pygtk packages don't include it by default)
  * python-libxml2
  * python-notify and python-dbus (to allow libnotify "balloons")
  * python-svn (optional, for the Subversion watch)
  * xdg-utils

---


What to do now that you took care of those dependencies? Don't panic. There are two options: running specto locally or installing it system-wide.

To run specto without installing it: just run the script
```
launch.sh
```

To install specto system-wide (do this if you have multiple users doing it, if you are a package maintainer or if you want the translations to work). You need to run the setup script as a super-user. Do this in the folder where you extracted Specto:
```
python setup.py build
sudo python setup.py install
```

You can then run specto by typing "specto" and pressing enter in a terminal, or look in your GNOME applications menu, there should be an entry for Specto in the "accessories" submenu.

If you need to uninstall the version you installed with setup.py, simply run `sudo python setup.py uninstall`.