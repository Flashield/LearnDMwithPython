print("Hello, World!")
import numpy as np
dataset_filename = "affinity_dataset.txt" 
X = np.loadtxt(dataset_filename)
print(X[:5])
apple_purchase=0
for i in X:
    if i[3] == 1:
        apple_purchase=apple_purchase+1
print("%s people bought apples",apple_purchase)