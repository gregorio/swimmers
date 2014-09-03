# from scipy.stats import wald
# import matplotlib.pyplot as plt
# import numpy as np
# from invgauss import ivpdf


# fig, ax = plt.subplots(1, 1)

# x = np.linspace(wald.ppf(0.01), wald.ppf(0.99), 100)
# #ax.plot(x, wald.pdf(x), 'r-', lw=5, alpha=0.6, label='wald pdf')
# ax.plot(x, ivpdf(x, 1, 1), 'r-', lw=5, alpha=0.6, label='wald pdf')

# rv = wald()
# ax.plot(x, rv.pdf(x), 'k-', lw=2, label='frozen pdf')

# r = wald.rvs(size=1000)

# ax.hist(r, 40, normed=True, histtype='stepfilled', alpha=0.2)
# ax.legend(loc='best', frameon=False)
# plt.show()

import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)

t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2*np.pi*t)
line, = ax.plot(t, s, lw=2)

ax.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
            arrowprops=dict(facecolor='black', shrink=0.05),
            )

ax.set_ylim(-2,2)
plt.show()