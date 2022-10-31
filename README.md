# Diffusion2D-Python-Package

## Project description
This package solves the diffusion equation on a 2D plate, which is at an 
initial temperature and has a disk with a fixed different temperature. The 
mesh intervals and the thermal diffusivity of the metal can be given by 
the user, and the diffusion equation is solved by the finite difference
method. The outputs are four plots of the plate's temperature as time 
passes, showing the evolving temperature field on the plate.

## Installing the package
`pip install lacerdar_diffusion2d`

### Using pip3 to install from PyPI
`pip install -i https://test.pypi.org/simple/ lacerdar_diffusion2d==0.0.1`

### Required dependencies
`numpy`
`matplotlib`

## Running this package
In an interactive python prompt, import `lacerdar_diffusion2d` and 
call `lacerdar_diffusion2d.solve()`. You may pass values for dx, dy and D.

## Citing
The theoretical background for this package is found in:
[Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book2/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/)
