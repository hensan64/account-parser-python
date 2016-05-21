
import unittest

from accountparser.skandiabanken_chrome import parse
 
class TcSkandiabankenChrome(unittest.TestCase):
 
  def test_parse(self):
    input = ['2011-06-12\tDescriptive Text 1\t-1234,56\t12345,67',
             '2012-07-13\tDescriptive Text 2\t2345,67\t23456,78']
    prefix = "SB"
    output = parse(input, prefix)

    data_1 = output[0]
    data_2 = output[1]
    
    self.assertEqual(data_1.year,   '2011')
    self.assertEqual(data_1.month,  '06')
    self.assertEqual(data_1.day,    '12')
    self.assertEqual(data_1.prefix, 'SB')
    self.assertEqual(data_1.memo,   'Descriptive Text 1')
    self.assertEqual(data_1.type,   'debit')
    self.assertEqual(data_1.value,  '1234.56')
    
    self.assertEqual(data_2.year,   '2012')
    self.assertEqual(data_2.month,  '07')
    self.assertEqual(data_2.day,    '13')
    self.assertEqual(data_2.prefix, 'SB')
    self.assertEqual(data_2.memo,   'Descriptive Text 2')
    self.assertEqual(data_2.type,   'credit')
    self.assertEqual(data_2.value,  '2345.67')