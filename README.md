# haasro_diffusion2d

## Description
This package solves the diffusion equation over a two dimensional square domain which is at a certain temperature, and a circular disc at its center which is at a higher temperature. The diffusion equation is solved using the finite-difference method. The thermal diffusivity and initial conditions of the system can be changed by the user. The code produces four plots at various timepoints of the simulation. The diffusion process can be clearly observed in these plots.

## Installing the package
Simply run this command in your venv:

```
pip install --extra-index-url https://test.pypi.org/simple/ haasro_diffusion2d
```

## Running this package
Inside a Juypter Notebook:

```
import haasro_diffusion2d as df
df.solve()
```

You can also provide parameters:

```
df.solve(dx=0.1, dy=0.1, D=4.0)
```

## Citing
The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).
