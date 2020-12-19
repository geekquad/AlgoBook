#include <bits/stdc++.h>
using namespace std;

//a function to check whether a grid is valid or not
bool isvalid(int x, int y, int **tour, int n){
    return(x>=0 && y>=0 && x<n && y<n && tour[x][y]==-1);
}

//function to solve the tour 
bool solve_knighttour(int x, int y, int moves,int n, int **tour, int nxt_x[8], int nxt_y[8]){
    //if moves are equal to no of grids then solved (base case)
    if(moves==n*n){
        return true;
    }
    //variables for the next grid
    int new_x, new_y;
    for(int k=0; k<n; k++){
        //updating next grid
        new_x = x + nxt_x[k];
        new_y = y + nxt_y[k];
        //checking for validity
        if(isvalid(new_x, new_y, tour, n)){
            tour[new_x][new_y] = moves;
            if(solve_knighttour(new_x, new_y, moves+1, n, tour, nxt_x, nxt_y))
                return true;
            else
                //back tracking
                tour[new_x][new_y] = -1;
        }
    }
    //if not found return false
    return false;
}

//function to print the solution
void print(int **tour,int n){
    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            cout << tour[i][j] <<"  ";
        }
        cout << endl;
    }
}

int main(){
    int n = 8;

    int **tour = new int *[n];              //matrix for the knights tour
    for(int i=0; i<n; i++){
        tour[i] = new int [n];
        for(int j=0; j<n; j++){
            tour[i][j] = -1;                    //mark all the points as -1
        }
    }

    //knight is initially here(0,0)
    tour[0][0] = 0; 
    //next coordinates of x and y for the knight
    int nxt_x_move[8] = {2, 1, -1, -2, -2, -1, 1, 2};
    int nxt_y_move[8] = {1, 2, 2, 1, -1, -2, -2, -1};

    //start exploring the matrix by function call starting from (0,0)
    if(solve_knighttour(0, 0, 1, n, tour, nxt_x_move, nxt_y_move)){
        //if the tour exists then a function call for printing.
        print(tour, n);
        return 0;
    }
    else{
        cout << "No tour found!!" <<endl;
    }
    return 0;
}
