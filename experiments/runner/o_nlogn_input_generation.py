import random


def generate_intervals(filename, num_intervals, max_value):
    # Generate a list of random intervals
    intervals = []
    for _ in range(num_intervals):
        start = random.randint(0, max_value)
        end = random.randint(start, max_value)  # Ensure end >= start
        intervals.append([start, end])

    # Write intervals to the file
    with open(filename, 'w') as f:
        for interval in intervals:
            f.write(f'{interval[0]} {interval[1]}\n')


# Parameters
num_intervals = 20000  # Number of intervals to generate, within the constraint
max_value = 10**8  # Maximum value for start and end

# File name
filename = './O_nlogn_problem/arr1.txt'

# Generate the file
generate_intervals(filename, num_intervals, max_value)

print(f'File {filename} has been generated.')
