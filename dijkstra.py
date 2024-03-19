import itertools
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

def dijkstra_tsp(distance_matrix):
    num_cities = len(distance_matrix)
    shortest_route = None
    shortest_length = float('inf')
    start_time = time.time()
    update_interval = 1
    visited = set()
    limit_time = 43200

    def dijkstra(start):
        nonlocal shortest_route, shortest_length
        distances = [float('inf')] * num_cities
        distances[start] = 0
        unvisited = set(range(num_cities))

        while unvisited:
            current = min(unvisited, key=lambda x: distances[x])
            unvisited.remove(current)
            visited.add(current)

            for neighbor in unvisited:
                new_distance = distances[current] + distance_matrix[current][neighbor]
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance

        if len(visited) == num_cities:
            for perm in [[start] + list(path) for path in itertools.permutations(visited - {start})]:
                current_length = route_length(perm, distance_matrix)
                if current_length < shortest_length:
                    shortest_length = current_length
                    shortest_route = perm

    for start in range(num_cities):
        dijkstra(start)
        if time.time() - start_time > limit_time:
            print("\033[91m\nTempo limite de 12 horas excedido.\033[0m")
            break
        if time.time() - start_time > update_interval:
            show_timer(start_time)
            update_interval += 1

    return shortest_route, shortest_length
