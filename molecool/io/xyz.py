"""
functions for manipulating xyz files.
"""

import numpy as np


def open_xyz(file_location):

    # Open an xyz file and return symbols and coordinates.
    xyz_file = np.genfromtxt(fname=file_location, skip_header=2, dtype="unicode")
    symbols = xyz_file[:, 0]
    coords = xyz_file[:, 1:]
    coords = coords.astype(float)
    return symbols, coords


def write_xyz(file_location, symbols, coordinates):

    # Write an xyz file given a file location, symbols, and coordinates.
    num_atoms = len(symbols)

    if num_atoms != len(coordinates):
        raise ValueError(
            f"write_xyz : the number of symbols ({num_atoms}) and number of "
            f"coordinates ({len(coordinates)}) must be the same to write xyz file!"
        )

    with open(file_location, "w+") as f:
        f.write("{}\n".format(num_atoms))
        f.write("XYZ file\n")

        for i in range(num_atoms):
            f.write(
                "{}\t{}\t{}\t{}\n".format(
                    symbols[i], coordinates[i, 0], coordinates[i, 1], coordinates[i, 2]
                )
            )