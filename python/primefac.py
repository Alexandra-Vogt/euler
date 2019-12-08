import math


def primefinder(target):
    primes = [2]
    for val in range(3, target):
        for prime in primes:
            if prime > math.sqrt(val):
                primes.append(val)
                break
            if val % prime == 0:
                break
    return primes


def primefac(target):
    factors = []
    primes = primefinder(math.ceil(math.sqrt(target)))
    for prime in primes:
        if target % prime == 0:
            factors.append(prime)
    return factors


print(primefac(600851475143)[-1])
