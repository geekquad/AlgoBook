//Magnet Puzzle
#include <iostream>
using namespace std;
 
// M x N matrix
#define M 5
#define N 6
 
// A utility function to print solution
void printSolution(char board[M][N])
{
    for (int i = 0; i < M; i++)
    {
        for (int j = 0; j < N; j++)
            cout << board[i][j] << " ";
        cout << endl;
    }
}
 
// A utility function to count number of characters ch in current column j
int countInColumns(char board[N][N], char ch, int j)
{
    int count = 0;
    for (int i = 0; i < M; i++)
        if (board[i][j] == ch)
            count++;
 
    return count;
}
 
// A utility function to count number of characters ch in current row i
int countInRow(char board[N][N], char ch, int i)
{
    int count = 0;
    for (int j = 0; j < N; j++)
        if (board[i][j] == ch)
            count++;
 
    return count;
}
 
// Function to check if it safe to put 'ch' at board[row][col]
bool isSafe(char board[N][N], int row, int col, char ch, int top[],
             int left[], int bottom[], int right[])
{
    // check for adjacent cells
    if ((row - 1 >= 0 && board[row - 1][col] == ch) ||
        (col + 1 < N && board[row][col + 1] == ch) ||
        (row + 1 < M && board[row + 1][col] == ch) ||
        (col - 1 >= 0 && board[row][col - 1] == ch))
    return false;
 
    // count ch in current row
    int rowCount = countInRow(board, ch, row);
 
    // count ch in current column
    int colCount = countInColumns(board, ch, col);
 
    // if given character is '+', check top[] & left[]
    if (ch == '+')
    {
        // check top
        if (top[col] != -1 && colCount >= top[col])
            return false;
 
        // check left
        if (left[row] != -1 && rowCount >= left[row])
            return false;
    }
 
    // if given character is '-', check bottom[] & right[]
    if (ch == '-')
    {
        // check bottom
        if (bottom[col] != -1 && colCount >= bottom[col])
            return false;
 
        // check left
        if (right[row] != -1 && rowCount >= right[row])
            return false;
    }
 
    return true;
}
 
// Function to validate Configuration of output board
bool validateConfiguration(char board[N][N], int top[], int left[],
                        int bottom[], int right[])
{
    // check top
    for (int i = 0; i < N; i++)
        if (top[i] != -1 &&
            countInColumns(board, '+', i) != top[i])
        return false;
 
    // check left
    for (int j = 0; j < M; j++)
        if (left[j] != -1 &&
            countInRow(board, '+', j) != left[j])
        return false;
 
    // check bottom
    for (int i = 0; i < N; i++)
        if (bottom[i] != -1 &&
            countInColumns(board, '-', i) != bottom[i])
        return false;
 
    // check right
    for (int j = 0; j < M; j++)
        if (right[j] != -1 &&
            countInRow(board, '-', j) != right[j])
        return false;
 
    return true;
}
 
