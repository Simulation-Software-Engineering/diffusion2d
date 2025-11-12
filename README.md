# pydiffusion

## Description

This code solves the diffusion equation over a two dimensional square domain which is at a certain temperature, and a circular disc at its center which is at a higher temperature. The diffusion equation is solved using the finite-difference method. The thermal diffusivity and initial conditions of the system can be changed by the user. The code produces four plots at various timepoints of the simulation. The diffusion process can be clearly observed in these plots.

## Installing the package

For the installation, Python >= 3.12 and pip >= 3.12 are needed. Install pydiffusion via pip:

```sh
pip install pydiffusion
```

or locally by cloning the repository and running

```sh
pip install .
```

when inside the cloned repository

## Running this package

You can use the pydiffusion library by importing its modules and then calling its functions:

```py
from pydiffusion import diffusion2d

diffusion2d.solve()
```

## Citing
