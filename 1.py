import numpy as np
# Practical 1
# a. Create a two-dimensional array (ARR1) with random values and compute mean, standard deviation, and variance along the second axis.
ARR1 = np.random.rand(3, 4)
mean_arr1 = np.mean(ARR1, axis=1)
std_dev_arr1 = np.std(ARR1, axis=1)
variance_arr1 = np.var(ARR1, axis=1)

print("ARR1:\n", ARR1)
print("Mean along second axis:", mean_arr1)
print("Standard Deviation along second axis:", std_dev_arr1)
print("Variance along second axis:", variance_arr1)
print("\n")

# b. Create a 2-dimensional array with user inputs for size and reshape it.
m = int(input("Enter the number of rows (m): "))
n = int(input("Enter the number of columns (n): "))
array_b = np.random.randint(0, 10, size=(m, n))

print("Array_b:\n", array_b)
print("Shape:", array_b.shape)
print("Type:", type(array_b))
print("Data Type:", array_b.dtype)

array_b_reshaped = array_b.reshape((n, m))
print("\nReshaped Array_b:\n", array_b_reshaped)
print("\n")

# c. Test whether elements of a given 1D array are zero, non-zero, and NaN. Record the indices.
array_c = np.array([1, 0, 3, 0, np.nan])
zero_indices = np.where(array_c == 0)[0]
nonzero_indices = np.where(array_c != 0)[0]
nan_indices = np.where(np.isnan(array_c))[0]

print("Array_c:", array_c)
print("Zero Indices:", zero_indices)
print("Non-zero Indices:", nonzero_indices)
print("NaN Indices:", nan_indices)
print("\n")

# d. Create three random arrays and perform operations as described.
Array1 = np.random.rand(5)
Array2 = np.random.rand(5)
Array3 = np.random.rand(5)

Array4 = Array3 - Array2
Array5 = 2 * Array1

covariance_array1_array4 = np.cov(Array1, Array4)[0, 1]
correlation_array1_array5 = np.corrcoef(Array1, Array5)[0, 1]

print("Array1:", Array1)
print("Array2:", Array2)
print("Array3:", Array3)
print("Array4 (Array3 - Array2):", Array4)
print("Array5 (2 * Array1):", Array5)
print("Covariance (Array1, Array4):", covariance_array1_array4)
print("Correlation (Array1, Array5):", correlation_array1_array5)
print("\n")

# e. Create two random arrays and find sum and product of specified halves.
Array1_e = np.random.rand(10)
Array2_e = np.random.rand(10)

sum_first_half = np.sum(Array1_e[:5]) + np.sum(Array2_e[:5])
product_second_half = np.prod(Array1_e[5:]) * np.prod(Array2_e[5:])

print("Array1_e:", Array1_e)
print("Array2_e:", Array2_e)
print("Sum of the first half:", sum_first_half)
print("Product of the second half:", product_second_half)
print("\n")

# f. Create an array with random values and determine memory occupied.
array_f = np.random.rand(4, 5)
memory_size = array_f.nbytes

print("Array_f:", array_f)
print("Memory Size (in bytes):", memory_size)
print("\n")

# g. Create a 2-dimensional array and perform specified operations.
m_g = 3
n_g = 4
array_g = np.random.randint(10, 100, size=(m_g, n_g))

row1, row2 = 1, 2  # indices of rows to swap
col_to_reverse = 2  # index of column to reverse

array_g_swapped_rows = np.copy(array_g)
array_g_swapped_rows[[row1, row2], :] = array_g_swapped_rows[[row2, row1], :]

array_g_reversed_col = np.copy(array_g)
array_g_reversed_col[:, col_to_reverse] = array_g_reversed_col[::-1, col_to_reverse]

print("Original Array_g:\n", array_g)
print("Swapped Rows (Row {} with Row {}):\n".format(row1, row2), array_g_swapped_rows)
print("Reversed Column {}:\n".format(col_to_reverse), array_g_reversed_col)
