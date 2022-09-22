from collections import deque


def daily_temps(temperatures):
    ans = [0] * len(temperatures)

    # Brute Force: T: O(n^2), M: O(n)
    # for i in range(n):
    #     count = 0
    #     for j in range(i, n):
    #         if temperatures[j] > temperatures[i]:
    #             ans.append(count)
    #             break
    #         elif j == n-1:
    #             ans.append(0)
    #
    #         count += 1

    # T: O(n), M: O(n)
    # 'stack' takes extra n, so M is O(2n) actually

    stack = []
    for i, t in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < t:
            cur = stack.pop()
            ans[cur] = i - cur
        stack.append(i)

    return ans


if __name__ == '__main__':
    temperatures1 = [73, 74, 75, 71, 69, 72, 76, 73]  # Output: [1, 1, 4, 2, 1, 1, 0, 0]
    temperatures2 = [30,40,50,60]  # Output: [1,1,1,0]
    temperatures3 = [30, 60, 90]  # Output: [1, 1, 0]

    assert daily_temps(temperatures1) == [1, 1, 4, 2, 1, 1, 0, 0]
    assert daily_temps(temperatures2) == [1,1,1,0]
    assert daily_temps(temperatures3) == [1, 1, 0]
