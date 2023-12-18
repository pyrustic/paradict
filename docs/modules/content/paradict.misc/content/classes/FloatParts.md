Back to [All Modules](https://github.com/pyrustic/paradict/blob/master/docs/modules/README.md#readme)

# Module Overview

**paradict.misc**
 
Private miscellaneous functions and classes. Do not use them !

> **Classes:** &nbsp; [FloatParts](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.misc/content/classes/FloatParts.md#class-floatparts) &nbsp;&nbsp; [IntParts](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.misc/content/classes/IntParts.md#class-intparts)
>
> **Functions:** &nbsp; [\_count\_leading\_zeros](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.misc/content/functions.md#_count_leading_zeros) &nbsp;&nbsp; [\_parse\_significand](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.misc/content/functions.md#_parse_significand) &nbsp;&nbsp; [\_prepare\_float](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.misc/content/functions.md#_prepare_float) &nbsp;&nbsp; [\_tidy\_up\_right\_significand](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.misc/content/functions.md#_tidy_up_right_significand) &nbsp;&nbsp; [add\_leading\_zeros](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.misc/content/functions.md#add_leading_zeros) &nbsp;&nbsp; [calc\_uint\_bytes](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.misc/content/functions.md#calc_uint_bytes) &nbsp;&nbsp; [construct\_date](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.misc/content/functions.md#construct_date) &nbsp;&nbsp; [construct\_datetime](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.misc/content/functions.md#construct_datetime) &nbsp;&nbsp; [construct\_time](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.misc/content/functions.md#construct_time) &nbsp;&nbsp; [count\_indents](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.misc/content/functions.md#count_indents) &nbsp;&nbsp; [count\_leading\_zeros](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.misc/content/functions.md#count_leading_zeros) &nbsp;&nbsp; [decode\_unicode](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.misc/content/functions.md#decode_unicode) &nbsp;&nbsp; [deconstruct\_date](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.misc/content/functions.md#deconstruct_date) &nbsp;&nbsp; [deconstruct\_datetime](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.misc/content/functions.md#deconstruct_datetime) &nbsp;&nbsp; [deconstruct\_time](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.misc/content/functions.md#deconstruct_time) &nbsp;&nbsp; [dedent](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.misc/content/functions.md#dedent) &nbsp;&nbsp; [encode\_unicode](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.misc/content/functions.md#encode_unicode) &nbsp;&nbsp; [forge\_bin](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.misc/content/functions.md#forge_bin) &nbsp;&nbsp; [get\_int\_base](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.misc/content/functions.md#get_int_base) &nbsp;&nbsp; [is\_whole\_number](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.misc/content/functions.md#is_whole_number) &nbsp;&nbsp; [left\_pad\_int](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.misc/content/functions.md#left_pad_int) &nbsp;&nbsp; [make\_indent\_str](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.misc/content/functions.md#make_indent_str) &nbsp;&nbsp; [prettify\_b16](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.misc/content/functions.md#prettify_b16) &nbsp;&nbsp; [prettify\_grid](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.misc/content/functions.md#prettify_grid) &nbsp;&nbsp; [split\_float](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.misc/content/functions.md#split_float) &nbsp;&nbsp; [split\_int](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.misc/content/functions.md#split_int) &nbsp;&nbsp; [stringify\_bin](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.misc/content/functions.md#stringify_bin) &nbsp;&nbsp; [strip\_block\_extra\_space](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.misc/content/functions.md#strip_block_extra_space) &nbsp;&nbsp; [tidy\_up\_float](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.misc/content/functions.md#tidy_up_float) &nbsp;&nbsp; [tidy\_up\_int](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.misc/content/functions.md#tidy_up_int)
>
> **Constants:** &nbsp; None

# Class FloatParts
FloatParts(sign, left_significand, right_significand, exponent)

## Base Classes
tuple

## Class Attributes
\_field\_defaults &nbsp;&nbsp; \_fields &nbsp;&nbsp; \_fields\_defaults &nbsp;&nbsp; \_make &nbsp;&nbsp; exponent &nbsp;&nbsp; left\_significand &nbsp;&nbsp; right\_significand &nbsp;&nbsp; sign

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
Return a new FloatParts object replacing specified fields with new values



**Signature:** (self, /, \*\*kwds)





**Return Value:** None

[Back to Top](#module-overview)



