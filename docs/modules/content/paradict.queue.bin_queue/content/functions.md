Back to [All Modules](https://github.com/pyrustic/paradict/blob/master/docs/modules/README.md#readme)

# Module Overview

**paradict.queue.bin\_queue**
 
A FIFO queue for processing binary Paradict data

> **Classes:** &nbsp; [BinQueue](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.queue.bin_queue/content/classes/BinQueue.md#class-binqueue) &nbsp;&nbsp; [Datum](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.queue.bin_queue/content/classes/Datum.md#class-datum)
>
> **Functions:** &nbsp; [extract\_datum](#extract_datum) &nbsp;&nbsp; [read\_bin](#read_bin) &nbsp;&nbsp; [read\_nint\_big](#read_nint_big) &nbsp;&nbsp; [read\_nint\_heavy](#read_nint_heavy) &nbsp;&nbsp; [read\_nintx](#read_nintx) &nbsp;&nbsp; [read\_payload\_size](#read_payload_size) &nbsp;&nbsp; [read\_pint\_big](#read_pint_big) &nbsp;&nbsp; [read\_pint\_heavy](#read_pint_heavy) &nbsp;&nbsp; [read\_pintx](#read_pintx) &nbsp;&nbsp; [read\_str](#read_str) &nbsp;&nbsp; [read\_strx](#read_strx) &nbsp;&nbsp; [read\_tag](#read_tag)
>
> **Constants:** &nbsp; SIZE_TO_STR

# All Functions
[extract\_datum](#extract_datum) &nbsp;&nbsp; [read\_bin](#read_bin) &nbsp;&nbsp; [read\_nint\_big](#read_nint_big) &nbsp;&nbsp; [read\_nint\_heavy](#read_nint_heavy) &nbsp;&nbsp; [read\_nintx](#read_nintx) &nbsp;&nbsp; [read\_payload\_size](#read_payload_size) &nbsp;&nbsp; [read\_pint\_big](#read_pint_big) &nbsp;&nbsp; [read\_pint\_heavy](#read_pint_heavy) &nbsp;&nbsp; [read\_pintx](#read_pintx) &nbsp;&nbsp; [read\_str](#read_str) &nbsp;&nbsp; [read\_strx](#read_strx) &nbsp;&nbsp; [read\_tag](#read_tag)

## extract\_datum
This function is used read STR_SHORT, STR_MEDIUM, STR_LONG,
 STR_HEAVY, BIN_SHORT, BIN_MEDIUM, BIN_LONG and BIN_HEAVY datums.

nb is the number of bytes to encode the size of payload

This function returns a Datum



**Signature:** (buffer, tag, nb=1)





**Return Value:** None

[Back to Top](#module-overview)


## read\_bin
No description



**Signature:** (tag, buffer)





**Return Value:** None

[Back to Top](#module-overview)


## read\_nint\_big
No description



**Signature:** (tag, buffer)





**Return Value:** None

[Back to Top](#module-overview)


## read\_nint\_heavy
No description



**Signature:** (tag, buffer)





**Return Value:** None

[Back to Top](#module-overview)


## read\_nintx
No description



**Signature:** (tag, buffer)





**Return Value:** None

[Back to Top](#module-overview)


## read\_payload\_size
Read the expected size of payload
Note that nb is the number of bytes encoding the size of payload



**Signature:** (buffer, nb=1, offset=1)





**Return Value:** None

[Back to Top](#module-overview)


## read\_pint\_big
No description



**Signature:** (tag, buffer)





**Return Value:** None

[Back to Top](#module-overview)


## read\_pint\_heavy
No description



**Signature:** (tag, buffer)





**Return Value:** None

[Back to Top](#module-overview)


## read\_pintx
No description



**Signature:** (tag, buffer)





**Return Value:** None

[Back to Top](#module-overview)


## read\_str
No description



**Signature:** (tag, buffer)





**Return Value:** None

[Back to Top](#module-overview)


## read\_strx
No description



**Signature:** (tag, buffer)





**Return Value:** None

[Back to Top](#module-overview)


## read\_tag
No description



**Signature:** (tag, buffer)





**Return Value:** None

[Back to Top](#module-overview)


