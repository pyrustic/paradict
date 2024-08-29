###### Paradict API Reference
[Home](/docs/api/README.md) | [Project](/README.md) | [Module](/docs/api/modules/paradict/__init__/README.md) | [Source](/paradict/__init__.py)

# Functions within module
> Module: [paradict.\_\_init\_\_](/docs/api/modules/paradict/__init__/README.md)

Here are functions exposed in the module:
- [decode](#decode)
- [dump](#dump)
- [encode](#encode)
- [forge\_bin](#forge_bin)
- [is\_valid](#is_valid)
- [load](#load)
- [pack](#pack)
- [read](#read)
- [split\_kv](#split_kv)
- [stringify\_bin](#stringify_bin)
- [unpack](#unpack)
- [write](#write)

## decode
Convert some textual Paradict data into a Python dictionary

```python
def decode(text, type_ref=None, receiver=None, obj_builder=None, skip_comments=False, root_dir=None):
    ...
```

| Parameter | Description |
| --- | --- |
| text | string to convert into a Python dict |
| type\_ref | optional TypeRef object |
| receiver | callback function that will be called at the end of conversion. This callback function accepts the Decoder instance as argument |
| obj\_builder | function that accepts a paradict.box.Obj container and returns a fresh new Python object |
| skip\_comments | boolean to tell whether comments should be ignored or not |
| root\_dir | root directory in which the attachments dir is supposed to be |

### Value to return
Return the newly built Python object

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## dump
Convert some Python dict in the Paradict binary format
then dump it in a file

```python
def dump(data, path, *, type_ref=None, skip_comments=False):
    ...
```

| Parameter | Description |
| --- | --- |
| path | path string or pathlib.Path instance |
| type\_ref | optional TypeRef object |
| skip\_comments | boolean to tell whether comments should be ignored or not |

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## encode
Convert a Python dictionary object to Paradict binary format

```python
def encode(data, *, mode='d', type_ref=None, skip_comments=False, bin_to_text=True, root_dir=None, attachments_dir='attachments'):
    ...
```

| Parameter | Description |
| --- | --- |
| data | Python dict |
| mode | either const.DATA_MODE or const.CONFIG_MODE. Defaults to DATA_MODE. |
| type\_ref | optional TypeRef object |
| skip\_comments | boolean to tell whether comments should be ignored or not |
| bin\_to\_text | boolean to tell whether bin data should be converted into text or not |
| root\_dir | root directory in which the attachments dir is supposed to be |
| attachments\_dir | attachments directory. This is a path that is relative to the root dir. Note that relative paths should use a slash as separator. |

### Value to return
Return a string in the Paradict text format

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## forge\_bin
items are int, bytes, bytearrays, or Nones, returns a bytearray

```python
def forge_bin(*items):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## is\_valid
This function returns True if the given data
successfully validates against the given schema

```python
def is_valid(data, schema, type_ref=None):
    ...
```

| Parameter | Description |
| --- | --- |
| data | some Python object (like a dict, a list, ...) that is part or include datatypes defined in VALID_DATATYPES. |
| schema | a valid schema. It might be a collection containing Spec instances and/or type-strings. The benefit of using Spec is that you can add a checker function that will serve as an extra programmatic validation. |
| type\_ref | optional TypeRef object |

### Value to return
Returns True or False

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## load
Open a binary Paradict file then unpack its contents into Python dict

```python
def load(path, type_ref=None, receiver=None, obj_builder=None, skip_comments=False):
    ...
```

| Parameter | Description |
| --- | --- |
| path | a path string, or a pathlib.Path instance |
| type\_ref | optional TypeRef object |
| receiver | callback function that will be called at the end of conversion. This callback function accepts the Decoder instance as argument |
| obj\_builder | function that accepts a paradict.box.Obj container and returns a fresh new Python object |
| skip\_comments | boolean to tell whether comments should be ignored or not |

### Value to return
Return the newly built Python object

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## pack
Convert a Python dictionary object to Paradict binary format

```python
def pack(data, *, type_ref=None, skip_comments=False):
    ...
```

| Parameter | Description |
| --- | --- |
| data | Python dict |
| type\_ref | optional TypeRef object |
| skip\_comments | boolean to tell whether comments should be ignored or not |

### Value to return
Return a Python bytes object packed in the Paradict binary format

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## read
Open a textual Paradict file then read its contents into Python dict

```python
def read(path, type_ref=None, receiver=None, obj_builder=None, skip_comments=False):
    ...
```

| Parameter | Description |
| --- | --- |
| path | a path string, or a pathlib.Path instance |
| type\_ref | optional TypeRef object |
| receiver | callback function that will be called at the end of conversion. This callback function accepts the Decoder instance as argument |
| obj\_builder | function that accepts a paradict.box.Obj container and returns a fresh new Python object |
| skip\_comments | boolean to tell whether comments should be ignored or not |

### Value to return
Return the newly built Python object

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## split\_kv
Split a non-empty string into key val.
The string should follow one of these format:
- data_mode format: key: value
- config_mode format: key = value

```python
def split_kv(val):
    ...
```

| Parameter | Description |
| --- | --- |
| val | non-empty string |

### Value to return
Return an Info namedtuple made of: key, val, sep, and mode attributes.
The key and val are strings. The sep is either ":" or "=".
The mode is either paradict.const.DATA_MODE or paradict.const.CONFIG_MODE.
Note that if the sep is a colon, it means that the mode is DATA_MODE.

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## stringify\_bin
Good for debug. Stringify some binary data

```python
def stringify_bin(b, offset=0, width=None, spaced=False):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## unpack
Convert some binary Paradict data into a Python dictionary

```python
def unpack(raw, type_ref=None, receiver=None, obj_builder=None, skip_comments=False):
    ...
```

| Parameter | Description |
| --- | --- |
| raw | raw data previously packed with Paradict |
| type\_ref | optional TypeRef object |
| receiver | callback function that will be called at the end of conversion. This callback function accepts the Decoder instance as argument |
| obj\_builder | function that accepts a paradict.box.Obj container and returns a fresh new Python object |
| skip\_comments | boolean to tell whether comments should be ignored or not |

### Value to return
Return the newly built Python object

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## write
Convert some Python dict in the Paradict textual format
then write it to a file

```python
def write(data, path, *, mode='d', type_ref=None, skip_comments=False, bin_to_text=False, attachments_dir='attachments'):
    ...
```

| Parameter | Description |
| --- | --- |
| path | path string or pathlib.Path instance |
| mode | either const.DATA_MODE or const.CONFIG_MODE. Defaults to DATA_MODE. |
| type\_ref | optional TypeRef object |
| skip\_comments | boolean to tell whether comments should be ignored or not |
| bin\_to\_text | boolean to tell whether bin data should be converted into text or not |
| attachments\_dir | path to attachments directory. Relative paths should use a slash as separator |

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>
