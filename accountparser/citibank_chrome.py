
# Citibank Chrome parser

import re

from accountparser.account_data import AccountData
from accountparser.lib import isBlank, format_memo, format_value

class CitibankChrome():

    def parse(self, lines, prefix):
        data_list = []
        for line in lines:
            if isBlank(line): continue
            regex_string = r'^.+?\t(?P<day>\d{2})\/(?P<month>\d{2})\/(?P<year>\d{4})(?:\t.*?){2}\t(?P<memo>.+?)(?:\t.*?){5}\t(?P<sign>-?)(?P<value>.+?)$'
            pattern = re.compile(regex_string)
            match = re.match(pattern, line)
            if match:
                if match.group('sign') == '-':
                    type = 'credit'
                else :
                    type = 'debit'
                data_list += [AccountData(match.group('year'),
                                          match.group('month'),
                                          match.group('day'),
                                          prefix,
                                          format_memo(match.group('memo')),
                                          type,
                                          format_value(match.group('value')))]
            else:
                raise RuntimeError("Line did not match regexp: " + line)
        return data_list