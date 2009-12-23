#!/usr/bin/python

import random

weights = {
	'A': 2,
	'B': 4,
	'C': 3,
	'D': 1
}

dist = []
for x in weights.keys():
	dist += weights[x] * x

results = {}
for i in range(100000):
	wRndChoice = random.choice(dist)
	results[wRndChoice] = results.get(wRndChoice, 0) + 1

print results
