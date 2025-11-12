# diffusion2d

## Instructions for students

Please follow the instructions in [pypi_exercise.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/03_building_and_packaging/pypi_exercise.md).

The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).

---

## Description

This package provides a solver for the **two-dimensional diffusion equation**.  
It simulates heat diffusion on a square plate and visualizes the results using `matplotlib`.

The package is modular:

- `diffusion2d.py` contains the solver function `solve()`.
- `output.py` contains plotting functions (`create_plot` and `output_plots`).

Key features:

- Forward-time, central-space finite difference solver
- Configurable grid spacing (`dx`, `dy`) and thermal diffusivity (`D`)
- Produces 2×2 subplot figure showing temperature evolution at selected timesteps

---

## Installing the package

You can install the package directly from GitLab:

```bash
pip install git+https://github.com/BobSolyman/diffusion2d.git
```
