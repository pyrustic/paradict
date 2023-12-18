Back to [All Modules](https://github.com/pyrustic/paradict/blob/master/docs/modules/README.md#readme)

# Module Overview

**paradict**
 
No description

> **Classes:** &nbsp; [ConfigFile](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/classes/ConfigFile.md#class-configfile) &nbsp;&nbsp; [Decoder](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/classes/Decoder.md#class-decoder) &nbsp;&nbsp; [Document](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/classes/Document.md#class-document) &nbsp;&nbsp; [Encoder](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/classes/Encoder.md#class-encoder) &nbsp;&nbsp; [FileDoc](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/classes/FileDoc.md#class-filedoc) &nbsp;&nbsp; [Packer](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/classes/Packer.md#class-packer) &nbsp;&nbsp; [TypeRef](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/classes/TypeRef.md#class-typeref) &nbsp;&nbsp; [Unpacker](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/classes/Unpacker.md#class-unpacker) &nbsp;&nbsp; [Validator](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/classes/Validator.md#class-validator)
>
> **Functions:** &nbsp; [decode](#decode) &nbsp;&nbsp; [dump](#dump) &nbsp;&nbsp; [encode](#encode) &nbsp;&nbsp; [forge\_bin](#forge_bin) &nbsp;&nbsp; [load](#load) &nbsp;&nbsp; [pack](#pack) &nbsp;&nbsp; [split\_kv](#split_kv) &nbsp;&nbsp; [stringify\_bin](#stringify_bin) &nbsp;&nbsp; [unpack](#unpack) &nbsp;&nbsp; [validate](#validate)
>
> **Constants:** &nbsp; None

# All Functions
[decode](#decode) &nbsp;&nbsp; [dump](#dump) &nbsp;&nbsp; [encode](#encode) &nbsp;&nbsp; [forge\_bin](#forge_bin) &nbsp;&nbsp; [load](#load) &nbsp;&nbsp; [pack](#pack) &nbsp;&nbsp; [split\_kv](#split_kv) &nbsp;&nbsp; [stringify\_bin](#stringify_bin) &nbsp;&nbsp; [unpack](#unpack) &nbsp;&nbsp; [validate](#validate)

## decode
Convert some textual Paradict data into a Python dictionary



**Signature:** (text, type\_ref=None, receiver=None, obj\_builder=None, skip\_comments=False)

|Parameter|Description|
|---|---|
|text|string to convert into a Python dict|
|type\_ref|optional TypeRef object|
|receiver|callback function that will be called at the end of conversion. This callback function accepts the Decoder instance as argument|
|obj\_builder|function that accepts a paradict.box.Obj container and returns a fresh new Python object|
|skip\_comments|boolean to tell whether comments should be ignored or not|





**Return Value:** Return the newly built Python object

[Back to Top](#module-overview)


## dump
Convert some Python dict in the Paradict binary format
then dump it in a file



**Signature:** (data, path, \*, type\_ref=None, skip\_comments=False)

|Parameter|Description|
|---|---|
|path|path string or pathlib.Path instance|
|type\_ref|optional TypeRef object|
|skip\_comments|boolean to tell whether comments should be ignored or not|





**Return Value:** None

[Back to Top](#module-overview)


## encode
Convert a Python dictionary object to Paradict binary format



**Signature:** (data, \*, mode=1, type\_ref=None, skip\_comments=False, skip\_bin\_data=False)

|Parameter|Description|
|---|---|
|data|Python dict|
|mode|either const.DATA_MODE or const.CONFIG_MODE. Defaults to DATA_MODE.|
|type\_ref|optional TypeRef object|
|skip\_comments|boolean to tell whether comments should be ignored or not|
|skip\_bin\_data|boolean to tell whether bin data should be ignored or not|





**Return Value:** Return a string in the Paradict text format

[Back to Top](#module-overview)


## forge\_bin
items are int, bytes, bytearrays, or Nones, returns a bytearray



**Signature:** (\*items)





**Return Value:** None

[Back to Top](#module-overview)


## load
Open a binary Paradict file then unpack its contents into Python dict



**Signature:** (path, type\_ref=None, obj\_builder=None, skip\_comments=False)

|Parameter|Description|
|---|---|
|path|a path string, or a pathlib.Path instance|
|type\_ref|optional TypeRef object|
|receiver|callback function that will be called at the end of conversion. This callback function accepts the Decoder instance as argument|
|obj\_builder|function that accepts a paradict.box.Obj container and returns a fresh new Python object|
|skip\_comments|boolean to tell whether comments should be ignored or not|





**Return Value:** Return the newly built Python object

[Back to Top](#module-overview)


## pack
Convert a Python dictionary object to Paradict binary format



**Signature:** (data, \*, type\_ref=None, skip\_comments=False)

|Parameter|Description|
|---|---|
|data|Python dict|
|type\_ref|optional TypeRef object|
|skip\_comments|boolean to tell whether comments should be ignored or not|





**Return Value:** Return a Python bytes object packed in the Paradict binary format

[Back to Top](#module-overview)


## split\_kv
Split a non-empty string into key val.
The string should follow one of these format:
- data_mode format: key: value
- config_mode format: key = value



**Signature:** (val)

|Parameter|Description|
|---|---|
|val|non-empty string|





**Return Value:** Return an Info namedtuple made of: key, val, sep, and mode attributes.
The key and val are strings. The sep is either ":" or "=".
The mode is either paradict.const.DATA_MODE or paradict.const.CONFIG_MODE.
Note that if the sep is a colon, it means that the mode is DATA_MODE.

[Back to Top](#module-overview)


## stringify\_bin
Good for debug. Stringify some binary data



**Signature:** (b, offset=0, width=None, spaced=False)





**Return Value:** None

[Back to Top](#module-overview)


## unpack
Convert some binary Paradict data into a Python dictionary



**Signature:** (raw, type\_ref=None, receiver=None, obj\_builder=None, skip\_comments=False)

|Parameter|Description|
|---|---|
|raw|raw data previously packed with Paradict|
|type\_ref|optional TypeRef object|
|receiver|callback function that will be called at the end of conversion. This callback function accepts the Decoder instance as argument|
|obj\_builder|function that accepts a paradict.box.Obj container and returns a fresh new Python object|
|skip\_comments|boolean to tell whether comments should be ignored or not|





**Return Value:** Return the newly built Python object

[Back to Top](#module-overview)


## validate
This function returns True if the given data
successfully validates against the given schema



**Signature:** (data, schema, type\_ref=None)

|Parameter|Description|
|---|---|
|data|some Python object (like a dict, a list, ...) that is part or include datatypes defined in VALID_DATATYPES.|
|schema|a valid schema. It might be a collection containing Spec instances and/or type-strings. The benefit of using Spec is that you can add a checker function that will serve as an extra programmatic validation.|
|type\_ref|optional TypeRef object|





**Return Value:** Returns True or False

[Back to Top](#module-overview)


