#!/usr/bin/env bash
#
# Create a VASP POTCAR file by concatenating POTCAR files
# Usage: potcar.sh C H O
#

# ---!!! Please confirm your pseudopotential library path here !!!---
repo="$HOME/pseudopotentials/potpaw_PBE"

# Check if a POTCAR file already exists in the current directory
if [ -f POTCAR ] ; then
    mv -f POTCAR old-POTCAR
    echo " ** Warning: old POTCAR file found and renamed to 'old-POTCAR'."
fi

# Main loop - iterate through all the elements you input
for i in "$@"
do
    if [ -f "$repo/$i/POTCAR" ] ; then
        cat "$repo/$i/POTCAR" >> POTCAR
    elif [ -f "$repo/$i/POTCAR.Z" ] ; then
        zcat "$repo/$i/POTCAR.Z" >> POTCAR
    elif [ -f "$repo/$i/POTCAR.gz" ] ; then
        gunzip -c "$repo/$i/POTCAR.gz" >> POTCAR
    else
        echo " ** Warning: No suitable POTCAR for element '$i' found!! Skipped this element."
    fi
done
