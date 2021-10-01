#include <bits/stdc++.h>
using namespace std;

//function to print the solution
void print_solution(int color[], int v){
    cout << "Solution exists."<<endl;
    for(int i=0; i<v; i++){
        cout << color[i]<< " ";
    }
}

//function to check whether the next node is safe to color or not
bool is_safe(int k, int **G, int color[], int i, int v){
    for(int j=0; j<v; j++){
        //checks whether there is an edge between them , if yes then checks if this color is already used by its adjacents or not!!
        if(G[k][j] && i== color[j])
            return false;
    }
    return true;
}

//Actual function
//It returns false if the m colors cannot be assigned, otherwise 
//return true and prints assignments of colors to all vertices.
bool graph_coloring(int **graph, int m,int color[], int v, int vertex){
    //base case, if all nodes are done then returns true
    if(vertex == v){
        return true;
    }

    for(int i=1; i<=m; i++){
        //check if this node is safe asign this color
        if(is_safe(vertex, graph, color, i, v)){
            color[vertex] = i;
            // recur to assign colors to rest of the vertices
            if(graph_coloring(graph, m, color, v, vertex+1))             
                return true;
            //back tracking
            color[vertex] = 0;
        }
    }
    //If no color can be assigned to this vertex then return false
    return false;
}

int main(){
    //v-> no of nodes in the graph
    //m-> no of colors
    int v,m;
    cout << "enter no of nodes: ";
    cin >> v;
    cout << "enter graph matrix (0|1)'s:  "<<endl;

    //graph matrix (if there is an edge between two nodes then value 1 else 0)
    int **graph = new int *[v];
    for(int i=0; i<v; i++){
        graph[i] = new int [v];
        for(int j=0; j<v; j++){
            cin>>graph[i][j];       //taking input of the graph matrix
        }
    }
    //taking input for colors
    cout << "enter no of colors:";
    cin >> m;

    //initialising all colors to '0', is usful in is_safe function
    int color[v];
    for(int i=0; i<v; i++){
        color[i] = 0;
    }

    //call graph_coloring function for vertex 0
    if(graph_coloring(graph, m, color, v, 0))
        //call for print function
        print_solution(color,v);
    
    //else no solution exists
    else
        cout<<"no solution exists!!"<<endl;
    return 0;
}
