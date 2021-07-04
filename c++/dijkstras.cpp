#include <iostream>
#include <queue>
#include <vector>
#include <limits>
#include <fstream>

using namespace std;

struct compare {
	bool operator()(const pair<unsigned int, unsigned int>& a, const pair<unsigned int, unsigned int>& b) {
		return a.second > b.second;//second is weight
	}
};

vector<unsigned int> dijkstras(vector<vector <pair< unsigned int, unsigned int >>> graph, unsigned int numNodes, unsigned int start, unsigned int end) {
	unsigned int src, dest, weight;
	priority_queue<pair< unsigned int, unsigned int >, vector<pair< unsigned int, unsigned int > >, compare> pq;//datatype, vector datatype, comparator
	vector<unsigned int> distance(numNodes);//size numNodes
	vector<bool> visited(numNodes, false);
	vector<unsigned int> bestPathToNode(numNodes);

	distance[start] = 0;
	for (unsigned int i = 1; i < numNodes; i++)
		distance[i] = numeric_limits<unsigned int>::max();;

	pq.push(make_pair(start, 0));

	while (!pq.empty()) {
		src = pq.top().first;
		pq.pop();
		if (visited[src])//id visited, skip
			continue;

		for (unsigned int i = 0; i < graph[src].size(); i++) {//for all the edges of the unvisited node
			dest = graph[src][i].first;
			weight = graph[src][i].second;
			if (!visited[dest] && distance[src] + weight < distance[dest]) {//if the destination node is not visited and the new weight is less than old
				distance[dest] = distance[src] + weight;//set best weight
				bestPathToNode[dest] = src;//sets the best path to that node
				pq.push(pair< int, int >(dest, distance[dest]));//push the destination and its new best weight
			}
		}
		visited[src] = true;
	}
	//distance[end] is the distance to the src
	cout << "Distance to Target Node: " << distance[end] << endl;
	return bestPathToNode;
}

void printPath(vector<unsigned int> path, unsigned int start, unsigned int end) {
	if (path[end] == start)
		return;
	printPath(path, start, path[end]);
	cout << path[end] << " ";
	return;
}

int main(int argc, char* argv[]) {
	vector<vector <pair< unsigned int, unsigned int >>> graph;
	unsigned int numNodes, numEdges;
	unsigned int start, end;
	
	if (argc == 1) {
		cout << "Enter the number of nodes and edges: ";
		cin >> numNodes >> numEdges;
		
		graph.resize(numEdges);

		unsigned int src, dest, weight;
		cout << "Enter the edges with weight: <source> <destination> <weight>: " << endl;

		for (unsigned int i = 0; i < numEdges; i++) {
			cin >> src >> dest >> weight;
			graph[src].push_back(make_pair(dest, weight));
			graph[dest].push_back(make_pair(src, weight));//cause you can go both ways
		}
		cout << "Enter the source node: ";
		cin >> start;
		cout << "Enter target node: ";
		cin >> end;
	}
	else {
		ifstream in(argv[1]);
		in >> numNodes >> numEdges;
		graph.resize(numEdges);
		unsigned int src, dest, weight;
		
		for (unsigned int i = 0; i < numEdges; i++) {
			in >> src >> dest >> weight;
			graph[src].push_back(make_pair(dest, weight));
			graph[dest].push_back(make_pair(src, weight));//cause you can go both ways
		}
		in >> start >> end;
	}

	vector<unsigned int> path = dijkstras(graph, numNodes, start, end);
	
	cout << "Best Path to Target Node: " << start << ' ';
	printPath(path, start, end);
	cout << end << endl;
	return 0;
}