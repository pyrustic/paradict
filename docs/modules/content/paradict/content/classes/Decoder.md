Back to [All Modules](https://github.com/pyrustic/paradict/blob/master/docs/modules/README.md#readme)

# Module Overview

**paradict**
 
No description

> **Classes:** &nbsp; [ConfigFile](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/classes/ConfigFile.md#class-configfile) &nbsp;&nbsp; [Decoder](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/classes/Decoder.md#class-decoder) &nbsp;&nbsp; [Document](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/classes/Document.md#class-document) &nbsp;&nbsp; [Encoder](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/classes/Encoder.md#class-encoder) &nbsp;&nbsp; [FileDoc](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/classes/FileDoc.md#class-filedoc) &nbsp;&nbsp; [Packer](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/classes/Packer.md#class-packer) &nbsp;&nbsp; [TypeRef](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/classes/TypeRef.md#class-typeref) &nbsp;&nbsp; [Unpacker](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/classes/Unpacker.md#class-unpacker) &nbsp;&nbsp; [Validator](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/classes/Validator.md#class-validator)
>
> **Functions:** &nbsp; [decode](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/functions.md#decode) &nbsp;&nbsp; [dump](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/functions.md#dump) &nbsp;&nbsp; [encode](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/functions.md#encode) &nbsp;&nbsp; [forge\_bin](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/functions.md#forge_bin) &nbsp;&nbsp; [load](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/functions.md#load) &nbsp;&nbsp; [pack](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/functions.md#pack) &nbsp;&nbsp; [split\_kv](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/functions.md#split_kv) &nbsp;&nbsp; [stringify\_bin](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/functions.md#stringify_bin) &nbsp;&nbsp; [unpack](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/functions.md#unpack) &nbsp;&nbsp; [validate](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/functions.md#validate)
>
> **Constants:** &nbsp; None

# Class Decoder
Class to convert some textual Paradict data into a Python dict

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
[\_\_init\_\_](#__init__) &nbsp;&nbsp; [feed](#feed) &nbsp;&nbsp; [\_add\_whitespace\_to\_parent\_context](#_add_whitespace_to_parent_context) &nbsp;&nbsp; [\_check\_key](#_check_key) &nbsp;&nbsp; [\_check\_line](#_check_line) &nbsp;&nbsp; [\_check\_multiline\_tag](#_check_multiline_tag) &nbsp;&nbsp; [\_cleanup\_stack](#_cleanup_stack) &nbsp;&nbsp; [\_consume\_bin\_block](#_consume_bin_block) &nbsp;&nbsp; [\_consume\_grid\_block](#_consume_grid_block) &nbsp;&nbsp; [\_consume\_obj\_block](#_consume_obj_block) &nbsp;&nbsp; [\_consume\_raw\_block](#_consume_raw_block) &nbsp;&nbsp; [\_consume\_str\_block](#_consume_str_block) &nbsp;&nbsp; [\_decode\_bin](#_decode_bin) &nbsp;&nbsp; [\_decode\_bool](#_decode_bool) &nbsp;&nbsp; [\_decode\_complex\_number](#_decode_complex_number) &nbsp;&nbsp; [\_decode\_container](#_decode_container) &nbsp;&nbsp; [\_decode\_date](#_decode_date) &nbsp;&nbsp; [\_decode\_datetime](#_decode_datetime) &nbsp;&nbsp; [\_decode\_float](#_decode_float) &nbsp;&nbsp; [\_decode\_int](#_decode_int) &nbsp;&nbsp; [\_decode\_null](#_decode_null) &nbsp;&nbsp; [\_decode\_str](#_decode_str) &nbsp;&nbsp; [\_decode\_time](#_decode_time) &nbsp;&nbsp; [\_decode\_value](#_decode_value) &nbsp;&nbsp; [\_get\_context](#_get_context) &nbsp;&nbsp; [\_get\_parent\_context](#_get_parent_context) &nbsp;&nbsp; [\_interpret](#_interpret) &nbsp;&nbsp; [\_process](#_process) &nbsp;&nbsp; [\_update\_context](#_update_context) &nbsp;&nbsp; [\_update\_dict\_container](#_update_dict_container) &nbsp;&nbsp; [\_update\_list\_container](#_update_list_container) &nbsp;&nbsp; [\_update\_obj\_container](#_update_obj_container) &nbsp;&nbsp; [\_update\_parent\_context](#_update_parent_context) &nbsp;&nbsp; [\_update\_set\_container](#_update_set_container) &nbsp;&nbsp; [\_update\_stack](#_update_stack)

## \_\_init\_\_
Init



**Signature:** (self, \*, type\_ref=None, receiver=None, obj\_builder=None, skip\_comments=False)

|Parameter|Description|
|---|---|
|type\_ref|optional TypeRef object|
|receiver|callback function that will be called at the end of conversion. This callback function accepts the Decoder instance as argument|
|obj\_builder|function that accepts a paradict.box.Obj container and returns a fresh new Python object|
|skip\_comments|boolean to tell whether comments should be ignored or not|





**Return Value:** None

[Back to Top](#module-overview)


## feed
        Feed the decoder engine with some string.
        The string might represent a line in the textual Paradict data,
        or an arbitrary length of characters.

        Note: it is very important to make sure that each line is ended
        by a "
" newline character

        Check the paradict.decode function to see an example of
        how to use this class



**Signature:** (self, s)





**Return Value:** None

[Back to Top](#module-overview)


## \_add\_whitespace\_to\_parent\_context
No description



**Signature:** (self, parent\_context)





**Return Value:** None

[Back to Top](#module-overview)


## \_check\_key
No description



**Signature:** (self, key, mode)





**Return Value:** None

[Back to Top](#module-overview)


## \_check\_line
Check the validity of the indent in the line
Returns the indent-less version of line



**Signature:** (self, line)





**Return Value:** None

[Back to Top](#module-overview)


## \_check\_multiline\_tag
No description



**Signature:** (self, value)





**Return Value:** None

[Back to Top](#module-overview)


## \_cleanup\_stack
No description



**Signature:** (self, indents)





**Return Value:** None

[Back to Top](#module-overview)


## \_consume\_bin\_block
No description



**Signature:** (self, parent\_context, context)





**Return Value:** None

[Back to Top](#module-overview)


## \_consume\_grid\_block
No description



**Signature:** (self, parent\_context, context)





**Return Value:** None

[Back to Top](#module-overview)


## \_consume\_obj\_block
No description



**Signature:** (self, parent\_context, context)





**Return Value:** None

[Back to Top](#module-overview)


## \_consume\_raw\_block
No description



**Signature:** (self, parent\_context, context)





**Return Value:** None

[Back to Top](#module-overview)


## \_consume\_str\_block
No description



**Signature:** (self, parent\_context, context)





**Return Value:** None

[Back to Top](#module-overview)


## \_decode\_bin
No description



**Signature:** (self, val)





**Return Value:** None

[Back to Top](#module-overview)


## \_decode\_bool
No description



**Signature:** (self, val)





**Return Value:** None

[Back to Top](#module-overview)


## \_decode\_complex\_number
No description



**Signature:** (self, val)





**Return Value:** None

[Back to Top](#module-overview)


## \_decode\_container
No description



**Signature:** (self, val)





**Return Value:** None

[Back to Top](#module-overview)


## \_decode\_date
No description



**Signature:** (self, val)





**Return Value:** None

[Back to Top](#module-overview)


## \_decode\_datetime
No description



**Signature:** (self, val)





**Return Value:** None

[Back to Top](#module-overview)


## \_decode\_float
No description



**Signature:** (self, val)





**Return Value:** None

[Back to Top](#module-overview)


## \_decode\_int
No description



**Signature:** (self, val)





**Return Value:** None

[Back to Top](#module-overview)


## \_decode\_null
No description



**Signature:** (self, val)





**Return Value:** None

[Back to Top](#module-overview)


## \_decode\_str
No description



**Signature:** (self, val)





**Return Value:** None

[Back to Top](#module-overview)


## \_decode\_time
No description



**Signature:** (self, val)





**Return Value:** None

[Back to Top](#module-overview)


## \_decode\_value
No description



**Signature:** (self, value)





**Return Value:** None

[Back to Top](#module-overview)


## \_get\_context
No description



**Signature:** (self)





**Return Value:** None

[Back to Top](#module-overview)


## \_get\_parent\_context
No description



**Signature:** (self)





**Return Value:** None

[Back to Top](#module-overview)


## \_interpret
No description



**Signature:** (self, line)





**Return Value:** None

[Back to Top](#module-overview)


## \_process
No description



**Signature:** (self, line)





**Return Value:** None

[Back to Top](#module-overview)


## \_update\_context
No description



**Signature:** (self, line)





**Return Value:** None

[Back to Top](#module-overview)


## \_update\_dict\_container
No description



**Signature:** (self, context, line)





**Return Value:** None

[Back to Top](#module-overview)


## \_update\_list\_container
No description



**Signature:** (self, context, line)





**Return Value:** None

[Back to Top](#module-overview)


## \_update\_obj\_container
No description



**Signature:** (self, context, line)





**Return Value:** None

[Back to Top](#module-overview)


## \_update\_parent\_context
No description



**Signature:** (self, parent\_context, data)





**Return Value:** None

[Back to Top](#module-overview)


## \_update\_set\_container
No description



**Signature:** (self, context, line)





**Return Value:** None

[Back to Top](#module-overview)


## \_update\_stack
No description



**Signature:** (self, container\_name, container, indents)





**Return Value:** None

[Back to Top](#module-overview)



