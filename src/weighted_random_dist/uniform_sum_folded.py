#!/usr/bin/python

import random

wTotal = 20
results = {}
for i in range(10000):
	wRndNr = (random.random() * wTotal) + (random.random() * wTotal)
	if wRndNr > wTotal:
		wRndNr = wTotal * 2.0 - wRndNr
	wRndNr = int(wRndNr) + 1

	results[wRndNr] = results.get(wRndNr, 0) + 1

for k, v in results.items():
	print k, v
