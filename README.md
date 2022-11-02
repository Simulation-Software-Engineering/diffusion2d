# Diffusion2D-Python-Package

## Instructions for students

Please follow the instructions in [pypi_exercise.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/03_building_and_packaging/pypi_exercise.md).

The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).

## Project description

- **Information about diffusion2d.py**: This code solves the diffusion equation in 2D over a square domain which is at a certain temperature and a circular disc at the center which is at a higher temperature. This code solves the diffusion equation using the Finite Difference Method. The thermal diffusivity and initial conditions of the system can be changed by the user. The code produces four plots at various timepoints of the simulation. The diffusion process can be clearly observed in these plots.
- Take a few minutes to play around with parameters `dx`, `dy` and `D` in the solver file and observe how the value of `dt` and the output changes. Do you notice if the code takes more or less time to finish the computation? *This tuning is only for you to understand the underlying physical phenomenon and not part of the evaluation.*
- If you are interested in the theoretical background of the code, please have a look in [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).

## Installing the package

### Using pip3 to install from PyPI
It is recommended to install diffusion2d via

```bash
pip3 install --user --extra-index-url https://test.pypi.org/simple/ weilinms-diffusion2d
```

This should work out of the box, if all dependencies are installed correctly.


### Required dependencies
Make sure to install the following dependencies:

* [NumPy](https://numpy.org/)
* [Matplotlib](https://matplotlib.org/)

## Running this package
Just import the pachage into your python file and use the solve method.

## Cite
Since this implemetation is based on literature please have a look at [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/)