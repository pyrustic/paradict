Back to [All Modules](https://github.com/pyrustic/paradict/blob/master/docs/modules/README.md#readme)

# Module Overview

**paradict**
 
No description

> **Classes:** &nbsp; [ConfigFile](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/classes/ConfigFile.md#class-configfile) &nbsp;&nbsp; [Decoder](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/classes/Decoder.md#class-decoder) &nbsp;&nbsp; [Document](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/classes/Document.md#class-document) &nbsp;&nbsp; [Encoder](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/classes/Encoder.md#class-encoder) &nbsp;&nbsp; [FileDoc](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/classes/FileDoc.md#class-filedoc) &nbsp;&nbsp; [Packer](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/classes/Packer.md#class-packer) &nbsp;&nbsp; [TypeRef](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/classes/TypeRef.md#class-typeref) &nbsp;&nbsp; [Unpacker](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/classes/Unpacker.md#class-unpacker) &nbsp;&nbsp; [Validator](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/classes/Validator.md#class-validator)
>
> **Functions:** &nbsp; [decode](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/functions.md#decode) &nbsp;&nbsp; [dump](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/functions.md#dump) &nbsp;&nbsp; [encode](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/functions.md#encode) &nbsp;&nbsp; [forge\_bin](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/functions.md#forge_bin) &nbsp;&nbsp; [load](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/functions.md#load) &nbsp;&nbsp; [pack](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/functions.md#pack) &nbsp;&nbsp; [split\_kv](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/functions.md#split_kv) &nbsp;&nbsp; [stringify\_bin](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/functions.md#stringify_bin) &nbsp;&nbsp; [unpack](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/functions.md#unpack) &nbsp;&nbsp; [validate](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/functions.md#validate)
>
> **Constants:** &nbsp; None

# Class Validator
Class to validate data against a schema

## Base Classes
object

## Class Attributes
No class attributes.

## Class Properties
|Property|Type|Description|Inherited from|
|---|---|---|---|
|schema|getter|None||
|type_ref|getter|None||



# All Methods
[\_\_init\_\_](#__init__) &nbsp;&nbsp; [validate](#validate) &nbsp;&nbsp; [\_ensure\_spec](#_ensure_spec) &nbsp;&nbsp; [\_validate](#_validate) &nbsp;&nbsp; [\_validate\_datatype](#_validate_datatype) &nbsp;&nbsp; [\_validate\_dict](#_validate_dict) &nbsp;&nbsp; [\_validate\_list](#_validate_list) &nbsp;&nbsp; [\_validate\_obj](#_validate_obj) &nbsp;&nbsp; [\_validate\_set](#_validate_set)

## \_\_init\_\_
No description



**Signature:** (self, schema, type\_ref=None)

|Parameter|Description|
|---|---|
|schema|the schema|
|type\_ref|optional TypeRef instance|





**Return Value:** None

[Back to Top](#module-overview)


## validate
Validate data, then return a boolean



**Signature:** (self, data)





**Return Value:** None

[Back to Top](#module-overview)


## \_ensure\_spec
No description



**Signature:** (self, target, spec)





**Return Value:** None

[Back to Top](#module-overview)


## \_validate
No description



**Signature:** (self, target, schema)





**Return Value:** None

[Back to Top](#module-overview)


## \_validate\_datatype
No description



**Signature:** (self, target, datatype)





**Return Value:** None

[Back to Top](#module-overview)


## \_validate\_dict
No description



**Signature:** (self, target, schema)





**Return Value:** None

[Back to Top](#module-overview)


## \_validate\_list
Schema SHOULD be a list



**Signature:** (self, target, schema)





**Return Value:** None

[Back to Top](#module-overview)


## \_validate\_obj
No description



**Signature:** (self, target, schema)





**Return Value:** None

[Back to Top](#module-overview)


## \_validate\_set
Schema SHOULD be a set



**Signature:** (self, target, schema)





**Return Value:** None

[Back to Top](#module-overview)



