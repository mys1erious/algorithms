s1 = "A man, a plan, a canal: Panama"
s2 = "a."
s3 = ".,"
s4 = "race a car"
s5 = "a.b,."


def is_palindrome(s: str) -> bool:
    n = len(s)

    lp = 0
    rp = -1
    while lp < n:
        if not s[lp].isalnum():
            lp += 1
            continue
        if not s[rp].isalnum():
            rp -= 1
            continue

        if s[lp].lower() != s[rp].lower():
            return False

        lp += 1
        rp -= 1
    return True


print(is_palindrome(s1))
print(is_palindrome(s2))
print(is_palindrome(s3))
print(is_palindrome(s4))
print(is_palindrome(s5))
