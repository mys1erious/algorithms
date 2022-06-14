import math


def min_eating_speed(piles: list[int], h: int) -> int:
    left = 1
    right = max(piles)
    res = right

    while left <= right:
        k = (left + right) // 2
        hrs_left = h

        for pile in piles:
            hrs_to_eat_pile = math.ceil(pile / k)
            hrs_left -= hrs_to_eat_pile

        if hrs_left < 0:
            left = k + 1
        elif hrs_left >= 0:
            res = min(res, k)
            right = k-1

    return res


if __name__ == '__main__':
    piles1 = [3,6,7,11]
    h1 = 8

    piles2 = [30, 11, 23, 4, 20]
    h2 = 5  # k = 30
    piles3 = [30, 11, 23, 4, 20]
    h3 = 6  # k = 23
    piles4 = [312884470]
    h4 = 312884469  # k = 2

    assert min_eating_speed(piles1, h1), 4
    assert min_eating_speed(piles2, h2), 30
    assert min_eating_speed(piles3, h3), 23
    assert min_eating_speed(piles4, h4), 2
