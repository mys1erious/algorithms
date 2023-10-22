from typing import List
import heapq


# Heapify - T: O(nlogn), M: O(1)
# def findKthLargest(nums: List[int], k: int) -> int:
#     heapq.heapify(nums)
#
#     i = len(nums) - k
#     while i > 0:
#         heapq.heappop(nums)
#
#         i-=1
#
#     return nums[0]


# QuickSelect - T: O(n), M: O(1)
def partition(nums: List[int], left: int, right: int) -> int:
    pivot, fill = nums[right], left

    for i in range(left, right):
        if nums[i] <= pivot:
            nums[fill], nums[i] = nums[i], nums[fill]
            fill += 1

    nums[fill], nums[right] = nums[right], nums[fill]

    return fill


def findKthLargest(nums: List[int], k: int) -> int:
    k = len(nums) - k
    left, right = 0, len(nums) - 1

    while left < right:
        pivot = partition(nums, left, right)

        if pivot < k:
            left = pivot + 1
        elif pivot > k:
            right = pivot - 1
        else:
            break

    return nums[k]


if __name__ == '__main__':
    nums1, k1 = [3, 2, 1, 5, 6, 4], 2
    nums2, k2 = [3, 2, 3, 1, 2, 4, 5, 5, 6], 4

    ans1 = findKthLargest(nums1, k1)
    ans2 = findKthLargest(nums2, k2)

    print(ans1)
    print(ans2)

    assert ans1 == 5
    assert ans2 == 4
