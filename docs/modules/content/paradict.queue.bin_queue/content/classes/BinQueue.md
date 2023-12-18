Back to [All Modules](https://github.com/pyrustic/paradict/blob/master/docs/modules/README.md#readme)

# Module Overview

**paradict.queue.bin\_queue**
 
A FIFO queue for processing binary Paradict data

> **Classes:** &nbsp; [BinQueue](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.queue.bin_queue/content/classes/BinQueue.md#class-binqueue) &nbsp;&nbsp; [Datum](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.queue.bin_queue/content/classes/Datum.md#class-datum)
>
> **Functions:** &nbsp; [extract\_datum](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.queue.bin_queue/content/functions.md#extract_datum) &nbsp;&nbsp; [read\_bin](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.queue.bin_queue/content/functions.md#read_bin) &nbsp;&nbsp; [read\_nint\_big](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.queue.bin_queue/content/functions.md#read_nint_big) &nbsp;&nbsp; [read\_nint\_heavy](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.queue.bin_queue/content/functions.md#read_nint_heavy) &nbsp;&nbsp; [read\_nintx](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.queue.bin_queue/content/functions.md#read_nintx) &nbsp;&nbsp; [read\_payload\_size](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.queue.bin_queue/content/functions.md#read_payload_size) &nbsp;&nbsp; [read\_pint\_big](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.queue.bin_queue/content/functions.md#read_pint_big) &nbsp;&nbsp; [read\_pint\_heavy](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.queue.bin_queue/content/functions.md#read_pint_heavy) &nbsp;&nbsp; [read\_pintx](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.queue.bin_queue/content/functions.md#read_pintx) &nbsp;&nbsp; [read\_str](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.queue.bin_queue/content/functions.md#read_str) &nbsp;&nbsp; [read\_strx](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.queue.bin_queue/content/functions.md#read_strx) &nbsp;&nbsp; [read\_tag](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.queue.bin_queue/content/functions.md#read_tag)
>
> **Constants:** &nbsp; SIZE_TO_STR

# Class BinQueue
A FIFO queue for processing binary Paradict data

## Base Classes
object

## Class Attributes
No class attributes.

## Class Properties
|Property|Type|Description|Inherited from|
|---|---|---|---|
|buffer|getter|None||



# All Methods
[\_\_init\_\_](#__init__) &nbsp;&nbsp; [get](#get) &nbsp;&nbsp; [put](#put) &nbsp;&nbsp; [\_clear\_status](#_clear_status) &nbsp;&nbsp; [\_read](#_read) &nbsp;&nbsp; [\_read\_buffer](#_read_buffer) &nbsp;&nbsp; [\_update\_expected\_width\_var](#_update_expected_width_var) &nbsp;&nbsp; [\_update\_tag\_var](#_update_tag_var)

## \_\_init\_\_
Initialize self.  See help(type(self)) for accurate signature.



**Signature:** (self)





**Return Value:** None

[Back to Top](#module-overview)


## get
Generator for iteratively getting each tag-payload tuple composing the
raw data stored in the buffer



**Signature:** (self)





**Return Value:** None

[Back to Top](#module-overview)


## put
Store binary data in the buffer. This data will then be iteratively
extracted by the 'get' method



**Signature:** (self, raw)





**Return Value:** None

[Back to Top](#module-overview)


## \_clear\_status
No description



**Signature:** (self)





**Return Value:** None

[Back to Top](#module-overview)


## \_read
No description



**Signature:** (self)





**Return Value:** None

[Back to Top](#module-overview)


## \_read\_buffer
No description



**Signature:** (self, reader)





**Return Value:** None

[Back to Top](#module-overview)


## \_update\_expected\_width\_var
No description



**Signature:** (self)





**Return Value:** None

[Back to Top](#module-overview)


## \_update\_tag\_var
No description



**Signature:** (self)





**Return Value:** None

[Back to Top](#module-overview)



