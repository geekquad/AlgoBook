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



	void BFS(T src){ 
		queue<T> q;
		q.push(src);

		map<T, bool> visited;
		visited[src] = true;

		while(!q.empty()){
			T temp = q.front();
			cout<<temp<<" ";

			q.pop();

			for(auto neigh : m[temp]){ // traverse list of neighbours
				if(!visited[neigh]){ // if not visited
					q.push(neigh);
					visited[neigh] = true;
				}
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
  
    g.BFS(src);

  return 0;
}
