# diffusion2d

## Instructions for students

Please follow the instructions in [pypi_exercise.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/03_building_and_packaging/pypi_exercise.md).

The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).

## Description
This package solves the two-dimensional diffusion equation on a square plate with fixed boundary conditions using an explicit finite difference method. The temperature distribution is computed over time, and the results are visualized using contour plots.

## Installing the package
To install the package, use pip:

```bash
pip install -i https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple oezsoyik-diffusion2d
```

## Running this package
After installing the package, you can run the diffusion simulation by executing the following command in your terminal:

```python
from oezsoyik_diffusion2d import diffusion2d
solve()
```

## Citing
If you use this code in your research, please cite the following book:
> L. Hatton, "Learning Scientific Programming with Python", 2nd Edition, Cambridge University Press, 2024.
