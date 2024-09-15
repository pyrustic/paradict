###### Paradict API Reference
[Home](/docs/api/README.md) | [Project](/README.md) | [Module](/docs/api/modules/paradict/validator/__init__/README.md) | [Source](/paradict/validator/__init__.py)

# Class Spec
> Module: [paradict.validator.\_\_init\_\_](/docs/api/modules/paradict/validator/__init__/README.md)
>
> Class: **Spec**
>
> Inheritance: `object`

A Spec can be used to form a schema along with string-types.
The particularity of a Spec is that it can carry a checker that
is a function to serve as an extra programmatic validation

## Properties table
Here are properties exposed in the class:

| Property | Methods | Description |
| --- | --- | --- |
| checker | _getter_ | No docstring. |
| datatype | _getter_ | No docstring. |

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

# Methods within class
Here are methods exposed in the class:
- [\_\_init\_\_](#__init__)

## \_\_init\_\_
Init

```python
def __init__(self, datatype, checker=None):
    ...
```

| Parameter | Description |
| --- | --- |
| datatype | a string representing a valid datatype. Check the VALID_DATATYPES variable to discover valid types. |
| checker | an optional function that will be called with passed as argument, the specific data it should check. This function should return a boolean to validate this piece of data |

### Exceptions table
The table below outlines exceptions that may occur.

| Exception | Circumstance |
| --- | --- |
| ValidationError | raised if the datatype isn't a valid one |

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>
