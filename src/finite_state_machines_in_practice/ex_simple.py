#!/usr/bin/python

s = "ls -la 'My Documents' /home /etc"

STATE_UNQUOTED = 1
STATE_QUOTED = 2

CHAR_QUOTE = "'"
CHAR_SPACE = " "

words = []
cur_state = STATE_UNQUOTED
cur_word = ''

# Break s up in words. Words are delimited by 
# spaces, unless we're between quotes.
for char in s:
    if cur_state == STATE_QUOTED:
        if char == CHAR_QUOTE:
            words.append(cur_word)
            cur_word = ''
            cur_state = STATE_UNQUOTED
        else:
            cur_word += char
    elif cur_state == STATE_UNQUOTED:
        if char == CHAR_QUOTE:
            cur_state = STATE_QUOTED
        elif char == CHAR_SPACE:
            if cur_word:
                words.append(cur_word)
            cur_word = ''
        else:
            cur_word += char
words.append(cur_word)

print words
