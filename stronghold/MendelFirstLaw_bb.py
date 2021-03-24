#!/usr/bin/env python
import sys

def dominantPhenotypeProbability(k, m, n):
    t = sum([k,m,n]) # population
    d = t*(t-1.0) # prob tree denominator
    prob_kk = k*(k-1)/d
    prob_km = 2.0*k*m/d
    prob_kn = 2.0*k*n/d
    prob_mm = m*(m-1)/d
    prob_mn = 2.0*m*n/d
    prob_nn = n*(n-1)/d

    prob_dom = prob_kk + prob_km + prob_kn + 3*prob_mm/4 + prob_mn/2

    return str("{:.5f}".format(prob_dom))

# alternative solution: simulation
def dominantPhenotypeProbability_sim(k, m, n, N):
    import random
    t = sum([k,m,n]) # population
    cnt = 0
    samples = k*["XX"] + m*["Xx"] + n*["xx"]
    print(random.sample(samples, 2))
    for i in range(N):
        parent1, parent2 = random.sample(samples, 2)
        offspring = parent1[random.randint(0,1)] + parent2[random.randint(0,1)]
        if "X" in offspring : cnt+=1

    return str("{:.5f}".format(cnt/N))


if __name__ == "__main__":
    try:
        inFile = sys.argv[1]
        outFile = "results/result_" + inFile.split("/")[1]
    except:
        print("Bad Systen Arguments")
    try:
        with open(inFile, 'r') as handle:
            k, m, n = list(map(int, handle.readline().split(" ")))
    except:
        print("Incorrect Data Format")

    #prob_dom = dominantPhenotypeProbability(k,m,n)
    prob_dom = dominantPhenotypeProbability_sim(k,m,n,10000000)
    print(prob_dom)
    with open(outFile,'w') as file:
        file.write(prob_dom)
