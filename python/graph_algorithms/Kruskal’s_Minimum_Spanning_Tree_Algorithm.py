from copy import deepcopy

class InvalidVertex(Exception):
    pass


class InvalidEdge(Exception):
    pass
class InvalidParametter(Exception):
    pass
class Graph:
    QTD_MAX_SPLITER = 1
    SPLITER = '-'

    def __init__(self, V: object = [], E: object = {}) -> object:
        for v in V:
            if not (Graph.validVertex(v)):
                raise InvalidVertex('Invalid Vertex ' + v )

            self.V = V

            for e in E:
                if not (self.validEdge(E[e])):
                    raise InvalidEdge('Invalid Edge' + E[e])

            self.E = E

    def validEdge(self, edge=''):
        if edge.count(Graph.SPLITER) != Graph.QTD_MAX_SPLITER:
            return False

        # Index element 
        i_edge = edge.index(Graph.SPLITER)

        if i_edge == 0 or edge[-1] == Graph.SPLITER:
            return False

        if not (self.thereIsVertex(edge[:i_edge])) or not (self.thereIsVertex(edge[i_edge + 1:])):
            return False

        return True

    @classmethod
    def validVertex(self, vertex=''):
        
        return vertex != '' and vertex.count(Graph.SPLITER) == 0
    
    def thereIsVertex(self, vertex=''):
        
        return Graph.validVertex(vertex) and self.V.count(vertex) > 0

    def Minimum_Spanning_Tree(self, root='', parents=[], tree=[]):
        if (root == '') or not(self.thereIsVertex(root)):
            raise InvalidEdge('Invalid Root' + root)
        
        graphV = list(self.V[:])
        graphE = self.E
        aux = 2

        if root in graphV:
            if root not in tree:
                tree.append(root)

            parents.append(root)
            for i in graphE:
                if ((root == graphE[i][0] or root == graphE[i][2]) and (
                ((graphE[i][0] not in parents) or (graphE[i][2] not in parents)))):
                    if graphE[i].index(root) == 2:
                        aux = 0
                    tree.append(i)

                    self.Minimum_Spanning_Tree(graphE[i][aux], parents, tree)

        return tree
        
    def __str__(self):
        
        graph_str = ''

        for v in range(len(self.V)):
            graph_str += self.V[v]
            if v < (len(self.V) - 1):  
                graph_str += ", "

        graph_str += '\n'

        for i, e in enumerate(self.E):
            graph_str += self.E[e]
            if not (i == len(self.E) - 1):  
                grafo_str += ", "

        return graph_str
