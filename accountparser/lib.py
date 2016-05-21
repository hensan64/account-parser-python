# Support library

import re


def isBlank(line):
    pattern = re.compile(r'^\s*$')
    if pattern.match(line):
        return True
    else:
        return False


def format_memo(string):
    string = re.sub(r',', r' ', string)
    return re.sub(r'\s{2,}', ' ', string)


def format_value(string):
    string = re.sub(r'[.\s]', r'', string)
    return re.sub(r',', r'.', string)
