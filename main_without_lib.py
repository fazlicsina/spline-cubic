import matplotlib.pyplot as plt


def f(x):
    return 1 / (x + 1)

def cubic_spline_interpolation(x, y, x_new):
    n = len(x)
    h = [x[i + 1] - x[i] for i in range(n - 1)]
    
    alpha = [0] * (n - 1)
    for i in range(1, n - 1):
        alpha[i] = (3 / h[i] * (y[i + 1] - y[i]) - 3 / h[i - 1] * (y[i] - y[i - 1]))

    l = [1] + [0] * (n - 1)
    mu = [0] * (n - 1)
    z = [0] * n

    for i in range(1, n - 1):
        l[i] = 2 * (x[i + 1] - x[i - 1]) - h[i - 1] * mu[i - 1]
        mu[i] = h[i] / l[i]
        z[i] = (alpha[i] - h[i - 1] * z[i - 1]) / l[i]

    l[n - 1] = 1
    z[n - 1] = 0

    c = [0] * n
    b = [0] * (n - 1)
    d = [0] * (n - 1)
    a = [y[i] for i in range(n - 1)]

    for j in range(n - 2, -1, -1):
        c[j] = z[j] - mu[j] * c[j + 1]
        b[j] = (y[j + 1] - y[j]) / h[j] - h[j] * (c[j + 1] + 2 * c[j]) / 3
        d[j] = (c[j + 1] - c[j]) / (3 * h[j])

    interpolated = []
    for xi in x_new:
        for i in range(n - 1):
            if x[i] <= xi <= x[i + 1]:
                dx = xi - x[i]
                yi = a[i] + b[i] * dx + c[i] * dx**2 + d[i] * dx**3
                interpolated.append(yi)
                break

    return interpolated

def infinity_norm_error(y, y_predicted):
    return max(abs(y_a - y_p) for y_a, y_p in zip(y, y_predicted))


a = int(input("Enter a (a>5): "))
n = int(input("Enter n: "))
z = int(input("Enter z (test points count): "))

x = [-a + i * (2 * a / (n - 1)) for i in range(n)]
y = [f(xi) for xi in x]
x_new = [-a + i * (2 * a / (z - 1)) for i in range(z)]
y_new = [f(xi) for xi in x_new]

y_interp = cubic_spline_interpolation(x, y, x_new)

error = infinity_norm_error(y_new, y_interp)
print(f"Infinity norm of the error: {error:.10f}")

plt.scatter(x_new, y_new, color='red', label='Data points')
plt.plot(x_new, y_interp, color='blue', label='Interpolation points')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.grid()
plt.show()
