from utils import show_timer
import itertools
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

def brute_force(distance_matrix):
    num_cities = len(distance_matrix)
    shortest_route = None
    shortest_length = float('inf')
    start_time = time.time()
    update_interval = 1 
    
    for perm in itertools.permutations(range(num_cities)):
        current_length = route_length(perm, distance_matrix)
        limit_time = 43200

        if current_length < shortest_length:
            shortest_length = current_length
            shortest_route = perm

        if time.time() - start_time > limit_time:
            print("\033[91m\nTempo limite de 12 horas excedido.\033[0m")
            break

        if time.time() - start_time > update_interval:
            show_timer(start_time)
            update_interval += 1

    return shortest_route, shortest_length
