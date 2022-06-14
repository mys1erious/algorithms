def climb_stairs(n: int) -> int:
    next1 = 1
    next2 = 1

    for step in range(n-1):
        tmp = next1
        next1 = next1 + next2
        next2 = tmp
    return next1


if __name__ == '__main__':
    assert climb_stairs(5) == 8
    assert climb_stairs(2) == 2
    assert climb_stairs(3) == 3
