# Diffusion 2D

## Overview

This code solves the 2D diffusion equation using the finite-difference method. It simulates heat diffusion over a square domain with a circular disc at its center maintained at a higher temperature.

## Features

- Solves the diffusion equation in two dimensions
- Uses finite-difference numerical method
- Customizable thermal diffusivity and initial conditions
- Generates four plots showing the diffusion process at different timepoints
- Visual representation of temperature distribution evolution

## Usage

Run the solver to simulate the diffusion process. The code will generate plots showing the temperature distribution at various stages of the simulation.

## Parameters

You can modify the following parameters in the solver file:

- `dx`: Spatial step size in x-direction
- `dy`: Spatial step size in y-direction
- `D`: Thermal diffusivity coefficient

**Note**: Changing these parameters will affect the timestep `dt` and computational time. Smaller spatial steps (`dx`, `dy`) typically require smaller timesteps and longer computation times.

## Initial Conditions

- Square domain at a certain base temperature
- Circular disc at the center at a higher temperature
- Temperature diffuses from the hot disc to the cooler surrounding domain

## Output

The code produces four plots visualizing the diffusion process at different timepoints, clearly showing how heat spreads from the central disc throughout the domain.

## Further Reading

For theoretical background on the numerical methods used, refer to **Chapter 7** of *"Learning Scientific Programming with Python"*.
