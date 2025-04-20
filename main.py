
#%%

# This is a comment I wrote as a change
import numpy as np
import matplotlib.pyplot as plt




x = 1
lix = [x]
k = 1.1
for n in range(20):
    fx = x**2 - 4
    dfx = 2*x
    x = x - k*fx/dfx
    lix.append(x)


plt.plot(lix)

# a line with a comment