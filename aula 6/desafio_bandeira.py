import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
bandeira = [
  [0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0],
  [2, 2, 2, 2, 2, 2, 2],
  [2, 2, 2, 2, 2, 2, 2],
  [1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1],
  [0, 0, 0, 0, 0, 0, 0]
]
cmap = ListedColormap(["white","red", "blue"])
plt.figure(figsize=(5, 5))
plt.imshow(bandeira, cmap=cmap)
plt.axis('off')
plt.show()

