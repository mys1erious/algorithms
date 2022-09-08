def is_unique(s):
    hash = {}

    for i, c in enumerate(s):
        if c in hash:
            return True
        hash[c] = i
    return False


# Rework
def is_unique_no_ds(s):
    in_chars = ''
    for c in s:
        if c in in_chars:
            return True
        in_chars += c
    return False
