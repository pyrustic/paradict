###### Paradict API Reference
[Home](/docs/api/README.md) | [Project](/README.md) | [Module](/docs/api/modules/paradict/xtypes/__init__/README.md) | [Source](/src/paradict/xtypes/__init__.py)

# Class Obj
> Module: [paradict.xtypes.\_\_init\_\_](/docs/api/modules/paradict/xtypes/__init__/README.md)
>
> Class: **Obj**
>
> Inheritance: `collections.UserDict`

Box to hold an Extension Object. Such objects behave like a dictionary.
An object builder is passed as argument to the right functions, thus,
the object is consumed/used to build a new valid data value

## Fields table
Here are fields exposed in the class:

| Field | Value |
| --- | --- |
| \_MutableMapping\_\_marker | `<object object at 0x794d9eecc1d0>` |
| \_abc\_impl | `<_abc._abc_data object at 0x794d9e1f0580>` |

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

# Methods within class
Here are methods exposed in the class:
- [\_\_init\_\_](#__init__)
- [clear](#clear)
- [copy](#copy)
- [fromkeys](#fromkeys)
- [get](#get)
- [items](#items)
- [keys](#keys)
- [pop](#pop)
- [popitem](#popitem)
- [setdefault](#setdefault)
- [update](#update)
- [values](#values)

## \_\_init\_\_
Initialize self.  See help(type(self)) for accurate signature.

```python
def __init__(self, dict=None, /, **kwargs):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## clear
D.clear() -> None.  Remove all items from D.

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

## fromkeys
No docstring

```python
@classmethod
def fromkeys(iterable, value=None):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## get
D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.

```python
def get(self, key, default=None):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## items
D.items() -> a set-like object providing a view on D's items

```python
def items(self):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## keys
D.keys() -> a set-like object providing a view on D's keys

```python
def keys(self):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## pop
D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
If key is not found, d is returned if given, otherwise KeyError is raised.

```python
def pop(self, key, default=<object object at 0x794d9eecc1d0>):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## popitem
D.popitem() -> (k, v), remove and return some (key, value) pair
as a 2-tuple; but raise KeyError if D is empty.

```python
def popitem(self):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## setdefault
D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D

```python
def setdefault(self, key, default=None):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## update
D.update([E, ]**F) -> None.  Update D from mapping/iterable E and F.
If E present and has a .keys() method, does:     for k in E: D[k] = E[k]
If E present and lacks .keys() method, does:     for (k, v) in E: D[k] = v
In either case, this is followed by: for k, v in F.items(): D[k] = v

```python
def update(self, other=(), /, **kwds):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## values
D.values() -> an object providing a view on D's values

```python
def values(self):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>
