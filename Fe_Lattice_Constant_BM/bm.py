#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This script is based on the bm.py script from the tutorial
# 'Learn VASP The Hard Way' by BigBro (www.bigbrosci.com).
# It is used for educational purposes to fit the Birch-Murnaghan EOS.

import math
import numpy as np

print("################################################################")
print("####### Warning #######")
print("This script is designed for fitting data with a scaling factor.")
print("If your data's first column is the lattice constant 'a',")
print("you MUST modify the formula for 'x' on line 24.")
print("################################################################")

# --- Step 1: Read data from the 'data' file ---
# usecols=(0,1) reads the 1st and 2nd columns.
# delimiter='\t' means columns are separated by a Tab.
a_scale, E = np.loadtxt('data', usecols=(0,1), delimiter='\t', unpack=True)

# --- Step 2: Convert scaling factor to x=(1/a)^2 for fitting ---
# The experimental lattice constant for Fe is 2.8664 Å.
# We multiply the scaling factor by this to get the actual 'a'.
# Then calculate x = (1/a)^2.
x = (a_scale * 2.8664)**(-2)

# --- Step 3: Perform a 3rd-order polynomial fit ---
# This fits the equation: E = p[0]*x^3 + p[1]*x^2 + p[2]*x + p[3]
# which corresponds to the BM equation form.
# The coefficients are stored in the list 'p'.
p = np.polyfit(x, E, 3)
c3, c2, c1, c0 = p[0], p[1], p[2], p[3]

# --- Step 4: Solve the derivative to find the minimum ---
# The derivative of the polynomial is: 3*c3*x^2 + 2*c2*x + c1 = 0
# We solve this quadratic equation for x.
x1 = (-2*c2 + math.sqrt(4*c2**2 - 12*c3*c1)) / (6*c3)
x2 = (-2*c2 - math.sqrt(4*c2**2 - 12*c3*c1)) / (6*c3)

# --- Step 5: Convert x back to lattice constant 'a' and print ---
# The positive solution is the physically meaningful one.
a = (1/x1)**0.5
print("The equilibrium lattice constant is: %.4f Angstrom" % a)
