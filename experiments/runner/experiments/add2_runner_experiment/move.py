import csv

# Input and output file names
input_csv = 'run_table.csv'
output_csv = 'run_table_move.csv'


# Function to update the run_id
def update_run_id(run_id):
    if run_id.startswith("run_") and run_id.endswith("_repetition_0"):
        try:
            # Extract the number part
            run_number = int(run_id.split('_')[1])
            # Check if it is within the range 0 to 17
            if 0 <= run_number <= 17:
                # Update the number to the new range 342 to 359
                new_run_number = run_number + 342
                return f"run_{new_run_number}_repetition_0"
        except ValueError:
            pass
    # Return the original if no changes are needed
    return run_id


# Read from the input CSV and write to the output CSV
with open(input_csv, 'r') as infile, open(output_csv, 'w', newline='') as outfile:
    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)

    # Write the header
    writer.writeheader()

    # Update the run_id and write rows to the new file
    for row in reader:
        row['__run_id'] = update_run_id(row['__run_id'])
        writer.writerow(row)

print(f"Updated CSV file has been saved as {output_csv}.")
