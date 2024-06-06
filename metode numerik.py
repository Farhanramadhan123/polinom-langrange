import numpy as np
import matplotlib.pyplot as plt

# Fungsi Lagrange Interpolation
def lagrange_interpolation(x, y, x_interp):
    def L(k, x_val):
        product = 1
        for j in range(len(x)):
            if j != k:

                
                product *= (x_val - x[j]) / (x[k] - x[j])
        return product
    
    y_interp = 0
    for i in range(len(x)):
        y_interp += y[i] * L(i, x_interp)
    return y_interp

# Data inputnya
x_data = np.array([5, 10, 15, 20, 25, 30, 35, 40])
y_data = np.array([40, 30, 25, 40, 18, 20, 22, 15])

# Plotting
x_vals = np.linspace(5, 40, 100)
y_vals = [lagrange_interpolation(x_data, y_data, x) for x in x_vals]

plt.plot(x_data, y_data, 'o', label='Data points')
plt.plot(x_vals, y_vals, '-', label='Lagrange interpolation')
plt.xlabel('Tegangan (kg/mm^2)')
plt.ylabel('Waktu patah (jam)')
plt.legend()
plt.title('Lagrange Interpolation')
plt.show()
