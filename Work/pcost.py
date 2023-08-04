# pcost.py
#
# Exercises 1.27, 1.30-1

import sys

def get_cost(filename):

    cost = 0

    with open(filename, 'rt') as f:
        next(f)
        for line in f:
            row = line.split(',')
            try:
                cost += int(row[1]) * float(row[2])
            except:
                print('missing value')

    return cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

print('Total cost', get_cost(filename))