Back to [All Modules](https://github.com/pyrustic/paradict/blob/master/docs/modules/README.md#readme)

# Module Overview

**paradict.serializer.packer**
 
No description

> **Classes:** &nbsp; [Packer](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.serializer.packer/content/classes/Packer.md#class-packer)
>
> **Functions:** &nbsp; [\_pack\_float\_1](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.serializer.packer/content/functions.md#_pack_float_1) &nbsp;&nbsp; [\_pack\_float\_2](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.serializer.packer/content/functions.md#_pack_float_2) &nbsp;&nbsp; [\_pack\_float\_3](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.serializer.packer/content/functions.md#_pack_float_3) &nbsp;&nbsp; [\_pack\_regular\_float](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.serializer.packer/content/functions.md#_pack_regular_float) &nbsp;&nbsp; [pack\_bin](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.serializer.packer/content/functions.md#pack_bin) &nbsp;&nbsp; [pack\_bin\_int](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.serializer.packer/content/functions.md#pack_bin_int) &nbsp;&nbsp; [pack\_bool](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.serializer.packer/content/functions.md#pack_bool) &nbsp;&nbsp; [pack\_comment](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.serializer.packer/content/functions.md#pack_comment) &nbsp;&nbsp; [pack\_comment\_id](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.serializer.packer/content/functions.md#pack_comment_id) &nbsp;&nbsp; [pack\_complex](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.serializer.packer/content/functions.md#pack_complex) &nbsp;&nbsp; [pack\_date](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.serializer.packer/content/functions.md#pack_date) &nbsp;&nbsp; [pack\_datetime](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.serializer.packer/content/functions.md#pack_datetime) &nbsp;&nbsp; [pack\_float](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.serializer.packer/content/functions.md#pack_float) &nbsp;&nbsp; [pack\_hex\_int](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.serializer.packer/content/functions.md#pack_hex_int) &nbsp;&nbsp; [pack\_int](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.serializer.packer/content/functions.md#pack_int) &nbsp;&nbsp; [pack\_nint](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.serializer.packer/content/functions.md#pack_nint) &nbsp;&nbsp; [pack\_oct\_int](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.serializer.packer/content/functions.md#pack_oct_int) &nbsp;&nbsp; [pack\_pint](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.serializer.packer/content/functions.md#pack_pint) &nbsp;&nbsp; [pack\_str](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.serializer.packer/content/functions.md#pack_str) &nbsp;&nbsp; [pack\_time](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.serializer.packer/content/functions.md#pack_time)
>
> **Constants:** &nbsp; ALPHABET &nbsp;&nbsp; SIZE_TO_NINT &nbsp;&nbsp; SIZE_TO_PINT &nbsp;&nbsp; SIZE_TO_STR

# Class Packer
Class to convert some binary Python dict into Paradict binary format

## Base Classes
object

## Class Attributes
No class attributes.

## Class Properties
|Property|Type|Description|Inherited from|
|---|---|---|---|
|skip_comments|getter|None||
|skip_comments|setter|None||
|type_ref|getter|None||
|type_ref|setter|None||



# All Methods
[\_\_init\_\_](#__init__) &nbsp;&nbsp; [pack](#pack) &nbsp;&nbsp; [\_pack](#_pack) &nbsp;&nbsp; [\_pack\_bin](#_pack_bin) &nbsp;&nbsp; [\_pack\_bin\_int](#_pack_bin_int) &nbsp;&nbsp; [\_pack\_bool](#_pack_bool) &nbsp;&nbsp; [\_pack\_comment](#_pack_comment) &nbsp;&nbsp; [\_pack\_comment\_id](#_pack_comment_id) &nbsp;&nbsp; [\_pack\_complex](#_pack_complex) &nbsp;&nbsp; [\_pack\_date](#_pack_date) &nbsp;&nbsp; [\_pack\_datetime](#_pack_datetime) &nbsp;&nbsp; [\_pack\_dict](#_pack_dict) &nbsp;&nbsp; [\_pack\_float](#_pack_float) &nbsp;&nbsp; [\_pack\_grid](#_pack_grid) &nbsp;&nbsp; [\_pack\_hex\_int](#_pack_hex_int) &nbsp;&nbsp; [\_pack\_int](#_pack_int) &nbsp;&nbsp; [\_pack\_list](#_pack_list) &nbsp;&nbsp; [\_pack\_null](#_pack_null) &nbsp;&nbsp; [\_pack\_obj](#_pack_obj) &nbsp;&nbsp; [\_pack\_oct\_int](#_pack_oct_int) &nbsp;&nbsp; [\_pack\_set](#_pack_set) &nbsp;&nbsp; [\_pack\_str](#_pack_str) &nbsp;&nbsp; [\_pack\_time](#_pack_time)

## \_\_init\_\_
Init



**Signature:** (self, type\_ref=None, skip\_comments=False)

|Parameter|Description|
|---|---|
|type\_ref|optional TypeRef object|
|skip\_comments|boolean to tell whether comments should be ignored or not|





**Return Value:** None

[Back to Top](#module-overview)


## pack
Generator for iteratively packing data by yielding bytes datum forged in
Paradict binary format



**Signature:** (self, data)





**Return Value:** None

[Back to Top](#module-overview)


## \_pack
No description



**Signature:** (self, data)





**Return Value:** None

[Back to Top](#module-overview)


## \_pack\_bin
No description



**Signature:** (self, data)





**Return Value:** None

[Back to Top](#module-overview)


## \_pack\_bin\_int
No description



**Signature:** (self, data)





**Return Value:** None

[Back to Top](#module-overview)


## \_pack\_bool
No description



**Signature:** (self, data)





**Return Value:** None

[Back to Top](#module-overview)


## \_pack\_comment
No description



**Signature:** (self, data)





**Return Value:** None

[Back to Top](#module-overview)


## \_pack\_comment\_id
No description



**Signature:** (self, data)





**Return Value:** None

[Back to Top](#module-overview)


## \_pack\_complex
No description



**Signature:** (self, data)





**Return Value:** None

[Back to Top](#module-overview)


## \_pack\_date
No description



**Signature:** (self, data)





**Return Value:** None

[Back to Top](#module-overview)


## \_pack\_datetime
No description



**Signature:** (self, data)





**Return Value:** None

[Back to Top](#module-overview)


## \_pack\_dict
No description



**Signature:** (self, data)





**Return Value:** None

[Back to Top](#module-overview)


## \_pack\_float
No description



**Signature:** (self, data)





**Return Value:** None

[Back to Top](#module-overview)


## \_pack\_grid
No description



**Signature:** (self, data)





**Return Value:** None

[Back to Top](#module-overview)


## \_pack\_hex\_int
No description



**Signature:** (self, data)





**Return Value:** None

[Back to Top](#module-overview)


## \_pack\_int
No description



**Signature:** (self, data)





**Return Value:** None

[Back to Top](#module-overview)


## \_pack\_list
No description



**Signature:** (self, data)





**Return Value:** None

[Back to Top](#module-overview)


## \_pack\_null
No description



**Signature:** (self, data)





**Return Value:** None

[Back to Top](#module-overview)


## \_pack\_obj
No description



**Signature:** (self, data)





**Return Value:** None

[Back to Top](#module-overview)


## \_pack\_oct\_int
No description



**Signature:** (self, data)





**Return Value:** None

[Back to Top](#module-overview)


## \_pack\_set
No description



**Signature:** (self, data)





**Return Value:** None

[Back to Top](#module-overview)


## \_pack\_str
No description



**Signature:** (self, data)





**Return Value:** None

[Back to Top](#module-overview)


## \_pack\_time
No description



**Signature:** (self, data)





**Return Value:** None

[Back to Top](#module-overview)



