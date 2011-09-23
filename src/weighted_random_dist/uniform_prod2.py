import random

wTotal = 20
results = {}
for i in range(10000):
	wRndNr = random.random() * random.random() * random.random() * wTotal
	wRndNr = int(wTotal - wRndNr) + 1

	results[wRndNr] = results.get(wRndNr, 0) + 1

for k, v in results.items():
	print k, v
