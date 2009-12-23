#!/usr/bin/python

import random

weights = {
	'A': 2,
	'B': 4,
	'C': 3,
	'D': 1
}

wTotal = sum(weights.values())

results = {}
for i in range(100000):
	wRndNr = random.randint(0, wTotal - 1)
	s = 0
	for w in weights.items():
		s += w[1]
		if s > wRndNr:
			break;
	results[w[0]] = results.get(w[0], 0) + 1

print results
