###### Paradict API Reference
[Home](/docs/api/README.md) | [Project](/README.md) | [Module](/docs/api/modules/paradict/serializer/__init__/README.md) | [Source](/src/paradict/serializer/__init__.py)

# Functions within module
> Module: [paradict.serializer.\_\_init\_\_](/docs/api/modules/paradict/serializer/__init__/README.md)

Here are functions exposed in the module:
- [encode](#encode)
- [pack](#pack)

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
