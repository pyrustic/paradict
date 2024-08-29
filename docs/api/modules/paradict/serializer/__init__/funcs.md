###### Paradict API Reference
[Home](/docs/api/README.md) | [Project](/README.md) | [Module](/docs/api/modules/paradict/serializer/__init__/README.md) | [Source](/paradict/serializer/__init__.py)

# Functions within module
> Module: [paradict.serializer.\_\_init\_\_](/docs/api/modules/paradict/serializer/__init__/README.md)

Here are functions exposed in the module:
- [dump](#dump)
- [encode](#encode)
- [pack](#pack)
- [write](#write)

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
