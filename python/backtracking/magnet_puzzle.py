class MagnetPuzzle:
    def __init__(self, size, top, bottom, left, right, slots):
        self.M, self.N = size
        self.top, self.bottom, self.left, self.right = top, bottom, left, right
        self.slots = slots
        self.board = [['X' for j in range(N)] for i in range(M)]

    def display(self):
        if self.solve(0, 0):
            for i in range(self.M):
                for j in range(self.N):
                    print(self.board[i][j], end=' ')
                print()
        else:
            print("Solution does not exist")

    # A utility function to count number of characters ch in current column j
    def countInColumn(self, ch, j):
        count = 0
        for i in range(self.M):
            if self.board[i][j] == ch:
                count += 1
        return count

    # A utility function to count number of characters ch in current row i
    def countInRow(self, ch, i):
        count = 0
        for j in range(self.N):
            if self.board[i][j] == ch:
                count += 1
        return count

    # Function to check if it safe to put 'ch' at board[row][col]
    def isSafe(self, row, col, ch):
        # check for contents of adjacent cells to ensure they don't contain same character
        if ((row - 1 >= 0 and self.board[row - 1][col] == ch) or (col + 1 < N and self.board[row][col + 1] == ch) or
                (row + 1 < M and self.board[row + 1][col] == ch) or (col - 1 >= 0 and self.board[row][col - 1] == ch)):
            return False

        rowCount = self.countInRow(ch, row)
        colCount = self.countInColumn(ch, col)

        # if given character is '+', check top & left
        if ch == '+':
            if self.top[col] != -1 and colCount >= self.top[col]:
                return False
            if self.left[row] != -1 and rowCount >= self.left[row]:
                return False

        # if given character is '-', check bottom & right
        if ch == '-':
            if self.bottom[col] != -1 and colCount >= self.bottom[col]:
                return False
            if self.right[row] != -1 and rowCount >= self.right[row]:
                return False

        # Passed all checks, allowed to put character in the board
        return True

    # Function to validate Configuration of output board
    def validate(self):
        for i in range(self.N):
            if self.top[i] != -1 and self.countInColumn('+', i) != self.top[i]:
                return False
            if self.bottom[i] != -1 and self.countInColumn('-', i) != self.bottom[i]:
                return False
        for j in range(self.M):
            if self.left[j] != -1 and self.countInRow('+', j) != self.left[j]:
                return False
            if self.right[j] != -1 and self.countInRow('-', j) != self.right[j]:
                return False
        # Passed all checks, valid board
        return True

    def solve(self, row, col):
        top, bottom, left, right = self.top, self.bottom, self.left, self.right
        slots, board = self.slots, self.board
        isSafe = self.isSafe
        # if we have reached last cell
        if row >= self.M - 1 and col >= self.N - 1:
            return self.validate()

        # if last column of current row is already processed, go to next row, first column
        if col >= self.N:
            col = 0
            row = row + 1

        # if current cell contains R (end of horizontal slot) or B (end of vertical slot) recur for next cell
        if slots[row][col] == 'R' or slots[row][col] == 'B':
            if self.solve(row, col + 1):
                return True

        # if horizontal slot contains L and R
        if slots[row][col] == 'L' and slots[row][col + 1] == 'R':
            # put ('+', '-') pair and recur
            if isSafe(row, col, '+') and isSafe(row, col + 1, '-'):
                board[row][col] = '+'
                board[row][col + 1] = '-'
                if self.solve(row, col + 2):
                    return True
                # if it doesn't lead to a solution, backtrack
                board[row][col] = 'X'
                board[row][col + 1] = 'X'

            # put ('-', '+') pair and recur
            if isSafe(row, col, '-') and isSafe(row, col + 1, '+'):
                board[row][col] = '-'
                board[row][col + 1] = '+'
                if self.solve(row, col + 2):
                    return True
                # if it doesn't lead to a solution, backtrack
                board[row][col] = 'X'
                board[row][col + 1] = 'X'

        # if vertical slot contains T and B
        if slots[row][col] == 'T' and slots[row + 1][col] == 'B':
            # put ('+', '-') pair and recur
            if isSafe(row, col, '+') and isSafe(row + 1, col, '-'):
                board[row][col] = '+'
                board[row + 1][col] = '-'
                if self.solve(row, col + 1):
                    return True
                # if it doesn't lead to a solution, backtrack
                board[row][col] = 'X'
                board[row + 1][col] = 'X'

            # put ('-', '+') pair and recur
            if isSafe(row, col, '-') and isSafe(row + 1, col, '+'):
                board[row][col] = '-'
                board[row + 1][col] = '+'
                if self.solve(row, col + 1):
                    return True
                # if it doesn't lead to a solution, backtrack
                board[row][col] = 'X'
                board[row + 1][col] = 'X'

        # ignore current cell and recur
        if self.solve(row, col + 1):
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

    ob = MagnetPuzzle((M, N), top, bottom, left, right, slots)
    ob.display()
