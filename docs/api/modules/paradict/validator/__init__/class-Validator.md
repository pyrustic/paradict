###### Paradict API Reference
[Home](/docs/api/README.md) | [Project](/README.md) | [Module](/docs/api/modules/paradict/validator/__init__/README.md) | [Source](/paradict/validator/__init__.py)

# Class Validator
> Module: [paradict.validator.\_\_init\_\_](/docs/api/modules/paradict/validator/__init__/README.md)
>
> Class: **Validator**
>
> Inheritance: `object`

Class to validate data against a schema

## Properties table
Here are properties exposed in the class:

| Property | Methods | Description |
| --- | --- | --- |
| schema | _getter_ | No docstring. |
| type\_ref | _getter_ | No docstring. |

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

# Methods within class
Here are methods exposed in the class:
- [\_\_init\_\_](#__init__)
- [validate](#validate)
- [\_ensure\_spec](#_ensure_spec)
- [\_validate](#_validate)
- [\_validate\_datatype](#_validate_datatype)
- [\_validate\_dict](#_validate_dict)
- [\_validate\_list](#_validate_list)
- [\_validate\_obj](#_validate_obj)
- [\_validate\_set](#_validate_set)

## \_\_init\_\_
Init

```python
def __init__(self, schema, type_ref=None):
    ...
```

| Parameter | Description |
| --- | --- |
| schema | the schema |
| type\_ref | optional TypeRef instance |

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## validate
Validate data. Might raise a validation error

```python
def validate(self, data):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_ensure\_spec
No docstring

```python
def _ensure_spec(self, target, spec):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_validate
No docstring

```python
def _validate(self, target, schema):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_validate\_datatype
No docstring

```python
def _validate_datatype(self, target, datatype):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_validate\_dict
No docstring

```python
def _validate_dict(self, target, schema):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_validate\_list
Schema SHOULD be a list

```python
def _validate_list(self, target, schema):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_validate\_obj
No docstring

```python
def _validate_obj(self, target, schema):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_validate\_set
Schema SHOULD be a set

```python
def _validate_set(self, target, schema):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>
