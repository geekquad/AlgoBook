from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        # Add an edge from vertex u to vertex v
        self.graph[u].append(v)

    def bfs(self, start_vertex):
        visited = set()  # Set to keep track of visited vertices
        queue = deque()   # Queue for BFS traversal

        visited.add(start_vertex)  # Mark the start vertex as visited
        queue.append(start_vertex)  # Add the start vertex to the queue

        while queue:
            vertex = queue.popleft()  # Get the next vertex from the queue
            print(f"Visited vertex: {vertex}")

            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)   # Mark the neighbor as visited
                    queue.append(neighbor)  # Add the neighbor to the queue

# Example usage and test
if __name__ == "__main__":
    # Create a sample graph
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)

    print("Breadth-First Traversal (starting from vertex 2):")
    g.bfs(2)