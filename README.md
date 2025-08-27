# VASP-Scripts

My personal collection of VASP and Linux scripts for computational chemistry. This repository contains useful tools and calculation examples from the 'Learn VASP The Hard Way' tutorial.

---

## Ⅰ. General Utility Scripts 

These scripts are general-purpose tools that can be used in various VASP calculations.

* **`potcar.sh`**: Automatically generates a `POTCAR` file by concatenating individual element files.
* **`kpoints.sh`**: Quickly generates a `KPOINTS` file for Gamma-centered meshes.
* **`direct2cart.py`**: Converts a VASP `POSCAR`/`CONTCAR` file from Direct to Cartesian coordinates.

---

## Ⅱ. Calculation Examples 

This section contains specific calculation projects. Each folder is self-contained with its own data, analysis scripts, and a detailed `README.md`.

* **`/Fe_Lattice_Constant_BM`**: Contains the data and analysis for calculating the lattice constant of bulk Fe using the Birch-Murnaghan fitting method. **See the `README.md` inside this folder for details.**
