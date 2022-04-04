# my_script.py
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

mu_in = 5
std_in = 5.0
size = 100

def norm_dist(mu, std, size=100):
	"""Generate normal distribution."""
	return norm.rvs(mu, std, size=size)

data = norm_dist(mu_in, std_in, size=size)

# Fit the normal distribution
mu, std = norm.fit(data)

# Make some plots
x = np.linspace(-40, 40, 100)
y = norm.pdf(x, mu, std)

title = f"Fit results: {mu=:.2f},  {std=:.2f}"

fig, ax = plt.subplots()
ax.hist(data, bins=50, density=True)
ax.plot(x, y, 'k', linewidth=2)
ax.set_title(title)

plt.show()