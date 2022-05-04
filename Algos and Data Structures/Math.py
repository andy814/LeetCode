import math

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def eu_gcd(a,b):
    return eu_gcd(b,a%b) if b!=0 else a

def math_gcd(a,b):
    return math.gcd(a,b)

def LCM(a,b): # Number1 * Number2 = L.C.M. * G.C.D.
    greater=max(a,b)
    while(True):
        if((greater % a == 0) and (greater % b == 0)):
            lcm = greater
            break
        greater += 1
    return lcm

def LCM2(a,b):
    lcm = (a*b)//eu_gcd(a,b)
    return lcm