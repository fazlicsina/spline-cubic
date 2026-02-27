import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline


def f(x):
    return 1 / (x + 1)

a = int(input("Enter a (a>5): "))
n = int(input("Enter n: "))
z = int(input("Enter z (test points count): "))

x = np.linspace(-a, a, n)
y = f(x)

cs = CubicSpline(x, y)

x_new = np.linspace(-a, a, z)
y_new = f(x_new)
y_interp = cs(x_new)

error_vector = y_new - y_interp
infinity_norm_error = np.linalg.norm(error_vector, ord=np.inf)
print(f"Infinity norm of the error: {infinity_norm_error:.10f}")

plt.scatter(x_new, y_new, color='red', label='Data points')
plt.plot(x_new, y_interp, color='blue', label='Interpolation points')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.grid()
plt.show()
