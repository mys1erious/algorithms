def set_zeros(matrix):
    m = len(matrix)
    n = len(matrix[0])

    for row in range(m):
        for col in range(n):
            if matrix[row][col] == 0:
                matrix[row][:] = [0] * n
                matrix[:][col] = [0] * m


if __name__ == '__main__':
    matrix1 = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ]
    # [
    # [1, 0, 1],
    # [0, 0, 0],
    # [1, 0, 1]
    # ]

    matrix2 = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]  # [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

    print(matrix1)
    set_zeros(matrix1)
    print(matrix1)
