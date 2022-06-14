def two_sum(nums: list[int], target: int) -> list[int] or None:
    hash = {}

    for i in range(len(nums)):
        sub = target-nums[i]
        if sub in hash:
            return [hash[sub], i]
        hash[nums[i]] = i

    return None


print(two_sum([2, 7, 11, 15], 9))
print(two_sum([3, 2, 4], 6))
print(two_sum([3, 3], 6))
