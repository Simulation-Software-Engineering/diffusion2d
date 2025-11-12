# diffusion2d

## Instructions for students

Please follow the instructions in [pypi_exercise.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/03_building_and_packaging/pypi_exercise.md).
The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).

---

## Description

This package provides a minimal 2D diffusion (heat) solver for a square plate. It numerically integrates the diffusion equation with a simple FTCS finite‑difference scheme and exposes a `solve()` function that produces one figure with four time‑snapshot subplots. The goal is to turn the classroom script into an importable, redistributable Python package that can be installed, imported, and reused in other projects.

---

## Installing the package

### (1) From TestPyPI
```bash
pip install --index-url https://test.pypi.org/simple/ \
            --extra-index-url https://pypi.org/simple \
            gufg_diffusion2d
```

### (2) From source (editable)
From the repository root:
```bash
python -m pip install -e .
```

---

## Running this package

If you exposed `solve` in `__init__.py`:
```python
from diffusion2d import solve
solve()  
```

Or via the submodule:
```python
from diffusion2d import diffusion2d
diffusion2d.solve()
```

---

## Citing
- SciPython example: [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).

