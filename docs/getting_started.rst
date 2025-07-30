Getting Started
===============

This page details how to get started with molecool. Molecool is a package which was developed for the MolSSI Best Practices workshop.

Installation
------------
To install molecool, you will need an environment with the following packages:

* Python 3.11
* NumPy
* Matplotlib

Once you have these packages installed, you can install molecool in the same environment using
::

     pip install -e .

Usage
-------
Once installed, you can use the package. This example draws a benzene molecule from an xyz file.
::

    import molecool

    benzene_symbols, benzene_coords = molecool.open_xyz('benzene.xyz')
    benzene_bonds = molecool.build_bond_list(benzene_coords)
    molecool.draw_molecule(benzene_coords, benzene_symbols, draw_bonds=benzene_bonds)
