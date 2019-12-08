def getEvenFibNums(target_val):
    nums = []
    prev_val = 0
    temp = 0
    val = 1
    while val < target_val:
        if val % 2 == 0:
            nums.append(val)
        temp = val
        val = temp + prev_val
        prev_val = temp
    return nums


print(getEvenFibNums(2000000000000000000))
