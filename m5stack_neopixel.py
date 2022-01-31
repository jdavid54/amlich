import numpy as np

# matrix 83x3
neo = np.arange(83*3).reshape((83,3))

for i in range(0,83):
    neo[i] = (85-i,i-80,1)
    
print(neo)