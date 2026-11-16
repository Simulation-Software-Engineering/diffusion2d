# diffusion2d

## Instructions for students

Please follow the instructions in [pypi_exercise.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/03_building_and_packaging/pypi_exercise.md).

The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).

## Description

This code solves the diffusion equation over a two-dimensional square domain which is at a certain temperature, and a circular disc at its center which is at a higher temperature. The diffusion equation is solved using the [finite-difference method](https://en.wikipedia.org/wiki/Finite_difference_method). The thermal diffusivity and initial conditions of the system can be changed by the user. The code produces four plots at various timepoints of the simulation. The diffusion process can be clearly observed in these plots.

The package contains two modules:

- `diffusion2d.py`: the solver, with the function `solve(dx=0.1, dy=0.1, D=4.)`
- `output.py`: plotting, with the functions `create_plot()` and `output_plots()`

## Installing the package

The package is published on [TestPyPI](https://test.pypi.org/project/vashissm-diffusion2d/). Its dependencies (NumPy and Matplotlib) come from PyPI:

```bash
pip install -i https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ vashissm_diffusion2d
```

## Running this package

```python
from vashissm_diffusion2d import diffusion2d

diffusion2d.solve()                    # default parameters
diffusion2d.solve(dx=0.2, dy=0.2, D=2.)  # mesh intervals in mm, thermal diffusivity in mm^2/s
```

The solver prints the time step `dt` and opens a figure with the temperature field at four time points.

## Citing

The code is based on the example in [Chapter 7 of "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/) by Christian Hill. If you use this package, please cite that book and link to this repository.
