import os
import sys
import typing
from contextlib import contextmanager
from pathlib import Path


# from qutebrowser configfiles.py
@contextmanager
def saved_sys_properties() -> typing.Iterator[None]:
    """Save various sys properties such as sys.path and sys.modules."""
    old_cwd = Path.cwd()
    old_path = sys.path.copy()
    old_modules = sys.modules.copy()

    try:
        yield
    finally:
        sys.path = old_path
        for module in set(sys.modules).difference(old_modules):
            del sys.modules[module]
        os.chdir(old_cwd)

