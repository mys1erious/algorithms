def longest_consecutive(nums):
    uniques = set(nums)

    max_len = 0
    for num in uniques:
        if num - 1 not in uniques:
            cur_len = 1
            expected_next = num + 1
            while expected_next in uniques:
                cur_len += 1
                expected_next += 1
            if cur_len > max_len:
                max_len = cur_len

    return max_len


if __name__ == '__main__':
    nums1 = [100, 4, 200, 1, 3, 2]  # Output: 4
    nums2 = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]  # Output: 9

    assert longest_consecutive(nums1) == 4
    assert longest_consecutive(nums2) == 9
