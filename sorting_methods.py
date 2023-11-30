"""
Program Name: Assignment 2
Author: Christopher Shenton
Date: 10-27-2023

Description: Four sorting functions; shell sort, insertion sort, selection sort,
and bubble sort, as well as a method to generate random, decreasing, and increasing
arrays, and a function to test these sorting algorithms with varying array sizes.
"""

import random
import time


# Sorts a given array using the shell sort (modified insertion sort) method.
# Input: an unsorted list (arr) of n length.
# Output: None; the given list is sorted in-place.
def shell_sort(arr):
    n = len(arr)
    gap = n // 2  # Define initial gap

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]  # Store current element in a temporary variable
            j = i
            while j >= gap and arr[j - gap] > temp:  # Move elements that are 'gap' positions apart
                arr[j] = arr[j - gap]                # and greater than 'temp' one space ahead
                j -= gap
            arr[j] = temp  # Place 'temp' in the correct sorted position within the gap
        gap //= 2


# Sorts a given array using the insertion sort method.
# Input: an unsorted list (arr) of n length.
# Output: None; the given list is sorted in-place.
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Move array elements that are greater than the key one space ahead
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


# Sorts a given array using the selection sort method.
# Input: an unsorted list (arr) of n length.
# Output: None; the given list is sorted in-place.
def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        # Find the smallest element in the unsorted section of the list
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the minimum element with the first element in the unsorted section
        arr[i], arr[min_index] = arr[min_index], arr[i]


# Sorts a given array using the bubble sort method.
# Input: an unsorted list (arr) of n length.
# Output: None; the given list is sorted in-place.
def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        # 'Swap' variable; if false, the array is sorted
        swap = False

        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap the elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap = True

        # If no elements are swapped, then the array is sorted
        if not swap:
            break

# Generates a list of a given size (n) and order (random, increasing, or decreasing)
# Input: size (int); the size of the specified array, and order(str); the order of elements.
def generate_array(size, order):
    if order == 'random':
        return [random.randint(1, 1000) for _ in range(size)]
    elif order == 'increasing':
        return [i for i in range(1, size + 1)]
    elif order == 'decreasing':
        return [i for i in range(size, 0, -1)]

# Tests the four sorting algorithms with random, increasing, and decreasing arrays of sizes 100,1000,10000,100000, and 200000.
# Input: None
# Output: Time elapsed for each sorting algorithm.
def test_algorithms():
    array_sizes = [100,1000,10000,100000,200000]
    orders = ['random', 'increasing', 'decreasing']

    sorting_algorithms = [shell_sort, insertion_sort, selection_sort, bubble_sort]

    for size in array_sizes:  # Loop through each array size
        for order in orders:  # Loop through random, decreasing, and increasing arrays for each sort function
            arr = generate_array(size, order)
            for sort_func in sorting_algorithms:  # Loop through each sort function
                arr_copy = arr.copy()
                start_time = time.time()
                sort_func(arr_copy)
                end_time = time.time()
                execution_time = end_time - start_time  # Record total time elapsed for each sort function
                print(f"Sorting {order} array of size {size} using {sort_func.__name__}: {execution_time:.6f} seconds")
    print("Tests concluded")


if __name__ == "__main__":
    test_algorithms()
