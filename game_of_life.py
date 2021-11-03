def gameOfLife(board) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    m = len(board)
    n = len(board[0])

    ## mapping ##
    # 0,1 -> 2
    # 1,0 -> 3
    # 1,1 -> 4
    # 0,0 -> 5
    living = [2, 4, 1]

    def evaluate(row, col):
        value = board[row][col]
        if value == 3 or value == 4 or value == 1:
            return 1
        else:
            return 0

    for row in range(m):
        for col in range(n):
            counts = 0
            if board[row][col] == 0:
                for i, j in ((row + 1, col), (row - 1, col), (row, col + 1),
                             (row, col - 1), (row - 1, col - 1), (row - 1, col + 1),
                             (row + 1, col - 1), (row + 1, col + 1)):
                    if i >= 0 and i < m and j >= 0 and j < n:
                        counts += evaluate(i, j)
                if counts == 3:
                    board[row][col] = 2
                else:
                    board[row][col] = 5
            else:
                for i, j in ((row + 1, col), (row - 1, col), (row, col + 1),
                             (row, col - 1), (row - 1, col - 1), (row - 1, col + 1),
                             (row + 1, col - 1), (row + 1, col + 1)):
                    if i >= 0 and i < m and j >= 0 and j < n:
                        counts += evaluate(i, j)
                if counts < 2 or counts > 3:
                    board[row][col] = 3
                else:
                    board[row][col] = 4

    for row in range(m):
        for col in range(n):
            if board[row][col] in living:
                board[row][col] = 1
            else:
                board[row][col] = 0
    return board


print(gameOfLife([[1, 0, 1],
                  [0, 0, 1],
                  [1, 1, 0]]))
