import numpy as np

np_height = np.array([74, 74, 72, 75, 75, 73], dtype=int64)
np_baseball = np.array([[74, 180], [74, 215], [72, 210], [
                       75, 205], [75, 190], [73, 195]], dtype=int64)

for height in np.nditer(np_height):
    print(f"{height} inches")

for baseball in np.nditer(np_baseball):
    print(baseball)