def scan_string(s, hash_map):
    for num in s:
        if num not in hash_map:
            hash_map[num] = 1
        else:
            hash_map[num] += 1

    return hash_map


def isAnagram(s: str, t: str) -> bool:
    # 2 hash_maps with key: char, val: count
    # and then compare those 2 hashmaps
    # n - len(s); m - len(t)
    # M: O(n*m)
    # T: O(n*m)
    s_map = {}
    t_map = {}

    s_map = scan_string(s, s_map)
    t_map = scan_string(t, t_map)

    if s_map == t_map:
        return True
    return False

