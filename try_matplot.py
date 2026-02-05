import matplotlib.pyplot as mpl
import numpy as np
r = np.arange(0,2,0.01)
theta = 2 * np.pi * r
ax = mpl.subplot(111, projection='polar')
ax.plot(theta, r)
ax.set_rmax(2)
ax.set_rticks([0.5,1,1.5,2])
ax.set_rlabel_position(-22.5)
ax.grid(True)
ax.set_title('A line plot on a polar axis', va='bottom')
mpl.show()
