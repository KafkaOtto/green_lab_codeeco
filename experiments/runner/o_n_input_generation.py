import random

def generate_files(filename1, size, max_value):
    # Generate two large arrays with integers up to max_value
    arr1 = [random.randint(1, max_value) for _ in range(size)]

    # Write arr1 to filename1
    with open(filename1, 'w') as f1:
        f1.write(' '.join(map(str, arr1)))

# Parameters
size = 40000  # Number of elements in each array
max_value = 10**8  # Maximum value for the random integers

# File names
filename1 = './O_n_problem/arr1.txt'

# Generate the files
generate_files(filename1, size, max_value)

print(f'Files {filename1} have been generated.')
