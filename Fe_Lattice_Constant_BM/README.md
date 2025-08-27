# BM Equation of State Fitting for Fe Lattice Constant (Ex33-35)

This directory contains the calculation process for determining the equilibrium lattice constant of bulk Fe (BCC structure) using the Birch-Murnaghan (BM) equation of state (EOS) fitting method.

This exercise is based on the tutorial "Learn VASP The Hard Way".

---

### File Descriptions

* **`data`**: The raw data points (scaling factor, total energy) generated from the VASP single-point calculations. This is the input data for the fitting script.
* **`bm.py`**: The Python script used to read the `data` file and perform the BM EOS fit. Based on the version provided in the tutorial.

### How to Run

In the directory containing `data` and `bm.py`, execute the following command:

```bash
python3 bm.py