# Diffusion2D-Python-Package

## Instructions for students

Please follow the instructions in [pypi_exercise.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/03_building_and_packaging/pypi_exercise.md).

The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).

## Project description
This code solves the diffusion equation in 2D over a square domain which is at a certain temperature and a circular disc at the center which is at a higher temperature. This code solves the diffusion equation using the Finite Difference Method. The thermal diffusivity and initial conditions of the system can be changed by the user. The code produces four plots at various timepoints of the simulation. The diffusion process can be clearly observed in these plots.
## Installing the package

### Using pip3 to install from PyPI
```
pip install --user --index-url https://test.pypi.org/simple/ schiztn-diffusion2D==0.03
```
### Required dependencies
- NumPy
- Matplotlib

Matplotlib is not available on test.pypi.org. To install it manually use
```
pip install matplotlib
```

## Running this package
```python
from schiztn_diffusion2D import diffusion2d

diffusion2d.solve()
```
## Citing