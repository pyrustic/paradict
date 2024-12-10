###### Paradict API Reference
[Home](/docs/api/README.md) | [Project](/README.md) | [Module](/docs/api/modules/paradict/__init__/README.md) | [Source](/src/paradict/__init__.py)

# Functions within module
> Module: [paradict.\_\_init\_\_](/docs/api/modules/paradict/__init__/README.md)

Here are functions exposed in the module:
- [decode](#decode)
- [decode\_from](#decode_from)
- [encode](#encode)
- [encode\_into](#encode_into)
- [forge\_bin](#forge_bin)
- [is\_valid](#is_valid)
- [pack](#pack)
- [pack\_into](#pack_into)
- [scan](#scan)
- [split\_kv](#split_kv)
- [stringify\_bin](#stringify_bin)
- [unpack](#unpack)
- [unpack\_from](#unpack_from)

## decode
Convert some textual Paradict data into a Python dictionary

```python
def decode(text, type_ref=None, receiver=None, obj_builder=None, root_dir=None):
    ...
```

| Parameter | Description |
| --- | --- |
| text | string to convert into a Python dict |
| type\_ref | optional TypeRef object |
| receiver | callback function that will be called at the end of conversion. This callback function accepts the Decoder instance as argument |
| obj\_builder | function that accepts a paradict.xtypes.Obj container and returns a fresh new Python object |
| root\_dir | root directory in which the attachments dir is supposed to be |

### Value to return
Return the newly built Python object

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## decode\_from
Open a textual Paradict file then read its contents into Python dict

```python
def decode_from(file, type_ref=None, receiver=None, obj_builder=None, root_dir=None):
    ...
```

| Parameter | Description |
| --- | --- |
| file | text file object |
| type\_ref | optional TypeRef object |
| receiver | callback function that will be called at the end of conversion. This callback function accepts the Decoder instance as argument |
| obj\_builder | function that accepts a paradict.xtypes.Obj container and returns a fresh new Python object |
| root\_dir | The root_dir should be set only when the file object doesn't have a '.name' property. The root_dir will help to load attachments. |

### Value to return
Return the newly built Python object

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## encode
Serialize a Python dict object with the Paradict binary format

```python
def encode(data, *, mode='d', type_ref=None, bin_to_text=True, root_dir=None, attachments_dir='attachments'):
    ...
```

| Parameter | Description |
| --- | --- |
| data | Python dict |
| mode | either const.DATA_MODE or const.CONFIG_MODE. Defaults to DATA_MODE. |
| type\_ref | optional TypeRef object |
| bin\_to\_text | boolean to tell whether bin data should be converted into text or not |
| root\_dir | root directory in which the attachments dir is supposed to be |
| attachments\_dir | attachments directory. This is a path that is relative to the root dir. Note that relative paths should use a slash as separator. |

### Value to return
Return a string in the Paradict text format

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## encode\_into
Serialize a Python dict object with the Paradict text format then write it to a file

```python
def encode_into(data, file, *, mode='d', type_ref=None, bin_to_text=False, root_dir=None, attachments_dir='attachments'):
    ...
```

| Parameter | Description |
| --- | --- |
| data | Python dict object |
| file | text file object |
| mode | either const.DATA_MODE or const.CONFIG_MODE. Defaults to DATA_MODE. |
| type\_ref | optional TypeRef object |
| bin\_to\_text | boolean to tell whether bin data should be converted into text or not |
| root\_dir | the root_dir inside which attachments_dir is supposed to be. Set this only when bin_to_text is False and when the file object doesn't have a '.name' property that is basically the filename. |
| attachments\_dir | path to attachments directory. Relative paths should use a slash as separator |

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

## pack
Serialize a Python dict object with the Paradict binary format

```python
def pack(data, *, type_ref=None, dict_only=False):
    ...
```

| Parameter | Description |
| --- | --- |
| data | Python data object |
| type\_ref | optional TypeRef object |
| dict\_only | boolean to enforce dict as root |

### Value to return
Return a Python bytes object packed in the Paradict binary format

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## pack\_into
Serialize a Python data object with the Paradict binary format
then dump it in a file

```python
def pack_into(data, file, *, type_ref=None):
    ...
```

| Parameter | Description |
| --- | --- |
| data | Python data object |
| file | binary file object |
| type\_ref | optional TypeRef object |
| dict\_only | boolean to enforce dict as root |

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## scan
Scan a binary Paradict file object, yielding a tag with
the slice object of its associated payload

```python
def scan(file):
    ...
```

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
def unpack(raw, type_ref=None, receiver=None, obj_builder=None):
    ...
```

| Parameter | Description |
| --- | --- |
| raw | raw data previously packed with Paradict |
| type\_ref | optional TypeRef object |
| receiver | callback function that will be called at the end of conversion. This callback function accepts the Decoder instance as argument |
| obj\_builder | function that accepts a paradict.xtypes.Obj container and returns a fresh new Python object |
| dict\_only | boolean to enforce dict as root |

### Value to return
Return the newly built Python object

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## unpack\_from
Open a binary Paradict file then unpack its contents into Python dict

```python
def unpack_from(file, type_ref=None, receiver=None, obj_builder=None):
    ...
```

| Parameter | Description |
| --- | --- |
| file | bin file object |
| type\_ref | optional TypeRef object |
| receiver | callback function that will be called at the end of conversion. This callback function accepts the Decoder instance as argument |
| obj\_builder | function that accepts a paradict.xtypes.Obj container and returns a fresh new Python object |

### Value to return
Return the newly built Python object

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>
