###### Paradict API Reference
[Home](/docs/api/README.md) | [Project](/README.md) | [Module](/docs/api/modules/paradict/deserializer/__init__/README.md) | [Source](/paradict/deserializer/__init__.py)

# Functions within module
> Module: [paradict.deserializer.\_\_init\_\_](/docs/api/modules/paradict/deserializer/__init__/README.md)

Here are functions exposed in the module:
- [decode](#decode)
- [load](#load)
- [read](#read)
- [unpack](#unpack)

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
