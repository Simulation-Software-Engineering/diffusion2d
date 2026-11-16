# diffusion2d

## Instructions for students

Please follow the instructions in [pypi_exercise.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/03_building_and_packaging/pypi_exercise.md).

The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).

## Description

diffusion2d solves the diffusion equation over a two-dimensional square domain. The domain starts at a uniform temperature, with a circular disc at its center at a higher temperature. The diffusion equation is solved with the finite-difference method: forward differences in time and central differences in space. The time step is chosen automatically so that the explicit scheme stays stable.

The thermal diffusivity and the spatial resolution can be changed by the user. The code produces four plots at different time points of the simulation and combines them into one figure, so the diffusion of heat from the hot disc into the cold surroundings can be observed directly.

Default setup:

| Quantity | Value |
|---|---|
| Plate size | 10 mm × 10 mm |
| Grid spacing `dx`, `dy` | 0.1 mm |
| Thermal diffusivity `D` | 4 mm²/s (steel) |
| Initial temperature of the plate | 300 K |
| Initial temperature of the central disc | 700 K |
| Number of time steps | 101 (plots at steps 0, 10, 50, 100) |

The package consists of two modules:

- `diffusion2d.py`: the solver, with the function `solve()` as entry point
- `output.py`: the plotting functions `create_plot()` and `output_plots()`

Changing `dx`, `dy` and `D` also changes the time step `dt`. A finer grid (smaller `dx`, `dy`) leads to a much smaller `dt`, so the computation takes noticeably longer and the time labels in the plots change accordingly.

For the theoretical background, see Chapter 7 of the book "Learning Scientific Programming with Python" (linked above).

## Installing the package

Requirements:

- Python >= 3.6
- [NumPy](https://numpy.org/install/)
- [Matplotlib](https://matplotlib.org/stable/users/installing/index.html)

NumPy and Matplotlib are installed automatically when you install the package with pip.

```bash
pip install diffusion2d
```

## Running this package

Run the solver with the default parameters from Python:

```python
import diffusion_equation2d.diffusion2d as dif

dif.solve()
```

This prints the time step `dt` and shows one figure with four plots of the temperature field at different times.

The parameters `dx`, `dy` and `D` can be passed to `solve()`:

```python
diffusion2d.solve(dx=0.2, dy=0.2, D=2.)
```

## Citing
