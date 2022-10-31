# Diffusion2D-Python-Package

## Instructions for users

Please follow the instructions in this file for installation. Do a step wise command implementation for getting access to this package.

The package is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).

## Project description
This code solves the diffusion equation in 2D over a square domain which is at 
a certain temperature and a circular disc at the center which is at a higher 
temperature. This code solves the diffusion equation using the 
Finite Difference Method. The thermal diffusivity and initial conditions of the
system can be changed by the user. The code produces four plots at various 
timepoints of the simulation. The diffusion process can be clearly observed in 
these plots.

## Installing the package
Go to the following url where the package details are available : https://test.pypi.org/project/sumanth0703-diffusion2d/0.1.1/
Now copy this line into the terminal window of choice which allows to install pacakges

pip install -i https://test.pypi.org/simple/ sumanth0703-diffusion2d==0.1.4

After running this in the terminal the "successful installation" message will be given and the pacakge is ready for accesing and using.

### Using pip to install from PyPI
pip install -i https://test.pypi.org/simple/ sumanth0703-diffusion2d==0.1.4

After running this in the terminal the "successful installation" message will be given and the pacakge is ready for accesing and using.

### Required dependencies
A user further needs numpy, matplotlib and a python version>=3.8 for working with this package.

## Running this package
Now  run the code by importing the solve() functionality in a Python script or an interactive Python shell.

from sumanth0703_diffusion2d import diffusion2d

diffusion2d.solve(dx,dy,D)

Give choice of values for dx, dy and D

## Citing

Further versions will be released based on the users input, so any suggestion is very welcome.