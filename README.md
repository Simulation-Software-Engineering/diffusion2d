# dogukangundemir_diffusion2d

This package solves the two-dimensional heat diffusion equation over a square
domain using a finite-difference method. The square starts at a cold
temperature, with a hotter circular disc at its centre. The simulation
produces four plots showing how heat diffuses through the domain.

The implementation is based on [Chapter 7 of *Learning Scientific Programming
with Python*](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).

## Installation

Install the package from TestPyPI:

```bash
python -m pip install --index-url https://test.pypi.org/simple/ \
  --extra-index-url https://pypi.org/simple/ dogukangundemir_diffusion2d
```

## Running the simulation

```python
from dogukangundemir_diffusion2d import diffusion2d

diffusion2d.solve()
diffusion2d.solve(dx=0.2, dy=0.2, D=2.0)
```

The arguments are grid spacing in millimetres (`dx` and `dy`) and thermal
diffusivity in square millimetres per second (`D`). All have defaults.

## Development

Build distribution archives with:

```bash
python -m build
```

The generated files are placed in `dist/`. Do not commit build artifacts.

Run the test suite with:

```bash
python -m unittest discover -s tests -v
```

## Citing

This exercise code is based on the diffusion equation example by the authors
of *Learning Scientific Programming with Python*.
