def top_k_frequent(nums, k):
    count = {}
    freq = [[] for i in range(len(nums)+1)]

    for num in nums:
        count[num] = 1 + count.get(num, 0)
    for key, val in count.items():
        freq[val].append(key)

    res = []
    for i in range(len(freq)-1, 0, -1):
        for num in freq[i]:
            res.append(num)
            if len(res) == k:
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
