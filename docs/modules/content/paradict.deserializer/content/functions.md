Back to [All Modules](https://github.com/pyrustic/paradict/blob/master/docs/modules/README.md#readme)

# Module Overview

**paradict.deserializer**
 
High-level functions to deserialize Paradict binary/text data into a Python dict

> **Classes:** &nbsp; None
>
> **Functions:** &nbsp; [decode](#decode) &nbsp;&nbsp; [load](#load) &nbsp;&nbsp; [unpack](#unpack)
>
> **Constants:** &nbsp; None

# All Functions
[decode](#decode) &nbsp;&nbsp; [load](#load) &nbsp;&nbsp; [unpack](#unpack)

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


