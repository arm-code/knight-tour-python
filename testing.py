import numpy as np
chess = np.ones((8,8))
n = 8

def s(key):
    for i in range(0, n):
        for j  in range(0, n):
            if chess[i,j] == key:
                return i, j


print(s(1))
x, y = s(1)
print(x)
print(y)
