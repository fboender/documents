#!/bin/sh

python uniform.py > uniform.dat
python uniform_sum.py > uniform_sum.dat
python uniform_sum2.py > uniform_sum2.dat
python uniform_sum_folded.py > uniform_sum_folded.dat
python uniform_prod.py > uniform_prod.dat
python uniform_prod2.py > uniform_prod2.dat

gnuplot -e 'load "uniform.gplt"'
