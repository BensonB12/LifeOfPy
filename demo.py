
# %% 

import numpy as np
a = np.random.random((4,5))
print(a)
print(np.arange(50).reshape((5,10)))

# %%
range(10)

# %%
list(range(10))

# %%
np.array(range(10))

# %%
np.arange(12).reshape(3,4)

# %%
n = 3
m = 4
a = np.arange(n * m).reshape((n, m))

print(a * 8)

# %%
print(a * a)

# %%
# Left pad, small shape with ones
np.arange(3)+5
# %%
np.ones((3,3))+np.arange(3)

# %%
np.arange(3).reshape((3, 1))+np.arange(3)

# %%
print(np.arange(3))
# %%
print(np.arange(3).shape)
# %%
print(a)
print(a[1,2])
print(a[1][2])
print(a.reshape(2,6))
print(a.reshape(12,1))
print(a.reshape(12,))
print(a.reshape(12))
# %%
b = np.arange(12).reshape((3,4)) < 6

# %%
c = b < 6
# %%
b[c]