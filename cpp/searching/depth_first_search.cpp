#include<iostream>
#include<map>
#include<queue>
#include<list>
using namespace std;

template<typename T> // for generic

class Graph{

	map<T, list<T> > m;
public:
	void AddEdge(T src, T dest, bool nondirectional = true){ // by default undirected graph

		m[src].push_back(dest);
		if(nondirectional){ // bi-directional
			m[dest].push_back(src);
		}
	}

void DFS_helper(T src, map<int, bool> &visited){

		cout << src <<" ";

		visited[src] = true;
		for(auto i : m[src]){
			if(!visited[i]){
				DFS_helper(i, visited);
			}
		}
	}

	void DFS(T src){ 
		map<int, bool> visited;

	    DFS_helper(src, visited);

	    for(auto i : m){ // for disconnected part
	    	if(!visited[i.first]){
	    		DFS_helper(i.first,visited);
	    	}
	    }

	}

};

int main(){
       Graph<int> g;

       int n; // number of edges
       int u,v; // nodes
    
       cin >> n;
       for(int i=0;i<n;i++){
           cin >> u >> v;
          g.AddEdge(u,v);
       }

       int src;
       cin >> src;
  
       g.DFS(src);

  return 0;
}
