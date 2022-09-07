def product_except_self(nums):
    ans = []

    pre = 1
    for num in nums:
        ans.append(pre)
        pre *= num

    post = 1
    for i in range(len(nums)-1, -1, -1):
        ans[i] *= post
        post *= nums[i]

    return ans


if __name__ == '__main__':
    nums1 = [1, 2, 3, 4]  # [24, 12, 8, 6]
    nums2 = [-1, 1, 0, -3, 3]  # [0, 0, 9, 0, 0]

    assert product_except_self(nums1) == [24, 12, 8, 6]
    assert product_except_self(nums2) == [0, 0, 9, 0, 0]

