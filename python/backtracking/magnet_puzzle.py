# Function to check if it safe to put 'ch' at board[row][col]
def isSafe(board, row, col, ch, top, left, bottom, right):
    # A utility function to count number of characters ch in current column j
    def countInColumn(board, ch, j):
        count = 0
        for i in range(M):
            if board[i][j] == ch:
                count = count + 1
        return count

    # A utility function to count number of characters ch in current row i
    def countInRow(board, ch, i):
        count = 0
        for j in range(N):
            if board[i][j] == ch:
                count = count + 1
        return count

    # check for contents of adjacent cells to ensure they don't contain same character
    if ((row - 1 >= 0 and board[row - 1][col] == ch) or (col + 1 < N and board[row][col + 1] == ch) or
            (row + 1 < M and board[row + 1][col] == ch) or (col - 1 >= 0 and board[row][col - 1] == ch)):
        return False

    rowCount = countInRow(board, ch, row)
    colCount = countInColumn(board, ch, col)

    # if given character is '+', check top & left
    if ch == '+':
        if top[col] != -1 and colCount >= top[col]:
            return False
        if left[row] != -1 and rowCount >= left[row]:
            return False

    # if given character is '-', check bottom & right
    if ch == '-':
        if bottom[col] != -1 and colCount >= bottom[col]:
            return False
        if right[row] != -1 and rowCount >= right[row]:
            return False

    # Passed all checks, allowed to put character in the board
    return True


if __name__ == '__main__':
    # indicates the count of + or - at the top (+), bottom (-), left (+) and right (-) edges respectively.
    # value of -1 indicates any number of + or - signs
    top = [1, -1, -1, 2, 1, -1]
    bottom = [2, -1, -1, 2, -1, 3]
    left = [2, 3, -1, -1, -1]
    right = [-1, -1, -1, 1, -1]

    # rules matrix
    str = [
        ['L', 'R', 'L', 'R', 'T', 'T'],
        ['L', 'R', 'L', 'R', 'B', 'B'],
        ['T', 'T', 'T', 'T', 'L', 'R'],
        ['B', 'B', 'B', 'B', 'T', 'T'],
        ['L', 'R', 'L', 'R', 'B', 'B']
    ]

    (M, N) = (5, 6)