// Main function to solve the Bipolar Magnets puzzle
bool solveMagnetPuzzle(char board[N][N], int row, int col, int top[],
                int left[], int bottom[], int right[], char str[M][N])
{
    // if we have reached last cell
    if (row >= M - 1 && col >= N - 1)
    {
        if (validateConfiguration(board, top, left, bottom, right))
            return true;
 
        return false;
    }
 
    // if last column of current row is already processed,
    // go to next row, first column
    if (col >= N)
    {
        col = 0;
        row = row + 1;
    }
 
    // if current cell contains 'R' or 'B' (end of horizontal
    // or vertical slot) recur for next cell
    if (str[row][col] == 'R' || str[row][col] == 'B')
    {
        if (solveMagnetPuzzle(board, row, col + 1, top,
                                left, bottom, right, str))
            return true;
    }
 
    // if horizontal slot contains L and R
    if (str[row][col] == 'L' && str[row][col + 1] == 'R')
    {
        // put ('+', '-') pair and recur
        if (isSafe(board, row, col, '+', top, left, bottom, right) &&
            isSafe(board, row, col + 1, '-', top, left, bottom, right))
        {
            board[row][col] = '+';
            board[row][col + 1] = '-';
 
            if (solveMagnetPuzzle(board, row, col + 2,
                            top, left, bottom, right, str))
                return true;
 
            // if it doesn't lead to a solution, backtrack
            board[row][col] = 'X';
            board[row][col + 1] = 'X';
        }
 
        // put ('-', '+') pair and recur
        if (isSafe(board, row, col, '-', top, left, bottom, right) &&
            isSafe(board, row, col + 1, '+', top, left, bottom, right))
        {
            board[row][col] = '-';
            board[row][col + 1] = '+';
 
            if (solveMagnetPuzzle(board, row, col + 2,
                            top, left, bottom, right, str))
                return true;
 
            // if it doesn't lead to a solution, backtrack
            board[row][col] = 'X';
            board[row][col + 1] = 'X';
        }
    }
 
    // if vertical slot contains T and B
    if (str[row][col] == 'T' && str[row + 1][col] == 'B')
    {
        // put ('+', '-') pair and recur
        if (isSafe(board, row, col, '+', top, left, bottom, right) &&
            isSafe(board, row + 1, col, '-', top, left, bottom, right))
        {
            board[row][col] = '+';
            board[row + 1][col] = '-';
 
            if (solveMagnetPuzzle(board, row, col + 1,
                            top, left, bottom, right, str))
                return true;
 
            // if it doesn't lead to a solution, backtrack
            board[row][col] = 'X';
            board[row + 1][col] = 'X';
        }
 
        // put ('-', '+') pair and recur
        if (isSafe(board, row, col, '-', top, left, bottom, right) &&
            isSafe(board, row + 1, col, '+', top, left, bottom, right))
        {
            board[row][col] = '-';
            board[row + 1][col] = '+';
 
            if (solveMagnetPuzzle(board, row, col + 1,
                            top, left, bottom, right, str))
                return true;
 
            // if it doesn't lead to a solution, backtrack
            board[row][col] = 'X';
            board[row + 1][col] = 'X';
        }
    }
 
    // ignore current cell and recur
    if (solveMagnetPuzzle(board, row, col + 1,
                        top, left, bottom, right, str))
        return true;
 
    // if no solution is possible, return false
    return false;
}
 
void solveMagnetPuzzle(int top[], int left[], int bottom[],
                        int right[], char str[M][N])
{
    // to store result
    char board[M][N];
 
    // initialize all cells by 'X'
    for (int i = 0; i < M; i++)
        for (int j = 0; j < N; j++)
            board[i][j] = 'X';
 
    // start from (0, 0) cell
    if (!solveMagnetPuzzle(board, 0, 0, top, left, bottom, right, str))
    {
        cout << "Solution does not exist";
        return;
    }
 
    // print result if given configuration is solvable
    printSolution(board);
}
 
int main()
{
    // indicates the count of + or - along the top (+), bottom (-),
    // left (+) and right (-) edges respectively.
    // Value of -1 indicates any number of + or - signs
    int top[N] = { 1, -1, -1, 2, 1, -1 };
    int bottom[N] = { 2, -1, -1, 2, -1, 3 };
    int left[M] = { 2, 3, -1, -1, -1 };
    int right[M] = { -1, -1, -1, 1, -1 };
 
    // rules matrix
    char str[M][N] =
    {
        { 'L', 'R', 'L', 'R', 'T', 'T' },
        { 'L', 'R', 'L', 'R', 'B', 'B' },
        { 'T', 'T', 'T', 'T', 'L', 'R' },
        { 'B', 'B', 'B', 'B', 'T', 'T' },
        { 'L', 'R', 'L', 'R', 'B', 'B' }
    };
 
    solveMagnetPuzzle(top, left, bottom, right, str);
 
    return 0;
}
