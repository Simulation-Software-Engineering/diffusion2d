# Diffusion2D-Python-Package

## Project description

This code solves the diffusion equation in 2D over a square domain which is at a certain temperature and a circular disc at the center which is at a higher temperature. This code solves the diffusion equation using the Finite Difference Method. The thermal diffusivity and initial conditions of the system can be changed by the user. The code produces four plots at various timepoints of the simulation. The diffusion process can be clearly observed in these plots.

## Installing the package

### Using pip3 to install from PyPI

```
pip3 install --user --index-url https://test.pypi.org/simple/ bergdola_diffusion2D==0.0.4
```

### Required dependencies

```
numpy
``` 
```
matplotlib
```

## Running this package

```
from bergdola_diffusion2D import diffusion2d

diffusion2d.solve()
```

## Citing