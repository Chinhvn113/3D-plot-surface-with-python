import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

ax=plt.axes(projection='3d')

x_data = np.arange(0, 50, 0.1)
y_data = np.arange(50, 100, 0.1)

X,Y = np.meshgrid(x_data, y_data)
Z=np.sin(X)*np.sin(Y)
ax.plot_surface(X,Y,Z, cmap='plasma')
ax.view_init(elev=0, azim=0)
ax.set_xlabel('Truc X')
ax.set_ylabel('Truc Y')
ax.set_zlabel('Truc z')
plt.show()
