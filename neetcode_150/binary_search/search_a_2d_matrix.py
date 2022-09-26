def search_binary_2d_matrix(matrix: list[list[int]], target: int) -> bool:
    m = len(matrix)
    n = len(matrix[0])

    lp = 0
    rp = (m*n) - 1
    while lp <= rp:
        mp = (rp+lp) // 2
        rowp = mp // n
        colp = mp % n

        if target < matrix[rowp][colp]:
            rp = mp-1
        elif target > matrix[rowp][colp]:
            lp = mp+1
        else:
            return True

    return False


if __name__ == '__main__':
    matrix4 = [[1]]
    target4 = 0

    matrix1 = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60]]
    target1 = 3

    matrix2 = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60]]
    target2 = 30

    matrix3 = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60]]
    target3 = 13

    assert search_binary_2d_matrix(matrix1, target1) == True
    assert search_binary_2d_matrix(matrix2, target2) == True
    assert search_binary_2d_matrix(matrix3, target3) == False
    assert search_binary_2d_matrix(matrix4, target4) == False
