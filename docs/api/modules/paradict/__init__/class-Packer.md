###### Paradict API Reference
[Home](/docs/api/README.md) | [Project](/README.md) | [Module](/docs/api/modules/paradict/__init__/README.md) | [Source](/src/paradict/__init__.py)

# Class Packer
> Module: [paradict.\_\_init\_\_](/docs/api/modules/paradict/__init__/README.md)
>
> Class: **Packer**
>
> Inheritance: `object`

Class to convert some binary Python dict into Paradict binary format

## Properties table
Here are properties exposed in the class:

| Property | Methods | Description |
| --- | --- | --- |
| auto\_index | _getter_ | No docstring. |
| dict\_only | _getter_ | No docstring. |
| index\_dict | _getter_ | Index dictionary for when the root container is a dict |
| type\_ref | _getter, setter_ | No docstring. |

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

# Methods within class
Here are methods exposed in the class:
- [\_\_init\_\_](#__init__)
- [pack](#pack)
- [\_pack](#_pack)
- [\_pack\_bin](#_pack_bin)
- [\_pack\_bin\_int](#_pack_bin_int)
- [\_pack\_bool](#_pack_bool)
- [\_pack\_complex](#_pack_complex)
- [\_pack\_date](#_pack_date)
- [\_pack\_datetime](#_pack_datetime)
- [\_pack\_dict](#_pack_dict)
- [\_pack\_float](#_pack_float)
- [\_pack\_grid](#_pack_grid)
- [\_pack\_hex\_int](#_pack_hex_int)
- [\_pack\_int](#_pack_int)
- [\_pack\_list](#_pack_list)
- [\_pack\_null](#_pack_null)
- [\_pack\_obj](#_pack_obj)
- [\_pack\_oct\_int](#_pack_oct_int)
- [\_pack\_set](#_pack_set)
- [\_pack\_str](#_pack_str)
- [\_pack\_time](#_pack_time)

## \_\_init\_\_
Init

```python
def __init__(self, type_ref=None, dict_only=False, auto_index=False):
    ...
```

| Parameter | Description |
| --- | --- |
| type\_ref | optional TypeRef object |
| dict\_only | boolean to enforce dict as root |

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## pack
Generator for iteratively packing data by yielding bytes datum forged in
Paradict binary format

```python
def pack(self, data):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_pack
No docstring

```python
def _pack(self, data):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_pack\_bin
No docstring

```python
def _pack_bin(self, data):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_pack\_bin\_int
No docstring

```python
def _pack_bin_int(self, data):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_pack\_bool
No docstring

```python
def _pack_bool(self, data):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_pack\_complex
No docstring

```python
def _pack_complex(self, data):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_pack\_date
No docstring

```python
def _pack_date(self, data):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_pack\_datetime
No docstring

```python
def _pack_datetime(self, data):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_pack\_dict
No docstring

```python
def _pack_dict(self, data):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_pack\_float
No docstring

```python
def _pack_float(self, data):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_pack\_grid
No docstring

```python
def _pack_grid(self, data):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_pack\_hex\_int
No docstring

```python
def _pack_hex_int(self, data):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_pack\_int
No docstring

```python
def _pack_int(self, data):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_pack\_list
No docstring

```python
def _pack_list(self, data):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_pack\_null
No docstring

```python
def _pack_null(self, data):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_pack\_obj
No docstring

```python
def _pack_obj(self, data):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_pack\_oct\_int
No docstring

```python
def _pack_oct_int(self, data):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_pack\_set
No docstring

```python
def _pack_set(self, data):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_pack\_str
No docstring

```python
def _pack_str(self, data):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_pack\_time
No docstring

```python
def _pack_time(self, data):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>
