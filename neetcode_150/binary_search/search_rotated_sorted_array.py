def search(nums, target):
    n = len(nums)
    lp = 0
    rp = n

    while lp <= rp:
        mp = (rp+lp) // 2

        if target == nums[mp]:
            return mp

        # Left side
        if nums[mp] >= nums[lp]:
            if target > nums[mp] or target < nums[lp]:
                lp = mp+1
            else:
                rp = mp-1

        # Right side
        else:
            if target < nums[mp] or target > nums[rp]:
                rp = mp-1
            else:
                lp = mp+1

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

    assert search(nums1, target1) == 4
    assert search(nums2, target2) == -1
    assert search(nums3, target3) == -1
    assert search(nums4, target4) == 1
