def countBeautifulSubset(nums, k):
    count = [0] * len(nums)
    nums.sort()
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] - nums[j] == k:
                count[i] += count[j] + 1
        if count[i] == 0:
            count[i] = 1
    return sum(count)

nums = [2, 4, 6]
k = 2

print(countBeautifulSubset(nums, k))