//Code for Prim’s Minimum Spanning Tree (MST) algorithm

//Minimium spanning tree
//The cost of the spanning tree is the sum of the weights of all the edges in the tree. 
//Minimum spanning tree is the spanning tree where the cost is minimum among all the spanning trees. 

//Prims's algorithm
//Prim's Algorithm is used to find the minimum spanning tree from a graph. 
//Prim's algorithm finds the subset of edges that includes every vertex of the graph such that the sum of the weights of the edges can be minimized.
//Prim's algorithm starts with the single node and explore all the adjacent nodes with all the connecting edges at every step.
#include <bits/stdc++.h>
// Number of vertices in the graph 
#define w 5
using namespace std;
int minimum_key(int key[],int mst_set[])
{
    int keymin=INT_MAX;
    int index;
    for(int i=0;i<w;i++)
    {
        if(mst_set[i]==0 && key[i]<keymin)
        {
            keymin=key[i];
            index=i;
        }
    }
    return index;
}
void print_mst(int vertices_mst[], int graph[w][w])  
{    
    for (int i = 1; i < w; i++)  
        cout<<vertices_mst[i]<<" - "<<i<<" \t"<<graph[i][vertices_mst[i]]<<" \n";  
}  
void primMST(int graph[w][w])
{
    int mst_set[w],key[w],vertices_mst[w];
    int count=0;
    for(int i=0;i<w;i++)
    {
      //initializing all keys as INFINITE
        key[i]=INT_MAX;
      //initializing all vertices used in mst set as false or "0"
        mst_set[i]=0;
    }
    key[0]=0;
    vertices_mst[0]=-1;
    while(count<w)
    {
        //finding vertice , not included in mst set ,with mimnimum key 
        int key_min=minimum_key(key,mst_set);
        //including the minimum key in the mst set , and setting the index as true or "1"
        mst_set[key_min]=1;
        count++;
        for(int i=0;i<w;i++)
        {
            //// Update the key only if graph[u][v] is smaller than key[v]
            if(graph[key_min][i]!=0 && mst_set[i]==0 && graph[key_min][i]<key[i])
            {
                key[i]=graph[key_min][i];
                vertices_mst[i]=key_min;
            }
        }

    }
    print_mst(vertices_mst, graph); 
}
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
  primMST(graph);
}

//This code is contributed by Sanjeevani Ratna Tiwari 

