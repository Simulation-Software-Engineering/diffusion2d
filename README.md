# diffusion2d

## Instructions for students

Please follow the instructions in [pypi_exercise.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/03_building_and_packaging/pypi_exercise.md).

The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).


# Two-Dimensional Diffusion Simulation

## Description

This project implements a numerical simulation of the
two-dimensional diffusion equation using Python.

It simulates heat diffusion across a square plate with
a circular disc at its center. The square domain starts
at a cold temperature, while the circular disc starts
at a higher temperature.

The diffusion equation is solved using the finite
difference method.

The simulation produces four plots showing the
temperature distribution at different time steps.
These plots allow the heat diffusion process to be
observed over time.

## Features

- Two-dimensional heat diffusion simulation.
- Finite difference numerical method.
- Configurable thermal diffusivity.
- Configurable spatial resolution.
- Four temperature distribution plots.
- Visualization using Matplotlib.

## Requirements

- Python >= 3.6
- NumPy
- Matplotlib

## Installation

Install the package using pip:

```bash
pip install merchahm_diffusion2d
```

## Usage

Import the simulation:

```python
from diffusion2d import diffusion2d

diffusion2d.solve()
```

You can also customize the simulation parameters:

```python
diffusion2d.solve(dx=0.2, dy=0.2, D=4.0)
```

Parameters:

- dx: Spatial interval in the x direction.
- dy: Spatial interval in the y direction.
- D: Thermal diffusivity.

All parameters have default values.

## Repository

https://github.com/Simulation-Software-Engineering/diffusion2D

## License

MIT License


