#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

struct edge {
	unsigned int source, destination, weight;
};

void printMST(vector<bool> inTree, vector<edge> set, int cost) {
	cout << "Edges in MST" << endl;
	cout << "S D W" << endl;
	for (int i = 0; i < set.size(); ++i)
		if(inTree[i])
			cout << set[i].source << " " << set[i].destination << " " << set[i].weight << endl;
	cout << endl << "Cost of MST: " << cost << endl;
}

unsigned int find(vector<unsigned int> set, unsigned int i) {
	if (i == set[i])
		return i;
	else {
		set[i] = find(set, set[i]);
		return set[i];
	}
}

void u(vector<unsigned int> &set, unsigned int x, unsigned int y) {
	int a = find(set, x);
	int b = find(set, y);
	set[b] = a;
	return;
}

void kruskal(vector<edge> &graph) {
	vector<bool> inMST(graph.size());
	vector<unsigned int> set(graph.size());
	unsigned int cost = 0;

	for (unsigned int i = 0; i < set.size(); ++i)
		set[i] = i;
	sort(graph.begin(), graph.end(), [](const edge i, const edge& j) {return i.weight < j.weight; });

	for (unsigned int i = 0; i < graph.size(); i++) {
		unsigned int x = find(set, graph[i].source);
		unsigned int y = find(set, graph[i].destination);
		if (x != y) {
			inMST[i] = true;
			u(set, graph[i].source, graph[i].destination);//union the two nodes
			cost += graph[i].weight;
		}
		else
			inMST[i] = false;
	}
	printMST(inMST, graph, cost);
	return;
}

int main(int argc, char* argv[]) {
	unsigned int numEdges;
	vector<edge> graph;
	if (argc == 1) {
		cout << "Enter the number of edges: ";
		cin >> numEdges;
		graph.resize(numEdges);
		cout << "Enter the edges with weight: <source> <destination> <weight>: " << endl;
		for (unsigned int i = 0; i < graph.size(); i++)
			cin >> graph[i].source >> graph[i].destination >> graph[i].weight;
	}

	else {
		ifstream in(argv[1]);
		in >> numEdges;
		for (unsigned int i = 0; i < graph.size(); i++)
			in >> graph[i].source >> graph[i].destination >> graph[i].weight;
	}
	
	kruskal(graph);
	return 0;
}
