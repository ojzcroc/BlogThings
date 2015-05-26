import math
def factor(x):
    factors = []
    factorfreq = {}
    i = 2
    while x > 1:
        if x % i == 0:
            x = x / i
            factors.append(i)
        else:
            i += 1
    factors = list(set(factors))
    return factors

def factorfreq(x):
    factors = []
    factorfreq = {}
    i = 2
    while x > 1:
        if x % i == 0:
            x = x / i
            factors.append(i)
        else:
            i += 1
    from itertools import groupby
    freq = [len(list(group)) for key, group in groupby(factors)]
    factors = list(set(factors))
    for x in range(0,len(factors)):
        factorfreq[factors[x]] =freq[x]
    return factorfreq

def pythagoreantriplicator(n):
    factorfrequency = factorfreq(n**2)
    factors = factor(n)
    print factorfrequency
    frequencies = []
    for x in range(0,len(factors)):
        frequencies.append(factorfrequency[factors[x]])
    print frequencies
    i = 1
    for x in frequencies:
        i *= (x+1)
    i -= 1
    print i

#This part above is for calculating number of triples; next will calculate the actual triples.
def alltriples(n,check_mode='n'):
    if n%2 != 0:
        factors = factorise(n**2)
        factors = factors[:factors.index(n)]
        for x in factors:
            print str(n) + chr(0x00B2),"+",str(((n**2)-(x**2))/(2*x))+chr(0x00B2), "=", str(((n**2)-(x**2))/(2*x)+x)+chr(0x00B2)
            if check_mode.lower() == 'y':
                print math.sqrt(n**2+(((n**2)-(x**2))/(2*x))**2)
    else:
        factors = factorise(n**2)
        factors = factors[:factors.index(n)]
        factordummy = factorise(n**2)
        for x in range(0,len(factors)):
            if factordummy[x]%2 != 0:
                if factordummy[x] in factors:
                    factors.remove(factordummy[x])
            if n**2%(2*factordummy[x]) != 0:
                if factordummy[x] in factors:
                    factors.remove(factordummy[x])
        for x in factors:
            print str(n) + chr(0x00B2),"+",str(((n**2)-(x**2))/(2*x))+chr(0x00B2), "=", str(((n**2)-(x**2))/(2*x)+x)+chr(0x00B2)
            if check_mode.lower() == 'y':
                print math.sqrt(n**2+(((n**2)-(x**2))/(2*x))**2)

CurrentHighest = 5

def Most(n = 0):
    global CurrentHighest
    if n == 0:
        x = CurrentHighest
    else:
        x = n
    while 1 == 1:
        if MostTriples(x) > MostTriples(CurrentHighest):
            print x, MostTriples(x)
            CurrentHighest = x
        x += 1
        print x
        
def MostTriples(n):
    if n%2 != 0:
        factors = factorise(n**2)
        factors = factors[:factors.index(n)]
        return len(factors)
    else:
        factors = factorise(n**2)
        factordummy = factorise(n**2)
        factors = factors[:factors.index(n)]
        for x in range(0, len(factors)):
            if factordummy[x]%2 != 0:
                if factordummy[x] in factors:
                    factors.remove(factordummy[x])
            if n**2%(2*factordummy[x]) != 0:
                if factordummy[x] in factors:
                    factors.remove(factordummy[x])
        return len(factors)
        

def factorise(n):    
    factors = sorted(set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))
    factors.remove(n)
    return factors
