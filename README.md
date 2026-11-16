
# aswathvn_diffusion2d

A Python package for solving the two-dimensional diffusion equation using a finite-difference method.

## Installation

```bash
pip install aswathvn_diffusion2d
```

## Usage

```python
from aswathvn_diffusion2d import diffusion2d

diffusion2d.solve()
```

You can also provide custom values for the spatial steps and thermal diffusivity:

```python
diffusion2d.solve(dx=0.1, dy=0.1, D=4.0)
```

## Dependencies

- NumPy
- Matplotlib

