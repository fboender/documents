#!/usr/bin/python

import string

STATE_NUMERIC = 1
STATE_ALPHA = 2

CHAR_SPACE = " "

def validate_zipcode(s):
    cur_state = STATE_NUMERIC

    for char in s:
        if cur_state == STATE_NUMERIC:
            if char == CHAR_SPACE:
                cur_state = STATE_ALPHA
            elif char not in string.digits:
                return False
        elif cur_state == STATE_ALPHA:
            if char not in string.letters:
                return False
    return True

zipcodes = [
    "3900 AB",
    "45D6 9A",
]

for zipcode in zipcodes:
    print zipcode, validate_zipcode(zipcode)
