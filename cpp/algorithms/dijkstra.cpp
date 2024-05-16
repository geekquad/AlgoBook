#include <iostream>
#include <cstring>
#include <vector>
#include <queue>
#include <unordered_map>

using namespace std;

class Graph {
    int v;
    vector<vector<pair<int, int>>> adj;
    vector<int> parent;
public:
    Graph(int v) {
        this->v = v;
        adj = vector<vector<pair<int, int>>> (this->v, vector<pair<int, int>>());
        parent = vector<int> (v, -1);
    }

    void createGraph() {
        int e, x, y, w;
        cin >> e;
        for (int i = 0; i < e; i++) {
            cin >> x >> y >> w;
            adj[x].push_back({y, w});
        }
    }

    void djikstra(int s = 0) {
        vector<int> distance(v, INT_MAX);
        distance[s] = 0;
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq; 
        pq.push({s, 0});
        while (!pq.empty()) {
            int u = pq.top().first;
            int d = pq.top().second;
            pq.pop();
            for (auto it : adj[u]) {
                int v = it.first;
                int w = it.second;
                if (distance[v] > d + w) {
                    distance[v] = d + w;
                    parent[v] = u;
                    pq.push({v, distance[v]});
                }
            }
        }
        for (int i = 0; i < v; i++) {
            cout << distance[i] << " ";
        }
        cout << endl;
    }

    void shortestPath(int s, int t) {
        if (s == t) {
            cout << "Source and destination are same." << endl;
        }
        vector<int> result;
        for (int i = t; i != s; i = parent[i]) {
            result.push_back(i);
        }
        if (result.size() == 0) {
            cout << "No path possible.";
        }
        cout << s << " ";
        for (int i = result.size() - 1; i >= 0; i--) {
            cout << result[i] << " ";
        }
        cout << endl;
    }
};

int main() {
    Graph g(5);
    g.createGraph();
    g.djikstra();
    g.shortestPath(0, 3);
}