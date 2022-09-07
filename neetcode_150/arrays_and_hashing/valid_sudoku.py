class SetsObject:
    def __init__(self):
        self.__data = {}

    def __setitem__(self, key, value):
        if not isinstance(value, set):
            raise TypeError(f'Can assign only \'set\' type, given: {type(value)}')
        self.__data[key] = value

    def __getitem__(self, item):
        try:
            return self.__data[item]
        except KeyError:
            self.__data[item] = set()
            return self.__data[item]

    def __str__(self):
        return str(self.__data)

    def __repr__(self):
        return str(self.__data)


def isValidSudoku2(board):
    n = len(board)

    rows = SetsObject()
    cols = SetsObject()
    blocks = SetsObject()

    for row in range(n):
        for col in range(n):
            block_row = row//3
            block_col = col//3

            val = board[row][col]
            if val == '.':
                continue

            if (val in rows[row] or val in cols[col] or val in blocks[block_row, block_col]
            ):
                return False

            rows[row].add(val)
            cols[col].add(val)
            blocks[block_row, block_col].add(val)

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

    assert isValidSudoku2(board1) == True
    assert isValidSudoku2(board2) == False

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
