import unittest

from accountparser import lib


class TestLib(unittest.TestCase):
 
    def test_blank(self):
        self.assertEqual(True, lib.isBlank(' \n'))
        self.assertEqual(True, lib.isBlank('\n'))

    def test_format_memo(self):
        self.assertEqual(' a b c d e ', lib.format_memo('   a,b ,c    d,e '))

    def test_format_value(self):
        self.assertEqual('1234.56', lib.format_value('1.234,56'))
        self.assertEqual('1234.56', lib.format_value('1 234,56'))