Back to [All Modules](https://github.com/pyrustic/paradict/blob/master/docs/modules/README.md#readme)

# Module Overview

**paradict.serializer.encoder**
 
No description

> **Classes:** &nbsp; [Context](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.serializer.encoder/content/classes/Context.md#class-context) &nbsp;&nbsp; [Encoder](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.serializer.encoder/content/classes/Encoder.md#class-encoder)
>
> **Functions:** &nbsp; [encode\_bin](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.serializer.encoder/content/functions.md#encode_bin) &nbsp;&nbsp; [encode\_bin\_int](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.serializer.encoder/content/functions.md#encode_bin_int) &nbsp;&nbsp; [encode\_bool](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.serializer.encoder/content/functions.md#encode_bool) &nbsp;&nbsp; [encode\_complex](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.serializer.encoder/content/functions.md#encode_complex) &nbsp;&nbsp; [encode\_date](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.serializer.encoder/content/functions.md#encode_date) &nbsp;&nbsp; [encode\_datetime](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.serializer.encoder/content/functions.md#encode_datetime) &nbsp;&nbsp; [encode\_float](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.serializer.encoder/content/functions.md#encode_float) &nbsp;&nbsp; [encode\_hex\_int](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.serializer.encoder/content/functions.md#encode_hex_int) &nbsp;&nbsp; [encode\_int](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.serializer.encoder/content/functions.md#encode_int) &nbsp;&nbsp; [encode\_null](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.serializer.encoder/content/functions.md#encode_null) &nbsp;&nbsp; [encode\_oct\_int](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.serializer.encoder/content/functions.md#encode_oct_int) &nbsp;&nbsp; [encode\_raw](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.serializer.encoder/content/functions.md#encode_raw) &nbsp;&nbsp; [encode\_string](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.serializer.encoder/content/functions.md#encode_string) &nbsp;&nbsp; [encode\_text](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.serializer.encoder/content/functions.md#encode_text) &nbsp;&nbsp; [encode\_time](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.serializer.encoder/content/functions.md#encode_time)
>
> **Constants:** &nbsp; None

# Class Context
Context(name, collection, indents)

## Base Classes
tuple

## Class Attributes
\_field\_defaults &nbsp;&nbsp; \_fields &nbsp;&nbsp; \_fields\_defaults &nbsp;&nbsp; \_make &nbsp;&nbsp; collection &nbsp;&nbsp; indents &nbsp;&nbsp; name

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
Return a new Context object replacing specified fields with new values



**Signature:** (self, /, \*\*kwds)





**Return Value:** None

[Back to Top](#module-overview)



