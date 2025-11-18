# diffusion2d

## Description

This code solves the diffusion equation over a two dimensional square domain which is at a certain temperature, and a circular disc at its center which is at a higher temperature. The diffusion equation is solved using the [finite-difference method](https://en.wikipedia.org/wiki/Finite_difference_method). The thermal diffusivity and initial conditions of the system can be changed by the user. The code produces four plots at various timepoints of the simulation. The diffusion process can be clearly observed in these plots.

## Installing the package

### Windows

Run

```bash
python -m venv venv

.\venv\Scripts\activate

pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ shayo_diffusion2d
```

### macOS / Linux

Run

```bash
python -m venv venv

source venv/Scripts/activate

pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ shayo_diffusion2d
```

## Running this package

```python
from shayo_diffusion2d import diffusion2d

diffusion2d.solve()
```

The `solve()` function accepts `dx`, `dy` and `D` as optional arguments. You can override default values easily by passing new parameters.

```python
from shayo_diffusion2d import diffusion2d

diffusion2d.solve(dx=0.1, dy=0.1, D=4)
```

## Citing

This code is an exercise for the [Simulation Software Engineering](https://github.com/Simulation-Software-Engineering) lecture at University of Stuttgart.
