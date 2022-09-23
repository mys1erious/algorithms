def car_fleet(target, position, speed):
    car_fleets = 0
    max_time = 0
    for pos, spd in sorted(zip(position, speed))[::-1]:
        dist = target-pos
        time = dist / spd

        if car_fleets == 0 or time > max_time:
            max_time = time
            car_fleets += 1

    return car_fleets


if __name__ == '__main__':
    target1 = 12
    position1 = [10, 8, 0, 5, 3]
    speed1 = [2, 4, 1, 1, 3]  # Output: 3

    target2 = 10
    position2 = [3]
    speed2 = [3]  # Output: 1

    target3 = 100
    position3 = [0, 2, 4]
    speed3 = [4, 2, 1]  # Output: 1

    assert car_fleet(target1, position1, speed1) == 3
    assert car_fleet(target2, position2, speed2) == 1
    assert car_fleet(target3, position3, speed3) == 1
