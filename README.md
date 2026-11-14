# 2D Heat Diffusion Simulation

A Python package for simulating heat diffusion in a two-dimensional square plate using an explicit finite-difference method.

## Description

The simulation models a 10 mm × 10 mm plate initially at 300 K, with a hotter circular region (700 K) at its center. It updates the temperature distribution over time using the two-dimensional diffusion equation and generates a single figure containing four temperature heatmaps (steps 0, 10, 50, and 100).

The spatial grid resolution (`dx`, `dy`) and thermal diffusivity (`D`) can be configured. The timestep `dt` is calculated to satisfy the explicit solver's stability constraint.

## Installing the package

After publishing to TestPyPI, install with:

```powershell
python -m pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ kantarhl_diffusion2d==0.0.1
```

## Running this package

```python
from kantarhl_diffusion2d import diffusion2d

diffusion2d.solve()                  # defaults: dx=0.1, dy=0.1, D=4.0
diffusion2d.solve(dx=0.2, dy=0.2, D=4.0)
```

Running the code displays four temperature plots and a shared color bar. A graphical display is needed to view the figure.

## Dependencies

- Python 3.10 or later
- NumPy
- Matplotlib

## Citing and attribution

This project refactors the diffusion example provided in the Simulation Software Engineering exercise repository, itself based on the example from *Learning Scientific Programming with Python* (Chapter 7), available at https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/ .

Original exercise repository: https://github.com/Simulation-Software-Engineering/diffusion2d

The exercise repository includes a CC BY 4.0 `LICENSE` file, which is retained in the fork. This version reorganizes the original code into separate solver and visualization modules and adds packaging metadata.

## About

Created for the Simulation Software Engineering course's Python packaging exercise.

Source repository: https://github.com/hazalkntr/diffusion2d.git
