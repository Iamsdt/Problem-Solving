def twoSum(nums, target):
    total = len(nums)
    for i in range(total):
        for j in range(i, total):
            s = i + j

            if target == s:
                return [i, j]


print(twoSum([2, 7, 11, 15], 9))
