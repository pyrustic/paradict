###### Paradict API Reference
[Home](/docs/api/README.md) | [Project](/README.md) | [Module](/docs/api/modules/paradict/deserializer/unpacker/README.md) | [Source](/src/paradict/deserializer/unpacker.py)

# Class Unpacker
> Module: [paradict.deserializer.unpacker](/docs/api/modules/paradict/deserializer/unpacker/README.md)
>
> Class: **Unpacker**
>
> Inheritance: `object`

Class to convert some binary Paradict data into a Python dict

## Properties table
Here are properties exposed in the class:

| Property | Methods | Description |
| --- | --- | --- |
| data | _getter_ | No docstring. |
| obj\_builder | _getter, setter_ | No docstring. |
| queue | _getter, setter_ | No docstring. |
| receiver | _getter, setter_ | No docstring. |
| type\_ref | _getter, setter_ | No docstring. |

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

# Methods within class
Here are methods exposed in the class:
- [\_\_init\_\_](#__init__)
- [feed](#feed)
- [process](#process)
- [\_cleanup\_stack](#_cleanup_stack)
- [\_consume\_block](#_consume_block)
- [\_create\_alpha\_context](#_create_alpha_context)
- [\_create\_beta\_context](#_create_beta_context)
- [\_create\_context](#_create_context)
- [\_get\_context](#_get_context)
- [\_interpret](#_interpret)
- [\_remove\_block](#_remove_block)
- [\_remove\_context](#_remove_context)
- [\_unpack\_bin](#_unpack_bin)
- [\_unpack\_bin\_int](#_unpack_bin_int)
- [\_unpack\_bool](#_unpack_bool)
- [\_unpack\_complex](#_unpack_complex)
- [\_unpack\_date](#_unpack_date)
- [\_unpack\_datetime](#_unpack_datetime)
- [\_unpack\_float](#_unpack_float)
- [\_unpack\_float\_misc](#_unpack_float_misc)
- [\_unpack\_grid](#_unpack_grid)
- [\_unpack\_hex\_int](#_unpack_hex_int)
- [\_unpack\_int](#_unpack_int)
- [\_unpack\_null](#_unpack_null)
- [\_unpack\_obj](#_unpack_obj)
- [\_unpack\_oct\_int](#_unpack_oct_int)
- [\_unpack\_payload](#_unpack_payload)
- [\_unpack\_str](#_unpack_str)
- [\_unpack\_time](#_unpack_time)
- [\_update\_context](#_update_context)

## \_\_init\_\_
Init

```python
def __init__(self, type_ref=None, receiver=None, obj_builder=None):
    ...
```

| Parameter | Description |
| --- | --- |
| type\_ref | optional TypeRef object |
| receiver | callback function that will be called at the end of conversion. This callback function accepts the Unpacker instance as argument |
| obj\_builder | function that accepts a paradict.xtypes.Obj container and returns a fresh new Python object |

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## feed
Feed in arbitrary chunks of data

```python
def feed(self, raw):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## process
Pass in a tag and its associated payload

```python
def process(self, tag, payload):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_cleanup\_stack
No docstring

```python
def _cleanup_stack(self):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_consume\_block
No docstring

```python
def _consume_block(self):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_create\_alpha\_context
No docstring

```python
def _create_alpha_context(self, tag):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_create\_beta\_context
No docstring

```python
def _create_beta_context(self, tag):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_create\_context
No docstring

```python
def _create_context(self, tag):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_get\_context
No docstring

```python
def _get_context(self):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_interpret
No docstring

```python
def _interpret(self, tag, payload):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_remove\_block
No docstring

```python
def _remove_block(self):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_remove\_context
No docstring

```python
def _remove_context(self):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_unpack\_bin
No docstring

```python
def _unpack_bin(self, tag, payload=None):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_unpack\_bin\_int
No docstring

```python
def _unpack_bin_int(self, tag, payload_list=None):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_unpack\_bool
No docstring

```python
def _unpack_bool(self, tag, payload=None):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_unpack\_complex
No docstring

```python
def _unpack_complex(self, tag, payload_list=None):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_unpack\_date
No docstring

```python
def _unpack_date(self, tag, payload_list=None):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_unpack\_datetime
No docstring

```python
def _unpack_datetime(self, tag, payload_list=None):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_unpack\_float
No docstring

```python
def _unpack_float(self, tag, payload_list=None):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_unpack\_float\_misc
No docstring

```python
def _unpack_float_misc(self, tag, payload=None):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_unpack\_grid
No docstring

```python
def _unpack_grid(self, tag, payload_list=None):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_unpack\_hex\_int
No docstring

```python
def _unpack_hex_int(self, tag, payload_list=None):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_unpack\_int
No docstring

```python
def _unpack_int(self, tag, payload=None):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_unpack\_null
No docstring

```python
def _unpack_null(self, tag, payload=None):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_unpack\_obj
No docstring

```python
def _unpack_obj(self, tag, payload_obj=None):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_unpack\_oct\_int
No docstring

```python
def _unpack_oct_int(self, tag, payload_list=None):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_unpack\_payload
No docstring

```python
def _unpack_payload(self, tag, payload=None):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_unpack\_str
No docstring

```python
def _unpack_str(self, tag, payload=None):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_unpack\_time
No docstring

```python
def _unpack_time(self, tag, payload_list=None):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_update\_context
No docstring

```python
def _update_context(self, data):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>
