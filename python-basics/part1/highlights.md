# highlights from readings and notes

> tasks from this section can be found in [this repo folder](https://github.com/karenbocardo/python-basic/tree/master/practice/1_python_part_1)

- _ in interactive mode
- raw strings `r"string""` 
- match statements https://docs.python.org/3/tutorial/controlflow.html#match-statements
- enums
- multiple line strings definition 
```python
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")
```
- keyword and positional arguments https://docs.python.org/3/tutorial/controlflow.html#keyword-arguments
- special parameters https://docs.python.org/3/tutorial/controlflow.html#special-parameters
- unpacking argument lists https://docs.python.org/3/tutorial/controlflow.html#unpacking-argument-lists
- lambda expressions https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions
- documentation strings https://docs.python.org/3/tutorial/controlflow.html#documentation-strings

## data structures

### lists
- `append()`
- `extend()`
- `insert()`
- `remove()`
- `pop()`
- `clear()`
- `index(...)`
- `count()`
- `sort()`
- `reverse()`
- `copy()`

### list comprehensions

- nested list comprehensions 

The following list comprehension will transpose rows and columns:
```
>>> matrix = [
...     [1, 2, 3, 4],
...     [5, 6, 7, 8],
...     [9, 10, 11, 12],
... ]
>>> [[row[i] for row in matrix] for i in range(4)]
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
```
equivalent to:
```
transposed = []
>>> for i in range(4):
...     transposed.append([row[i] for row in matrix])
...
>>> transposed
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
```
same as:
```python
transposed = []
>>> for i in range(4):
...     # the following 3 lines implement the nested listcomp
...     transposed_row = []
...     for row in matrix:
...         transposed_row.append(row[i])
...     transposed.append(transposed_row)
...
>>> transposed
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
```
- tuples are immutable
- dict() constructor builds dictionaries directly from sequences of key-value pairs `dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])`
and keyword arguments `dict(sape=4139, guido=4127, jack=4098)`

### looping
- `zip()` function https://docs.python.org/3/library/functions.html#zip to iterate through multiple lists at the same time
- `items()`
- `enumerate()`
- `reversed()`
- `sorted()`