import math


def get_nth_prime(target):
    primes = [2]
    val = 2
    while len(primes) < target:
        for prime in primes:
            if prime > math.sqrt(val):
                primes.append(val)
                break
            if val % prime == 0:
                break
        val += 1
    return primes[-1]


print(get_nth_prime(10001))
