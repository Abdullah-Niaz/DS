# 🧠 Beginner’s Guide to Python for Data Science

---

## **1. Python Basics**

### 🔹 Introduction

Python is one of the most popular and beginner-friendly programming languages used in data science, machine learning, and AI. Its simple syntax and vast library ecosystem make it ideal for analyzing data, visualizing results, and building models.

---

### 🔸 **Variables**

A **variable** is a container that stores data values.
You can assign any type of value to a variable.

```python
x = 10
name = "Abdullah"
is_data_scientist = True
```

Python automatically detects the data type — this is called **dynamic typing**.

---

### 🔸 **Data Types**

Python provides several built-in data types commonly used in data science:

| Type    | Example                           | Description                   |
| ------- | --------------------------------- | ----------------------------- |
| `int`   | `10`                              | Integer values                |
| `float` | `3.14`                            | Decimal values                |
| `str`   | `"Hello"`                         | Text data                     |
| `bool`  | `True / False`                    | Logical values                |
| `list`  | `[1,2,3]`                         | Ordered, mutable collection   |
| `tuple` | `(1,2,3)`                         | Ordered, immutable collection |
| `dict`  | `{'name': 'Abdullah', 'age': 21}` | Key-value pairs               |
| `set`   | `{1,2,3}`                         | Unordered, unique elements    |

---

### 🔸 **Objects**

In Python, *everything is an object*, meaning each variable is an instance of a class.
Example:

```python
a = 10
print(type(a))  # <class 'int'>
```

This concept becomes powerful when you start using **NumPy arrays**, **Pandas DataFrames**, and **custom classes**.

---

### 🔸 **Conditions**

Conditional statements allow your program to make decisions.

```python
x = 5
if x > 0:
    print("Positive")
elif x == 0:
    print("Zero")
else:
    print("Negative")
```

---

### 🔸 **Loops**

Loops help execute code repeatedly.

**For loop:**

```python
for i in range(5):
    print(i)
```

**While loop:**

```python
i = 0
while i < 5:
    print(i)
    i += 1
```

---

### 🔸 **Functions**

Functions make code reusable and organized.

```python
def add(a, b):
    return a + b

result = add(10, 20)
print(result)
```

---

### 🔸 **String Functions**

Strings are sequences of characters and can be manipulated easily.

```python
text = "Python for Data Science"
print(text.upper())        # Uppercase
print(text.lower())        # Lowercase
print(text.split())        # Split into words
print(text.replace("Python", "Machine Learning"))
```

---

## **2. Lists, Tuples, Dictionaries, and Sets**

These are Python’s **collection data structures**.

### 🔹 List

```python
fruits = ["apple", "banana", "cherry"]
fruits.append("mango")
```

✅ Mutable — can be modified.

---

### 🔹 Tuple

```python
numbers = (1, 2, 3)
```

✅ Immutable — cannot be changed after creation.

---

### 🔹 Dictionary

```python
student = {"name": "Abdullah", "age": 21}
print(student["name"])
```

✅ Stores data in key-value pairs.

---

### 🔹 Set

```python
unique_nums = {1, 2, 2, 3, 4}
```

✅ Removes duplicates automatically.

---

## **3. Jupyter Notebook**

Jupyter Notebook is one of the **most used tools in data science**.
It allows you to combine **code, output, and documentation** in one place.

### 🔹 Key Features

* **Interactive coding environment** (run code cell-by-cell)
* **Markdown support** for documentation
* **Rich outputs** (charts, images, tables)

### 🔹 Getting Started

1. Install with: `pip install jupyterlab`
2. Launch: `jupyter notebook`
3. Create a new Python notebook

### 🔹 Markdown for Documentation

You can write:

```markdown
# Heading
**Bold**, *Italic*, `inline code`
- Bullet points
1. Numbered list
```

Using Markdown helps you keep your analysis clean and well-documented.

---

## **4. NumPy — Numerical Python**

NumPy provides powerful tools for **numerical computation** and **array processing**.

### 🔹 Why NumPy?

