first_hundred_nums = range(100)

square_of_sums = pow(sum(first_hundred_nums), 2)
sum_of_squares = sum([pow(x, 2) for x in first_hundred_nums])

print(square_of_sums - sum_of_squares)
