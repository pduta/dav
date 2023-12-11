import pandas as pd

# a. Create a series with 5 elements. Display the series sorted on index and also sorted on values separately.
series_a = pd.Series([4, 2, 7, 1, 5], index=['d', 'b', 'e', 'a', 'c'])

sorted_by_index = series_a.sort_index()
sorted_by_values = series_a.sort_values()

print("Original Series_a:\n", series_a)
print("Sorted by Index:\n", sorted_by_index)
print("Sorted by Values:\n", sorted_by_values)
print("\n")

# b. Create a series with N elements with some duplicate values. Find the minimum and maximum ranks assigned to the values using ‘first’ and ‘max’ methods.
series_b = pd.Series([3, 5, 2, 1, 5, 4, 2, 3, 1])

min_rank_first = series_b.rank(method='first', ascending=True)
max_rank = series_b.rank(method='max', ascending=True)

print("Original Series_b:\n", series_b)
print("Minimum Rank (using 'first' method):\n", min_rank_first)
print("Maximum Rank (using 'max' method):\n", max_rank)
print("\n")

# c. Display the index value of the minimum and maximum element of a Series.
min_index = series_b.idxmin()
max_index = series_b.idxmax()

print("Original Series_b:\n", series_b)
print("Index of Minimum Element:", min_index)
print("Index of Maximum Element:", max_index)
