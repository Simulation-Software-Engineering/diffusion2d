# diffusion2d

## Description

This package can be used to solve diffusion equations over a two-dimensional square domain
where the domain starts with a fixed temperature except for a circle in its center which is at a higher temperature.

## Installing the package

The package can be installed from [TestPyPI](https://test.pypi.org).
Its name there is `reichsl-diffusion2d`.

To install using pip, run
`pip install --index-url https://test.pypi.org/simple reichsl-diffusion2d --extra-index-url https://pypi.org/simple`

## Running this package

Once installed, you can import the package with
`import reichsl_diffusion2d`

The package exposes one method called `solve()`

Usage example:
```py
import reichsl_diffusion2d as diffusion2d

diffusion2d.solve(0.1, 0.1, 4.)
```

## Citing

This package is part of the [exercise on packaging Python code](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/03_building_and_packaging/pypi_exercise.md) from the [Simulation Software Engineering](https://github.com/Simulation-Software-Engineering) course.

The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).

