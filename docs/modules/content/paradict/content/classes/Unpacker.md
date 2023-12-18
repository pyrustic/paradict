Back to [All Modules](https://github.com/pyrustic/paradict/blob/master/docs/modules/README.md#readme)

# Module Overview

**paradict**
 
No description

> **Classes:** &nbsp; [ConfigFile](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/classes/ConfigFile.md#class-configfile) &nbsp;&nbsp; [Decoder](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/classes/Decoder.md#class-decoder) &nbsp;&nbsp; [Document](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/classes/Document.md#class-document) &nbsp;&nbsp; [Encoder](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/classes/Encoder.md#class-encoder) &nbsp;&nbsp; [FileDoc](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/classes/FileDoc.md#class-filedoc) &nbsp;&nbsp; [Packer](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/classes/Packer.md#class-packer) &nbsp;&nbsp; [TypeRef](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/classes/TypeRef.md#class-typeref) &nbsp;&nbsp; [Unpacker](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/classes/Unpacker.md#class-unpacker) &nbsp;&nbsp; [Validator](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/classes/Validator.md#class-validator)
>
> **Functions:** &nbsp; [decode](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/functions.md#decode) &nbsp;&nbsp; [dump](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/functions.md#dump) &nbsp;&nbsp; [encode](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/functions.md#encode) &nbsp;&nbsp; [forge\_bin](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/functions.md#forge_bin) &nbsp;&nbsp; [load](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/functions.md#load) &nbsp;&nbsp; [pack](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/functions.md#pack) &nbsp;&nbsp; [split\_kv](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/functions.md#split_kv) &nbsp;&nbsp; [stringify\_bin](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/functions.md#stringify_bin) &nbsp;&nbsp; [unpack](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/functions.md#unpack) &nbsp;&nbsp; [validate](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/functions.md#validate)
>
> **Constants:** &nbsp; None

# Class Unpacker
Class to convert some binary Paradict data into a Python dict

## Base Classes
object

## Class Attributes
No class attributes.

## Class Properties
|Property|Type|Description|Inherited from|
|---|---|---|---|
|data|getter|None||
|feedable|getter|None||
|feedable|setter|None||
|obj_builder|getter|None||
|obj_builder|setter|None||
|queue|getter|None||
|queue|setter|None||
|receiver|getter|None||
|receiver|setter|None||
|skip_comments|getter|None||
|skip_comments|setter|None||
|type_ref|getter|None||
|type_ref|setter|None||



# All Methods
[\_\_init\_\_](#__init__) &nbsp;&nbsp; [feed](#feed) &nbsp;&nbsp; [\_cleanup\_stack](#_cleanup_stack) &nbsp;&nbsp; [\_consume\_block](#_consume_block) &nbsp;&nbsp; [\_create\_alpha\_context](#_create_alpha_context) &nbsp;&nbsp; [\_create\_beta\_context](#_create_beta_context) &nbsp;&nbsp; [\_create\_context](#_create_context) &nbsp;&nbsp; [\_get\_context](#_get_context) &nbsp;&nbsp; [\_interpret](#_interpret) &nbsp;&nbsp; [\_process](#_process) &nbsp;&nbsp; [\_remove\_block](#_remove_block) &nbsp;&nbsp; [\_remove\_context](#_remove_context) &nbsp;&nbsp; [\_unpack\_bin](#_unpack_bin) &nbsp;&nbsp; [\_unpack\_bin\_int](#_unpack_bin_int) &nbsp;&nbsp; [\_unpack\_bool](#_unpack_bool) &nbsp;&nbsp; [\_unpack\_comment](#_unpack_comment) &nbsp;&nbsp; [\_unpack\_comment\_id](#_unpack_comment_id) &nbsp;&nbsp; [\_unpack\_complex](#_unpack_complex) &nbsp;&nbsp; [\_unpack\_date](#_unpack_date) &nbsp;&nbsp; [\_unpack\_datetime](#_unpack_datetime) &nbsp;&nbsp; [\_unpack\_float](#_unpack_float) &nbsp;&nbsp; [\_unpack\_float\_misc](#_unpack_float_misc) &nbsp;&nbsp; [\_unpack\_grid](#_unpack_grid) &nbsp;&nbsp; [\_unpack\_hex\_int](#_unpack_hex_int) &nbsp;&nbsp; [\_unpack\_int](#_unpack_int) &nbsp;&nbsp; [\_unpack\_null](#_unpack_null) &nbsp;&nbsp; [\_unpack\_obj](#_unpack_obj) &nbsp;&nbsp; [\_unpack\_oct\_int](#_unpack_oct_int) &nbsp;&nbsp; [\_unpack\_payload](#_unpack_payload) &nbsp;&nbsp; [\_unpack\_raw](#_unpack_raw) &nbsp;&nbsp; [\_unpack\_str](#_unpack_str) &nbsp;&nbsp; [\_unpack\_time](#_unpack_time) &nbsp;&nbsp; [\_update\_context](#_update_context) &nbsp;&nbsp; [\_update\_flags](#_update_flags)

## \_\_init\_\_
Init



**Signature:** (self, type\_ref=None, receiver=None, obj\_builder=None, skip\_comments=False)

|Parameter|Description|
|---|---|
|type\_ref|optional TypeRef object|
|receiver|callback function that will be called at the end of conversion. This callback function accepts the Unpacker instance as argument|
|obj\_builder|function that accepts a paradict.box.Obj container and returns a fresh new Python object|
|skip\_comments|boolean to tell whether comments should be ignored or not|





**Return Value:** None

[Back to Top](#module-overview)


## feed
Feed in arbitrary chunks of data



**Signature:** (self, raw)





**Return Value:** None

[Back to Top](#module-overview)


## \_cleanup\_stack
No description



**Signature:** (self)





**Return Value:** None

[Back to Top](#module-overview)


## \_consume\_block
No description



**Signature:** (self)





**Return Value:** None

[Back to Top](#module-overview)


## \_create\_alpha\_context
No description



**Signature:** (self, tag)





**Return Value:** None

[Back to Top](#module-overview)


## \_create\_beta\_context
No description



**Signature:** (self, tag)





**Return Value:** None

[Back to Top](#module-overview)


## \_create\_context
No description



**Signature:** (self, tag)





**Return Value:** None

[Back to Top](#module-overview)


## \_get\_context
No description



**Signature:** (self)





**Return Value:** None

[Back to Top](#module-overview)


## \_interpret
No description



**Signature:** (self, tag, payload)





**Return Value:** None

[Back to Top](#module-overview)


## \_process
No description



**Signature:** (self, tag, payload)





**Return Value:** None

[Back to Top](#module-overview)


## \_remove\_block
No description



**Signature:** (self)





**Return Value:** None

[Back to Top](#module-overview)


## \_remove\_context
No description



**Signature:** (self)





**Return Value:** None

[Back to Top](#module-overview)


## \_unpack\_bin
No description



**Signature:** (self, tag, payload=None)





**Return Value:** None

[Back to Top](#module-overview)


## \_unpack\_bin\_int
No description



**Signature:** (self, tag, payload\_list=None)





**Return Value:** None

[Back to Top](#module-overview)


## \_unpack\_bool
No description



**Signature:** (self, tag, payload=None)





**Return Value:** None

[Back to Top](#module-overview)


## \_unpack\_comment
No description



**Signature:** (self, tag, payload=None)





**Return Value:** None

[Back to Top](#module-overview)


## \_unpack\_comment\_id
No description



**Signature:** (self, tag, payload=None)





**Return Value:** None

[Back to Top](#module-overview)


## \_unpack\_complex
No description



**Signature:** (self, tag, payload\_list=None)





**Return Value:** None

[Back to Top](#module-overview)


## \_unpack\_date
No description



**Signature:** (self, tag, payload\_list=None)





**Return Value:** None

[Back to Top](#module-overview)


## \_unpack\_datetime
No description



**Signature:** (self, tag, payload\_list=None)





**Return Value:** None

[Back to Top](#module-overview)


## \_unpack\_float
No description



**Signature:** (self, tag, payload\_list=None)





**Return Value:** None

[Back to Top](#module-overview)


## \_unpack\_float\_misc
No description



**Signature:** (self, tag, payload=None)





**Return Value:** None

[Back to Top](#module-overview)


## \_unpack\_grid
No description



**Signature:** (self, tag, payload\_list=None)





**Return Value:** None

[Back to Top](#module-overview)


## \_unpack\_hex\_int
No description



**Signature:** (self, tag, payload\_list=None)





**Return Value:** None

[Back to Top](#module-overview)


## \_unpack\_int
No description



**Signature:** (self, tag, payload=None)





**Return Value:** None

[Back to Top](#module-overview)


## \_unpack\_null
No description



**Signature:** (self, tag, payload=None)





**Return Value:** None

[Back to Top](#module-overview)


## \_unpack\_obj
No description



**Signature:** (self, tag, payload\_obj=None)





**Return Value:** None

[Back to Top](#module-overview)


## \_unpack\_oct\_int
No description



**Signature:** (self, tag, payload\_list=None)





**Return Value:** None

[Back to Top](#module-overview)


## \_unpack\_payload
No description



**Signature:** (self, tag, payload=None)





**Return Value:** None

[Back to Top](#module-overview)


## \_unpack\_raw
No description



**Signature:** (self, tag, payload=None)





**Return Value:** None

[Back to Top](#module-overview)


## \_unpack\_str
No description



**Signature:** (self, tag, payload=None)





**Return Value:** None

[Back to Top](#module-overview)


## \_unpack\_time
No description



**Signature:** (self, tag, payload\_list=None)





**Return Value:** None

[Back to Top](#module-overview)


## \_update\_context
No description



**Signature:** (self, data)





**Return Value:** None

[Back to Top](#module-overview)


## \_update\_flags
No description



**Signature:** (self, tag)





**Return Value:** None

[Back to Top](#module-overview)



