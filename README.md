# Diffusion2D Python Package
## Project Description
Diffusion2D code solves the diffusion equation in 2D over a square domain which is at a certain temperature and a circular disc at the center which is at a higher temperature. 

This package code solves the diffusion equation using the Finite Difference Method the simplest approach to applying the partial difference equation.

The code produces four plots at various time-points.
The diffusion process can be clearly observed in these plots.

Remark: The thermal diffusivity and physical parameters of the system can be changed by the user by passing arguments to solver function.

## Installing the package
### Using pip to install from TestPyPI
To install the package copy and run below code into terminal at your workspace.<br />
pip install -i https://test.pypi.org/simple/ diffusion2d-cevikma

### Required Dependencies
In order to package to fully works; numpy and matplotlib must be installed onto the system.<br />
To install these packages in case needed, run below codes in the workspace environment:<br />
pip install numpy<br />
pip install matplotlib

## Running this package
Once the package is downloaded. Write the following code into the source file wherever the diffusion equation needed:<br />
from diffusion2d_cevikma import diffusion2d<br />
diffusion2d.solve()
