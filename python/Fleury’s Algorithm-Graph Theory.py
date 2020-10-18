from collections import defaultdict
  
  class Graph:
  
    def __init__(self,vertices):
        self.V= vertices 
        self.graph = defaultdict(list) 
        self.Time = 0
  
    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)
 
    def rmvEdge(self, u, v):
        for index, key in enumerate(self.graph[u]):
            if key == v:
                self.graph[u].pop(index)
        for index, key in enumerate(self.graph[v]):
            if key == u:
                self.graph[v].pop(index)
 
    def DFSCount(self, v, visited):
        count = 1
        visited[v] = True
        for i in self.graph[v]:
            if visited[i] == False:
                count = count + self.DFSCount(i, visited)        
        return count
 
    def isValidNextEdge(self, u, v):
       
        if len(self.graph[u]) == 1:
            return True
        else:
            visited =[False]*(self.V)
            count1 = self.DFSCount(u, visited)
 
            self.rmvEdge(u, v)
            visited =[False]*(self.V)
            count2 = self.DFSCount(u, visited)
 
            self.addEdge(u,v)
 
            return False if count1 > count2 else True
 
 
    def printEulerUtil(self, u):
        for v in self.graph[u]:
            if self.isValidNextEdge(u, v):
                print("%d-%d " %(u,v)),
                self.rmvEdge(u, v)
                self.printEulerUtil(v)
 
 
   def printEulerTour(self):
        u = 0
        for i in range(self.V):
            if len(self.graph[i]) %2 != 0 :
                u = i
                break
        print ("\n")
        self.printEulerUtil(u)
        
#Create the graph here#
