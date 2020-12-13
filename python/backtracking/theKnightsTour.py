# Python3 program to solve The Knight Tour problem using Backtracking

def printSolution(n, board):
    """
    Print the solution Chessboard matrix
    """
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=' ')
        print()


def isSafe(x, y, n, board):
    """
        Function to check if x, y are vaild index 
        on the N*N board
    """
    if x >= 0 and y >= 0 and x < n and y < n and board[x][y] == -1:
        return True
    else:
        return False


def solveKnightsTour(n):
    """
    function to solve the Knight Tour problem using Backtracking,
    It calls the recursive function with the required parameters
    Print one of the possible solution
    """
    # initialization og board matrix all boxes as -1 means yeat to visit
    board = [[-1 for i in range(n)] for i in range(n)]
    # move_x and move_y defines the next move of the Knight
    move_x = [2, 1, -1, -2, -2, -1, 1, 2]
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]

    # start from first block
    board[0][0] = 0
    # Step counter
    pos = 1

    # chacking if solution exists
    if (not solveKnightsTourRec(n, board, 0, 0, move_x, move_y, pos)):
        print("Solution does not exist")
    else:
        printSolution(n, board)


def solveKnightsTourRec(n, board, curr_x, curr_y, move_x, move_y, pos):
    """
    A recursive function to check all the possible paths
    using backtracking
    """
    # if pos is n^2, means we have moved to all the boxes
    # so, exit the recursion and return true
    if pos == n**2:
        return True
    # check all the possible moves
    for i in range(8):
        # next postion if ith move is choses
        next_x = curr_x + move_x[i]
        next_y = curr_y + move_y[i]
        if(isSafe(next_x, next_y, n, board)):
            # set box to the present counter and check if solution exists
            board[next_x][next_y] = pos
            if(solveKnightsTourRec(n, board, next_x, next_y, move_x, move_y, pos+1)):
                return True
            # backtracking
            # if no solution exist for the move[i]
            # set board again to -1, means we are
            # yet to move on that box
            board[next_x][next_y] = -1
    # if no solution found exit recursion
    # and return false
    return False


# Driver program to solve The Knight's Tour Problem
# n is the side of the board
if __name__ == "__main__":
    solveKnightsTour(int(input('Enter value of n: ')))