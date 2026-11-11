# diffusion2d

## Description

diffusion2d solves the diffusion equation over a two dimensional square domain which is at a certain temperature, and a circular disc at its center which is at a higher temperature. The diffusion equation is solved using the finite-difference method. The thermal diffusivity and initial conditions of the system can be changed by the user. The code produces four plots at various timepoints of the simulation. The diffusion process can be clearly observed in these plots.

## Installing the package

```bash
python3 -m pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ variyaah_diffusion2d
```

## Running this package

```python
from variyaah_diffusion2d import diffusion2d
diffusion2d.solve()

#optional args
# dx, dy intervals in x-, y- directions, mm
# D Thermal diffusivity of steel, mm^2/s
#diffusion2d.solve(dx, dy, D)
```

## Citing

The code used is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).
