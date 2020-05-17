[![tests](https://github.com/loiccoyle/myopy/workflows/tests/badge.svg)](https://github.com/loiccoyle/myopy/actions) [![pypi](https://img.shields.io/pypi/v/myopy)](https://pypi.org/project/myopy/)

# myopy

> Run blind python files.

This single class package, provides python objects to a python file at run time. This is ideal for configuration files where the user does not need to know where an object comes from or how to initialize it. It allows the python file to be blind to the origin of it's objects, removing the need for imports, object initializations or convoluted subclassing.

This is pretty much a standalone clone of the way the amazing [qutebrowser](https://github.com/qutebrowser/qutebrowser) handles it's config files.

Feel free to copy paste the `PyFile` class if you don't want the added dependency.

# Installation
```
pip install myopy
```

# Usage

Say you want to allow the user to change a `dict` containing some settings for an application in a configuration file called `config.py`:

In the application you would have something along the lines of:

```python
from myopy import PyFile

user_dict = {'something': 2}

config = PyFile('path/to/config.py')
# we provide the config file the user_dict in the 'settings' variable
config.provide(settings=user_dict)
module = config.run()  # returns a module object
print('after running config: ', user_dict)
print('module: ', module)
```
And in the user facing `config.py`, the `user_dict` object would be provided in the `settings` variable, and the user can change its values at will:
```python
print('in config: ', settings)
settings['something_else'] = 4
settings['something'] = 3
```

The output would be:
```
in config: {'something': 2}
after running config: {'something': 3, 'something_else': 4}
module: <module 'config' from 'path/to/config.py'>
```
the `user_dict` is modified in place.

