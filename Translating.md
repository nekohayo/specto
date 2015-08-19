Translating the .po files directly and sending them by email to **nekohayo [a](a.md) gmail.com** is preferred.

Here is a short guide to translating under Linux, it is here as a "quick reference" or reminder for people like Kiddo who always forget.

You will need:
  * specto
  * a good efficiency in your language - it is not encouraged to translate if it is not in your mother tongue
  * a .po file editor. We recommend [poedit](http://www.poedit.org), but you are free to use whatever suits you. poedit will most likely be available from your distribution packages. For example, ubuntu users can easily install "poedit" with synaptic.

This guide will assume you are using the development (Bazaar) version of Specto.

  1. recreate the template file by executing the script called **generate\_template.py** in the **po** folder
  1. if your language does not exist yet, create a subfolder in po/ (such as po/fr for French)
  1. open specto.pot with your translation tool (ex.: poedit)
  1. you will now be able to create a .po file that you can put in your directory (for example, po/fr/specto.po)
  1. translate and save your work
  1. poedit automatically creates a .mo file besides the .po file
  1. edit setup.py and find the line where it says i18n\_languages = _something_. Add your locale code (fr for French, de for German, it for Italian, etc) to the list
  1. run installation script again: **sudo python setup.py install**

If your language already exists in Specto and you want to translate new strings that were added:
  1. run **generate\_template.py** in the **po** folder
  1. open your .po file (such as po/fr/specto.po), and tell your translation software to update from the .pot template file (poedit has this in the Catalog menu).
  1. translate, save, reinstall.