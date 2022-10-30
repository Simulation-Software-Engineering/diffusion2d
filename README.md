# Diffusion2D-Python-Package

## Instructions for students

Please follow the instructions in [pypi_exercise.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/03_building_and_packaging/pypi_exercise.md).

The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).

## Project description
This code solves the diffusion equation in 2D over a square domain which is at a certain temperature and a circular disc at the center which is at a higher temperature. This code solves the diffusion equation using the Finite Difference Method. The thermal diffusivity and initial conditions of the system can be changed by the user. The code produces four plots at various timepoints of the simulation. The diffusion process can be clearly observed in these plots.

## Installing the package

### Using pip3 to install from PyPI
```
pip3 install --user --index-url https://test.pypi.org/simple/ strackmsdiffusion2D
```
### Required dependencies
-`numpy`
-`matplotlib`

`matplotlib` is not available on test.pypi.org so it has to be installed before by
```
pip3 install matplotlib
```
## Running this package
```
from strackmsdiffusion2D import diffusion2d

diffusion2d.solve()
```
## Citing
Theoretical background of the code: Chapter 7 of the book "Learning Scientific Programming with Python" 
