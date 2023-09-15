import heapq
from typing import List


# Brute force
# class KthLargest:
#     def __init__(self, k: int, nums: List[int]):
#         self.k = k
#         self.nums = sorted(nums, reverse=True)
#
#     def add(self, val: int) -> int:
#         added = False
#
#         for i in range(len(self.nums)):
#             if val > self.nums[i]:
#                 self.nums.insert(i, val)
#                 added = True
#                 break
#
#         if not added:
#             self.nums.append(val)
#
#         return self.nums[self.k-1]


# Min Heap of Size K
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.min_heap, self.k = nums, k
        heapq.heapify(self.min_heap)
        while len(self.min_heap) > k:
            heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        return self.min_heap[0]


if __name__ == '__main__':
    kthLargest1 = KthLargest(3, [4, 5, 8, 2])
    print(kthLargest1.add(3))  # return 4
    print(kthLargest1.add(5))  # return 5
    print(kthLargest1.add(10))  # return 5
    print(kthLargest1.add(9))  # return 8
    print(kthLargest1.add(4))  # return 8

    kthLargest2 = KthLargest(1, [])
    print(kthLargest2.add(-3))

    kthLargest3 = KthLargest(2, [0])
    print(kthLargest3.add(-1))  # return ?
