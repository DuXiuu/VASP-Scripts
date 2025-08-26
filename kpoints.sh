#!/usr/bin/env bash
# This script generates a KPOINTS file
# Usage: kpoints.sh 3 3 1

echo "K-POINTS" > KPOINTS
echo "0" >> KPOINTS
echo "Gamma" >> KPOINTS
echo "$1 $2 $3" >> KPOINTS
echo "0 0 0" >> KPOINTS
