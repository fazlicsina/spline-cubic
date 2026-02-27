# Spline Cubic

Cubic spline interpolation demo for the function `f(x) = 1 / (x + 1)` over `[-a, a]`. The project includes two scripts:

- `main.py`: uses SciPy's `CubicSpline`.
- `main_without_lib.py`: pure-Python implementation (no SciPy).

Both scripts compute the infinity norm of the interpolation error and plot the true function vs. the interpolated curve.

## Requirements

- Python 3.8+
- `matplotlib`
- `numpy` (for `main.py` only)
- `scipy` (for `main.py` only)

Install dependencies:

```bash
pip install matplotlib numpy scipy
```

## Usage

### SciPy version

```bash
python main.py
```

### Pure-Python version

```bash
python main_without_lib.py
```

## Inputs

Each script prompts for:

- `a` (must be > 5): interval half-width, the domain is `[-a, a]`
- `n`: number of interpolation nodes
- `z`: number of test points

## Output

- Prints the infinity norm of the error.
- Displays a plot with:
  - red points: exact function values at test points
  - blue curve: spline interpolation

## Notes

- The function `1 / (x + 1)` has a singularity at `x = -1`. Make sure your chosen interval and node counts avoid numerical issues near `x = -1`.
