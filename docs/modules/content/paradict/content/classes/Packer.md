Back to [All Modules](https://github.com/pyrustic/paradict/blob/master/docs/modules/README.md#readme)

# Module Overview

**paradict**
 
No description

> **Classes:** &nbsp; [ConfigFile](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/classes/ConfigFile.md#class-configfile) &nbsp;&nbsp; [Decoder](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/classes/Decoder.md#class-decoder) &nbsp;&nbsp; [Document](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/classes/Document.md#class-document) &nbsp;&nbsp; [Encoder](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/classes/Encoder.md#class-encoder) &nbsp;&nbsp; [FileDoc](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/classes/FileDoc.md#class-filedoc) &nbsp;&nbsp; [Packer](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/classes/Packer.md#class-packer) &nbsp;&nbsp; [TypeRef](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/classes/TypeRef.md#class-typeref) &nbsp;&nbsp; [Unpacker](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/classes/Unpacker.md#class-unpacker) &nbsp;&nbsp; [Validator](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/classes/Validator.md#class-validator)
>
> **Functions:** &nbsp; [decode](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/functions.md#decode) &nbsp;&nbsp; [dump](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/functions.md#dump) &nbsp;&nbsp; [encode](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/functions.md#encode) &nbsp;&nbsp; [forge\_bin](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/functions.md#forge_bin) &nbsp;&nbsp; [load](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/functions.md#load) &nbsp;&nbsp; [pack](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/functions.md#pack) &nbsp;&nbsp; [split\_kv](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/functions.md#split_kv) &nbsp;&nbsp; [stringify\_bin](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/functions.md#stringify_bin) &nbsp;&nbsp; [unpack](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/functions.md#unpack) &nbsp;&nbsp; [validate](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/functions.md#validate)
>
> **Constants:** &nbsp; None

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
[\_\_init\_\_](#__init__) &nbsp;&nbsp; [pack](#pack) &nbsp;&nbsp; [\_pack](#_pack) &nbsp;&nbsp; [\_pack\_bin](#_pack_bin) &nbsp;&nbsp; [\_pack\_bin\_int](#_pack_bin_int) &nbsp;&nbsp; [\_pack\_bool](#_pack_bool) &nbsp;&nbsp; [\_pack\_command](#_pack_command) &nbsp;&nbsp; [\_pack\_comment](#_pack_comment) &nbsp;&nbsp; [\_pack\_comment\_id](#_pack_comment_id) &nbsp;&nbsp; [\_pack\_complex](#_pack_complex) &nbsp;&nbsp; [\_pack\_date](#_pack_date) &nbsp;&nbsp; [\_pack\_datetime](#_pack_datetime) &nbsp;&nbsp; [\_pack\_dict](#_pack_dict) &nbsp;&nbsp; [\_pack\_float](#_pack_float) &nbsp;&nbsp; [\_pack\_grid](#_pack_grid) &nbsp;&nbsp; [\_pack\_hex\_int](#_pack_hex_int) &nbsp;&nbsp; [\_pack\_int](#_pack_int) &nbsp;&nbsp; [\_pack\_list](#_pack_list) &nbsp;&nbsp; [\_pack\_null](#_pack_null) &nbsp;&nbsp; [\_pack\_obj](#_pack_obj) &nbsp;&nbsp; [\_pack\_oct\_int](#_pack_oct_int) &nbsp;&nbsp; [\_pack\_set](#_pack_set) &nbsp;&nbsp; [\_pack\_str](#_pack_str) &nbsp;&nbsp; [\_pack\_time](#_pack_time)

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


## \_pack\_command
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



