# diffusion2d

## Description

This Python package simulates the two-dimensional heat diffusion equation.

It models how heat spreads over a square steel plate over time. The simulation starts with a hot circular region in the center of a colder plate. The temperature distribution is calculated using a finite difference method.

The simulation uses NumPy for numerical calculations and Matplotlib to visualize the temperature distribution at different time steps.

The simulation parameters, such as the spatial resolution (`dx`, `dy`) and the thermal diffusivity (`D`), can be adjusted.

## Installing the package

Make sure you have Python 3.10 or newer installed.

Install the package using pip:

```bash
pip install rofailan-diffusion2d
```

The required dependencies, NumPy and Matplotlib, are installed automatically.

## Running this package

You can run the simulation using Python:

```bash
python -m rofailan_diffusion2d.diffusion2d
```

The simulation calculates the temperature distribution and displays four plots showing how heat spreads over time.

## Citing

The code used in this package is based on Chapter 7 of *Learning Scientific Programming with Python*:

https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/

The package was developed as part of the Simulation Software Engineering course at the University of Stuttgart.