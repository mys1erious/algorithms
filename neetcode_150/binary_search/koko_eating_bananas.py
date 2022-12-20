import math


def min_eating_speed(piles: list[int], h: int) -> int:
    '''
    :param piles[i]: - num of bananas in pile i
    :param h: - hours before the guard comes back
    :var n: - num of piles
    :var k: - bananas-per-hour eating speed

    :Desc:
    each hour she eats k bananas from 1 pile
    if piles[i] < k: she eats all of them and won't eat any more during this hour;
    likes to eat slowly, but wants to finish all the bananas before the guard returns

    :return: min. k such that she can eat all the bananas in h hours
    '''
    lp = 1
    rp = max(piles)
    k = rp
    while lp <= rp:
        mp = (lp + rp) // 2
        cur_h = 0
        for pile in piles:
            cur_h += math.ceil(pile / mp)
            if cur_h > h:
                lp = mp + 1
                break

        if not cur_h > h:
            rp = mp - 1
            k = min(k, mp)

    return k


if __name__ == '__main__':
    piles1 = [3,6,7,11]
    h1 = 8
    piles2 = [30, 11, 23, 4, 20]
    h2 = 5  # k = 30
    piles3 = [30, 11, 23, 4, 20]
    h3 = 6  # k = 23

    assert min_eating_speed(piles1, h1) == 4
    assert min_eating_speed(piles2, h2) == 30
    assert min_eating_speed(piles3, h3) == 23
