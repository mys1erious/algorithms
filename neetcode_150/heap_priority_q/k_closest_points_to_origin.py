from collections import defaultdict
from typing import List
import math
import heapq


def euc_dist(x1, x2, y1, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)


def kClosest(points: List[List[int]], k: int) -> List[List[int]]:
    distances = []
    for x, y in points:
        distances.append((math.sqrt((0-x)**2 + (0-y)**2), x, y))
    heapq.heapify(distances)

    res = []
    while k > 0:
        _, x, y = heapq.heappop(distances)
        res.append([x, y])
        k-=1
    return res


if __name__ == '__main__':
    points1, k1 = [[1,3],[-2,2]], 1
    points2, k2 = [[3, 3], [5, -1], [-2, 4]], 2
    points3, k3 = [[0,1],[1,0]], 2
    points4, k4 = [[6,10],[-3,3],[-2,5],[0,2]], 3

    res1 = kClosest(points1, k1)
    res2 = kClosest(points2, k2)
    res3 = kClosest(points3, k3)
    res4 = kClosest(points4, k4)

    print(res1)
    print(res2)
    print(res3)
    print(res4)

    assert res1 == [[-2,2]]
    assert res2 == [[3,3],[-2,4]]
    assert res3 == [[0,1],[1,0]]
