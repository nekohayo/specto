# Introduction #

As written in a [rant](http://pascal.lecomplet.ca/?p=3) (fr) I would like to code a XML parser for specto. But first, let's see what needs to be modified.

# Details #

I put the headers of the code here, so we can discuss about it.

```
class Watch_io:
    def __init__(self, specto, file_name):
```
> Pascal: It creates the file if it is not existing.
> It also checks if the file is a valid INI one (but not in a 100% sure way).

```
    def read_all_watches(self, startup=False):
        """
        Read the watch options from the config file
        and return a dictionary containing the info needed to start the watches.
        """
```
> Pascal: Just like the doc says. Basically a for loop calling **read\_watch** each time.

```
    def read_watch(self,name, startup=False):
        """
        Read the watch options from one watch.
        """
```
> Pascal: Creates an option dict, and put the options inside, using **read\_option** each time.

```
    def read_option(self, name, option, startup=False):
        """ Read one option from a watch """
```
> Pascal: Returns one option from the file at a time. We could write the code to verify the options here, or just take this method out of the code.

```
    def write_watch(self, values):
        """
        Write or change the watch options in a configuration file.
        Values has to be a dictionary with the name from the options and the value. example: { 'name':'value', 'interval':'value' }
        If the name is not found, a new watch will be added, else the excisting watch will be changed.
        """
```
> Pascal: So many _try/except_ in this part of the code! Here, we read the file once again. That can be taken out. I also think that if the name of the watch is not found, it should not create a new watch, but raise an exception.

```
    def write_option(self, name, option, value):
```
> Pascal : Here, 50 % of the code is in a **try/except/else** statement. We could also take this out, and create a class for options. Or, instead of having a special class for options, we should at least make it that there is no writing involved directly here in the xml file.

```
    def remove_keyring(self, name):
```
> Pascal: This has nothing to do with the ini or the xml, only with the keyring manager, so we don't need to touch it.

```
    def remove_watch(self, name):
        """ Remove a watch from the configuration file. """
```

> Pascal: Just some rewriting to do.

```
    def is_unique_watch(self, name):
        """
        Returns True if the watch is found in the file.
        """
```

> Pascal: The same code that is here is rewritten in multiple other method. Perhaps we should make them call here.

```
    def replace_name(self, name, new_name):
        """ Replace a watch name (rename). """
```

> Pascal: This method will be easily replaced. However, I think it should check if the watch already exists before renaming it.

```
    def hide_brackets(self,name):
```

> Pascal: This will be avoidable, and I think we will be able to take it out of the code

```
    def show_brackets(self,name):
```

> Pascal: Same here.

```
    def encode_password(self, name, password):
```

> Pascal: Nothing to do with ini nor xml, pass along.

```
    def decode_password(self, name, password):
```

> Pascal: Nothing to see here too.

```
    def check_old_version(self, type):
```

> Pascal: Yes, that will be good, we'll be able to (and I think we should) give version numbers to the file.

## Other Ideas ? ##
I think there are some things to rewrite, and some methods have to be redefined. Do you have any thing you would like to be added in this code?
And if you are not a developer, but only a user of specto, is there some things you would like to see in the Watch list Database? I know it's really a backend thing, but if you have any ideas, feel free to write yours here.