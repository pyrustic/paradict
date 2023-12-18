Back to [All Modules](https://github.com/pyrustic/paradict/blob/master/docs/modules/README.md#readme)

# Module Overview

**paradict.queue.bin\_queue**
 
A FIFO queue for processing binary Paradict data

> **Classes:** &nbsp; [BinQueue](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.queue.bin_queue/content/classes/BinQueue.md#class-binqueue) &nbsp;&nbsp; [Datum](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.queue.bin_queue/content/classes/Datum.md#class-datum)
>
> **Functions:** &nbsp; [extract\_datum](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.queue.bin_queue/content/functions.md#extract_datum) &nbsp;&nbsp; [read\_bin](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.queue.bin_queue/content/functions.md#read_bin) &nbsp;&nbsp; [read\_nint\_big](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.queue.bin_queue/content/functions.md#read_nint_big) &nbsp;&nbsp; [read\_nint\_heavy](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.queue.bin_queue/content/functions.md#read_nint_heavy) &nbsp;&nbsp; [read\_nintx](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.queue.bin_queue/content/functions.md#read_nintx) &nbsp;&nbsp; [read\_payload\_size](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.queue.bin_queue/content/functions.md#read_payload_size) &nbsp;&nbsp; [read\_pint\_big](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.queue.bin_queue/content/functions.md#read_pint_big) &nbsp;&nbsp; [read\_pint\_heavy](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.queue.bin_queue/content/functions.md#read_pint_heavy) &nbsp;&nbsp; [read\_pintx](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.queue.bin_queue/content/functions.md#read_pintx) &nbsp;&nbsp; [read\_str](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.queue.bin_queue/content/functions.md#read_str) &nbsp;&nbsp; [read\_strx](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.queue.bin_queue/content/functions.md#read_strx) &nbsp;&nbsp; [read\_tag](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.queue.bin_queue/content/functions.md#read_tag)
>
> **Constants:** &nbsp; SIZE_TO_STR

# Class Datum
Datum(tag, payload, width)

## Base Classes
tuple

## Class Attributes
\_field\_defaults &nbsp;&nbsp; \_fields &nbsp;&nbsp; \_fields\_defaults &nbsp;&nbsp; \_make &nbsp;&nbsp; payload &nbsp;&nbsp; tag &nbsp;&nbsp; width

## Class Properties


# All Methods
[count](#count) &nbsp;&nbsp; [index](#index) &nbsp;&nbsp; [\_asdict](#_asdict) &nbsp;&nbsp; [\_replace](#_replace)

## count
Return number of occurrences of value.

**Inherited from:** tuple

**Signature:** (self, value, /)





**Return Value:** None

[Back to Top](#module-overview)


## index
Return first index of value.

Raises ValueError if the value is not present.

**Inherited from:** tuple

**Signature:** (self, value, start=0, stop=9223372036854775807, /)





**Return Value:** None

[Back to Top](#module-overview)


## \_asdict
Return a new dict which maps field names to their values.



**Signature:** (self)





**Return Value:** None

[Back to Top](#module-overview)


## \_replace
Return a new Datum object replacing specified fields with new values



**Signature:** (self, /, \*\*kwds)





**Return Value:** None

[Back to Top](#module-overview)



