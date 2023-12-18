Back to [All Modules](https://github.com/pyrustic/paradict/blob/master/docs/modules/README.md#readme)

# Module Overview

**paradict.configfile**
 
ConfigFile class for creating model for Paradict configuration file

> **Classes:** &nbsp; [ConfigFile](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.configfile/content/classes/ConfigFile.md#class-configfile)
>
> **Functions:** &nbsp; None
>
> **Constants:** &nbsp; None

# Class ConfigFile
A configfile is based on FileDoc, itself based on Document.
The difference between FileDoc and Document is that
FileDoc implies a physical file.
ConfigFile is a FileDoc but only for configuration file.
Its encoding_mode is const.CONFIG_MODE

## Base Classes
paradict.filedoc.FileDoc

## Class Attributes
No class attributes.

## Class Properties
|Property|Type|Description|Inherited from|
|---|---|---|---|
|encoding_mode|getter|None|paradict.document.Document|
|obj_builder|getter|None|paradict.document.Document|
|obj_builder|setter|None|paradict.document.Document|
|path|getter|None|paradict.filedoc.FileDoc|
|schema|getter|None|paradict.document.Document|
|schema|setter|None|paradict.document.Document|
|spacing|getter|None|paradict.document.Document|
|spacing|setter|None|paradict.document.Document|
|type_ref|getter|None|paradict.document.Document|
|type_ref|setter|None|paradict.document.Document|



# All Methods
[\_\_init\_\_](#__init__) &nbsp;&nbsp; [check](#check) &nbsp;&nbsp; [clear](#clear) &nbsp;&nbsp; [get](#get) &nbsp;&nbsp; [load](#load) &nbsp;&nbsp; [load\_from](#load_from) &nbsp;&nbsp; [load\_schema](#load_schema) &nbsp;&nbsp; [remove](#remove) &nbsp;&nbsp; [render](#render) &nbsp;&nbsp; [save](#save) &nbsp;&nbsp; [save\_to](#save_to) &nbsp;&nbsp; [set](#set) &nbsp;&nbsp; [update](#update) &nbsp;&nbsp; [validate](#validate) &nbsp;&nbsp; [\_ensure\_sections](#_ensure_sections)

## \_\_init\_\_
Init



**Signature:** (self, path, \*, schema=None, type\_ref=None, obj\_builder=None, spacing=1)

|Parameter|Description|
|---|---|
|path|path string or a pathlib.Path instance|
|schema|a Python dict that serves as schema to validate the sections of the document. It is a dictionary of dictionaries, with root keys representing a section header.|
|type\_ref|optional TypeRef object|
|obj\_builder|function that accepts a paradict.box.Obj container and returns a fresh new Python object|
|spacing|number of blank lines to place between two adjacent sections|





**Return Value:** None

[Back to Top](#module-overview)


## check
Return the ordered list (a 'tuple' to be precise)
of section's headers (strings)

**Inherited from:** paradict.filedoc.FileDoc

**Signature:** (self)





**Return Value:** None

[Back to Top](#module-overview)


## clear
clear the document (as well the model as the linked file's contents

**Inherited from:** paradict.filedoc.FileDoc

**Signature:** (self)





**Return Value:** None

[Back to Top](#module-overview)


## get
Decode and return the section whose header is provided

**Inherited from:** paradict.filedoc.FileDoc

**Signature:** (self, header, skip\_comments=True)

|Parameter|Description|
|---|---|
|header|the string header of the section|
|skip\_comments|boolean to tell whether comments should be ignored or not|





**Return Value:** None

[Back to Top](#module-overview)


## load
load the document from the linked file

**Inherited from:** paradict.filedoc.FileDoc

**Signature:** (self)





**Return Value:** None

[Back to Top](#module-overview)


## load\_from
Load the document from a file by providing
a path string or pathlib.Path object

**Inherited from:** paradict.document.Document

**Signature:** (self, path)





**Return Value:** None

[Back to Top](#module-overview)


## load\_schema
Load a schema file

**Inherited from:** paradict.document.Document

**Signature:** (self, src)

|Parameter|Description|
|---|---|
|src|either a path, a pathlib.Path object, or a file like object|





**Return Value:** None

[Back to Top](#module-overview)


## remove
remove specific sections from both the document model and the linked file

**Inherited from:** paradict.filedoc.FileDoc

**Signature:** (self, \*headers)





**Return Value:** None

[Back to Top](#module-overview)


## render
Render the entire document or a specific set of sections, i.e.,
return a textual Paradict string that may be stored in a file.

**Inherited from:** paradict.filedoc.FileDoc

**Signature:** (self, \*headers)

|Parameter|Description|
|---|---|
|\*headers|Headers of sections to render. Omitting this will render the entire document|





**Return Value:** Returns a string that contains sections (each made of square-brackets delimited header
and the associated body)

[Back to Top](#module-overview)


## save
Save the document in the linked file. Return a confirmation bool

**Inherited from:** paradict.filedoc.FileDoc

**Signature:** (self)





**Return Value:** None

[Back to Top](#module-overview)


## save\_to
Save the document to a new file.
Here, path is either a path string
or a pathlib.Path object

**Inherited from:** paradict.filedoc.FileDoc

**Signature:** (self, path)





**Return Value:** None

[Back to Top](#module-overview)


## set
Encode and set a new section.
Note that this operation will edit the linked file.
Also note that the update method is suited for
multiple 'set' operations

**Inherited from:** paradict.filedoc.FileDoc

**Signature:** (self, header, body=None)

|Parameter|Description|
|---|---|
|body|Python dictionary representing the data to encode|
|header|the string header of the section|





**Return Value:** None

[Back to Top](#module-overview)


## update
Encode and set new sections.
Note that this operation will edit the linked file.

**Inherited from:** paradict.filedoc.FileDoc

**Signature:** (self, \*sections)

|Parameter|Description|
|---|---|
|\*sections|A section is a 2-tuple: (header, body)|





**Return Value:** None

[Back to Top](#module-overview)


## validate
Validate this entire document or only specific section(s)

**Inherited from:** paradict.document.Document

**Signature:** (self, \*headers)

|Parameter|Description|
|---|---|
|\*headers|headers to validate. If you ignore this parameter, the document will be checked against the schema.|





**Return Value:** Return true if the document is valid. Raise an exception if the schema is missing

[Back to Top](#module-overview)


## \_ensure\_sections
No description

**Inherited from:** paradict.filedoc.FileDoc

**Signature:** (self)





**Return Value:** None

[Back to Top](#module-overview)



