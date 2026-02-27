# Spline Cubic

Cubic spline interpolation demo for the function `f(x) = 1 / (x + 1)` over `[-a, a]`. The project includes two scripts:

- `main.py`: uses SciPy's `CubicSpline`.
- `main_without_lib.py`: pure-Python implementation (no SciPy).

Both scripts compute the infinity norm of the interpolation error and plot the true function vs. the interpolated curve.

## Mathematical Background

A cubic spline interpolation builds a piecewise cubic function `S(x)` that matches the data at the interpolation nodes and is smooth across each interval. For nodes `x0 < x1 < ... < x_{n-1}`, the spline is defined on each interval `[x_i, x_{i+1}]` by a cubic

```
S_i(x) = a_i + b_i (x - x_i) + c_i (x - x_i)^2 + d_i (x - x_i)^3
```

The coefficients are chosen so that:

- `S(x_i) = f(x_i)` for all nodes (interpolation)
- `S` is continuous at all nodes
- `S'` is continuous at all nodes
- `S''` is continuous at all nodes

These constraints produce a tridiagonal linear system for the second-derivative coefficients `c_i`, which is solved in `main_without_lib.py`. This implementation uses **natural boundary conditions** (`S''(x0) = 0` and `S''(x_{n-1}) = 0`).

In `main.py`, SciPy's `CubicSpline` is used with its default **not-a-knot** boundary condition. This is a different boundary choice, so the two scripts may produce slightly different curves and error values near the endpoints.

### Error Metric

For a set of test points `{x_j}`, the infinity norm (max error) is computed as:

```
||f - S||_∞ = max_j |f(x_j) - S(x_j)|
```

This gives the worst-case deviation between the true function and the spline at the sampled test points.

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
- Displays a plot with red points (exact function values at test points) and a blue curve (spline interpolation).

## Notes

- The function `1 / (x + 1)` has a singularity at `x = -1`. Make sure your chosen interval and node counts avoid numerical issues near `x = -1`.
