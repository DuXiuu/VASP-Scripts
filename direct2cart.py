#!/usr/bin/env python3

# -*- coding: utf-8 -*-

# A script to convert a VASP POSCAR/CONTCAR file from

# Direct coordinates to Cartesian coordinates, while preserving

# "Selective dynamics" flags.

# Version 3.1: Corrected indentation.



import sys

import numpy as np



if len(sys.argv) < 2:

    print("Usage: direct2cart.py <filename>")

    sys.exit()



input_file = sys.argv[1]



with open(input_file, 'r') as f:

    lines = f.readlines()



comment = lines[0]

scale = float(lines[1])

lattice_vectors = np.array([list(map(float, line.split())) for line in lines[2:5]])

lattice_vectors *= scale



atom_symbols = lines[5].strip().split()

atom_counts = list(map(int, lines[6].strip().split()))

total_atoms = sum(atom_counts)



has_selective_dynamics = False

current_line_index = 7

if lines[current_line_index].strip().lower().startswith('s'):

    has_selective_dynamics = True

    coord_type_line = 8

    first_atom_line = 9

else:

    coord_type_line = 7

    first_atom_line = 8



coord_type = lines[coord_type_line].strip()



if coord_type.lower().startswith('c'):

    print(f"Coordinates in '{input_file}' are already Cartesian.")

    sys.exit()



frac_coords = []

tf_flags = []

for i in range(total_atoms):

    line_parts = lines[first_atom_line + i].split()

    frac_coords.append(list(map(float, line_parts[:3])))

    if has_selective_dynamics:

        tf_flags.append(line_parts[3:])



frac_coords = np.array(frac_coords)

cart_coords = np.dot(frac_coords, lattice_vectors)



output_file = input_file + "_cart"

with open(output_file, 'w') as f:

    f.write(comment)

    f.write("1.0\n")

    np.savetxt(f, lattice_vectors, fmt='%.10f')

    f.write(" ".join(atom_symbols) + "\n")

    f.write(" ".join(map(str, atom_counts)) + "\n")

    if has_selective_dynamics:

        f.write("Selective dynamics\n")

    f.write("Cartesian\n")

    for i in range(total_atoms):

        f.write(f"  {cart_coords[i,0]:.10f} {cart_coords[i,1]:.10f} {cart_coords[i,2]:.10f}")

        if has_selective_dynamics:

            f.write("   " + "   ".join(tf_flags[i]))

        f.write("\n")



print(f"Successfully converted '{input_file}' to Cartesian coordinates.")

print(f"T/F flags have been preserved.")

print(f"New file saved as: '{output_file}'")
