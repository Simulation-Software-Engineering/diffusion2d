# kakadesm_diffusion2d

## Instructions for students

Please follow the instructions in [pypi_exercise.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/03_building_and_packaging/pypi_exercise.md).

The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).

## Description

This code solves the diffusion equation over a two dimensional square domain which is at a certain temperature, and a circular disc at its center which is at a higher temperature. The diffusion equation is solved using the [finite-difference method](https://en.wikipedia.org/wiki/Finite_difference_method). The thermal diffusivity and initial conditions of the system can be changed by the user. The code produces four plots at various timepoints of the simulation. The diffusion process can be clearly observed in these plots.

## Installing the package

The package is hosted on TestPyPI. Its dependencies (NumPy, Matplotlib) are installed from PyPI:

```bash
pip install --extra-index-url https://test.pypi.org/simple/ kakadesm_diffusion2d==0.0.1
```

To install from source for local development, run this in the repository root:

```bash
pip install -e .
```

## Running this package

```python
from kakadesm_diffusion2d import diffusion2d

diffusion2d.solve()                          # default parameters
diffusion2d.solve(dx=0.5, dy=0.2, D=4.)      # custom parameters
```

or from the command line:

```bash
python -c "from kakadesm_diffusion2d import diffusion2d; diffusion2d.solve(dx=0.5, dy=0.2, D=4.)"
```

`solve()` takes the grid spacings `dx`, `dy` (in mm, default `0.1`) and the thermal diffusivity `D` (in mm^2/s, default `4.`). It prints the time step `dt` and shows a figure with four plots. A graphical environment is needed to see the figure.

## Citing
```yaml
cff-version: 0.0.1
message: "If you use this software, please cite it as below."
authors:
  - family-names: "Soham"
    given-names: "Kakade"
title: "kakadesm_diffusion2d: Diffusion equation solver with finite-difference method."
version: 0.0.1
date-released: 2026-11-13
url: "https://github.com/Soham-S-Kakade/diffusion2d-excercise"
```