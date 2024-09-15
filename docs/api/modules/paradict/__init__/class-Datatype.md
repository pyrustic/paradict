###### Paradict API Reference
[Home](/docs/api/README.md) | [Project](/README.md) | [Module](/docs/api/modules/paradict/__init__/README.md) | [Source](/paradict/__init__.py)

# Class Datatype
> Module: [paradict.\_\_init\_\_](/docs/api/modules/paradict/__init__/README.md)
>
> Class: **Datatype**
>
> Inheritance: `enum.Enum`

An enumeration.

## Fields table
Here are fields exposed in the class:

| Field | Value |
| --- | --- |
| DICT | `1` |
| LIST | `2` |
| SET | `3` |
| OBJ | `4` |
| BIN | `5` |
| BIN\_INT | `6` |
| BOOL | `7` |
| COMMENT | `8` |
| COMMENT\_ID | `9` |
| COMPLEX | `10` |
| DATE | `11` |
| DATETIME | `12` |
| FLOAT | `13` |
| GRID | `14` |
| HEX\_INT | `15` |
| INT | `16` |
| OCT\_INT | `17` |
| STR | `18` |
| TIME | `19` |

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

# Methods within class
Here are methods exposed in the class:
- [\_generate\_next\_value\_](#_generate_next_value_)
- [\_missing\_](#_missing_)

## \_generate\_next\_value\_
No docstring

```python
def _generate_next_value_(name, start, count, last_values):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_missing\_
No docstring

```python
@classmethod
def _missing_(value):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>
