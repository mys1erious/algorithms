def top_k_frequent(nums, k):
    # Need to rm .index from loops to get from n^2 to nlogn
    # uniques_map = {num: i}
    uniques = {}
    freqs = [0] * len(set(nums))

    uniques_count = 0
    for num in nums:
        if num not in uniques:
            uniques[num] = uniques_count
            uniques_count += 1

        freqs[uniques[num]] += 1

    res = []
    for _ in range(k):
        fi = freqs.index(max(freqs))
        freqs[fi] = -1
        max_val = list(uniques.keys())[list(uniques.values()).index(fi)]
        res.append(max_val)

    return res


if __name__ == '__main__':
    nums1 = [2,2,3,1,1,1]
    k1 = 2  # Output: [1,2]
    nums2 = [1]
    k2 = 1  # Output: [1]
    nums3 = [-1, -1]
    k3 = 1

    assert [1,2] == top_k_frequent(nums1, k1)
    assert [1] == top_k_frequent(nums2, k2)
    assert [-1] == top_k_frequent(nums3, k3)
