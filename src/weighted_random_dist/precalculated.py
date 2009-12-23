#!/usr/bin/python

import random
import bisect

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
	sWeights.append( (wTotal, w[0]) )

results = {}
for i in range(100000):
	wRndNr = random.randint(0, wTotal - 1)
	wRndChoice = sWeights[bisect.bisect(sWeights, (wRndNr, None))]

	results[wRndChoice[1]] = results.get(wRndChoice[1], 0) + 1

print results
