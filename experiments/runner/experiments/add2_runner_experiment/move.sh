#!/bin/bash

# This script moves directories from run_2_repetition_0 to run_17_repetition_0
# and renames them to run_344_repetition_0 to run_359_repetition_0

start_src=2
end_src=17
start_dest=344

for ((i=$start_src; i<=$end_src; i++)); do
    # Calculate the destination directory number
    dest=$((start_dest + i - start_src))

    # Define the source and destination directory names
    src_dir="run_${i}_repetition_0"
    dest_dir="run_${dest}_repetition_0"

    # Move the source directory to the destination directory
    if [ -d "$src_dir" ]; then
        mv "$src_dir" "$dest_dir"
        echo "Moved $src_dir to $dest_dir"
    else
        echo "Directory $src_dir does not exist, skipping."
    fi
done
