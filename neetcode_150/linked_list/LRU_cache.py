from collections import deque


# My first solution, T: O(n), M: O(n)
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self._cache = {}
        self._order = deque()
        self._key_node_map = {}

    def get(self, key: int) -> int:
        if key in self._cache:
            self._move_to_end(key)
            return self._cache[key]
        return -1

    def _move_to_end(self, key):
        self._order.remove(key)
        self._order.append(key)

    def put(self, key: int, value: int) -> None:
        if key in self._cache:
            self._move_to_end(key)
        else:
            if self.at_max_capacity:
                least_recently_used = self._order.popleft()
                del self._cache[least_recently_used]
            self._order.append(key)

        self._cache[key] = value

    @property
    def at_max_capacity(self):
        return len(self._cache) == self.capacity


# Solution 2 (optimized) T: O(1), M: O(n)
# TODO: make sure to fully understand
# class Node:
#     def __init__(self, key, val):
#         self.key, self.val = key, val
#         self.prev = self.next = None
#
#
# class LRUCache:
#     def __init__(self, capacity: int):
#         self.cap = capacity
#         self.cache = {}  # map key to node
#
#         self.left, self.right = Node(0, 0), Node(0, 0)
#         self.left.next, self.right.prev = self.right, self.left
#
#     # remove node from list
#     def remove(self, node):
#         prev, nxt = node.prev, node.next
#         prev.next, nxt.prev = nxt, prev
#
#     # insert node at right
#     def insert(self, node):
#         prev, nxt = self.right.prev, self.right
#         prev.next = nxt.prev = node
#         node.next, node.prev = nxt, prev
#
#     def get(self, key: int) -> int:
#         if key in self.cache:
#             self.remove(self.cache[key])
#             self.insert(self.cache[key])
#             return self.cache[key].val
#         return -1
#
#     def put(self, key: int, value: int) -> None:
#         if key in self.cache:
#             self.remove(self.cache[key])
#         self.cache[key] = Node(key, value)
#         self.insert(self.cache[key])
#
#         if len(self.cache) > self.cap:
#             # remove from the list and delete the LRU from hashmap
#             lru = self.left.next
#             self.remove(lru)
#             del self.cache[lru.key]


if __name__ == '__main__':
    lRUCache = LRUCache(2)
    lRUCache.put(1, 1)  # cache is {1 = 1}
    lRUCache.put(2, 2)  # cache is {1 = 1, 2 = 2}
    lRUCache.get(1)  # return 1
    lRUCache.put(3, 3)  # LRU key was 2, evicts key2, cache is {1 = 1, 3 = 3}
    lRUCache.get(2)  # returns - 1(not found)
    lRUCache.put(4, 4)  # LRU key was 1, evicts key 1, cache is {4 = 4, 3 = 3}
    lRUCache.get(1)  # return -1(not found)
    lRUCache.get(3)  # return 3
    lRUCache.get(4)  # return 4
