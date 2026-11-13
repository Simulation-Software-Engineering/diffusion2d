# salinajl_diffusion2d

## Instructions for students

Please follow the instructions in [pypi_exercise.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/03_building_and_packaging/pypi_exercise.md).

The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).

## Description
This package solves the diffusion equation over a two dimensional square domain which is at a certain temperature, and a circular disc at its center which is at a higher temperature. The diffusion equation is solved using the finite-difference method. The thermal diffusivity and initial conditions of the system can be changed by the user. The code produces four plots at various timepoints of the simulation. The diffusion process can be clearly observed in these plots.

## Installing the package
To install the package, use:

```
pip install salinajl_diffusion2d
```

## Running this package
To use this package, import it in the following way:

```python
from salinajl_diffusion2d import diffusion2d
```

Then, use the `solve()` function with `dx`, `dy`, and `D` as parameters to solve the diffusion equation with those values, as in the following example:

```python
diffusion2d.solve(0.3, 0.2, 2)
```

## Citing
```yaml
cff-version: 0.0.1
message: "If you use this software, please cite it as below."
authors:
  - family-names: "Salinas"
    given-names: "Jonatan"
title: "salinajl_diffusion2d: Diffusion equation solver with finite-difference method."
version: 0.0.1
date-released: 2026-11-11
url: "https://github.com/JonaSalinas18/diffusion2d"
```
