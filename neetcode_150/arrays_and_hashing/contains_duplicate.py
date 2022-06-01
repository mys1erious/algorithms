def containsDuplicate(nums: list[int]) -> bool:

    hash = {}

    for num in nums:
        if num not in hash:
            hash[num] = True
        else:
            return True

    return False


nums = [2,14,18,22]
print(containsDuplicate(nums))
