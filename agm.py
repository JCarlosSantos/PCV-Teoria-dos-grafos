def prim(distance_matrix):
    num_cities = len(distance_matrix)
    MST = []
    visited = [False] * num_cities
    distances = [float('inf')] * num_cities

    start_vertex = 0
    distances[start_vertex] = 0

    for _ in range(num_cities):
        min_distance = float('inf')
        min_vertex = -1
        for v in range(num_cities):
            if not visited[v] and distances[v] < min_distance:
                min_distance = distances[v]
                min_vertex = v

        visited[min_vertex] = True

        if min_vertex != start_vertex:
            MST.append((min_vertex, min_vertex))

        for v in range(num_cities):
            if not visited[v] and distance_matrix[min_vertex][v] < distances[v]:
                distances[v] = distance_matrix[min_vertex][v]

    return MST
