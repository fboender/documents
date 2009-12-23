#!/usr/bin/python

import random

weights = {
	'A': 2,
	'B': 4,
	'C': 3,
	'D': 1
}

wTotal = 0
sWeights = []
for w in weights.items():
	wTotal += w[1]
	sWeights.append( (w[0], wTotal) )

print sWeights

results = {}
for i in range(100000):
	wRndNr = random.randint(0, wTotal - 1)
	for wRndChoice in sWeights:
		if wRndChoice[1] > wRndNr:
			break
	results[wRndChoice[0]] = results.get(wRndChoice[0], 0) + 1

print results
