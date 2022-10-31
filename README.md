# Diffusion2D-Python-Package

## Project description

This code solves the diffusion equation in 2D over a square domain which is at a certain temperature and a circular disc at the center which is at a higher temperature. This code solves the diffusion equation using the Finite Difference Method. The thermal diffusivity and initial conditions of the system can be changed by the user. The code produces four plots at various timepoints of the simulation. The diffusion process can be clearly observed in these plots.

## Installing the package

### Using pip3 to install from PyPI

pip install --user --index-url https://test.pypi.org/simple/ chrispfae-diffusion2D

### Required dependencies

[numpy](https://numpy.org/) >= 1.23.4

[matplotlib](https://matplotlib.org/) >= 3.6.1, which requires a Python version < 3.11 at the moment

## Running this package

Import the package via `import diffusion2d` and solve the 2D diffusion equation with diffusion2d.solve() with default values or specify dx, dy, and D.

## Citing

A comprehensive guide on the theory of the code can be found [here](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/). Caution: lots of math.
