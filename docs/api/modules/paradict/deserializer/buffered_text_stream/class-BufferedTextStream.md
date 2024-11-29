###### Paradict API Reference
[Home](/docs/api/README.md) | [Project](/README.md) | [Module](/docs/api/modules/paradict/deserializer/buffered_text_stream/README.md) | [Source](/src/paradict/deserializer/buffered_text_stream.py)

# Class BufferedTextStream
> Module: [paradict.deserializer.buffered\_text\_stream](/docs/api/modules/paradict/deserializer/buffered_text_stream/README.md)
>
> Class: **BufferedTextStream**
>
> Inheritance: `object`

A FIFO queue for processing textual Paradict data

# Methods within class
Here are methods exposed in the class:
- [\_\_init\_\_](#__init__)
- [get](#get)
- [get\_all](#get_all)
- [is\_empty](#is_empty)
- [put](#put)

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
Generator for iteratively getting each line composing the
        textual data stored in the buffer.
        Note that lines yielded won't end with a newline '
' character

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
Store textual data in the buffer. This data will then be iteratively
        extracted by the 'get' method, line by line.
        Note: make sure that each line is ended with a newline '
' character

```python
def put(self, s):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>
