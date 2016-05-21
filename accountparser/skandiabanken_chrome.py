# Skandiabanken Chrome parser

import re

from accountparser.account_data import AccountData
from accountparser.lib import isBlank, format_memo, format_value


def parse(lines, prefix):
    data_list = []
    for line in lines:
        if isBlank(line): continue
        regex = r'^(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})\t(?P<memo>.+?)\t(?P<sign>-?)(?P<value>.+?)\t.*$'
        pattern = re.compile(regex)
        match = re.match(pattern, line)
        if match:
            if match.group('sign') == '-':
                type = 'debit'
            else:
                type = 'credit'

            data_list += [AccountData(match.group('year'),
                                      match.group('month'),
                                      match.group('day'),
                                      prefix,
                                      format_memo(match.group('memo')),
                                      type,
                                      format_value(match.group('value')))]
        else:
            raise RuntimeError("Line did not match regex: line: " + line)
    return data_list
