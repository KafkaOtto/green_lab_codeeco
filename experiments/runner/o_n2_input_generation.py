import random

def generate_files(filename1, filename2, size, max_value):
    # Generate two large arrays with integers up to max_value
    arr1 = [random.randint(1, max_value) for _ in range(size)]
    arr2 = [random.randint(1, max_value) for _ in range(size)]

    # Write arr1 to filename1
    with open(filename1, 'w') as f1:
        f1.write(' '.join(map(str, arr1)))

    # Write arr2 to filename2
    with open(filename2, 'w') as f2:
        f2.write(' '.join(map(str, arr2)))

# Parameters
size = 20000  # Number of elements in each array
max_value = 10**8  # Maximum value for the random integers

# File names
filename1 = './O_n2_problem/arr1.txt'
filename2 = './O_n2_problem/arr2.txt'

# Generate the files
generate_files(filename1, filename2, size, max_value)

print(f'Files {filename1} and {filename2} have been generated.')
