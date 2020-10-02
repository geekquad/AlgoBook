#Depth first Search 
# Depth first Search is an algorithm for traversal on graph or tree data structures.

# Using a Python dictionary to act as an adjacency list
graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F','G'],
    'D' : [],
    'E' : ['G'],
    'F' : [],
    'G' : [],
}

visited = set() # Set to keep track of visited nodes.

def depth_first_search(visited, graph, node):
    if node not in visited:               #ack if node is visited
        print (node)                      # if they are visited than print them
        visited.add(node)                 #and make it visited and add it it in visited 
        for neighbour in graph[node]:     # then recur on all its adjecent nodes 
            depth_first_search(visited, graph, neighbour)

# Driver Code
depth_first_search(visited, graph, 'A')