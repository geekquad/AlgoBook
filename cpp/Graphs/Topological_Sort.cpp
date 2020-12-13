#include <bits/stdc++.h>
using namespace std;
void toposort(vector<vector<int>> &adj , int n) {
	//Kahn's Algorithm
	vector<int> in(n);
	int i;
	for(i = 0 ; i < n ; i++) {
		for(auto v: adj[i]) {
			in[v]++; // Increasing in-degree
		}
	}
	queue <int> q;
	for(i = 0 ; i < n ; i++) {
		if(!in[i]) {
			q.push(i); //If indegree is zero, push it int the queue
		}
	}
	vector<int> order; // To store order of nodes
	while(q.size()) {
		int u = q.front();
		q.pop();
		order.push_back(u);
		for(auto v: adj[u]) {
			in[v]--;
			if(!in[v]) {
				q.push(v); //If indegree is zero, push it int the queue
			}
		}
	}
	if(order.size() != n) {
		cout<<"Cycle exists in graph";
	}
	else {
		for(auto nodes : order) {
			cout<<nodes<<" ";
		}
	}
}
int main() {
	vector<vector<int>> graph;
	int n = 3; //Number of nodes

	vector <int> edge_from_0 = {1 , 2}; // Edges: 0->1 , 0->2
	vector <int> edge_from_1 = {2}; // Edges: 1->2
	vector <int> edge_from_2 = {}; // No edges

	//Creating graph
	graph.push_back(edge_from_0);
	graph.push_back(edge_from_1);
	graph.push_back(edge_from_2);

	toposort(graph , n);

    return 0;
}
