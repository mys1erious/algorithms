def is_palindrome(s):
    s = ''.join([c for c in s if c.isalnum()]).lower()

    return s == s[::-1]


if __name__ == '__main__':
    s1 = "A man, a plan, a canal: Panama"  # Output: true
    s2 = "race a car"  # Output: false
    s3 = " "  # Output: true

    assert is_palindrome(s1) == True
    assert is_palindrome(s2) == False
    assert is_palindrome(s3) == True
