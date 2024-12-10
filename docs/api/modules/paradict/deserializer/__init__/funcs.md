###### Paradict API Reference
[Home](/docs/api/README.md) | [Project](/README.md) | [Module](/docs/api/modules/paradict/deserializer/__init__/README.md) | [Source](/src/paradict/deserializer/__init__.py)

# Functions within module
> Module: [paradict.deserializer.\_\_init\_\_](/docs/api/modules/paradict/deserializer/__init__/README.md)

Here are functions exposed in the module:
- [decode](#decode)
- [unpack](#unpack)

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
