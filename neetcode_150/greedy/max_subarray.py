def max_subarray(nums: list[int]) -> int:
    if len(nums) == 1:
        return nums[0]

    max_sum = nums[0]
    cur_sum = nums[0]

    for n in nums:
        if cur_sum < 0:
            cur_sum = 0
        cur_sum += n
        max_sum = max(max_sum, cur_sum)
    return max_sum


if __name__ == '__main__':
    nums1 = [-2,1,-3,4,-1,2,1,-5,4]
    nums2 = [-2, 1]
    nums3 = [5, 4, -1, 7, 8]

    #assert max_subarray(nums1), 6
    assert max_subarray(nums2), 1
    assert max_subarray(nums3), 23
