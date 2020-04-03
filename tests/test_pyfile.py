import unittest
from shutil import rmtree
from pathlib import Path
from myopy import PyFile

CONFIG_CONTENT = """\
test_dict['key'] = 2
test_dict['something'] = 5
test_class.some_method()
"""

CONFIG_CONTENT_ERR="""\
something_not_defined()
"""

CONFIG_CONTENT_IMP_1="""\
def importme():
    return True
"""

CONFIG_CONTENT_IMP_2="""\
from config_imp_1 import importme
importme()
"""


TEST_FOLDER = 'unittest'

class TestClass:
    __test__ = False
    def __init__(self):
        self.counter = 0
    def some_method(self):
        self.counter += 1

class TestPyConfig(unittest.TestCase):
    def setUp(self):
        self.test_folder = Path(TEST_FOLDER)
        self.test_folder.mkdir(exist_ok=True)
        self.config_file = self.test_folder / 'config.py'
        with self.config_file.open('w') as f:
            f.write(CONFIG_CONTENT)
        self.config_file_err = self.test_folder / 'config_err.py'
        with self.config_file_err.open('w') as f:
            f.write(CONFIG_CONTENT_ERR)
        self.config_file_imp_1 = self.test_folder / 'config_imp_1.py'
        with self.config_file_imp_1.open('w') as f:
            f.write(CONFIG_CONTENT_IMP_1)
        self.config_file_imp_2 = self.test_folder / 'config_imp_2.py'
        with self.config_file_imp_2.open('w') as f:
            f.write(CONFIG_CONTENT_IMP_2)

    def test_run(self):
        cfg_dict = {'something': 4}
        cfg_class = TestClass()

        config = PyFile(self.config_file)
        config.provide('test_dict', cfg_dict)
        config.provide('test_class', cfg_class)
        config.run()

        self.assertEqual(cfg_dict['something'], 5)
        self.assertEqual(cfg_dict['key'], 2)
        self.assertEqual(cfg_class.counter, 1)

    def test_exception(self):
        config = PyFile(self.config_file_err)
        with self.assertRaises(Exception):
            config.run()

    def test_import(self):
        config = PyFile(self.config_file_imp_2)
        config.run()


    def tearDown(self):
        rmtree(self.test_folder, ignore_errors=True)




