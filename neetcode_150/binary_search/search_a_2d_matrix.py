def search_binary_2d_matrix(matrix: list[list[int]], target: int) -> bool:
    m: int = len(matrix)
    n: int = len(matrix[0])

    left: int = 0
    right: int = m*n-1
    mid = right // 2

    while left <= right:
        row = mid // n
        col = mid % n

        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            left = mid + 1
        elif matrix[row][col] > target:
            right = mid - 1

        mid = (left + right) // 2

    return False


if __name__ == '__main__':
    matrix4 = [
        [1]
    ]
    target4 = 0

    matrix1 = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60]
    ]
    target1 = 3

    matrix2 = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60]
    ]
    target2 = 30

    matrix3 = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60]
    ]
    target3 = 13

    assert search_binary_2d_matrix(matrix1, target1), True
    assert search_binary_2d_matrix(matrix2, target2), True
    print(search_binary_2d_matrix(matrix3, target3) is False)
    print(search_binary_2d_matrix(matrix4, target4) is False)
