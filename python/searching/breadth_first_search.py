#Breadth First Search 
#Used to find shortest path in graph

#graph for example
graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F','G'],
  'D' : [],
  'E' : ['G'],
  'F' : [],
  'G' : []
}

visited = [] # List to keep track of visited nodes.
queue = []     #Initialize a queue

def breadth_first_search(visited, graph, node):
  visited.append(node)
  queue.append(node)

  while queue:
    s = queue.pop(0) 
    print (s, end = " ") 

    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

# Driver Code
breadth_first_search(visited, graph, 'A')  #starting search form 'A'
