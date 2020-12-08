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


# Function to check if it safe to put 'ch' at board[row][col]
def isSafe(board, row, col, ch, top, left, bottom, right):
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


# Function to validate Configuration of output board
def validate(board, top, left, bottom, right):
    for i in range(N):
        if top[i] != -1 and countInColumn(board, '+', i) != top[i]:
            return False
        if bottom[i] != -1 and countInColumn(board, '-', i) != bottom[i]:
            return False
    for j in range(M):
        if left[j] != -1 and countInRow(board, '+', j) != left[j]:
            return False
        if right[j] != -1 and countInRow(board, '-', j) != right[j]:
            return False
    # Passed all checks, valid board
    return True


def solve(board, row, col, top, left, bottom, right, slots):
    # if we have reached last cell
    if row >= M - 1 and col >= N - 1:
        return validate(board, top, left, bottom, right)

    # if last column of current row is already processed, go to next row, first column
    if col >= N:
        col = 0
        row = row + 1

    # if current cell contains R (end of horizontal slot) or B (end of vertical slot) recur for next cell
    if slots[row][col] == 'R' or slots[row][col] == 'B':
        if solve(board, row, col + 1, top, left, bottom, right, slots):
            return True

    # if horizontal slot contains L and R
    if slots[row][col] == 'L' and slots[row][col + 1] == 'R':
        # put ('+', '-') pair and recur
        if isSafe(board, row, col, '+', top, left, bottom, right) and isSafe(board, row, col + 1, '-', top, left, bottom, right):
            board[row][col] = '+'
            board[row][col + 1] = '-'
            if solve(board, row, col + 2, top, left, bottom, right, slots):
                return True
            # if it doesn't lead to a solution, backtrack
            board[row][col] = 'X'
            board[row][col + 1] = 'X'

        # put ('-', '+') pair and recur
        if isSafe(board, row, col, '-', top, left, bottom, right) and isSafe(board, row, col + 1, '+', top, left, bottom, right):
            board[row][col] = '-'
            board[row][col + 1] = '+'
            if solve(board, row, col + 2, top, left, bottom, right, slots):
                return True
            # if it doesn't lead to a solution, backtrack
            board[row][col] = 'X'
            board[row][col + 1] = 'X'

    # if vertical slot contains T and B
    if slots[row][col] == 'T' and slots[row + 1][col] == 'B':
        # put ('+', '-') pair and recur
        if isSafe(board, row, col, '+', top, left, bottom, right) and isSafe(board, row + 1, col, '-', top, left, bottom, right):
            board[row][col] = '+'
            board[row + 1][col] = '-'
            if solve(board, row, col + 1, top, left, bottom, right, slots):
                return True
            # if it doesn't lead to a solution, backtrack
            board[row][col] = 'X'
            board[row + 1][col] = 'X'

        # put ('-', '+') pair and recur
        if isSafe(board, row, col, '-', top, left, bottom, right) and isSafe(board, row + 1, col, '+', top, left, bottom, right):
            board[row][col] = '-'
            board[row + 1][col] = '+'
            if solve(board, row, col + 1, top, left, bottom, right, slots):
                return True
            # if it doesn't lead to a solution, backtrack
            board[row][col] = 'X'
            board[row + 1][col] = 'X'

    # ignore current cell and recur
    if solve(board, row, col + 1, top, left, bottom, right, slots):
        return True

    # if no solution is possible, return false
    return False


if __name__ == '__main__':
    # indicates the count of + or - at the top (+), bottom (-), left (+) and right (-) edges respectively.
    # value of -1 indicates any number of + or - signs
    top = [1, -1, -1, 2, 1, -1]
    bottom = [2, -1, -1, 2, -1, 3]
    left = [2, 3, -1, -1, -1]
    right = [-1, -1, -1, 1, -1]
    slots = [
        ['L', 'R', 'L', 'R', 'T', 'T'],
        ['L', 'R', 'L', 'R', 'B', 'B'],
        ['T', 'T', 'T', 'T', 'L', 'R'],
        ['B', 'B', 'B', 'B', 'T', 'T'],
        ['L', 'R', 'L', 'R', 'B', 'B']
    ]

    (M, N) = (5, 6)
    board = [['X' for x in range(N)] for y in range(M)]
    if solve(board, 0, 0, top, left, bottom, right, slots):
        for i in range(M):
            for j in range(N):
                print(board[i][j], end=' ')
            print()
    else:
        print("Solution does not exist")
