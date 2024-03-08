
from utils import read_matrix_from_file
from brute_force import brute_force


# file_names = ['att48', 'dantzig42', 'fri26', 'gr17', 'p01']
file_names = ['teste', 'teste']
selected_algorithm = brute_force

for file_name in file_names:
    file_directory = f'datasets/{file_name}.txt'
    distance_matrix = read_matrix_from_file(file_directory)

    print(f"\033[1mCalculando a menor rota para {file_name}...\033[0m")
    shortest_route, shortest_length, total_permutations = selected_algorithm(distance_matrix)
    print(f"\033[1;32m\nA menor rota para {file_name} é: {shortest_route}, com comprimento {shortest_length}.\033[0m")
    print(f"Número de permutações: {total_permutations}\n----------------------------------")
