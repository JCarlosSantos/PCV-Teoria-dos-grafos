import sys
import time

def read_matrix_from_file(file_directory):
    distance_matrix = []

    with open(file_directory, 'r') as file:
        for line in file:
            values = list(map(int, line.split()))
            distance_matrix.append(values)

    return distance_matrix

def show_timer(start_time):
    elapsed_time = time.time() - start_time
    progress_info = f"\033[93m\rTempo decorrido: {elapsed_time:.0f}s\033[0m"
    sys.stdout.write(progress_info)
    sys.stdout.flush()
