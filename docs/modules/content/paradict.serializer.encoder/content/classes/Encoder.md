Back to [All Modules](https://github.com/pyrustic/paradict/blob/master/docs/modules/README.md#readme)

# Module Overview

**paradict.serializer.encoder**
 
No description

> **Classes:** &nbsp; [Context](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.serializer.encoder/content/classes/Context.md#class-context) &nbsp;&nbsp; [Encoder](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.serializer.encoder/content/classes/Encoder.md#class-encoder)
>
> **Functions:** &nbsp; [encode\_bin](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.serializer.encoder/content/functions.md#encode_bin) &nbsp;&nbsp; [encode\_bin\_int](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.serializer.encoder/content/functions.md#encode_bin_int) &nbsp;&nbsp; [encode\_bool](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.serializer.encoder/content/functions.md#encode_bool) &nbsp;&nbsp; [encode\_complex](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.serializer.encoder/content/functions.md#encode_complex) &nbsp;&nbsp; [encode\_date](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.serializer.encoder/content/functions.md#encode_date) &nbsp;&nbsp; [encode\_datetime](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.serializer.encoder/content/functions.md#encode_datetime) &nbsp;&nbsp; [encode\_float](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.serializer.encoder/content/functions.md#encode_float) &nbsp;&nbsp; [encode\_hex\_int](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.serializer.encoder/content/functions.md#encode_hex_int) &nbsp;&nbsp; [encode\_int](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.serializer.encoder/content/functions.md#encode_int) &nbsp;&nbsp; [encode\_multiline\_str](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.serializer.encoder/content/functions.md#encode_multiline_str) &nbsp;&nbsp; [encode\_null](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.serializer.encoder/content/functions.md#encode_null) &nbsp;&nbsp; [encode\_oct\_int](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.serializer.encoder/content/functions.md#encode_oct_int) &nbsp;&nbsp; [encode\_str](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.serializer.encoder/content/functions.md#encode_str) &nbsp;&nbsp; [encode\_time](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.serializer.encoder/content/functions.md#encode_time)
>
> **Constants:** &nbsp; None

# Class Encoder
Convert a Python dictionary object to Paradict text format

## Base Classes
object

## Class Attributes
No class attributes.

## Class Properties
|Property|Type|Description|Inherited from|
|---|---|---|---|
|mode|getter|None||
|mode|setter|None||
|skip_bin_data|getter|None||
|skip_bin_data|setter|None||
|skip_comments|getter|None||
|skip_comments|setter|None||
|type_ref|getter|None||
|type_ref|setter|None||



# All Methods
[\_\_init\_\_](#__init__) &nbsp;&nbsp; [encode](#encode) &nbsp;&nbsp; [\_check\_key](#_check_key) &nbsp;&nbsp; [\_encode](#_encode) &nbsp;&nbsp; [\_encode\_bin](#_encode_bin) &nbsp;&nbsp; [\_encode\_bin\_int](#_encode_bin_int) &nbsp;&nbsp; [\_encode\_bool](#_encode_bool) &nbsp;&nbsp; [\_encode\_comment](#_encode_comment) &nbsp;&nbsp; [\_encode\_complex](#_encode_complex) &nbsp;&nbsp; [\_encode\_date](#_encode_date) &nbsp;&nbsp; [\_encode\_datetime](#_encode_datetime) &nbsp;&nbsp; [\_encode\_dict](#_encode_dict) &nbsp;&nbsp; [\_encode\_dict\_and\_obj](#_encode_dict_and_obj) &nbsp;&nbsp; [\_encode\_float](#_encode_float) &nbsp;&nbsp; [\_encode\_grid](#_encode_grid) &nbsp;&nbsp; [\_encode\_hex\_int](#_encode_hex_int) &nbsp;&nbsp; [\_encode\_int](#_encode_int) &nbsp;&nbsp; [\_encode\_list](#_encode_list) &nbsp;&nbsp; [\_encode\_null](#_encode_null) &nbsp;&nbsp; [\_encode\_obj](#_encode_obj) &nbsp;&nbsp; [\_encode\_oct\_int](#_encode_oct_int) &nbsp;&nbsp; [\_encode\_set](#_encode_set) &nbsp;&nbsp; [\_encode\_str](#_encode_str) &nbsp;&nbsp; [\_encode\_time](#_encode_time)

## \_\_init\_\_
Init



**Signature:** (self, mode=1, type\_ref=None, skip\_comments=False, skip\_bin\_data=False)

|Parameter|Description|
|---|---|
|mode|either const.DATA_MODE or const.CONFIG_MODE. Defaults to DATA_MODE.|
|type\_ref|optional TypeRef object|
|skip\_comments|boolean to tell whether comments should be ignored or not|
|skip\_bin\_data|boolean to tell whether bin data should be ignored or not|





**Return Value:** None

[Back to Top](#module-overview)


## encode
Generator for iteratively encoding data by yielding lines of Paradict text format



**Signature:** (self, data)





**Return Value:** None

[Back to Top](#module-overview)


## \_check\_key
No description



**Signature:** (self, key)





**Return Value:** None

[Back to Top](#module-overview)


## \_encode
No description



**Signature:** (self, data, indents=-1)





**Return Value:** None

[Back to Top](#module-overview)


## \_encode\_bin
No description



**Signature:** (self, data, indents=0)





**Return Value:** None

[Back to Top](#module-overview)


## \_encode\_bin\_int
No description



**Signature:** (self, data, indents=0)





**Return Value:** None

[Back to Top](#module-overview)


## \_encode\_bool
No description



**Signature:** (self, data, indents=0)





**Return Value:** None

[Back to Top](#module-overview)


## \_encode\_comment
No description



**Signature:** (self, data, indents=0)





**Return Value:** None

[Back to Top](#module-overview)


## \_encode\_complex
No description



**Signature:** (self, data, indents=0)





**Return Value:** None

[Back to Top](#module-overview)


## \_encode\_date
No description



**Signature:** (self, data, indents=0)





**Return Value:** None

[Back to Top](#module-overview)


## \_encode\_datetime
No description



**Signature:** (self, data, indents=0)





**Return Value:** None

[Back to Top](#module-overview)


## \_encode\_dict
No description



**Signature:** (self, data, indents)





**Return Value:** None

[Back to Top](#module-overview)


## \_encode\_dict\_and\_obj
No description



**Signature:** (self, tag, data, indents=0)





**Return Value:** None

[Back to Top](#module-overview)


## \_encode\_float
No description



**Signature:** (self, data, indents=0)





**Return Value:** None

[Back to Top](#module-overview)


## \_encode\_grid
No description



**Signature:** (self, data, indents=0)





**Return Value:** None

[Back to Top](#module-overview)


## \_encode\_hex\_int
No description



**Signature:** (self, data, indents=0)





**Return Value:** None

[Back to Top](#module-overview)


## \_encode\_int
No description



**Signature:** (self, data, indents=0)





**Return Value:** None

[Back to Top](#module-overview)


## \_encode\_list
No description



**Signature:** (self, data, indents=0)





**Return Value:** None

[Back to Top](#module-overview)


## \_encode\_null
No description



**Signature:** (self, data, indents=0)





**Return Value:** None

[Back to Top](#module-overview)


## \_encode\_obj
No description



**Signature:** (self, data, indents=0)





**Return Value:** None

[Back to Top](#module-overview)


## \_encode\_oct\_int
No description



**Signature:** (self, data, indents=0)





**Return Value:** None

[Back to Top](#module-overview)


## \_encode\_set
No description



**Signature:** (self, data, indents=0)





**Return Value:** None

[Back to Top](#module-overview)


## \_encode\_str
No description



**Signature:** (self, data, indents=0)





**Return Value:** None

[Back to Top](#module-overview)


## \_encode\_time
No description



**Signature:** (self, data, indents=0)





**Return Value:** None

[Back to Top](#module-overview)



