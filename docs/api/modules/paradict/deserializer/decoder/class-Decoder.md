###### Paradict API Reference
[Home](/docs/api/README.md) | [Project](/README.md) | [Module](/docs/api/modules/paradict/deserializer/decoder/README.md) | [Source](/paradict/deserializer/decoder.py)

# Class Decoder
> Module: [paradict.deserializer.decoder](/docs/api/modules/paradict/deserializer/decoder/README.md)
>
> Class: **Decoder**
>
> Inheritance: `object`

Class to convert some textual Paradict data into a Python dict

## Properties table
Here are properties exposed in the class:

| Property | Methods | Description |
| --- | --- | --- |
| data | _getter_ | No docstring. |
| is\_feedable | _getter, setter_ | No docstring. |
| obj\_builder | _getter, setter_ | No docstring. |
| queue | _getter, setter_ | No docstring. |
| receiver | _getter, setter_ | No docstring. |
| root\_dir | _getter, setter_ | No docstring. |
| skip\_comments | _getter, setter_ | No docstring. |
| type\_ref | _getter, setter_ | No docstring. |

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

# Methods within class
Here are methods exposed in the class:
- [\_\_init\_\_](#__init__)
- [feed](#feed)
- [\_add\_whitespace\_to\_parent\_context](#_add_whitespace_to_parent_context)
- [\_check\_key](#_check_key)
- [\_check\_line](#_check_line)
- [\_check\_multiline\_tag](#_check_multiline_tag)
- [\_cleanup\_stack](#_cleanup_stack)
- [\_consume\_bin\_block](#_consume_bin_block)
- [\_consume\_grid\_block](#_consume_grid_block)
- [\_consume\_obj\_block](#_consume_obj_block)
- [\_consume\_raw\_block](#_consume_raw_block)
- [\_consume\_str\_block](#_consume_str_block)
- [\_decode\_bin](#_decode_bin)
- [\_decode\_bool](#_decode_bool)
- [\_decode\_complex\_number](#_decode_complex_number)
- [\_decode\_container](#_decode_container)
- [\_decode\_date](#_decode_date)
- [\_decode\_datetime](#_decode_datetime)
- [\_decode\_float](#_decode_float)
- [\_decode\_int](#_decode_int)
- [\_decode\_load\_func](#_decode_load_func)
- [\_decode\_null](#_decode_null)
- [\_decode\_str](#_decode_str)
- [\_decode\_time](#_decode_time)
- [\_decode\_value](#_decode_value)
- [\_get\_context](#_get_context)
- [\_get\_parent\_context](#_get_parent_context)
- [\_interpret](#_interpret)
- [\_process](#_process)
- [\_update\_context](#_update_context)
- [\_update\_dict\_container](#_update_dict_container)
- [\_update\_list\_container](#_update_list_container)
- [\_update\_obj\_container](#_update_obj_container)
- [\_update\_parent\_context](#_update_parent_context)
- [\_update\_set\_container](#_update_set_container)
- [\_update\_stack](#_update_stack)

## \_\_init\_\_
Init

```python
def __init__(self, *, type_ref=None, receiver=None, obj_builder=None, skip_comments=False, root_dir=None):
    ...
```

| Parameter | Description |
| --- | --- |
| type\_ref | optional TypeRef object |
| receiver | callback function that will be called at the end of conversion. This callback function accepts the Decoder instance as argument |
| obj\_builder | function that accepts a paradict.box.Obj container and returns a fresh new Python object |
| skip\_comments | boolean to tell whether comments should be ignored or not |
| root\_dir | root directory in which the attachments dir is supposed to be |

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## feed
Feed the decoder engine with some string.
        The string might represent a line in the textual Paradict data,
        or an arbitrary length of characters.

        Note: it is very important to make sure that each line is ended
        by a "
" newline character

        Check the `paradict.decode` function to see an example of
        how to use this class

```python
def feed(self, s):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_add\_whitespace\_to\_parent\_context
No docstring

```python
def _add_whitespace_to_parent_context(self, parent_context):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_check\_key
No docstring

```python
def _check_key(self, key, mode):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_check\_line
Check the validity of the indent in the line
Returns the indent-less version of line

```python
def _check_line(self, line):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_check\_multiline\_tag
No docstring

```python
def _check_multiline_tag(self, value):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_cleanup\_stack
No docstring

```python
def _cleanup_stack(self, indents):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_consume\_bin\_block
No docstring

```python
def _consume_bin_block(self, parent_context, context):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_consume\_grid\_block
No docstring

```python
def _consume_grid_block(self, parent_context, context):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_consume\_obj\_block
No docstring

```python
def _consume_obj_block(self, parent_context, context):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_consume\_raw\_block
No docstring

```python
def _consume_raw_block(self, parent_context, context):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_consume\_str\_block
No docstring

```python
def _consume_str_block(self, parent_context, context):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_decode\_bin
No docstring

```python
def _decode_bin(self, val):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_decode\_bool
No docstring

```python
def _decode_bool(self, val):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_decode\_complex\_number
No docstring

```python
def _decode_complex_number(self, val):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_decode\_container
No docstring

```python
def _decode_container(self, val):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_decode\_date
No docstring

```python
def _decode_date(self, val):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_decode\_datetime
No docstring

```python
def _decode_datetime(self, val):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_decode\_float
No docstring

```python
def _decode_float(self, val):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_decode\_int
No docstring

```python
def _decode_int(self, val):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_decode\_load\_func
No docstring

```python
def _decode_load_func(self, val):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_decode\_null
No docstring

```python
def _decode_null(self, val):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_decode\_str
No docstring

```python
def _decode_str(self, val):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_decode\_time
No docstring

```python
def _decode_time(self, val):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_decode\_value
No docstring

```python
def _decode_value(self, value):
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

## \_get\_parent\_context
No docstring

```python
def _get_parent_context(self):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_interpret
No docstring

```python
def _interpret(self, line):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_process
No docstring

```python
def _process(self, line):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_update\_context
No docstring

```python
def _update_context(self, line):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_update\_dict\_container
No docstring

```python
def _update_dict_container(self, context, line):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_update\_list\_container
No docstring

```python
def _update_list_container(self, context, line):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_update\_obj\_container
No docstring

```python
def _update_obj_container(self, context, line):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_update\_parent\_context
No docstring

```python
def _update_parent_context(self, parent_context, data):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_update\_set\_container
No docstring

```python
def _update_set_container(self, context, line):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## \_update\_stack
No docstring

```python
def _update_stack(self, container_name, container, indents):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>
