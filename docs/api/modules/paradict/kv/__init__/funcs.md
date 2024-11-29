###### Paradict API Reference
[Home](/docs/api/README.md) | [Project](/README.md) | [Module](/docs/api/modules/paradict/kv/__init__/README.md) | [Source](/src/paradict/kv/__init__.py)

# Functions within module
> Module: [paradict.kv.\_\_init\_\_](/docs/api/modules/paradict/kv/__init__/README.md)

Here are functions exposed in the module:
- [split](#split)

## split
Split a non-empty string into key val.
The string should follow one of these format:
- data_mode format: key: value
- config_mode format: key = value

```python
def split(val):
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
