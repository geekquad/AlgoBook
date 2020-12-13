class MagnetPuzzle:
    """Class to solve the magnet puzzle solution"""

    def __init__(self, size, top, bottom, left, right, slots):
        """
        Constructor which takes input values
        Parameters
        size   - the size of the board in the form of a tuple
        top    - array with entries corresponding to '+' in columns
        bottom - array with entries corresponding to '-' in columns
        left   - array with entries corresponding to '+' in rows
        right  - array with entries corresponding to '-' in rows
        slots  - matrix that stores the data of slots LR for horizontal slot TB for vertical slot
        """

        self.M, self.N = size
        self.top, self.bottom, self.left, self.right = top, bottom, left, right
        self.slots = slots
        self.board = [['X' for j in range(N)] for i in range(M)]

    
    def checkConstraints(self, row, col, ch):
        """
        Function to check if it safe to put 'ch' at board[row][col]
        Parameters
        row, col - cell where the chracter ch is to put
        ch       - the character to be put
        """
        
        # Check for contents of orthogonal adjacent cells to ensure they don't contain same character
        board = self.board
        top, bottom = row - 1 >= 0 and board[row - 1][col] == ch, row + 1 < M and board[row + 1][col] == ch
        left, right = col - 1 >= 0 and board[row][col - 1] == ch, col + 1 < N and board[row][col + 1] == ch
        if top or right or bottom  or left:
            return False

        # If given character is '+', check top & left if given character is '-', check bottom & right
        top, bottom, left, right = self.top, self.bottom, self.left, self.right
        rowCount = sum([board[row][j] == ch for j in range(self.N)])
        colCount = sum([board[i][col] == ch for i in range(self.M)])
        if ch == '+':
            if (top[col] != -1 and colCount >= top[col]) or (left[row] != -1 and rowCount >= left[row]):
                return False
        elif ch == '-':
            if (bottom[col] != -1 and colCount >= bottom[col]) or (right[row] != -1 and rowCount >= right[row]):
                return False
        
        return True

    
    def validate(self):
        """
        Function to validate Configuration of output board
        """
        
        def countInRow(ch, i):
            return sum([self.board[i][j] == ch for j in range(self.N)])
        for i in range(self.M):
            if self.left[i] not in [-1, countInRow('+', i)] or self.right[i] not in [-1, countInRow('-', i)]:
                return False
                
        def countInColumn(ch, j):
            return sum([self.board[i][j] == ch for i in range(self.M)])
        for j in range(self.N):
            if self.top[j] not in [-1, countInColumn('+', j)] or self.bottom[j] not in [-1, countInColumn('-', j)]:
                return False
    
        return True

    def solve(self, row, col):
        """
        Function that solves the board given the initial conditions
        Parameters
        row - starting cell row index
        col - starting cell column index
        """
        
        top, bottom, left, right = self.top, self.bottom, self.left, self.right
        slots, board = self.slots, self.board
        checkConstraints = self.checkConstraints
        # if we have reached last cell
        if row >= self.M - 1 and col >= self.N - 1:
            return self.validate()

        # if last column of current row is already processed, go to next row, first column
        if col >= self.N:
            col, row = 0, row + 1

        # if current cell contains R (end of horizontal slot) or B (end of vertical slot) recur for next cell
        if slots[row][col] == 'R' or slots[row][col] == 'B':
            if self.solve(row, col + 1):
                return True

        # if horizontal slot contains L and R
        if slots[row][col] == 'L' and slots[row][col + 1] == 'R':
            # put ('+', '-') pair and recur
            if checkConstraints(row, col, '+') and checkConstraints(row, col + 1, '-'):
                board[row][col] = '+'
                board[row][col + 1] = '-'
                if self.solve(row, col + 2):
                    return True
                # if it doesn't lead to a solution, backtrack
                board[row][col] = 'X'
                board[row][col + 1] = 'X'

            # put ('-', '+') pair and recur
            if checkConstraints(row, col, '-') and checkConstraints(row, col + 1, '+'):
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
            if checkConstraints(row, col, '+') and checkConstraints(row + 1, col, '-'):
                board[row][col] = '+'
                board[row + 1][col] = '-'
                if self.solve(row, col + 1):
                    return True
                # if it doesn't lead to a solution, backtrack
                board[row][col] = 'X'
                board[row + 1][col] = 'X'

            # put ('-', '+') pair and recur
            if checkConstraints(row, col, '-') and checkConstraints(row + 1, col, '+'):
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


    def display(self):
        """
        Display the solved board or error message if no solution exists
        """
        
        if self.solve(0, 0):
            print("\nSolution exists")
            for i in range(self.M):
                for j in range(self.N):
                    print(self.board[i][j], end=' ')
                print()
        else:
            print("Solution does not exist")


if __name__ == '__main__':
    try:
        print("Dimensions must be such that there are even number of cells")
        M, N = list(map(int, input('Enter the board dimensions : ').split())) 
        if M*N % 2 != 0:
            raise Exception
        
        print('Enter -1 if any number of characters allowed')
        top = list(map(int, input('Enter "+" for columns : ').split()))
        if len(top) != N:
            raise Exception
        
        bottom = list(map(int, input('Enter "-" for columns : ').split()))
        if len(bottom) != N:
            raise Exception

        left = list(map(int, input('Enter "+" for rows : ').split()))
        if len(left) != M:
            raise Exception

        right = list(map(int, input('Enter "-" for rows : ').split()))
        if len(right) != M:
            raise Exception

        slots = [list(map(str, input('Input slots corresponding to row ' + str(i+1) + ": ").split())) for i in range(M)]
        if len(slots) != M:
            raise Exception
        for i in range(len(slots)):
            if len(slots[i]) != N:
                raise Exception
    except Exception:
        print("\nUsing default values since wrong input was given\n")
        (M, N) = (5, 6)
        top = [3, -1, -1, 2, 1, -1]
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
        
    print("Top : ", top)
    print("Bottom : ", bottom)
    print("Left : ", left)
    print("Right : ", right)
    print("Slots given : ", slots)
    ob = MagnetPuzzle((M, N), top, bottom, left, right, slots)
    ob.display()
