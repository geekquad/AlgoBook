/*This a Breadth first search implementation in graphs using C++ */
#include<bits/stdc++.h>
using namespace std;


void Breadth_First_Search(int Graph[][5], int n_nodes,int starting, int visited[])
{   visited[starting]=true;
    list<int> queue; 
    queue.push_back(starting);

    while(!queue.empty()){
        int node=queue.front();
        cout<<node<<" ";
        queue.pop_front();
    for(int vertex=0;vertex<n_nodes;vertex++)
        if(!visited[vertex] && Graph[node][vertex]==1){
            visited[vertex]=true;
            queue.push_back(vertex);
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
    
    Breadth_First_Search(Graph,5,4,visited);
    return 0;
}
