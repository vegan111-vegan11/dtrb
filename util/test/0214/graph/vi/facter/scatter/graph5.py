import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = [entry[1] for entry in data]
y = [entry[2] for entry in data]
z = [entry[6] for entry in data]

ax.scatter(x, y, z)

ax.set_xlabel('Width')
ax.set_ylabel('Height')
ax.set_zlabel('Success Rate')

plt.show()
