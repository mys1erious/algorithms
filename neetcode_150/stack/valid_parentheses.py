P_HASH = {
    ')': '(',
    '}': '{',
    ']': '['
}


def is_valid(s: str) -> bool:
    p_stack = []
    for char in s:
        if char in P_HASH.values():
            p_stack.append(char)
        elif char in P_HASH.keys():
            if p_stack.pop() != P_HASH[char]:
                return False

    if not p_stack:
        return True
    return False


if __name__ == '__main__':
    s1 = "(()"
    s2 = "()[]{}"
    s3 = "(]"

    assert is_valid(s1) is True
    assert is_valid(s2) is True
    assert is_valid(s3) is False
