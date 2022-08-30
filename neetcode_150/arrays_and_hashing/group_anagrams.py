def build_hashmap(s):
    hashmap = {}
    for c in s:
        if c not in hashmap:
            hashmap[c] = 1
        else:
            hashmap[c] += 1
    return hashmap


def group_anagrams(strs):
    # for each str make a hashmap where key:char val:count
    # if hashmap not in hashmaps u add it as key:hashmap val:[str]
    #   where hashmaps is a hashmap itself where key:frozen hashmap val:array of str anagrams
    # return str_hashmaps.values().all() as array
    hashmaps = {}

    for i, s in enumerate(strs):
        hashmap = frozenset(build_hashmap(s))
        if hashmap not in hashmaps:
            hashmaps[hashmap] = [s]
        else:
            hashmaps[hashmap].append(s)

    print(list(hashmaps.values()))
    return list(hashmaps.values())


if __name__ == '__main__':
    #strs1 = ["eat", "tea", "tan", "ate", "nat", "bat"]  # Output: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
    #strs2 = [""]  # Output: [[""]]
    #strs3 = ["a"]  # Output: [["a"]]
    strs4 = ["ddddddddddg", "dgggggggggg"]

    #assert group_anagrams(strs1) == [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
    #assert group_anagrams(strs2) == [[""]]
    #assert group_anagrams(strs3) == [["a"]]
    assert group_anagrams(strs4) == [["dgggggggggg"],["ddddddddddg"]]
