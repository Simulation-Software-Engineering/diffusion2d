# Diffusion2D-Python-Package

## Instructions for students

Please follow the instructions in [pypi_exercise.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/03_building_and_packaging/pypi_exercise.md).

The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).

## Project description

This code solves the diffusion equation in 2D over a square domain which is at a certain temperature and a circular disc at the center which is at a higher temperature. This code solves the diffusion equation using the Finite Difference Method. The thermal diffusivity and initial conditions of the system can be changed by the user. The code produces four plots at various timepoints of the simulation. The diffusion process can be clearly observed in these plots.

## Installing the package

### Using pip3 to install from PyPI

To install the package from PyPI, run the following command in the terminal:

```sh
pip3 install --user --index-url https://test.pypi.org/simple/ Wagnerln-diffusion2d
```

### Install from source

To install the package from source run:

```sh
pip3 install .
```

### Required dependencies

The package requires the following dependencies:

- numpy
- matplotlib

Additionally Python 3.6 or higher.

## Running this package

```python
import Wagnerln-diffusion2d as s2d # load the 2d diffusion solver
s2d.solve() # run the solver
```

:warning: Note that the package is not importable with its current name `Wagnerln-diffusion2d`. Stay tuned for a name change. :warning:
