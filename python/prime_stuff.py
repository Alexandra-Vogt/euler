import math


def primes_in_range(*args):
    """primes_in_range(stop) -> [primes]
    primes_in_range(start, stop) -> [primes]
    Returns a list of primes in the range between the start and stop values.
    If no start value is provided it returns the primes in the range between
    0 and the stop value."""
    if len(args) == 1:
        stop = args[0]
        start = 3
    else:
        return_start = args[0]
        stop = args[1]
    return_start_idx = 0
    start = 3
    primes = [2]
    for val in range(start, stop):
        for prime in primes:
            if prime > math.sqrt(val):
                primes.append(val)
                if val > return_start and return_start_idx == 0:
                    return_start_idx = len(primes)
                break
            if val % prime == 0:
                break
    return primes[return_start_idx:]


print(primes_in_range(10, 200))


def prime_factors(target):
    factors = []
    primes = primes_in_range(math.ceil(math.sqrt(target)))
    for prime in primes:
        if target % prime == 0:
            factors.append(prime)
    return factors


def get_nth_prime(target):
    primes = [2]
    val = 3
    while len(primes) < target:
        for prime in primes:
            if prime > math.sqrt(val):
                primes.append(val)
                break
            if val % prime == 0:
                break
        val += 1
    return primes[-1]
