def max_profit(prices):
    # Need to return max dif of buy_price, sell_price

    # Brute Force:
    # profit = 0
    # for i in range(len(prices)):
    #     for j in range(i, len(prices)):
    #         dif = prices[j] - prices[i]
    #         if dif > profit:
    #             profit = dif
    #
    # return profit

    # 2 pointers?
    profit = 0
    lp = 0
    rp = 1
    while lp < rp < len(prices):
        if prices[rp] > prices[lp]:
            dif = prices[rp] - prices[lp]
            if dif > profit:
                profit = dif

        if prices[rp] < prices[lp]:
            lp = rp
            rp += 1
        else:
            rp += 1

    return profit


if __name__ == '__main__':
    prices1 = [7, 1, 5, 3, 6, 4]  # Output: 5
    prices2 = [7, 6, 4, 3, 1]  # Output: 0

    assert max_profit(prices1) == 5
    assert max_profit(prices2) == 0
