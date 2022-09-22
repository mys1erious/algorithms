def generate_parentheses(n):
    res = []

    def dfs(left, right, s=''):
        if right > left: return
        if left == n and right == n:
            res.append(s)
            return
        if left < n:
            dfs(left+1, right, s+'(')
        if right < n:
            dfs(left, right+1, s+')')

    dfs(0, 0)
    return res


if __name__ == '__main__':
    n1 = 3  # Output: ["((()))", "(()())", "(())()", "()(())", "()()()"]
    n2 = 1  # Output: ["()"]
    n3 = 2  # ["()()", "(())"]

    assert generate_parentheses(n1) == ["((()))", "(()())", "(())()", "()(())", "()()()"]
    assert generate_parentheses(n2) == ["()"]
