import random
import time


def rob(nums: list[int]) -> int:

    if len(nums) == 1:
        return nums[0]

    max1, max2 = nums[0], nums[1]
    for i in range(2, len(nums)):
        tmp = max(nums[i]+max1, max2)
        max1 = max2
        max2 = tmp

    return max2


def rob_faster(nums: list[int]) -> int:
    rob1, rob2 = 0, 0
    for n in nums:
        temp = max(n + rob1, rob2)
        rob1 = rob2
        rob2 = temp
    return rob2


if __name__ == '__main__':
    nums = [random.randint(0, 401) for i in range(10000000)]

    s1s = time.time()
    print(rob(nums))
    s1e = time.time() - s1s

    s2s = time.time()
    print(rob_faster(nums))
    s2e = time.time() - s2s

    print('s1:', s1e)
    print('s2:', s2e)

# assert rob([2, 3, 2]), 4  # 0, 3
# assert rob([1, 2]), 2  # 0, 2
# assert rob([2, 7, 9, 3, 1]), 12  # 0, 2, 4
# assert rob([2, 1, 1, 9, 5]), 11  # 0, 3
