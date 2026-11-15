# diffusion2d

## Description

This package simulates how heat spreads across a square plate.

The simulation uses the finite-difference method and shows four plots at different points in time.

## Installing the package

```bash
# Create a virtual environment
python -m venv venv
venv\Scripts\activate

# Install the package
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ khaituia_diffusion2d
```

## Running this package

Import the package

```python
from khaituia_diffusion2d import diffusion2d

diffusion2d.solve()

# Choose your own parameters
diffusion2d.solve(dx=0.2, dy=0.2, D=8)
```

## Citing

This package is based on the original exercise repository: https://github.com/Simulation-Software-Engineering/diffusion2d
