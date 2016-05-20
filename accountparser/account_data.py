
# Account data

# -----------
# Data format
# -----------
# year:   '2011'
# month:  '06'
# day:    '12'
# prefix: 'SB'
# memo:   'Descriptive Text'
# type:   :debit | :credit
# value:  '1234.56'

class AccountData():

    def __init__(self, year, month, day, prefix, memo, type, value):
        self.year = year
        self.month = month
        self.day = day
        self.prefix = prefix
        self.memo = memo
        self.type = type
        self.value = value

    def dummy(self):
        print('Dummy')