* Much faster than Python lists
* Efficient memory usage
* Supports vectorized operations (no loops needed)

### 🔹 Basics

```python
import numpy as np

arr = np.array([1, 2, 3, 4])
print(arr.mean())   # Average
print(arr.std())    # Standard deviation
```

### 🔹 Common Functions

| Function                       | Description           |
| ------------------------------ | --------------------- |
| `np.arange(start, stop, step)` | Create range arrays   |
| `np.zeros(shape)`              | Create array of zeros |
| `np.ones(shape)`               | Create array of ones  |
| `np.random.rand(n)`            | Random numbers        |
| `np.reshape()`                 | Reshape array         |
| `np.concatenate()`             | Combine arrays        |

### 🔹 Time & Space Efficiency

NumPy operations are implemented in C, making them **much faster** than Python lists for large datasets.

---

## **5. Pandas — Data Analysis Library**

Pandas is the **heart of data analysis** in Python.

### 🔹 Core Data Structures

1. **Series** → One-dimensional labeled array

   ```python
   import pandas as pd
   s = pd.Series([1, 3, 5, 7], name="Numbers")
   ```
2. **DataFrame** → Two-dimensional table

   ```python
   df = pd.DataFrame({
       "Name": ["Ali", "Sara"],
       "Age": [22, 23]
   })
   ```

---

### 🔹 Key Functions

| Function                    | Description        |
| --------------------------- | ------------------ |
| `df.head()`                 | First 5 rows       |
| `df.tail()`                 | Last 5 rows        |
| `df.info()`                 | Summary of data    |
| `df.describe()`             | Descriptive stats  |
| `df.corr()`                 | Correlation matrix |
| `df.min()` / `df.max()`     | Min/Max values     |
| `df.mode()` / `df.median()` | Mode/Median values |

---

### 🔹 Data Cleaning with Pandas

Cleaning is the **most crucial step** before analysis.

```python
df.dropna(inplace=True)     # Remove missing rows
df.fillna(0, inplace=True)  # Replace missing with 0
df.rename(columns={'old': 'new'}, inplace=True)
```

---

### 🔹 Merging DataFrames

Combine multiple datasets to create meaningful insights.

```python
merged_df = pd.merge(df1, df2, on='id')
```

---

### 🔹 String Operations in Pandas

Pandas makes it easy to apply string functions to entire columns.

```python
df['Name'].str.split(' ')
df['Email'].str.contains('@gmail.com')
df['Address'].str.extract('(\d{5})')  # Extract ZIP code pattern
```

These are essential for **data cleaning and text preprocessing**.

---

## **6. Descriptive Statistics Functions**

These functions help summarize data:

| Function             | Description                          |
| -------------------- | ------------------------------------ |
| `describe()`         | Gives statistical summary            |
| `corr()`             | Measures correlation between columns |
| `min()`, `max()`     | Find smallest/largest value          |
| `mode()`, `median()` | Central tendency measures            |

Example:

```python
df.describe()
df['Age'].corr(df['Salary'])
```

---

## **7. Putting It All Together — A Practical Flow**

1. Load your dataset using `pandas.read_csv()`
2. Explore and describe data (`df.info()`, `df.describe()`)
3. Clean missing values (`dropna`, `fillna`)
4. Transform data (string operations, mapping)
5. Analyze data (correlation, summary)
6. Visualize (later using Matplotlib/Seaborn)

---

## ✅ Summary

| Topic                     | Purpose                              |
| ------------------------- | ------------------------------------ |
| Python Basics             | Logic, control flow, functions       |
| Jupyter Notebook          | Code + documentation + visualization |
| NumPy                     | Fast numerical computations          |
| Pandas                    | Data handling, cleaning, analysis    |
| Descriptive Stats         | Understanding data insights          |
| String & Merge Operations | Data cleaning and text processing    |

---

## 🚀 Final Note for Beginners

* Always **practice each topic** with mini examples.
* Keep your experiments in **Jupyter notebooks** with Markdown notes.
* Once you’re comfortable, move to **Matplotlib**, **Seaborn**, and **real datasets** (like Kaggle).
