# Diffusion2D-Python-Package

## Instructions for students

Please follow the instructions in [pypi_exercise.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/03_building_and_packaging/pypi_exercise.md).

The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).

## Project description
A project to solve the 2D diffusion problem based on the 3 base parameters: dX, dY and D.

## Installing the package

### Using pip3 to install from PyPI
pip install -i https://test.pypi.org/simple/ attilaks-diffusion2d==VERSION

### Required dependencies
numpy

matplotlib

## Running this package

from attilaks-diffusion2d import diffusion2d

// optional parameters dx, dy and D

diffusion2d.solve()

## Citing

Simulation Software Engineering Course @ University of Stuttgart
