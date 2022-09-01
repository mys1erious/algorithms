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