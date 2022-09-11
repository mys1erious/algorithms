def sum3(nums):
    target = 0
    nums.sort()
    ans = []

    ap = 0
    while ap < len(nums)-2:
        if ap > 0 and nums[ap] == nums[ap-1]:
            ap += 1
            continue

        bp = ap + 1
        cp = len(nums) - 1
        while bp < cp:
            abc_sum = nums[ap] + nums[bp] + nums[cp]

            if abc_sum < target:
                bp += 1
            elif abc_sum > target:
                cp -= 1
            else:
                ans.append([nums[ap], nums[bp], nums[cp]])
                bp += 1
                while nums[bp] == nums[bp-1] and bp < cp:
                    bp += 1
        else:
            ap += 1

    print(ans)
    return ans


if __name__ == '__main__':
    nums0 = [0,0,0]
    nums1 = [-1, 0, 1, 2, -1, -4]  # Output: [[-1, -1, 2], [-1, 0, 1]]
    nums2 = [0, 1, 1]  # Output: []
    nums3 = [0, 0, 0]  # Output: [[0, 0, 0]]

    #assert sum3(nums0) == [[0,0,0]]
    assert sum3(nums1) == [[-1, 0, 1], [-1, -1, 2]]
    assert sum3(nums2) == []
    assert sum3(nums3) == [[0, 0, 0]]
