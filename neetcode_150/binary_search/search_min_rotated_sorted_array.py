# Took 45min, no help used


def find_min(nums: list[int]) -> int:
    n = len(nums)
    if n == 1:
        return nums[0]

    lp = 0
    rp = n-1
    while lp <= rp:
        mp = (lp + rp) // 2

        if nums[mp - 1] > nums[mp]:
            return nums[mp]

        if nums[mp] > nums[0] and nums[mp] > nums[-1]:
            lp = mp+1
        else:
            if rp == 1:
                return nums[rp]
            rp = mp-1


if __name__ == '__main__':
    nums1 = [3, 4, 5, 1, 2]  # = 1
    nums2 = [4,5,6,7,0,1,2]  # = 0
    nums3 = [11, 13, 15, 17]  # = 11
    nums4 = [5,1,2,3,4]  # 1
    nums5 = [1]  # 1
    nums6 = [2, 1]  # 1

    assert find_min(nums1) == 1
    assert find_min(nums2) == 0
    assert find_min(nums3) == 11
    assert find_min(nums4) == 1
    assert find_min(nums5) == 1
    assert find_min(nums6) == 1
