from typing import List


def subsets(nums: List[int]) -> List[List[int]]:
    n = len(nums)
    res = []

    cur = []
    def dfs(i):
        if i >= n:
            res.append(cur.copy())
            return

        cur.append(nums[i])
        dfs(i+1)

        cur.pop()
        dfs(i+1)

    dfs(0)
    return res


if __name__ == '__main__':
    nums1 = [1,2,3]
    nums2 = [0]

    ans1 = subsets(nums1)
    ans2 = subsets(nums2)

    print(ans1)
    print(ans2)

    # assert ans1 == [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
    # assert ans2 == [[],[0]]
