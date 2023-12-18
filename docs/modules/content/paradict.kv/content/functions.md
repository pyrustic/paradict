Back to [All Modules](https://github.com/pyrustic/paradict/blob/master/docs/modules/README.md#readme)

# Module Overview

**paradict.kv**
 
This module exposes the split function that will parse a valid key-value string

> **Classes:** &nbsp; [Info](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.kv/content/classes/Info.md#class-info)
>
> **Functions:** &nbsp; [\_parse](#_parse) &nbsp;&nbsp; [split](#split)
>
> **Constants:** &nbsp; CONFIG_MODE_PATTERN &nbsp;&nbsp; DATA_MODE_PATTERN_1 &nbsp;&nbsp; DATA_MODE_PATTERN_2 &nbsp;&nbsp; DATA_MODE_PATTERN_3 &nbsp;&nbsp; KEY_PATTERN_1 &nbsp;&nbsp; KEY_PATTERN_2 &nbsp;&nbsp; KEY_PATTERN_3 &nbsp;&nbsp; KEY_PATTERN_4 &nbsp;&nbsp; KEY_VAL_PATTERN &nbsp;&nbsp; VALUE_PATTERN

# All Functions
[\_parse](#_parse) &nbsp;&nbsp; [split](#split)

## \_parse
regex parse



**Signature:** (val)





**Return Value:** None

[Back to Top](#module-overview)


## split
Split a non-empty string into key val.
The string should follow one of these format:
- data_mode format: key: value
- config_mode format: key = value



**Signature:** (val)

|Parameter|Description|
|---|---|
|val|non-empty string|





**Return Value:** Return an Info namedtuple made of: key, val, sep, and mode attributes.
The key and val are strings. The sep is either ":" or "=".
The mode is either paradict.const.DATA_MODE or paradict.const.CONFIG_MODE.
Note that if the sep is a colon, it means that the mode is DATA_MODE.

[Back to Top](#module-overview)


