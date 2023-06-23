import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

a = 0  # lower limit of integration
b = 5  # upper limit of integration

def func(x):
    return (1/(1+x**2))

area_quad, _ = quad(func, a, b)

N = 10000000
X = a + (b-a)*np.random.rand(N)
size = np.arange(10000, N+1, 10000)
mc_est = np.zeros(size.shape)
for i, k in enumerate(size):
    Z = X[:k]
    Y = func(Z)
    mc_est[i] = (b-a)*np.mean(Y)

plt.plot(size, mc_est)
plt.axhline(y=area_quad, color='r', linestyle='--')
plt.xlabel('Sample Size')
plt.ylabel('Estimate of Area')
plt.title('Monte Carlo Estimates as a Function of Sample Size')
plt.show()