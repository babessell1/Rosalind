#!/usr/bin/env python3

import sys

def breedRabbits(n, m):
    maturation_time = 1
    reproduction_time = 1

    for i in range(n):
        rabbit_population = 


if __name__ == "__main__":
    try:
        n = sys.argv[1]
        m = sys.argv[2]
    except:
        print("takes two arguments,\n   \
               1: n number of months to simulate\n  \
               2: m number of months a rabbit lives")

    pairs = breedRabbits(n, m)
    print(pairs)
