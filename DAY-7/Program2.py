#Create a Numpy array ; perform slicing , reshaping , and stats(mean/std/max)
import numpy as np

# Create a NumPy array
arr = np.array([10 , 20 , 40 , 80 , 160 , 320])

print("Original Array:")
print(arr)

# Slicing
print("\nSliced Array (index 1 to 4):")
print(arr[1:5])

# Reshaping
reshaped_arr = arr.reshape(2, 3)

print("\nReshaped Array (2x3):")
print(reshaped_arr)

# Statistical Operations
print("\nMean:", np.mean(arr))
print("Standard Deviation:", np.std(arr))
print("Maximum Value:", np.max(arr))