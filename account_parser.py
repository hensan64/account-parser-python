# Main script

from sys import argv

import accountparser.citibank_chrome as citibank_chrome
from accountparser.converter import execute
import accountparser.skandiabanken_chrome as skandiabanken_chrome

in_file_citibank = './files/in_citibank.txt'
out_file_citibank = './files/Citibank.csv'
prefix_citibank = 'CB'

in_file_skandiabanken = './files/in_skandiabanken.txt'
out_file_skandiabanken = './files/Skandiabanken.csv'
prefix_skandiabanken = 'SB'

if len(argv) != 2: raise RuntimeError(
    'Faulty command line arguments: Should be: python account_parser.py citibank|skandiabanken')

if argv[1] == 'citibank':
    execute(citibank_chrome, in_file_citibank, out_file_citibank, prefix_citibank)
elif argv[1] == 'skandiabanken':
    execute(skandiabanken_chrome, in_file_skandiabanken, out_file_skandiabanken, prefix_skandiabanken)
else:
    raise RuntimeError('Faulty bank argument: Should be citibank|skandiabanken')
