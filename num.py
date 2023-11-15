# ================== Scalar Value ================== #

import numpy as np;

num : np.ndarray = np.array(1000);

print(f"Object: {num}");

print(f"Object Shape: {num.shape}");

print(f"Object Type: {num.dtype}");

print(f"Object Type With Global Function: {type(num)}");

print(f"Number Of Dimension: {num.ndim}");

print(f"Total Items In Array: {num.size}");

print(f"Object Item Size: {num.itemsize}");

# ================== Vector Type ================== #

num2 : np.ndarray = np.array([1,2,3,4]);

print(f"Object: {num2}");

print(f"Object Shape: {num2.shape}");

print(f"Object Type: {num2.dtype}");

print(f"Object Type With Global Function: {type(num2)}");

print(f"Number Of Dimension: {num2.ndim}");

print(f"Total Items In Array: {num2.size}");

print(f"Object Item Size: {num2.itemsize}");

# ================== Matrix ================== #

data = [[0, 1, 2, 3],
        [4, 5, 6, 7,],
        [8, 9, 10, 11]];

num3 : np.ndarray = np.array(data);

print(f"Object: {num3}");

print(f"Object Shape: {num3.shape}");

print(f"Object Type: {num3.dtype}");

print(f"Object Type With Global Function: {type(num3)}");

print(f"Number Of Dimension: {num3.ndim}");

print(f"Total Items In Array: {num3.size}");

print(f"Object Item Size: {num3.itemsize}");