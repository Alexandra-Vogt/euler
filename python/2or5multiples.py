#!/usr/bin/env python3


def ismultiple(a, b):
    """This checks if a is a multiple of b."""
    if a % b == 0:
        return True
    else:
        return False


multiples = []
for val in range(1000):
    if ismultiple(val, 3) or ismultiple(val, 5):
        multiples.append(val)

print(multiples)
