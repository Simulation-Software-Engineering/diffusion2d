# diffusion2d

## Description

This package simulates two-dimensional diffusion by solving the diffusion equation using the finite-difference method.
The resolution in x- and y-direction as well as the diffusion coefficient can be specified.
Results are plotted after four different time steps.

## Installing the package

This package can be installed using `pip`:

```bash
# Optionally, create a virtual environment and activate it
python3 -m venv venv
. venv/bin/activate

# Install the package
pip install --index-url https://test.pypi.org/simple/ vonrosmo_diffusion2d
```

## Running this package

Here is an example script that shows how to use the package:

```python
import diffusion2d

# Perform the simulation using default parameters
diffusion2d.solve()

# Perform the simulation using custom parameters
diffusion2d.solve(dx=0.02, dy=0.02, D=8)
```

## Citing

If you use this package in your work, please cite the [diffusion2d repository](https://github.com/CodingMarco/diffusion2d) and include the package version or commit used:

> diffusion2d contributors. *diffusion2d: Two-dimensional diffusion using the finite-difference method* [Computer software]. https://github.com/CodingMarco/diffusion2d

Please also acknowledge the original example, ["The two-dimensional diffusion equation"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/), from Chapter 7 of *Learning Scientific Programming with Python*.
