"test lib"

import unittest

from simple_python_package import lib


class TestAddOne(unittest.TestCase):
    def test_add_one(self):
        actual = lib.add_one(6)
        expected = 7
        self.assertEqual(expected, actual)
