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


result = 1
primes = primefinder(20)
print(primes)
for val in primes:
    result *= val
print(result)
