Solving the two-dimensional diffusion equation using a simple explicit
forward-time, central-space finite-difference scheme. The implementation and
visualization are based on the scipython example:
https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/

## Description

This small package provides:
- A finite-difference solver for the 2D diffusion equation (diffusion2d.solve).
- A plotting helper module that generates and arranges snapshot plots.
- A packaging layout that makes the solver importable as a Python package.

The solver initializes a square plate with a hot circular disc at the center
and simulates heat diffusion. It outputs temperature snapshots at configurable
timesteps and displays the results with Matplotlib.

## Features

- Explicit forward-in-time, central-in-space finite-difference solver.
- Snapshot plotting for a handful of timesteps.
- Small, dependency-light package (numpy, matplotlib).
- Packaged for installation via pip / TestPyPI.

## Installation

From TestPyPI (example — replace version/name if different):
```bash
python3 -m pip install --index-url https://test.pypi.org/simple/ \
  --extra-index-url https://pypi.org/simple \
  sandisro_diffusion2d==0.0.1
```

From local source (development):
```bash
cd /path/to/project/root
python3 -m pip install -e .
```

## Usage

Run as a script:
```bash
python3 -m sandisro_diffusion2d.diffusion2d
```

Import and run from Python:
```python
from sandisro_diffusion2d import solve
solve(dx=0.1, dy=0.1, D=4.0)
```

The solve() function accepts physical parameters dx, dy and D (all have defaults).

## File layout

- sandisro_diffusion2d/
  - __init__.py         (exports solve)
  - diffusion2d.py      (solver and solve() entry point)
  - output.py           (create_plot, output_plots)
- pyproject.toml        (packaging metadata)
- README.md
- .gitignore

Do NOT commit build artifacts (dist/, build/, *.egg-info/) or credentials (.pypirc).

## Development / Packaging

Build local artifacts:
```bash
python3 -m pip install --upgrade build
rm -rf dist/ build/ *.egg-info
python3 -m build
ls -l dist
```

Upload to TestPyPI (requires ~/.pypirc configured with a TestPyPI token):
```bash
python3 -m pip install --upgrade twine
python3 -m twine upload --repository testpypi dist/*
```

## TestPyPI package page

Open the TestPyPI project page to verify the upload:
https://test.pypi.org/project/sandisro_diffusion2d/


## Notes

- Ensure matplotlib is usable in your environment when running the plotting code
  (desktop session or X/Wayland available).
- Keep ~/.pypirc private and do not commit it to version control.
```# filepath: /Users/ricky/Desktop/Uni/WiSe_25-26/SSE/diffusion2d/README.md
# sandisro_diffusion2d

Solving the two-dimensional diffusion equation using a simple explicit
forward-time, central-space finite-difference scheme. The implementation and
visualization are based on the scipython example:
https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/

## Description

This small package provides:
- A finite-difference solver for the 2D diffusion equation (diffusion2d.solve).
- A plotting helper module that generates and arranges snapshot plots.
- A packaging layout that makes the solver importable as a Python package.

The solver initializes a square plate with a hot circular disc at the center
and simulates heat diffusion. It outputs temperature snapshots at configurable
timesteps and displays the results with Matplotlib.

## Features

- Explicit forward-in-time, central-in-space finite-difference solver.
- Snapshot plotting for a handful of timesteps.
- Small, dependency-light package (numpy, matplotlib).
- Packaged for installation via pip / TestPyPI.

## Installation

From TestPyPI (example — replace version/name if different):
```bash
python3 -m pip install --index-url https://test.pypi.org/simple/ \
  --extra-index-url https://pypi.org/simple \
  sandisro_diffusion2d==0.0.1
```

From local source (development):
```bash
cd /path/to/project/root
python3 -m pip install -e .
```

## Usage

Run as a script:
```bash
python3 -m sandisro_diffusion2d.diffusion2d
```

Import and run from Python:
```python
from sandisro_diffusion2d import solve
solve(dx=0.1, dy=0.1, D=4.0)
```

The solve() function accepts physical parameters dx, dy and D (all have defaults).

## File layout

- sandisro_diffusion2d/
  - __init__.py         (exports solve)
  - diffusion2d.py      (solver and solve() entry point)
  - output.py           (create_plot, output_plots)
- pyproject.toml        (packaging metadata)
- README.md
- .gitignore

Do NOT commit build artifacts (dist/, build/, *.egg-info/) or credentials (.pypirc).

## Development / Packaging

Build local artifacts:
```bash
python3 -m pip install --upgrade build
rm -rf dist/ build/ *.egg-info
python3 -m build
ls -l dist
```

Upload to TestPyPI (requires ~/.pypirc configured with a TestPyPI token):
```bash
python3 -m pip install --upgrade twine
python3 -m twine upload --repository testpypi dist/*
```

## TestPyPI package page

Open the TestPyPI project page to verify the upload:
https://test.pypi.org/project/sandisro_diffusion2d/
