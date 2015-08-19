# Indentation #
You must use **four (4) spaces instead of tabs** to indent the code. Proper and consistent indentation in Python is crucial.

# PEP-8 style compliance #
All your patches and commits should be conforming to the Python PEP-8 style guide: http://www.python.org/dev/peps/pep-0008/
The exception is for line lengths. We don't require lines to be wrapped at 79 columns. They are smoking crack.
To check the code for compliance, install python-pep8 and run it with the "--ignore=E501" parameter, like so:
```
pep8 "spectlib/" --repeat --ignore=E501
pep8 "spectlib/tools" --repeat --ignore=E501
pep8 "spectlib/plugins" --repeat --ignore=E501
```

# Comments and documentation #
Try to comment as much as possible, meaning that you should add comments for anything that you feel might be confusing for others, to document special workarounds, etc. Normal comments use the # symbol before the comment (see also the PEP-8 guidelines on how to do spacing around it). When you feel some feature needs to be added, add #TODO: before the comment. When you see or predict a bug in a certain area, use the #FIXME: comment style instead. Do not forget to actually file an [issue](http://code.google.com/p/specto/issues/list) about it.

See also: [Terminology](Terminology.md)

# The code must remain anonymous #
Do not sign your name or nickname at the top of the code or inside the code. This is a community rule, for the following reasons:
  * signatures quickly become irrelevant (as an example here: a developer that no longer maintains any modules, and has not touched the code/project for over a year)
  * they _scare people off_ because they look like a territory mark; when someone is about to modify that code (be that a new contributor or a veteran), that contributor will certainly feel _"am I stepping on somebody's toes? maybe I'm not supposed to touch this? what if I awaken the Mummy?"_
  * that signature gives no idea of the _size of the contribution_ that person did, or the amount of code you need to (re)write to get your name on a file
Instead, your name can go in the AUTHORS file when you commit some significant changes. If you don't have the means/will to make your own branch and are providing a patch, we will be committing your patch and mentionning your name using the "--author" feature of Bazaar.

# Do not make modules talk to others directly #
In specto, everything is managed by main.py. As it is the central module, you must use it if you need to communicate to other modules. Main.py is the one who must do the job, NOT your specific module. For example, if we have dish.py who feels it needs to be washed, it must not ask dishwasher.py to be washed. It must ask main.py, which in turn will ask dishwasher.py to do the washing.
# Encoding #
The default encoding for all documents is UTF-8. In a Python file, this is done with a line like this at the top:
```
# -*- coding: utf-8 -*-
```

# Do not break Main #
The specto-main development branch is intended as a "stable" development branch. Only small and carefully tested bug fixes should be committed directly to it. Long-duration development is to be done in individual branches, which will be merged periodically or on request when they have been heavily tested and found to cause no regressions compared to Main. Thus, one can work on refactoring, or a new incomplete feature, in a separate bazaar branch, without breaking the stability of Specto's main development branch for the users who depend on it.
Also, in normal circumstances, you should start your individual branch by "branching" off from specto-main, and merge only from main instead of other individual branches.