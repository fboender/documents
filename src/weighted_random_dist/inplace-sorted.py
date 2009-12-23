#!/usr/bin/python

import random

weights = {
	'A': 2,
	'B': 4,
	'C': 3,
	'D': 1
}

sWeights = sorted(weights.items(), lambda x, y:cmp(x[1], y[1]))
wTotal = sum(weights.values())

print sWeights

results = {}
for i in range(100000):
	wRndNr = random.randint(0, wTotal - 1)
	s = wTotal
	for i in xrange(len(sWeights) - 1, -1, -1):
		wRndChoice = sWeights[i]
		s -= wRndChoice[1]
		if s <= wRndNr:
			break
	results[wRndChoice[0]] = results.get(wRndChoice[0], 0) + 1
print results
