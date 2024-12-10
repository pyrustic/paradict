###### Paradict API Reference
[Home](/docs/api/README.md) | [Project](/README.md) | [Module](/docs/api/modules/paradict/io_bin/__init__/README.md) | [Source](/src/paradict/io_bin/__init__.py)

# Functions within module
> Module: [paradict.io\_bin.\_\_init\_\_](/docs/api/modules/paradict/io_bin/__init__/README.md)

Here are functions exposed in the module:
- [pack\_into](#pack_into)
- [unpack\_from](#unpack_from)

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
