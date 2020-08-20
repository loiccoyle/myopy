import logging
import os
import sys
import typing
from pathlib import Path
from types import CodeType, ModuleType

from .utils import saved_sys_properties


class PyFile:
    def __init__(self, file_path: Path, raising: bool = True, verbose: bool = True):
        """Python file handler. Makes python objects accessible to the python
        file, compiles and runs it.

        Parameters:
            file_path: python file.
            verbose: If True, will print any compilation/runtime exception.
            raising: If True, will raise any compilation/runtime exception.
        """
        self.file_path = Path(file_path)
        self.module = self._init_module()
        self._raising = raising
        self._verbose = verbose
        self._log = logging.getLogger(__name__)

    def _init_module(self):
        module = ModuleType(self.file_path.stem)
        module.__file__ = str(self.file_path)
        return module

    def provide(self, **attr_obj):
        """Provide objects to the python file.

        Parameters:
            **attr_obj: attribute name and python object.

        Examples:
            To provide a float 1.5 to the variable "NUMBER" of "python_file.py"
            >>> pf = PyFile("python_file.py")
            >>> pf.provide(NUMBER=1.5)
        """
        for attr, obj in attr_obj.items():
            self._provide(attr, obj)

    def _provide(self, attr: str, obj: typing.Any):
        """Provide 'obj' to the python file as 'attr'.

        Parameters:
            attr: name of the attribute in which to provide 'obj' to the python
                file.
            obj: object to provide.
        """
        setattr(self.module, attr, obj)
        self._log.debug(f'Providing "{obj}" to "{self.file_path}" as "{attr}".')

    def _compile(self) -> CodeType:
        """Compile python file.
        """
        with self.file_path.open("r") as f:
            source_code = f.read()
        ast = compile(source_code, self.file_path, "exec")
        return ast

    def _run(self, ast: CodeType):
        """Run python file.

        Parameters:
            ast: compiled python code.
        """
        with saved_sys_properties():
            config_dir = str(self.file_path.parent.resolve())
            if config_dir not in sys.path:
                sys.path.insert(0, config_dir)
            os.chdir(config_dir)
            exec(ast, self.module.__dict__)

    def _maybe_print_maybe_raise(
        self, func: typing.Callable, prefix: str = ""
    ) -> typing.Any:
        try:
            return func()
        except Exception as e:
            if self._verbose:
                self._log.error(prefix + str(e))
            if self._raising:
                raise e

    def run(self) -> ModuleType:
        """Compile and run python file, with access to the provided objects.

        Returns:
            module: module of the python file.
        """
        ast = self._maybe_print_maybe_raise(
            self._compile, prefix=f'Error at compilation in "{self.file_path}": '
        )
        self._maybe_print_maybe_raise(
            lambda: self._run(ast), prefix=f'Error at execution in "{self.file_path}": '
        )
        return self.module

