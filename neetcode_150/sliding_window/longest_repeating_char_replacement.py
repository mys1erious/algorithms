def char_replacement(s, k):
    # T: O(n), M: O(n)
    max_len = 0
    max_count = 0
    count_sum = 0
    lp = 0
    rp = 0
    counts = {}
    while lp <= rp < len(s):
        if s[rp] not in counts:
            counts[s[rp]] = 1
        else:
            counts[s[rp]] += 1

        count_sum += 1
        if counts[s[rp]] > max_count:
            max_count = counts[s[rp]]

        while count_sum - max_count > k:
            counts[s[lp]] -= 1
            count_sum -= 1
            lp += 1

        if count_sum > max_len:
            max_len = count_sum

        rp += 1

    return max_len


def counts_sum_max(counts):
    max_count = 0
    count_sum = 0
    for key, val in counts.items():
        count_sum += val
        if val > max_count:
            max_count = val

    return count_sum, max_count


if __name__ == '__main__':
    s1 = "ABAB"
    k1 = 2  # Output: 4
    s2 = "AABABBA"
    k2 = 1  # Output: 4
    s3 = 'AAAA'
    k3 = 0
    s4 = 'ABAA'
    k4 = 0

    assert char_replacement(s1, k1) == 4
    assert char_replacement(s2, k2) == 4
    assert char_replacement(s3, k3) == 4
    assert char_replacement(s4, k4) == 2
