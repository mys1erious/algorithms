import heapq
from typing import List


def lastStoneWeight(stones: List[int]) -> int:
    stones = [-val for val in stones]
    heapq.heapify(stones)
    while len(stones) >= 2:
        y, x = heapq.heappop(stones), heapq.heappop(stones)
        if x != y:
            y -= x
            heapq.heappush(stones, y)
    return -stones[0] if len(stones) == 1 else 0


if __name__ == '__main__':
    stones1 = [2,7,4,1,8,1]

    res1 = lastStoneWeight(stones1)

    print(res1)

    assert res1 == 1
