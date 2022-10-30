# Diffusion2D-Python-Package

## Instructions for students

Please follow the instructions in [pypi_exercise.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/03_building_and_packaging/pypi_exercise.md).

The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).

## Project description
This code solves the diffusion equation in 2D over a square domain which is at a certain temperature and a circular disc at the center which is at a higher temperature. This code solves the diffusion equation using the Finite Difference Method. The thermal diffusivity and initial conditions of the system can be changed by the user. The code produces four plots at various timepoints of the simulation. The diffusion process can be clearly observed in these plots.
## Installing the package

### Using pip3 to install from PyPI
```
pip3 install --user --index-url https://test.pypi.org/simple/ ahmedmd_diffusion_2d

```
### Required dependencies
- pyhton >= 3.6
- numpy
- matplotlib

Note : You should install `matplotlib` manually before installing `ahmedmd_diffusion_2d` since it is not available on test.pypi.org while `numpy` is installed automatically by pip.
To install matplotlib manually use this command :
```
pip3 isntall matplotlib
```
## Running this package
Use  `test.py` to test the package.
## Citing
This code is based on an example from the book Learning Scientific Programming with Python by Christian Hill.