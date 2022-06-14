def search(nums: list[int], target: int) -> int:
    left = 0
    right = len(nums)-1

    while left <= right:
        start_index = (left+right) // 2
        if nums[start_index] > nums[right]:
            left = start_index+1
        elif nums[right] > nums[start_index] > nums[start_index - 1]:
            right = start_index-1
        else:
            break

    left = -(len(nums)-start_index)
    right = len(nums) + left - 1
    while left <= right:
        mid = (left + right) // 2
        if target == nums[mid]:
            if mid < 0:
                return len(nums)+mid
            return mid
        elif target > nums[mid]:
            left = mid+1
        elif target < nums[mid]:
            right = mid-1

    return -1


if __name__ == '__main__':
    nums1 = [4, 5, 6, 7, 0, 1, 2]
    target1 = 0

    nums2 = [4, 5, 6, 7, 0, 1, 2]
    target2 = 3

    nums3 = [1]
    target3 = 0

    nums4 = [3, 5, 1]
    target4 = 5

    print(search(nums1, target1))
    print(search([8, 9, 2, 3, 4], 9))
