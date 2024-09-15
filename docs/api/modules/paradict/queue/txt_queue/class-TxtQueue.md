###### Paradict API Reference
[Home](/docs/api/README.md) | [Project](/README.md) | [Module](/docs/api/modules/paradict/queue/txt_queue/README.md) | [Source](/paradict/queue/txt_queue.py)

# Class TxtQueue
> Module: [paradict.queue.txt\_queue](/docs/api/modules/paradict/queue/txt_queue/README.md)
>
> Class: **TxtQueue**
>
> Inheritance: `object`

A FIFO queue for processing textual Paradict data

## Properties table
Here are properties exposed in the class:

| Property | Methods | Description |
| --- | --- | --- |
| buffer | _getter_ | No docstring. |

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

# Methods within class
Here are methods exposed in the class:
- [\_\_init\_\_](#__init__)
- [dequeue](#dequeue)
- [enqueue](#enqueue)
- [\_read](#_read)

## \_\_init\_\_
Initialize self.  See help(type(self)) for accurate signature.

```python
def __init__(self):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## dequeue
Generator for iteratively getting each line composing the
        textual data stored in the buffer.
        Note that lines yielded won't end with a newline '
' character

```python
def dequeue(self):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## enqueue
Store textual data in the buffer. This data will then be iteratively
        extracted by the 'get' method, line by line.
        Note: make sure that each line is ended with a newline '
' character

```python
def enqueue(self, s):
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
