import numpy as np
import matplotlib.pyplot as plt

# Fungsi Newton Interpolation
def newton_interpolation(x, y, x_interp):
    def divided_diff(x, y):
        n = len(y)
        coef = np.zeros([n, n])
        coef[:, 0] = y
        for j in range(1, n):
            for i in range(n - j):
                coef[i][j] = (coef[i + 1][j - 1] - coef[i][j - 1]) / (x[i + j] - x[i])
        return coef[0, :]

    coef = divided_diff(x, y)
    n = len(coef)
    y_interp = coef[0]
    for i in range(1, n):
        term = coef[i]
        for j in range(i):
            term *= (x_interp - x[j])
        y_interp += term
    return y_interp

# Data inputnya
x_data = np.array([5, 10, 15, 20, 25, 30, 35, 40])
y_data = np.array([40, 30, 25, 40, 18, 20, 22, 15])

# Plotting
x_vals = np.linspace(5, 40, 100)
y_vals_newton = [newton_interpolation(x_data, y_data, x) for x in x_vals]

plt.plot(x_data, y_data, 'o', label='Data points')
plt.plot(x_vals, y_vals_newton, '-', label='Newton interpolation')
plt.xlabel('Tegangan (kg/mm^2)')
plt.ylabel('Waktu patah (jam)')
plt.legend()
plt.title('Newton Interpolation')
plt.show()
