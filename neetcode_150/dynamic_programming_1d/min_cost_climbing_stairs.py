def min_cost_climb_stairs(cost: list[int]) -> (int, list[int]):

    i = len(cost)-3
    while i >= 0:
        cost[i] += min(cost[i+1], cost[i+2])
        i -= 1
        # if cost[i+1] < cost[i+2]:
        #     cost[i] += cost[i+1]
        #     i-=1
        # else:
        #     cost[i] += cost[i+2]
        #     i-=1

    return min(cost[0], cost[1])


if __name__ == '__main__':
    cost1: list[int] = [10, 15, 20]
    cost2: list[int] = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    cost3: list[int] = [0, 2, 2, 1]

    assert min_cost_climb_stairs(cost1) == 15
    assert min_cost_climb_stairs(cost2) == 6
    assert min_cost_climb_stairs(cost3) == 2
