#!/usr/bin/python

import random

source = "jiKnp4bqpmAbp"
target = "Hello, World!"

def fitness(source, target):
   fitval = 0
   for i in range(0, len(source)):
      fitval += (ord(target[i]) - ord(source[i])) ** 2
   return(fitval)

def mutate(source):
   charpos = random.randint(0, len(source) - 1)
   parts = list(source)
   parts[charpos] = chr(ord(parts[charpos]) + random.randint(-1,1))
   return(''.join(parts))

random.seed()
fitval = fitness(source, target)
i = 0
while True:
   i += 1
   m = mutate(source)
   fitval_m = fitness(m, target)
   if fitval_m < fitval:
      fitval = fitval_m
      source = m
      print "%5i %5i %14s" % (i, fitval_m, m)
   if fitval == 0:
      break
