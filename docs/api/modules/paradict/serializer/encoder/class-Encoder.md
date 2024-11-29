###### Paradict API Reference
[Home](/docs/api/README.md) | [Project](/README.md) | [Module](/docs/api/modules/paradict/serializer/encoder/README.md) | [Source](/src/paradict/serializer/encoder.py)

# Class Encoder
> Module: [paradict.serializer.encoder](/docs/api/modules/paradict/serializer/encoder/README.md)
>
> Class: **Encoder**
>
> Inheritance: `object`

Convert a Python dictionary object to Paradict text format

## Properties table
Here are properties exposed in the class:

| Property | Methods | Description |
| --- | --- | --- |
| attachments\_dir | _getter, setter_ | No docstring. |
| bin\_to\_text | _getter, setter_ | No docstring. |
| mode | _getter, setter_ | No docstring. |
| root\_dir | _getter, setter_ | No docstring. |
| type\_ref | _getter, setter_ | No docstring. |

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

# Methods within class
Here are methods exposed in the class:
- [\_\_init\_\_](#__init__)
- [encode](#encode)
- [\_check\_key](#_check_key)
- [\_encode](#_encode)
- [\_encode\_bin](#_encode_bin)
- [\_encode\_bin\_int](#_encode_bin_int)
- [\_encode\_bool](#_encode_bool)
- [\_encode\_complex](#_encode_complex)
- [\_encode\_date](#_encode_date)
- [\_encode\_datetime](#_encode_datetime)
- [\_encode\_dict](#_encode_dict)
- [\_encode\_dict\_and\_obj](#_encode_dict_and_obj)
- [\_encode\_float](#_encode_float)
- [\_encode\_grid](#_encode_grid)
- [\_encode\_hex\_int](#_encode_hex_int)
- [\_encode\_int](#_encode_int)
- [\_encode\_list](#_encode_list)
- [\_encode\_null](#_encode_null)
- [\_encode\_obj](#_encode_obj)
- [\_encode\_oct\_int](#_encode_oct_int)
- [\_encode\_set](#_encode_set)
- [\_encode\_str](#_encode_str)
- [\_encode\_time](#_encode_time)

## \_\_init\_\_
Init

```python
def __init__(self, mode='d', type_ref=None, bin_to_text=True, root_dir=None, attachments_dir='attachments'):
    ...
```

| Parameter | Description |
| --- | --- |
| mode | either const.DATA_MODE or const.CONFIG_MODE. Defaults to DATA_MODE. |
| type\_ref | optional TypeRef object |
| bin\_to\_text | boolean to tell whether bin data should be embedded as base16 or stored in a linked file |
| root\_dir | root directory in which the attachments dir is supposed to be |
| attachments\_dir | attachments directory. This is a path that is relative to the root dir. Note that relative paths should use a slash as separator. |

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## encode
Generator for iteratively encoding data by yielding lines of Paradict text format

```python
def encode(self, data):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_check\_key
No docstring

```python
def _check_key(self, key):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_encode
No docstring

```python
def _encode(self, data, indents=-1):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_encode\_bin
No docstring

```python
def _encode_bin(self, data, indents=0):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_encode\_bin\_int
No docstring

```python
def _encode_bin_int(self, data, indents=0):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_encode\_bool
No docstring

```python
def _encode_bool(self, data, indents=0):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_encode\_complex
No docstring

```python
def _encode_complex(self, data, indents=0):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_encode\_date
No docstring

```python
def _encode_date(self, data, indents=0):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_encode\_datetime
No docstring

```python
def _encode_datetime(self, data, indents=0):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_encode\_dict
No docstring

```python
def _encode_dict(self, data, indents):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_encode\_dict\_and\_obj
No docstring

```python
def _encode_dict_and_obj(self, tag, data, indents=0):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_encode\_float
No docstring

```python
def _encode_float(self, data, indents=0):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_encode\_grid
No docstring

```python
def _encode_grid(self, data, indents=0):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_encode\_hex\_int
No docstring

```python
def _encode_hex_int(self, data, indents=0):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_encode\_int
No docstring

```python
def _encode_int(self, data, indents=0):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_encode\_list
No docstring

```python
def _encode_list(self, data, indents=0):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_encode\_null
No docstring

```python
def _encode_null(self, data, indents=0):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_encode\_obj
No docstring

```python
def _encode_obj(self, data, indents=0):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_encode\_oct\_int
No docstring

```python
def _encode_oct_int(self, data, indents=0):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_encode\_set
No docstring

```python
def _encode_set(self, data, indents=0):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_encode\_str
No docstring

```python
def _encode_str(self, data, indents=0):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_encode\_time
No docstring

```python
def _encode_time(self, data, indents=0):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>
