import unittest

from accountparser.account_data import AccountData


class TestAccountData(unittest.TestCase):
    def test_account_data(self):
        data_1 = AccountData('2011', '06', '12', 'SB', 'Descriptive Text 1', 'debit', '1234.56')
        data_2 = AccountData('2012', '07', '13', 'CB', 'Descriptive Text 2', 'credit', '2345.67')

        self.assertEqual(data_1.year, '2011')
        self.assertEqual(data_1.month, '06')
        self.assertEqual(data_1.day, '12')
        self.assertEqual(data_1.prefix, 'SB')
        self.assertEqual(data_1.memo, 'Descriptive Text 1')
        self.assertEqual(data_1.type, 'debit')
        self.assertEqual(data_1.value, '1234.56')

        self.assertEqual(data_2.year, '2012')
        self.assertEqual(data_2.month, '07')
        self.assertEqual(data_2.day, '13')
        self.assertEqual(data_2.prefix, 'CB')
        self.assertEqual(data_2.memo, 'Descriptive Text 2')
        self.assertEqual(data_2.type, 'credit')
        self.assertEqual(data_2.value, '2345.67')
