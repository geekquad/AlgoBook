NUMBER_OF_VERTICES = 5
INITIAL_VERTEX = 3
DISTANCE_MATRIX = { 0: { 0: 27.5, 1: 10, 2: 15, 3: 21, 4: 22 }, 1: { 0: 10, 1: 12, 2: 16, 3: 14, 4: 14.5 }, 2: { 0: 15, 1: 16, 2: 15, 3: 12, 4: 24 }, 3: { 0: 21, 1: 14, 2: 12, 3: 13.6, 4: 27 }, 4: { 0: 22, 1: 14.5, 2: 24, 3: 27, 4: 12 } }

def nearest_neighbors_solution(distance_matrix):
    visited = {i: False for i in range(NUMBER_OF_VERTICES)}
    nearest_neighbors = {i: -1 for i in range(NUMBER_OF_VERTICES)}
    last_vertex = INITIAL_VERTEX
    should_continue = True

    while should_continue:
        should_continue = False
        visited[last_vertex] = True
        shortest_distance = float("inf")
        closest_neighbor = -1

        for i in distance_matrix[last_vertex]:
            if distance_matrix[last_vertex][i] < shortest_distance and not (visited[i]):
                shortest_distance = distance_matrix[last_vertex][i]
                closest_neighbor = i
                should_continue = True

        if should_continue:
            nearest_neighbors[last_vertex] = closest_neighbor
            last_vertex = closest_neighbor
        else:
            nearest_neighbors[last_vertex] = INITIAL_VERTEX
    return nearest_neighbors

print(nearest_neighbors_solution(DISTANCE_MATRIX))