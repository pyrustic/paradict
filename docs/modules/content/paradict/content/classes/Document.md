Back to [All Modules](https://github.com/pyrustic/paradict/blob/master/docs/modules/README.md#readme)

# Module Overview

**paradict**
 
No description

> **Classes:** &nbsp; [ConfigFile](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/classes/ConfigFile.md#class-configfile) &nbsp;&nbsp; [Decoder](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/classes/Decoder.md#class-decoder) &nbsp;&nbsp; [Document](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/classes/Document.md#class-document) &nbsp;&nbsp; [Encoder](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/classes/Encoder.md#class-encoder) &nbsp;&nbsp; [FileDoc](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/classes/FileDoc.md#class-filedoc) &nbsp;&nbsp; [Packer](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/classes/Packer.md#class-packer) &nbsp;&nbsp; [TypeRef](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/classes/TypeRef.md#class-typeref) &nbsp;&nbsp; [Unpacker](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/classes/Unpacker.md#class-unpacker) &nbsp;&nbsp; [Validator](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/classes/Validator.md#class-validator)
>
> **Functions:** &nbsp; [decode](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/functions.md#decode) &nbsp;&nbsp; [dump](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/functions.md#dump) &nbsp;&nbsp; [encode](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/functions.md#encode) &nbsp;&nbsp; [forge\_bin](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/functions.md#forge_bin) &nbsp;&nbsp; [load](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/functions.md#load) &nbsp;&nbsp; [pack](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/functions.md#pack) &nbsp;&nbsp; [split\_kv](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/functions.md#split_kv) &nbsp;&nbsp; [stringify\_bin](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/functions.md#stringify_bin) &nbsp;&nbsp; [unpack](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/functions.md#unpack) &nbsp;&nbsp; [validate](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/functions.md#validate)
>
> **Constants:** &nbsp; None

# Class Document
Create a model for a textual Paradict Document made of sections.

## Base Classes
object

## Class Attributes
No class attributes.

## Class Properties
|Property|Type|Description|Inherited from|
|---|---|---|---|
|encoding_mode|getter|None||
|obj_builder|getter|None||
|obj_builder|setter|None||
|schema|getter|None||
|schema|setter|None||
|spacing|getter|None||
|spacing|setter|None||
|type_ref|getter|None||
|type_ref|setter|None||



# All Methods
[\_\_init\_\_](#__init__) &nbsp;&nbsp; [check](#check) &nbsp;&nbsp; [clear](#clear) &nbsp;&nbsp; [get](#get) &nbsp;&nbsp; [load\_from](#load_from) &nbsp;&nbsp; [load\_schema](#load_schema) &nbsp;&nbsp; [remove](#remove) &nbsp;&nbsp; [render](#render) &nbsp;&nbsp; [save\_to](#save_to) &nbsp;&nbsp; [set](#set) &nbsp;&nbsp; [validate](#validate)

## \_\_init\_\_
Init



**Signature:** (self, init\_text='', \*, schema=None, type\_ref=None, obj\_builder=None, spacing=1, encoding\_mode=1)

|Parameter|Description|
|---|---|
|init\_text|optional TypeRef object|
|schema|a Python dict that serves as schema to validate the sections of the document. It is a dictionary of dictionaries, with root keys representing a section header.|
|type\_ref|optional TypeRef object|
|obj\_builder|function that accepts a paradict.box.Obj container and returns a fresh new Python object|
|spacing|number of blank lines to place between two adjacent sections|
|encoding\_mode|either 1 or 2, to indicate if Python dicts should be encoded with the const.DATA_MODE or const.CONFIG_MODE. By default, a document's encoding mode is set to const.DATA_MODE|





**Return Value:** None

[Back to Top](#module-overview)


## check
Return the ordered list (a 'tuple' to be precise)
of section's headers (strings)



**Signature:** (self)





**Return Value:** None

[Back to Top](#module-overview)


## clear
Clear the entire document



**Signature:** (self)





**Return Value:** None

[Back to Top](#module-overview)


## get
Decode and return the section whose header is provided



**Signature:** (self, header, skip\_comments=True)

|Parameter|Description|
|---|---|
|header|the string header of the section|
|skip\_comments|boolean to tell whether comments should be ignored or not|





**Return Value:** None

[Back to Top](#module-overview)


## load\_from
Load the document from a file by providing
a path string or pathlib.Path object



**Signature:** (self, path)





**Return Value:** None

[Back to Top](#module-overview)


## load\_schema
Load a schema file



**Signature:** (self, src)

|Parameter|Description|
|---|---|
|src|either a path, a pathlib.Path object, or a file like object|





**Return Value:** None

[Back to Top](#module-overview)


## remove
Remove specific section(s) from this document



**Signature:** (self, \*headers)

|Parameter|Description|
|---|---|
|\*headers|the headers of the sections to remove|





**Return Value:** None

[Back to Top](#module-overview)


## render
Render the entire document or a specific set of sections, i.e.,
return a textual Paradict string that may be stored in a file.



**Signature:** (self, \*headers)

|Parameter|Description|
|---|---|
|\*headers|Headers of sections to render. Omitting this will render the entire document|





**Return Value:** Returns a string that contains sections (each made of square-brackets delimited header
and the associated body)

[Back to Top](#module-overview)


## save\_to
Save the contents of this document to a specific file



**Signature:** (self, path)

|Parameter|Description|
|---|---|
|path|path to filename. Path may be a pathlib.Path instance|





**Return Value:** None

[Back to Top](#module-overview)


## set
Encode and set a new section



**Signature:** (self, header, body=None)

|Parameter|Description|
|---|---|
|body|Python dictionary representing the data to encode|
|header|the string header of the section|





**Return Value:** None

[Back to Top](#module-overview)


## validate
Validate this entire document or only specific section(s)



**Signature:** (self, \*headers)

|Parameter|Description|
|---|---|
|\*headers|headers to validate. If you ignore this parameter, the document will be checked against the schema.|





**Return Value:** Return true if the document is valid. Raise an exception if the schema is missing

[Back to Top](#module-overview)



