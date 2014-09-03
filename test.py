from scipy.stats import invgauss
import matplotlib.pyplot as plt
import numpy as np

#invgauss.pdf(x, mu) = 1 / sqrt(2*pi*x**3) * exp(-(x-mu)**2/(2*x*mu**2))

fig, ax = plt.subplots(1, 1)

mu = 1


x = np.linspace(invgauss.pdf(0.01, mu),invgauss.pdf(0.99, mu), 100)
ax.plot(x, invgauss.pdf(x, mu),'r-', lw=5, alpha=0.6, label='invgauss pdf')

rv = invgauss(mu)
ax.plot(x, rv.pdf(x), 'k-', lw=2, label='frozen pdf')


r = invgauss.rvs(mu, size=1000)

ax.hist(r, normed=True, histtype='stepfilled', alpha=0.2)
ax.legend(loc='best', frameon=False)
plt.show()	