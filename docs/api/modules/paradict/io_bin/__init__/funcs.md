###### Paradict API Reference
[Home](/docs/api/README.md) | [Project](/README.md) | [Module](/docs/api/modules/paradict/io_bin/__init__/README.md) | [Source](/src/paradict/io_bin/__init__.py)

# Functions within module
> Module: [paradict.io\_bin.\_\_init\_\_](/docs/api/modules/paradict/io_bin/__init__/README.md)

Here are functions exposed in the module:
- [dump](#dump)
- [load](#load)

## dump
Serialize a Python data object with the Paradict binary format
then dump it in a file

```python
def dump(data, file, *, type_ref=None, dict_only=False):
    ...
```

| Parameter | Description |
| --- | --- |
| data | Python data object |
| file | binary file object |
| type\_ref | optional TypeRef object |
| dict\_only | boolean to enforce dict as root |

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## load
Open a binary Paradict file then unpack its contents into Python dict

```python
def load(file, type_ref=None, receiver=None, obj_builder=None, dict_only=False):
    ...
```

| Parameter | Description |
| --- | --- |
| file | bin file object |
| type\_ref | optional TypeRef object |
| receiver | callback function that will be called at the end of conversion. This callback function accepts the Decoder instance as argument |
| obj\_builder | function that accepts a paradict.box.Obj container and returns a fresh new Python object |
| dict\_only | boolean to enforce dict as root |

### Value to return
Return the newly built Python object

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>
