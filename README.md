# Diffusion2D-Python-Package

## Instructions for students

Please follow the instructions in [pypi_exercise.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/03_building_and_packaging/pypi_exercise.md).

The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).

## Project description
This code solves the diffusion equation in 2D over a square domain which is at a certain temperature and a circular disc at the center which is at a higher temperature. This code solves the diffusion equation using the Finite Difference Method. The thermal diffusivity and initial conditions of the system can be changed by the user. The code produces four plots at various timepoints of the simulation. The diffusion process can be clearly observed in these plots.

## Installing the package
pip install mananij-diffusion2D

to install the package from test pypi - 

pip install --extra-index-url https://test.pypi.org/simple/ mananij_diffusion2D==0.0.4

### Using pip3 to install from PyPI
pip3 install mananij-siffusion2D

to install the package from test pypi using pip3

pip install --extra-index-url https://test.pypi.org/simple/ mananij_diffusion2D==0.0.4

### Required dependencies
numpy==1.21.6
matplotlib==3.5.3

## Running this package
from mananij_diffusion2D import diffusion2D

diffusion2D.solve()

you can also pass the argument to solve,

diffusion2D.solve(dx = 0.1, dy = 0.1, D = 4)

## Citing
Link to the Python Package - https://test.pypi.org/project/mananij-diffusion2D/
