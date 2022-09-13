def max_area(height):
    # n - vertical lines
    # i - ith line
    # height[i] - ith height
    # Find 2 lines that form a container, such that the container contains most water
    # Cant slant the container
    # Return area of the container

    # If line1 < line2, then ur height of container = to line1, cuz otherwise the water will be spilled

    # Brute-Force: T: O(n^2), M: O(1)
    #   For each line I can compare it to all other lines and return max
    # area = 0
    # for i in range(len(height)):
    #     for j in range(i+1, len(height)):
    #         cur_height = min(height[i], height[j])
    #         cur_len = j - i
    #         cur_area = cur_height * cur_len
    #         if cur_area > area:
    #             area = cur_area
    # return area

    # Optimization, shifting lowest side line: T: O(n), M: O(1)
    # l = 0, r = n-1
    # shift pointers with lowest height
    area = 0

    lp = 0
    rp = len(height) - 1
    while lp < rp:
        cur_area = get_area_between_pointers(height, lp, rp)

        if cur_area > area:
            area = cur_area

        if height[lp] > height[rp]:
            rp = shift_right_pointer(height, lp, rp)
        else:
            lp = shift_left_pointer(height, lp, rp)

    return area


def get_area_between_pointers(height, lp, rp):
    cur_height = min(height[lp], height[rp])
    cur_len = rp - lp
    return cur_height * cur_len


def shift_right_pointer(height, lp, rp):
    cur_r_height = height[rp]
    rp -= 1
    while height[rp] < cur_r_height and lp < rp:
        rp -= 1
    return rp


def shift_left_pointer(height, lp, rp):
    cur_l_height = height[lp]
    lp += 1
    while height[lp] < cur_l_height and lp < rp:
        lp += 1
    return lp


if __name__ == '__main__':
    height1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]  # Output: 49
    height2 = [1, 1]  # Output: 1

    assert max_area(height1) == 49
    assert max_area(height2) == 1
