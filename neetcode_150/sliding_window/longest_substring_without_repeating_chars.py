def longest_substring_len(s):
    # Brute Force: T: O(n^2), M: O(n)
    # lp = 0
    # rp = 0
    # max_len = 0
    # subs = ''
    # while rp < len(s):
    #     if s[rp] not in subs:
    #         subs += s[rp]
    #         rp += 1
    #     else:
    #         if len(subs) > max_len:
    #             max_len = len(subs)
    #         subs = ''
    #         lp += 1
    #         rp = lp
    #
    # return max(max_len, len(subs))

    # With hashmap
    # lp = 0
    # rp = 0
    # max_len = 0
    # subs_map = {}
    # while rp < len(s):
    #     if s[rp] not in subs_map:
    #         subs_map[s[rp]] = rp
    #         rp += 1
    #     else:
    #         if len(subs_map) > max_len:
    #             max_len = len(subs_map)
    #
    #         # loop for long repeated chars
    #         lp = subs_map[s[rp]] + 1
    #         while lp < len(s) - 1 and s[lp + 1] == s[lp]:
    #             lp += 1
    #
    #         subs_map = {s[lp]: lp}
    #         rp = lp + 1
    #
    # return max(max_len, len(subs_map))

    # With set
    lp = 0
    rp = 0
    max_len = 0
    subs = set()
    while rp < len(s):
        if s[rp] not in subs:
            subs.add(s[rp])
            rp += 1
        else:
            if len(subs) > max_len:
                max_len = len(subs)

            while s[rp] in subs:
                subs.remove(s[lp])
                lp += 1

    return max(max_len, len(subs))


if __name__ == '__main__':
    s1 = "abcabcbb"  # Output: 3
    s2 = "bbbbb"  # Output: 1
    s3 = "pwwkew"  # Output: 3
    s4 = "jbpnbwwd"

    # assert longest_substring_len(s1) == 3
    # assert longest_substring_len(s2) == 1
    # assert longest_substring_len(s3) == 3
    assert longest_substring_len(s4) == 4

