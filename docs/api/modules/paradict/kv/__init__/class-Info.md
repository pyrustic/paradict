###### Paradict API Reference
[Home](/docs/api/README.md) | [Project](/README.md) | [Module](/docs/api/modules/paradict/kv/__init__/README.md) | [Source](/paradict/kv/__init__.py)

# Class Info
> Module: [paradict.kv.\_\_init\_\_](/docs/api/modules/paradict/kv/__init__/README.md)
>
> Class: **Info**
>
> Inheritance: `tuple`

Info(key, val, sep, mode)

## Fields table
Here are fields exposed in the class:

| Field | Description |
| --- | --- |
| key | Alias for field number 0 |
| val | Alias for field number 1 |
| sep | Alias for field number 2 |
| mode | Alias for field number 3 |

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
Make a new Info object from a sequence or iterable

```python
@classmethod
def _make(iterable):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_replace
Return a new Info object replacing specified fields with new values

```python
def _replace(self, /, **kwds):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>
