# Diffusion2D-Python-Package
bhawsina_diffusion2D

## Instructions for students

Please follow the instructions in [pypi_exercise.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/03_building_and_packaging/pypi_exercise.md).

The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).

## Project description
This code solves the diffusion equation in 2D over a square domain which is at a certain temperature and a circular disc at the center which is at a higher temperature. This code solves the diffusion equation using the Finite Difference Method. The thermal diffusivity and initial conditions of the system can be changed by the user. The code produces four plots at various timepoints of the simulation. The diffusion process can be clearly observed in these plots.

## Installing the package
pip install --user --index-url https://test.pypi.org/simple/ bhawsina_diffusion2D

### Using pip3 to install from PyPI
pip3 install numpy
pip3 install matplotlib

### Required dependencies
matplotlib:3.6.1
numpy:1.23.4

## Running this package
Default: from bhawsina_diffusion2D import diffusion2D diffusion2D.solve()
Parameterized: from bhawsina_diffusion2D import diffusion2D diffusion2D.solve(dx = 0.1, dy = 0.1, D = 4.)

## Citing
https://test.pypi.org/project/bhawsina_diffusion2D/
