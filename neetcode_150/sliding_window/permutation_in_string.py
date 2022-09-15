def check_inclusion(s1, s2):
    # u make a count{} of s1
    # then compare it to each count{} subs in s2

    s1_count = make_count_map(s1)
    s1_sum = get_count_sum(s1_count)

    lp = 0
    rp = s1_sum
    s2_count = make_count_map(s2[lp:rp])

    if s1_count == s2_count:
        return True

    while rp < len(s2):
        if s2[rp] not in s2_count:
            s2_count[s2[rp]] = 1
        else:
            s2_count[s2[rp]] += 1

        s2_count[s2[lp]] -= 1
        if s2_count[s2[lp]] == 0:
            del s2_count[s2[lp]]

        if s1_count == s2_count:
            return True

        lp += 1
        rp += 1

    return False


def get_count_sum(count):
    sum_ = 0
    for val in count.values():
        sum_ += val
    return sum_


def make_count_map(s):
    count = {}
    for char in s:
        if char not in count:
            count[char] = 1
        else:
            count[char] += 1
    return count


if __name__ == '__main__':
    s1_1 = "ab"
    s2_1 = "eidbaooo"  # Output: true
    s1_2 = "ab"
    s2_2 = "eidboaoo"  # Output: false
    s1_3 = 'adc'
    s2_3 = 'dcda'  # Output: true
    s1_4 = 'a'
    s2_4 = 'ab'  # true
    s1_5 = 'ab'
    s2_5 = 'ab'  # true

    assert check_inclusion(s1_1, s2_1) == True
    assert check_inclusion(s1_2, s2_2) == False
    assert check_inclusion(s1_3, s2_3) == True
    assert check_inclusion(s1_4, s2_4) == True
    assert check_inclusion(s1_5, s2_5) == True
