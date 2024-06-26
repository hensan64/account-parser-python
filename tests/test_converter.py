import unittest

import accountparser.citibank_chrome as citibank_chrome
from accountparser.converter import execute
import accountparser.skandiabanken_chrome as skandiabanken_chrome


class TestConverter(unittest.TestCase):
    def test_execute_citibank_chrome(self):
        in_path = './files/in_citibank.txt'
        out_path = './files/Citibank.csv'
        out_ref_path = './files/Citibank.ref.csv'
        prefix = 'CB'

        execute(citibank_chrome, in_path, out_path, prefix)

        out_file = open(out_path)
        out_ref_file = open(out_ref_path)
        self.assertListEqual(out_ref_file.readlines(), out_file.readlines())

    def test_execute_skandiabanken_chrome(self):
        in_path = './files/in_skandiabanken.txt'
        out_path = './files/Skandiabanken.csv'
        out_ref_path = './files/Skandiabanken.ref.csv'
        prefix = 'SB'

        execute(skandiabanken_chrome, in_path, out_path, prefix)

        out_file = open(out_path)
        out_ref_file = open(out_ref_path)
        self.assertListEqual(out_ref_file.readlines(), out_file.readlines())
