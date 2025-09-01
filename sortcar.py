#!/usr/bin/env python3
import sys
from operator import itemgetter

# --- Open input and output files ---
infile_name = sys.argv[1]
output_name = infile_name + '_sorted'

with open(infile_name, 'r') as poscar_in, open(output_name, 'w') as poscar_out:
    # --- Read and write the standard header (first 7 lines) ---
    title = poscar_in.readline()
    scaling_factor_line = poscar_in.readline()
    vec1 = poscar_in.readline()
    vec2 = poscar_in.readline()
    vec3 = poscar_in.readline()
    elements_line = poscar_in.readline()
    numbers_line = poscar_in.readline()

    # --- Intelligent check for Selective Dynamics (MODIFICATION) ---
    # Read the 8th line to check its content
    line8 = poscar_in.readline()
    
    # If the line starts with 'S' or 's', it's the Selective Dynamics line
    if line8.strip().lower().startswith('s'):
        selective_dynamics_line = line8
        coordinate_system_line = poscar_in.readline() # The next line is the coordinate system
    else:
        # Otherwise, the 8th line itself is the coordinate system
        selective_dynamics_line = "" # This line doesn't exist, so we use an empty string
        coordinate_system_line = line8
    # --- End of Modification ---

    # --- Write the header to the new file ---
    poscar_out.write(title)
    poscar_out.write(scaling_factor_line)
    poscar_out.write(vec1)
    poscar_out.write(vec2)
    poscar_out.write(vec3)
    poscar_out.write(elements_line)
    poscar_out.write(numbers_line)
    if selective_dynamics_line: # Only write this line if it exists
        poscar_out.write(selective_dynamics_line)
    poscar_out.write(coordinate_system_line)
    
    # --- Read coordinates ---
    total_atoms = sum(map(int, numbers_line.split()))
    coords = []
    for _ in range(total_atoms):
        line_parts = poscar_in.readline().split()
        if line_parts: # Make sure the line is not empty
            coords.append(line_parts)

    # --- Sort coordinates by the 3rd column (Z-coordinate) ---
    # The original sorting logic is correct
    coords.sort(key=itemgetter(2))

    # --- Write sorted coordinates to the new file ---
    for line_parts in coords:
        poscar_out.write("  " + "  ".join(line_parts) + '\n')

print(f"Successfully sorted atoms in '{infile_name}' and wrote to '{output_name}'")
