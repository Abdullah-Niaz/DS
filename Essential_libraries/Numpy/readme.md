# NumPy Fundamentals

Covers the fundamental concepts of NumPy, a powerful library for numerical computing in Python. It includes basic to advanced operations on NumPy arrays, such as creation, indexing, slicing, data types, reshaping, and more. The goal is to provide a hands-on learning experience to understand how NumPy can be used for data manipulation, analysis, and computational tasks.

## Table of Contents

- [Creating Arrays](#creating-arrays)
- [Indexing & Slicing](#indexing-slicing)
- [Data Types](#data-types)
- [Copy vs View](#copy-vs-view)
- [Array Shape](#array-shape)
- [Iterating Over Arrays](#iterating-over-arrays)
- [Join & Split](#join-split)
- [Search & Sort](#search-sort)
- [Filtering Arrays](#filtering-arrays)

## Creating Arrays

NumPy offers several ways to create arrays, which are the core data structure for numerical computations.

- `np.array()` – Create an array from a Python list or tuple.
- `np.zeros()` – Create an array filled with zeros.
- `np.ones()` – Create an array filled with ones.
- `np.arange()` – Create an array with evenly spaced values in a given interval.
- `np.linspace()` – Create an array with a specified number of evenly spaced values between a range.

## Indexing & Slicing

- **Basic Slicing**: Use `arr[start:end]` to access a subarray.
- **Advanced Indexing**: Use conditions like `arr[arr > 5]` to index elements that satisfy a condition.
- **Boolean Indexing**: Use a boolean array to index elements.

## Data Types

- **Setting Data Types**: Use the `dtype` parameter to set the data type of an array.
- **Type Conversion**: Use `astype()` to convert an array's data type.

## Copy vs View

- **View**: Views are references to the original data. Any modifications made to a view will affect the original array.
- **Copy**: A copy creates a new array, independent of the original data. Changes made to a copy do not affect the original.

## Array Shape

- **Getting Shape**: Use `arr.shape` to get the shape of an array.
- **Reshaping**: Use `reshape()` to modify the shape of an array without changing its data.

## Iterating Over Arrays

- Use `np.nditer()` to iterate over arrays efficiently, especially for multidimensional arrays.

## Join & Split

- **Concatenating Arrays**: Use `np.concatenate()`, `np.vstack()`, or `np.hstack()` to join multiple arrays together.
- **Splitting Arrays**: Use `np.split()` to divide an array into multiple subarrays.

## Search & Sort

- **Searching**: Use `np.where()` to find indices that satisfy a condition. Use `np.argmax()` and `np.argmin()` to find the index of the maximum and minimum values in an array.
- **Sorting**: Use `np.sort()` to sort an array. Use `np.argsort()` to get the indices that would sort an array.

## Filtering Arrays

- **Filtering**: Use conditions like `arr[arr > 5]` to filter elements from an array.
- **Complex Filtering**: Use `np.extract()` to apply complex conditions and extract values from an array.

## Usage

This repository provides various examples demonstrating how to use the above NumPy functions and operations. You can clone this repository and run the code examples in your Python environment.
