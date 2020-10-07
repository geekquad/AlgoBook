# AO star by Priyanka 
#input should be given such that, nodes having "*and* should be together

import sys
# input parameters
graph = { "A": [["B", "C"], ["D"]], "B": [ ["G"], ["H"] ], "D": [["E", "F"]] } 
node_cost ={ "B": 6, "C": 12, "D":10, "E": 4, "F": 4, "G": 5, "H": 7 } 
EDGE_COST = 1
NODE_MIN_COST = {}

# main function
def solve(node): 

  if node not in graph.keys():
    if node not in node_cost:
      return 0
    return node_cost[node]

  min_cost = sys.maxsize
  for child_path in graph[node]:
    cost = 0
    for child in child_path:
      NODE_MIN_COST[child] = solve(child)
      cost = cost + NODE_MIN_COST[child] + 1
    min_cost = min(cost, min_cost)
  
  return min_cost

def aostar():
  HEAD_NODE = ["A"] 
  NODE_MIN_COST[HEAD_NODE[0]] = solve(HEAD_NODE[0]) 
  print('Min Cost of graph = ', NODE_MIN_COST[HEAD_NODE[0]], '\n') 
  print('****Node-Wise Min Cost****\n')
  for i, v in NODE_MIN_COST.items():
    print('Node = ', i, ', Min Cost = ', v)

#calling main 
aostar()
