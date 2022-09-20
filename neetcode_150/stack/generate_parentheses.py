def generate_parentheses(n):
    stack = []
    res = []

    def backtrack(opened, closed):
        if opened == closed == n:
            res.append(''.join(stack))
            return

        if opened < n:
            stack.append('(')
            backtrack(opened+1, closed)
            stack.pop()

        if closed < opened:
            stack.append(')')
            backtrack(opened, closed+1)
            stack.pop()

    backtrack(0, 0)
    return res


if __name__ == '__main__':
    n1 = 3  # Output: ["((()))", "(()())", "(())()", "()(())", "()()()"]
    n2 = 1  # Output: ["()"]
    n3 = 2  # ["()()", "(())"]

    assert generate_parentheses(n1) == ["((()))", "(()())", "(())()", "()(())", "()()()"]
    assert generate_parentheses(n1) == ["()"]
