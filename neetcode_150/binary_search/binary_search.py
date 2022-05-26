# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] (t: 3)
def search(nums: list[int], target: int) -> int:
    left = 0
    right = len(nums) - 1
    pointer = right // 2
    while left <= right:
        if nums[pointer] < target:
            left = pointer + 1
        elif nums[pointer] > target:
            right = pointer - 1
        else:
            return pointer
        pointer = (left + right) // 2
    else:
        return -1


ar = [-1,0,3,5,9,12]
print(ar)
print(search(ar, 9))
