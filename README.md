# diffusion2d

## Instructions for students

Please follow the instructions in [pypi_exercise.md].

The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming
with Python"].

## Description

This package simulates two-dimensional heat diffusion on a square steel plate. It starts from a cold
plate with a hot circular region in the center and solves the diffusion equation with an explicit
finite-difference scheme, plotting the temperature field at several time steps.

## Installing the package

The package can be installed from [TestPyPI].

To install using pip execute:

```bash
pip install --index-url https://test.pypi.org/simple/ madebytimo-diffusion2d
```

To install the dependencies execute:

```bash
pip install numpy matplotlib
```

## Running this package

The package exposes one method called `solve()`. You can import it and use it directly:

```python
from madebytimo_diffusion2d import solve

solve()
```

## Citing

The code is based on [Chapter 7 of the book "Learning Scientific Programming with Python"].

[Chapter 7 of the book "Learning Scientific Programming with Python"]:
    https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/
[pypi_exercise.md]:
    https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/03_building_and_packaging/pypi_exercise.md
[TestPyPi]: https://test.pypi.org/project/madebytimo-diffusion2d
