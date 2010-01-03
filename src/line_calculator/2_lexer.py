#!/usr/bin/python

import shlex

s = '2 * (5 + 2.5)'

lex = shlex.shlex(s)
lex.wordchars += '.'
for token in lex:
	print token

