//Dijsktra algorithm to find shortest paths from source to all vertices in the given graph.
#include <bits/stdc++.h>
#define w 5
using namespace std;
int minkey(int store[],int spt_set[])
{
    int keymin=INT_MAX;
    int index;
    for(int i=0;i<w;i++)
    {
        if(spt_set[i]==0 && store[i]<keymin)
        {
            keymin=store[i];
            index=i;
        }
    }
    return index;
}
void print_spt(int store[])  
{    
    cout<<"vertex"<<"      "<<"Distance from Source"<<"\n";
    for (int i = 0; i < w; i++){
        cout<<i<<"               "<<store[i]<<" \n"; 
    } 
}  
void Dijsktra_spt(int graph[w][w],int source){
    int spt_set[w],store[w],count=0;
    for(int i=0;i<w;i++){
        //initializing the vertices not considered in spt set as 0 
        spt_set[i]=0;
        //// The output array dist[i] will hold the shortest distance from src to i 
        store[i]=INT_MAX;
    }
    store[source]=0;
    while(count<w){
        //select index from store array with min value 
        int key_min=minkey(store,spt_set);
        spt_set[key_min]=1;
        count++;
        //set that index as 1 , as it is included in spt set
        for(int i=0;i<w;i++)
        {
            //// Update the key only if graph[u][v] is smaller than key[v]
            if(graph[key_min][i]!=0 && spt_set[i]==0 && graph[key_min][i]<store[i])
            {
                store[i]=graph[key_min][i];
            }
        }

    }
    print_spt(store);
}
//driver code
int main() {
     /* Let us create the following graph  
        2     3  
     (0)--(1)--(2)  
      |   / \   | 
    8 | 6/   \5 |9  
      | /     \ |   
     (3)------(4)
          4       2    */
  //adjacency matrix representation of the graph
    int graph[w][w] = { { 0, 2, 0, 8, 0 },  
                        { 2, 0, 3, 6, 5 },  
                        { 0, 3, 0, 0, 9 },  
                        { 8, 6, 0, 0, 4 },  
                        { 0, 5, 9, 4, 0 } }; 
// considering 0 as the source, in the above graph
  Dijsktra_spt(graph,0);
}