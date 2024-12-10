###### Paradict API Reference
[Home](/docs/api/README.md) | [Project](/README.md) | [Module](/docs/api/modules/paradict/xtypes/__init__/README.md) | [Source](/src/paradict/xtypes/__init__.py)

# Class Grid
> Module: [paradict.xtypes.\_\_init\_\_](/docs/api/modules/paradict/xtypes/__init__/README.md)
>
> Class: **Grid**
>
> Inheritance: `collections.UserList`

Box to hold a grid. A grid is made of numbers and should
be consistent (rows should be of same size)

Example:
```
# a grid with 2 rows and 3 columns
my_grid = Grid([(0, 1, 0),
                (1, 0, 1)])
```

## Fields table
Here are fields exposed in the class:

| Field | Value |
| --- | --- |
| \_abc\_impl | `<_abc._abc_data object at 0x794d9e1e8880>` |

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

# Methods within class
Here are methods exposed in the class:
- [\_\_init\_\_](#__init__)
- [append](#append)
- [clear](#clear)
- [copy](#copy)
- [count](#count)
- [extend](#extend)
- [index](#index)
- [insert](#insert)
- [pop](#pop)
- [remove](#remove)
- [reverse](#reverse)
- [sort](#sort)
- [\_UserList\_\_cast](#_userlist__cast)

## \_\_init\_\_
Initialize self.  See help(type(self)) for accurate signature.

```python
def __init__(self, initlist=None):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## append
S.append(value) -- append value to the end of the sequence

```python
def append(self, item):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## clear
S.clear() -> None -- remove all items from S

```python
def clear(self):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## copy
No docstring

```python
def copy(self):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## count
S.count(value) -> integer -- return number of occurrences of value

```python
def count(self, item):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## extend
S.extend(iterable) -- extend sequence by appending elements from the iterable

```python
def extend(self, other):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## index
S.index(value, [start, [stop]]) -> integer -- return first index of value.
Raises ValueError if the value is not present.

Supporting start and stop arguments is optional, but
recommended.

```python
def index(self, item, *args):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## insert
S.insert(index, value) -- insert value before index

```python
def insert(self, i, item):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## pop
S.pop([index]) -> item -- remove and return item at index (default last).
Raise IndexError if list is empty or index is out of range.

```python
def pop(self, i=-1):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## remove
S.remove(value) -- remove first occurrence of value.
Raise ValueError if the value is not present.

```python
def remove(self, item):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## reverse
S.reverse() -- reverse *IN PLACE*

```python
def reverse(self):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## sort
No docstring

```python
def sort(self, /, *args, **kwds):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_UserList\_\_cast
No docstring

```python
def _UserList__cast(self, other):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>
