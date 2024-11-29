###### Paradict API Reference
[Home](/docs/api/README.md) | [Project](/README.md) | [Module](/docs/api/modules/paradict/io_text/__init__/README.md) | [Source](/src/paradict/io_text/__init__.py)

# Functions within module
> Module: [paradict.io\_text.\_\_init\_\_](/docs/api/modules/paradict/io_text/__init__/README.md)

Here are functions exposed in the module:
- [dump](#dump)
- [load](#load)

## dump
Serialize a Python dict object with the Paradict text format then write it to a file

```python
def dump(data, file, *, mode='d', type_ref=None, bin_to_text=False, root_dir=None, attachments_dir='attachments'):
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

## load
Open a textual Paradict file then read its contents into Python dict

```python
def load(file, type_ref=None, receiver=None, obj_builder=None, root_dir=None):
    ...
```

| Parameter | Description |
| --- | --- |
| file | text file object |
| type\_ref | optional TypeRef object |
| receiver | callback function that will be called at the end of conversion. This callback function accepts the Decoder instance as argument |
| obj\_builder | function that accepts a paradict.box.Obj container and returns a fresh new Python object |
| root\_dir | The root_dir should be set only when the file object doesn't have a '.name' property. The root_dir will help to load attachments. |

### Value to return
Return the newly built Python object

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>
