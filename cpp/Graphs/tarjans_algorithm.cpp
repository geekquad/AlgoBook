// A C++ program to find strongly connected components in a given directed graph 
//using Tarjan's algorithm
#include<iostream> 
#include <list> 
#include <stack> 
#define NIL -1 
using namespace std; 
  
// A class that represents an directed graph 
class Graph 
{ 
    int w;    // No. of vertices 
    list<int> *adj;    // A dynamic array of adjacency lists 
    void SCCUtil(int u, int disc[], int low[], 
                 stack<int> *st, bool stackmem[]); 
public: 
    Graph(int w);   // Constructor 
    void edge(int v, int w);   // function to add an edge to graph 
    void SCC();    // prints strongly connected components 
}; 
  
Graph::Graph(int w) 
{ 
    this->w = w; 
    adj = new list<int>[w]; 
} 
  
void Graph::edge(int v, int w) 
{ 
    adj[v].push_back(w); 
} 
  
void Graph::SCCUtil(int u, int disc[], int low[], stack<int> *st, 
                    bool stackmem[]) 
{ 
   
    static int time = 0; 
    disc[u] = low[u] = ++time; 
    st->push(u); 
    stackmem[u] = true; 
  
   
    list<int>::iterator i; 
    for (i = adj[u].begin(); i != adj[u].end(); ++i) 
    { 
        int v = *i;  
        if (disc[v] == -1) 
        { 
            SCCUtil(v, disc, low, st, stackmem); 
  
            
            low[u]  = min(low[u], low[v]); 
        } 
  
        else if (stackmem[v] == true) 
            low[u]  = min(low[u], disc[v]); 
    } 
  
   
    int w = 0;
    if (low[u] == disc[u]) 
    { 
        while (st->top() != u) 
        { 
            w = (int) st->top(); 
            cout << w << " "; 
            stackmem[w] = false; 
            st->pop(); 
        } 
        w = (int) st->top(); 
        cout << w << "\n"; 
        stackmem[w] = false; 
        st->pop(); 
    } 
}  
void Graph::SCC() 
{ 
    int *disc = new int[w]; 
    int *low = new int[w]; 
    bool *stackmem = new bool[w]; 
    stack<int> *st = new stack<int>(); 
  
    for (int i = 0; i < w; i++) 
    { 
        disc[i] = NIL; 
        low[i] = NIL; 
        stackmem[i] = false; 
    } 
  
    for (int i = 0; i < w; i++) 
        if (disc[i] == NIL) 
            SCCUtil(i, disc, low, st, stackmem); 
}  
int main() 
{ 
    /* Directed graph
        1---->0----->3
       /|\  /       | 
        |  /        |
        | /        \|/
        2           4
     */
    Graph g1(5); 
    g1.edge(1, 0); 
    g1.edge(0, 2); 
    g1.edge(2, 1); 
    g1.edge(0, 3); 
    g1.edge(3, 4); 
    g1.SCC(); 
    return 0;
}

