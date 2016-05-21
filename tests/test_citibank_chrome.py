
import unittest

from accountparser.citibank_chrome import CitibankChrome

class TestCitibankChrome(unittest.TestCase):
 
    def test_parse(self):
        input = ['1\t12/06/2011\t13/07/2012\t1234567890123\tDescriptive Text 1\tAdditional Info 1\t\t1.234,56\tSEK\t\t1.234,56',
                 '2\t13/07/2012\t14/08/2013\t2345678901234\tDescriptive Text 2\tAdditional Info 2\t\t-234,567\tUSD\tUSD = SEK 10.50\t-2.345,67']
        prefix = "CB"
        output = CitibankChrome().parse(input, prefix)
    
        data_1 = output[0]
        data_2 = output[1]

        self.assertEqual(data_1.year,   '2011')
        self.assertEqual(data_1.month,  '06')
        self.assertEqual(data_1.day,    '12')
        self.assertEqual(data_1.prefix, 'CB')
        self.assertEqual(data_1.memo,   'Descriptive Text 1')
        self.assertEqual(data_1.type,   'debit')
        self.assertEqual(data_1.value,  '1234.56')

        self.assertEqual(data_2.year,   '2012')
        self.assertEqual(data_2.month,  '07')
        self.assertEqual(data_2.day,    '13')
        self.assertEqual(data_2.prefix, 'CB')
        self.assertEqual(data_2.memo,   'Descriptive Text 2')
        self.assertEqual(data_2.type,   'credit')
        self.assertEqual(data_2.value,  '2345.67')