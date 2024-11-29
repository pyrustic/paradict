###### Paradict API Reference
[Home](/docs/api/README.md) | [Project](/README.md) | [Module](/docs/api/modules/paradict/deserializer/buffered_bin_stream/README.md) | [Source](/src/paradict/deserializer/buffered_bin_stream.py)

# Class BufferedBinStream
> Module: [paradict.deserializer.buffered\_bin\_stream](/docs/api/modules/paradict/deserializer/buffered_bin_stream/README.md)
>
> Class: **BufferedBinStream**
>
> Inheritance: `object`

A FIFO queue for processing binary Paradict data

## Properties table
Here are properties exposed in the class:

| Property | Methods | Description |
| --- | --- | --- |
| buffer | _getter_ | No docstring. |

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

# Methods within class
Here are methods exposed in the class:
- [\_\_init\_\_](#__init__)
- [get](#get)
- [get\_all](#get_all)
- [is\_empty](#is_empty)
- [put](#put)
- [\_clear\_status](#_clear_status)
- [\_read](#_read)
- [\_read\_buffer](#_read_buffer)
- [\_update\_expected\_width\_var](#_update_expected_width_var)
- [\_update\_tag\_var](#_update_tag_var)

## \_\_init\_\_
Initialize self.  See help(type(self)) for accurate signature.

```python
def __init__(self):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## get
No docstring

```python
def get(self):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## get\_all
Generator for iteratively getting each tag-payload tuple composing the
raw data stored in the buffer

```python
def get_all(self):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## is\_empty
No docstring

```python
def is_empty(self):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## put
Store binary data in the buffer. This data will then be iteratively
extracted by the 'get' method

```python
def put(self, raw):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_clear\_status
No docstring

```python
def _clear_status(self):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_read
No docstring

```python
def _read(self):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_read\_buffer
No docstring

```python
def _read_buffer(self, reader):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_update\_expected\_width\_var
No docstring

```python
def _update_expected_width_var(self):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_update\_tag\_var
No docstring

```python
def _update_tag_var(self):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>
