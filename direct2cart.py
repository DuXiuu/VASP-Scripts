#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# A script to convert a VASP POSCAR/CONTCAR file from
# Direct coordinates to Cartesian coordinates.
#
# Usage: python3 direct2cart.py YOUR_POSCAR_FILE
# It will create a new file named YOUR_POSCAR_FILE_cart
# Author: Gemini for DuXiuu

import sys
import numpy as np

# --- Check if an input file was provided ---
if len(sys.argv) < 2:
    print("Usage: python3 direct2cart.py <filename>")
    sys.exit()

input_file = sys.argv[1]

# --- Read the POSCAR/CONTCAR file ---
with open(input_file, 'r') as f:
    lines = f.readlines()

# --- Extract information from the file ---
comment = lines[0]
scale = float(lines[1])
lattice_vectors = np.array([list(map(float, line.split())) for line in lines[2:5]])

# Scale the lattice vectors
lattice_vectors *= scale

# Find where the coordinates start
# This handles both VASP 4 and VASP 5 formats for atom counts
if lines[5].strip().isdigit():
    # VASP 4 style (obsolete, but good to support)
    atom_counts_line = 5
    coord_type_line = 6
    first_atom_line = 7
else:
    # VASP 5 style
    atom_counts_line = 6
    coord_type_line = 7
    first_atom_line = 8

atom_symbols = lines[5].strip().split()
atom_counts = list(map(int, lines[atom_counts_line].strip().split()))
total_atoms = sum(atom_counts)

coord_type = lines[coord_type_line].strip()

# --- Check if conversion is needed ---
if coord_type.lower().startswith('c'):
    print(f"Coordinates in '{input_file}' are already Cartesian. No conversion needed.")
    sys.exit()

if not coord_type.lower().startswith('d'):
    print(f"Error: Unrecognized coordinate type '{coord_type}' in '{input_file}'.")
    sys.exit()

# --- Perform the conversion ---
frac_coords = np.array([list(map(float, line.split()[:3])) for line in lines[first_atom_line:first_atom_line + total_atoms]])

# The conversion formula: cart_coord = frac_coord . lattice_vectors
cart_coords = np.dot(frac_coords, lattice_vectors)

# --- Write the new file ---
output_file = input_file + "_cart"
with open(output_file, 'w') as f:
    f.write(comment)
    f.write("1.0\n") # New scaling factor is always 1.0
    np.savetxt(f, lattice_vectors, fmt='%.10f')
    f.write(" ".join(atom_symbols) + "\n")
    f.write(" ".join(map(str, atom_counts)) + "\n")
    f.write("Cartesian\n")
    np.savetxt(f, cart_coords, fmt='%.10f')

print(f"Successfully converted '{input_file}' to Cartesian coordinates.")
print(f"New file saved as: '{output_file}'")
