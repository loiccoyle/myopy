import sys
import unittest

import pyconf.utils as utils

class TestSysProperties(unittest.TestCase):

    def test_saved_sys_properties(self):
        old_path = sys.path
        with utils.saved_sys_properties():
            sys.path = ['bla', 'bla']
        self.assertEqual(sys.path, old_path)

