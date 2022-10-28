# Diffusion2D-Python-Package

## Instructions for students

Please follow the instructions in [pypi_exercise.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/03_building_and_packaging/pypi_exercise.md).

The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).

## Project description

This code solves the diffusion equation in 2D over a square domain which is at a certain temperature and a circular disc at the center which is at a higher temperature. This code solves the diffusion equation using the Finite Difference Method. The thermal diffusivity and initial conditions of the system can be changed by the user. The code produces four plots at various timepoints of the simulation. The diffusion process can be clearly observed in these plots.

## Installing the package

### Using pip3 to install from PyPI

```
pip3 install --user --index-url https://test.pypi.org/simple/ herbjs_diffusion2D
```

### Required dependencies
- `numpy`
- `matplotlib`

While `numpy` is automatically installed by `pip`, `matplotlib` has to be installed manually since it is not available on test.pypi.org.
This has to be done *before* installing `herbjs-diffusion2D` by
```
pip3 install matplotlib
```

## Running this package

> Here, the `pip` package is called `herbjs-diffusion2D`, but the python module is called `herbjs_diffusion2D`!

```python
from herbjs_diffusion2D import diffusion2d

diffusion2d.solve()
```

## Citing
This code is based on an [example](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/) from the book [Learning Scientific Programming with Python](https://scipython.com/) by Christian Hill.
