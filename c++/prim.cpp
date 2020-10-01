#include <iostream>
#include <vector>
#include <queue>
#include <limits>
#include <fstream>

using namespace std;

struct edge {
	unsigned int source, destination, weight;
	edge(unsigned int source, unsigned int destination, unsigned int weight) : source(source), destination(destination), weight(weight) {};
	edge() {};
};

struct compare {
	bool operator()(const edge& a, const edge& b) {
		return a.weight > b.weight;//second is weight
	}
};

void printMST(vector<edge> &edgesInMST, int cost) {
	cout << "Edges in MST" << endl;
	cout << "S D W" << endl;
	for (auto i : edgesInMST)
		cout << i.source << ' ' << i.destination << ' ' << i.weight << endl;
	cout << endl << "Cost of MST: " << cost << endl;
}

void prim(vector<vector <edge>> &graph, unsigned int numUnvisitedNodes) {
	priority_queue< edge, vector <edge>, compare > pq;
	vector<unsigned int> key(graph.size(), numeric_limits<unsigned int>::max());
	vector<bool> inMST(graph.size(), false);
	vector < edge> edgesInMST;
	unsigned int cost = 0;

	for (auto i : graph[0])
		pq.push(i);
	inMST[0] = true;
	numUnvisitedNodes--;
	
	edge e;
	while(numUnvisitedNodes > 0) {
		e = pq.top();
		pq.pop();
		if (!inMST[e.destination]) {
			edgesInMST.emplace_back(e);
			for (auto i : graph[e.destination])
				pq.push(i);
			numUnvisitedNodes--;
			inMST[e.destination] = true;
			cost += e.weight;
		}
	}
	printMST(edgesInMST, cost);
}

int main(int argc, char* argv[]) {
	vector<vector <edge>> graph;
	unsigned int numNodes, numEdges, src, dest, weight;

	if (argc == 1) {
		cout << "Enter the number of nodes and edges: ";
		cin >> numNodes >> numEdges;
		graph.resize(numNodes);
		cout << "Enter the edges with weight: <source> <destination> <weight>: " << endl;
		for (unsigned int i = 0; i < numEdges; i++) {
			cin >> src >> dest >> weight;
			graph[src].push_back(edge(src, dest, weight));
			graph[dest].push_back(edge(dest, src, weight));//cause you can go both ways
		}
	}

	else {
		ifstream in(argv[1]);
		in >> numEdges;
		for (unsigned int i = 0; i < numEdges; i++) {
			in >> src >> dest >> weight;
			graph[src].push_back(edge(src, dest, weight));
			graph[dest].push_back(edge(dest, src, weight));//cause you can go both ways
		}
	}
	prim(graph, numNodes);
	return 0;
}