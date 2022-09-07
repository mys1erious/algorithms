import collections


def add_to_dict_of_sets(dct, key, val):
    try:
        dct[key].add(val)
    except KeyError:
        dct[key] = set()
        dct[key].add(val)


def key_in_dict(dct, key):
    try:
        dct[key]
        return True
    except KeyError:
        return False


def isValidSudoku(board):
    n = len(board)

    rows = {}
    cols = {}
    squares = {}

    for row in range(n):
        for col in range(n):
            sq_row = row//3
            sq_col = col//3

            val = board[row][col]
            if val == '.':
                continue

            if (key_in_dict(rows, row) and val in rows[row] or
                key_in_dict(cols, col) and val in cols[col] or
                key_in_dict(squares, (sq_row, sq_col)) and val in squares[sq_row, sq_col]
            ):
                return False

            add_to_dict_of_sets(rows, row, val)
            add_to_dict_of_sets(cols, col, val)
            add_to_dict_of_sets(squares, (sq_row, sq_col), val)

    return True


if __name__ == '__main__':
    board1 = [  # Should return True
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

    board2 = [  # Should return False
        ["8", "8", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

    assert isValidSudoku(board1) == True
    assert isValidSudoku(board2) == False

# My own initial solution
# def isValidSudoku(board):
#     n = 9
#
#     cols = [[] for _ in range(n)]
#     for row in range(n):
#         row_vals = [int(v) for v in board[row] if v.isdigit()]
#         if len(row_vals) != len(set(row_vals)):
#             return False
#
#         for col in range(n):
#             if board[row][col].isdigit():
#                 cols[col].append(board[row][col])
#
#     for col in cols:
#         if len(col) != len(set(col)):
#             return False
#
#     edges = [0, 3, 0, 3]
#     row_offset = 0
#     col_offset = 0
#     for i in range(1, n+1):
#         row_start = edges[0] + row_offset
#         row_end = edges[1] + row_start
#         col_start = edges[2] + col_offset
#         col_end = edges[3] + col_offset
#         full_rows = board[row_start:row_end]
#         block = [row[col_start:col_end] for row in full_rows]
#
#         block_vals = [int(v) for v in [i for sub in block for i in sub] if v.isdigit()]
#         if len(block_vals) != len(set(block_vals)):
#             return False
#
#         if i % 3 == 0:
#             row_offset += 3
#             col_offset = 0
#         else:
#             col_offset += 3
#
#     return True
