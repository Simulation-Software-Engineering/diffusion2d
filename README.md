# Diffusion2D-Python-Package

## Project description

This code solves the diffusion equation in 2D over a square domain which is at a certain temperature and a circular disc at the center which is at a higher temperature. This code solves the diffusion equation using the Finite Difference Method. The thermal diffusivity and initial conditions of the system can be changed by the user. The code produces four plots at various timepoints of the simulation. The diffusion process can be clearly observed in these plots.

## Installing the package

Use `pip install .`

### Using pip3 to install from PyPI

`pip install -i https://test.pypi.org/simple/ neumantm-diffusion2d`

### Required dependencies

- `matplotlib`
- `numpy`

## Running this package

Open an interactive python prompt, import `diffusion2d` and call `diffusion2d.solve()`.
You may pass some parameters to solve. See the code.

## Citing

- Theoretical background: [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).
