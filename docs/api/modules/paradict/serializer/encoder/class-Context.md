###### Paradict API Reference
[Home](/docs/api/README.md) | [Project](/README.md) | [Module](/docs/api/modules/paradict/serializer/encoder/README.md) | [Source](/paradict/serializer/encoder.py)

# Class Context
> Module: [paradict.serializer.encoder](/docs/api/modules/paradict/serializer/encoder/README.md)
>
> Class: **Context**
>
> Inheritance: `tuple`

Context(name, collection, indents)

## Fields table
Here are fields exposed in the class:

| Field | Description |
| --- | --- |
| name | Alias for field number 0 |
| collection | Alias for field number 1 |
| indents | Alias for field number 2 |

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

# Methods within class
Here are methods exposed in the class:
- [\_asdict](#_asdict)
- [\_make](#_make)
- [\_replace](#_replace)

## \_asdict
Return a new dict which maps field names to their values.

```python
def _asdict(self):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_make
Make a new Context object from a sequence or iterable

```python
@classmethod
def _make(iterable):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_replace
Return a new Context object replacing specified fields with new values

```python
def _replace(self, /, **kwds):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>
