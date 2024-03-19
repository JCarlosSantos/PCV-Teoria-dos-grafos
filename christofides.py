from utils import show_timer
import time

def route_length(route, distance_matrix):
    total_distance = 0
    num_cities = len(route)

    for i in range(num_cities - 1):
        from_city = route[i]
        to_city = route[i + 1]
        total_distance += distance_matrix[from_city][to_city]
    total_distance += distance_matrix[route[num_cities - 1]][route[0]]

    return total_distance

def minimum_spanning_tree(distance_matrix):
    num_cities = len(distance_matrix)
    visited = [False] * num_cities
    MST = []

    visited[0] = True

    for _ in range(num_cities - 1):
        min_edge = [None, None, float('inf')]
        for i in range(num_cities):
            if visited[i]:
                for j in range(num_cities):
                    if not visited[j] and distance_matrix[i][j] < min_edge[2]:
                        min_edge = [i, j, distance_matrix[i][j]]
        MST.append(min_edge)
        visited[min_edge[1]] = True

    return MST

def find_odd_vertices(MST):
    vertices_degree = {}
    odd_vertices = []

    for edge in MST:
        for i in range(2):
            if edge[i] not in vertices_degree:
                vertices_degree[edge[i]] = 0
            vertices_degree[edge[i]] += 1

    for vertex, degree in vertices_degree.items():
        if degree % 2 == 1:
            odd_vertices.append(vertex)

    return odd_vertices

def minimum_weight_matching(odd_vertices, distance_matrix):
    matched = [False] * len(odd_vertices)
    edges = []
    num_vertices = len(odd_vertices)

    for i in range(num_vertices - 1):
        if not matched[i]:
            min_edge = [None, None, float('inf')]
            for j in range(i + 1, num_vertices):
                if not matched[j] and distance_matrix[odd_vertices[i]][odd_vertices[j]] < min_edge[2]:
                    min_edge = [i, j, distance_matrix[odd_vertices[i]][odd_vertices[j]]]
            matched[min_edge[0]] = True
            matched[min_edge[1]] = True
            edges.append((odd_vertices[min_edge[0]], odd_vertices[min_edge[1]]))

    return edges

def eulerian_tour(graph):
    tour = []
    for edge in graph:
        tour.append(edge[0])
        tour.append(edge[1])

    return tour

def remove_repeated_vertices(tour):
    visited = set()
    unique_tour = []
    for vertex in tour:
        if vertex not in visited:
            visited.add(vertex)
            unique_tour.append(vertex)

    return unique_tour

def christofides(distance_matrix):
    num_cities = len(distance_matrix)
    shortest_route = None
    shortest_length = float('inf')
    start_time = time.time()
    update_interval = 1
    limit_time = 43200

    def find_best_path(start, MST):
        nonlocal shortest_route, shortest_length
        odd_vertices = find_odd_vertices(MST)
        matching_edges = minimum_weight_matching(odd_vertices, distance_matrix)
        multigraph = MST + matching_edges
        tour = eulerian_tour(multigraph)
        tour = remove_repeated_vertices(tour)

        current_length = route_length(tour, distance_matrix)
        if current_length < shortest_length:
            shortest_length = current_length
            shortest_route = tour

    MST = minimum_spanning_tree(distance_matrix)

    for start in range(num_cities):
        find_best_path(start, MST)

        if time.time() - start_time > limit_time:
            print("\033[91m\nTempo limite de 12 horas excedido.\033[0m")
            break
        
        if time.time() - start_time > update_interval:
            show_timer(start_time)
            update_interval += 1

    return shortest_route, shortest_length
