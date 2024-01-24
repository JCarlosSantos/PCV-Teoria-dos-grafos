def read_matrix_from_file(file_directory):
    distance_matrix = []

    with open(file_directory, 'r') as file:
        for line in file:
            values = list(map(int, line.split()))
            distance_matrix.append(values)

    return distance_matrix

file_names = ['att48', 'dantzig42', 'fri26', 'gr17', 'p01']

for file_name in file_names:
    file_directory = f'datasets/{file_name}.txt'
    distance_matrix = read_matrix_from_file(file_directory)

    print(f'{file_name}: {distance_matrix}\n')
