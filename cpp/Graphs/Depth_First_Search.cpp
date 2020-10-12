/*This a Depth first search implementation in graphs using C++ */
#include<iostream>
using namespace std;


void Depth_First_Search(int Graph[][5], int n_nodes,int starting, int visited[])
{   visited[starting]=true;
    cout<<starting<<" ";
    
    for(int node=0;node<n_nodes;node++){
            int vertices=n_nodes;
            for(int vertex=0;vertex<vertices;vertex++)
                if(!visited[vertex] && Graph[node][vertex]==1){
                    Depth_First_Search(Graph,n_nodes,vertex,visited);
                }
    }
}

int main(){
    //Ajancy matrix for connections between nodes
    int Graph[5][5]={
        {0,1,0,1,0},//0->1,3
        {0,0,1,0,0},//1->2
        {0,0,0,0,1},//2->4
        {0,1,0,0,1},//3->1,4
        {1,0,0,0,0} //4->0
    };//initialize a graph with 5 nodes and null connections
    int visited[5];//initialize a visited array with everything false
    for(int node=0;node<5;node++){
        visited[node]=false;
    }
    
    Depth_First_Search(Graph,5,4,visited);
}