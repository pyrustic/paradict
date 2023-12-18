Back to [All Modules](https://github.com/pyrustic/paradict/blob/master/docs/modules/README.md#readme)

# Module Overview

**paradict.kv**
 
This module exposes the split function that will parse a valid key-value string

> **Classes:** &nbsp; [Info](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.kv/content/classes/Info.md#class-info)
>
> **Functions:** &nbsp; [\_parse](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.kv/content/functions.md#_parse) &nbsp;&nbsp; [split](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.kv/content/functions.md#split)
>
> **Constants:** &nbsp; CONFIG_MODE_PATTERN &nbsp;&nbsp; DATA_MODE_PATTERN_1 &nbsp;&nbsp; DATA_MODE_PATTERN_2 &nbsp;&nbsp; DATA_MODE_PATTERN_3 &nbsp;&nbsp; KEY_PATTERN_1 &nbsp;&nbsp; KEY_PATTERN_2 &nbsp;&nbsp; KEY_PATTERN_3 &nbsp;&nbsp; KEY_PATTERN_4 &nbsp;&nbsp; KEY_VAL_PATTERN &nbsp;&nbsp; VALUE_PATTERN

# Class Info
Info(key, val, sep, mode)

## Base Classes
tuple

## Class Attributes
\_field\_defaults &nbsp;&nbsp; \_fields &nbsp;&nbsp; \_fields\_defaults &nbsp;&nbsp; \_make &nbsp;&nbsp; key &nbsp;&nbsp; mode &nbsp;&nbsp; sep &nbsp;&nbsp; val

## Class Properties


# All Methods
[count](#count) &nbsp;&nbsp; [index](#index) &nbsp;&nbsp; [\_asdict](#_asdict) &nbsp;&nbsp; [\_replace](#_replace)

## count
Return number of occurrences of value.

**Inherited from:** tuple

**Signature:** (self, value, /)





**Return Value:** None

[Back to Top](#module-overview)


## index
Return first index of value.

Raises ValueError if the value is not present.

**Inherited from:** tuple

**Signature:** (self, value, start=0, stop=9223372036854775807, /)





**Return Value:** None

[Back to Top](#module-overview)


## \_asdict
Return a new dict which maps field names to their values.



**Signature:** (self)





**Return Value:** None

[Back to Top](#module-overview)


## \_replace
Return a new Info object replacing specified fields with new values



**Signature:** (self, /, \*\*kwds)





**Return Value:** None

[Back to Top](#module-overview)



