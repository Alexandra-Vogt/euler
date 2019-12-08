def is_palindrome(string):
    if string == string[::-1]:
        return True
    else:
        return False


pdromes = []

for num_a in range(100, 999):
    for num_b in range(100, 999):
        poss_pdrome = num_a * num_b
        if is_palindrome(str(poss_pdrome)):
            pdromes.append(poss_pdrome)

print(max(pdromes))
