# Diffusion2D-Python-Package

## Instructions for students

Please follow the instructions in [pypi_exercise.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/03_building_and_packaging/pypi_exercise.md).

The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).

## Project description
This code solves the diffusion equation in 2D over a square domain which is at a certain temperature and a circular disc at the center which is at a higher temperature and plots the results

## Installing the package

### Using pip3 to install from PyPI
 `pip install -i https://test.pypi.org/simple/ hofmanjn-diffusion2d==0.0.5`

### Required dependencies
* numpy
* matplotlib


## Running this package
```
import diffusion2d
diffusion2d.solve()
```

## Citing
https://simulation-software-engineering.github.io/homepage/
