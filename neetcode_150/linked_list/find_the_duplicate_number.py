from neetcode_150.linked_list.utils import ListNode, make_linked_list


# No modification
# T: O(n)
# M: O(1)

# Linked List Cycle problem
# Floyd algo

#
def find_duplicate(nums):
    slow, fast = 0, 0

    # Find slow and fast pointers intersection
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    # Add slow2 pointer and find intersection of slow and slow2
    slow2 = 0
    while True:
        slow = nums[slow]
        slow2 = nums[slow2]
        if slow == slow2:
            return slow


if __name__ == '__main__':
    nums = [1, 3, 4, 2, 2]

    dp = find_duplicate(nums)

    print(dp)
