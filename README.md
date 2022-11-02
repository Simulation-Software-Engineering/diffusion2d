# Diffusion2D-Python-Package

## Instructions for students

Please follow the instructions in [pypi_exercise.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/03_building_and_packaging/pypi_exercise.md).

The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).

## Project description
This code solves the diffusion equation in 2D over a square domain 
which is at a certain temperature and a circular disc at the center 
which is at a higher temperature. This code solves the diffusion equation 
using the Finite Difference Method. The thermal diffusivity and 
initial conditions of the system can be changed by the user. 
The code produces four plots at various timepoints of the simulation. 
The diffusion process can be clearly observed in these plots.
## Installing the package
The package is available on TestPyPI.
### Using pip3 to install from PyPI
Run the following command in a shell (e.g. bash):
```bash
pip3 install --user --index-url https://test.pypi.org/simple/ weinhovt-diffusion2D
```
Use at least version 0.0.7 the other version can not be imported due to a naming conflict.
### Required dependencies
This package requires matplotlib and numpy to function.
The package matplotlib has to be installed manually via pip from PyPI since it is not maintained on Test PyPI.
````bash
pip install matplotlib
````
## Running this package
For running the package import it in a python script or python console
and run the solve function as shown:
```python
from weinhovt_diffusion2D import diffusion2d

diffusion2d.solve()
```
Even though the package is named **weinhovt-diffusion2D** it hast to be imported 
under the name **weinhovt_diffusion2D** since the "-" conflicts with the python syntax when trying to
import the package.
## Citing
The code used for the diffusion solver and plotting the simulation steps was acquired from:
[https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/)
