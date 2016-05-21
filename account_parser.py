
# Main script

import sys

from accountparser.citibank_chrome import CitibankChrome
from accountparser.converter import execute
from accountparser.skandiabanken_chrome import SkandiabankenChrome

if len(sys.argv) != 2: raise RuntimeError('Faulty command line arguments: Should be: python account_parser.py citibank|skandiabanken')

if sys.argv(1) == 'citibank':
    execute(CitibankChrome, '../files/in_citibank.txt', '../files/Citibank.csv', "CB")
elif sys.argv(1) == 'skandiabanken':
    execute(SkandiabankenChrome, '../files/in_skandiabanken.txt', '../files/Skandiabanken.csv', 'SB')
else:
    raise RuntimeError('Faulty bank argument: Should be citibank|skandiabanken')