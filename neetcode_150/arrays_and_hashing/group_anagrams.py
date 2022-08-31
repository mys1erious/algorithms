from collections import defaultdict


def group_anagrams(strs):
    hashmap = defaultdict(list)

    for s in strs:

        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1

        hashmap[tuple(count)].append(s)

    return hashmap.values()


if __name__ == '__main__':
    strs1 = ["eat", "tea", "tan", "ate", "nat", "bat"]  # Output: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
    strs2 = [""]  # Output: [[""]]
    strs3 = ["a", "b"]  # Output: [["a"]]
    strs4 = ["ddddddddddg", "dgggggggggg"]

    assert group_anagrams(strs1) == [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
    #assert group_anagrams(strs2) == [[""]]
    #assert group_anagrams(strs3) == [["a"], ["b"]]
    #assert group_anagrams(strs4) == [["dgggggggggg"],["ddddddddddg"]]
