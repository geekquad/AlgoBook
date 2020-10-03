# class to represent a disjoint set:
class DisjointSet:
    parent = {}

    # perform MakeSet operation
    def makeSet(self, N):

        # create N disjoint sets (one for each vertex)
        for i in range(N):
            self.parent[i] = i

    # Find the root of the set in which element k belongs
    def find(self, k):

        # if k is root
        if self.parent[k] == k:
            return k

        return self.find(self.parent[k])

    # Perform Union of two subsets
    def union(self, rank, x, y):
        s1 = self.find(x)  # x present in s1 set
        s2 = self.find(y)  # y present in s2 set

        
        # (Union by Rank)
        if rank[s1] < rank[s2]:
            self.parent[s1] = s2
        elif rank[s1] > rank[s2]:
            self.parent[s2] = s1

        # If ranks are same, then make one as root
        # and increment its rank by one
        else:
            self.parent[s2] = s1
            rank[s1] += 1


# construct MST using Kruskal's algorithm
def KruskalAlgo(edges, N):
    # stores edges present in MST
    mst = []

    # initialize DisjointSet class # create singleton set for each elemente
    ds = DisjointSet()
    ds.makeSet(N)
    rank = []

    # initialisation
    for nodes in range(N):
        rank.append(0)

    index = 0

    # MST contains exactly V-1 edges
    while len(mst) != N - 1:

        # consider next edge with minimum weight from the graph
        (src, dest, weight) = edges[index]
        index = index + 1

        # find root of the sets to which two endpoint
        # vertices of next_edge belongs
        x = ds.find(src)
        y = ds.find(dest)

        # take that edge in MST if it doesn't form a cycle means belong to diffent parents
        if x != y:
            mst.append((src, dest, weight))
            ds.union(rank, x, y)

    return mst


if __name__ == '__main__':

    N = int(input())  # Number of vertices in the graph
    e = int(input())  # Number of edges in the graph
    edges=[]
    
    for i in range(e):
        x,y,z = map(int,input().split(" "))    # (x, y, z) Triplet represent undirected edge from vertex x to vertex y having weight z
        edges.append((x,y,z))


    # sort edges by increasing weight
    edges.sort(key=lambda x: x[2])

    
    # construct graph
    e = KruskalAlgo(edges, N)

    print(e)
