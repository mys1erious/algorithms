
# Rework when learn about Hashing

def containsDuplicate(nums: list[int]) -> bool:
    for i in range(len(nums)):
        cur_val = nums[i]
        for j in range(i+1, len(nums)):
            if nums[j] == cur_val:
                return True
    return False


nums = [2,14,18,22,22]
print(containsDuplicate(nums))
