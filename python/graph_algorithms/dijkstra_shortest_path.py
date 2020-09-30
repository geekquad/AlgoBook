import sys
def to_be_visited():
  global visited_and_distance
  v = -10
  for index in range(number_of_vertices):
    if visited_and_distance[index][0] == 0 \
      and (v < 0 or visited_and_distance[index][1] <= \
      visited_and_distance[v][1]):
        v = index
  return v
vertices = [[0, 1, 1, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1],
            [0, 0, 0, 0]]
edges =  [[0, 3, 4, 0],
          [0, 0, 0.5, 0],
          [0, 0, 0, 1],
          [0, 0, 0, 0]]

number_of_vertices = len(vertices[0])
visited_and_distance = [[0, 0]]
for i in range(number_of_vertices-1):
  visited_and_distance.append([0, sys.maxsize])

for vertex in range(number_of_vertices):
  to_visit = to_be_visited()
  for neighbor_index in range(number_of_vertices):
    if vertices[to_visit][neighbor_index] == 1 and \
     visited_and_distance[neighbor_index][0] == 0:
      new_distance = visited_and_distance[to_visit][1] \
      + edges[to_visit][neighbor_index]
      if visited_and_distance[neighbor_index][1] > new_distance:
        visited_and_distance[neighbor_index][1] = new_distance
  visited_and_distance[to_visit][0] = 1

i = 0 
    
for distance in visited_and_distance:
  print("The shortest distance of ",chr(ord('a') + i),\
  " from the source vertex a is:",distance[1])
  i = i + 1