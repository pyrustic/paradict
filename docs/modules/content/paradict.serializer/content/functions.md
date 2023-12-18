Back to [All Modules](https://github.com/pyrustic/paradict/blob/master/docs/modules/README.md#readme)

# Module Overview

**paradict.serializer**
 
High-level functions to serialize Python dict in Paradict binary/text format

> **Classes:** &nbsp; None
>
> **Functions:** &nbsp; [dump](#dump) &nbsp;&nbsp; [encode](#encode) &nbsp;&nbsp; [pack](#pack)
>
> **Constants:** &nbsp; None

# All Functions
[dump](#dump) &nbsp;&nbsp; [encode](#encode) &nbsp;&nbsp; [pack](#pack)

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


