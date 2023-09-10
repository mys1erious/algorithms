def input1():
    pass


# -- My solution
# Insert: O(n^2)
# Space: O(n^2)
# Search: O(1)
# WORD = 'word'
# PREFIX = 'prefix'
# class Trie:
#     def __init__(self):
#         self.hash_map = {}
#
#     def insert(self, word: str) -> None:
#         for i in range(1, len(word)):
#             prefix = word[:i]
#             if not self.hash_map.get(prefix):
#                 self.hash_map[prefix] = PREFIX
#         self.hash_map[word] = WORD
#
#     def search(self, word: str) -> bool:
#         return True if self.hash_map.get(word) == WORD else False
#
#     def startsWith(self, prefix: str) -> bool:
#         # return any(k for k in self.hash_map.keys() if k.startswith(prefix))
#         return True if self.hash_map.get(prefix) else False


# Prefix Tree
# Insert: O(n)
# Space: O(n)
# Search: O(n)
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word_end = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.word_end

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True


if __name__ == '__main__':
    trie1 = Trie()
    trie1.insert("apple")
    print(trie1.search("apple"))
    print(trie1.search("app"))
    print(trie1.startsWith("app"))
    trie1.insert("app")
    print(trie1.search("app"))
