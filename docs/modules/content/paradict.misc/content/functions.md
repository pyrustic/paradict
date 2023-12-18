Back to [All Modules](https://github.com/pyrustic/paradict/blob/master/docs/modules/README.md#readme)

# Module Overview

**paradict.misc**
 
Private miscellaneous functions and classes. Do not use them !

> **Classes:** &nbsp; [FloatParts](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.misc/content/classes/FloatParts.md#class-floatparts) &nbsp;&nbsp; [IntParts](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.misc/content/classes/IntParts.md#class-intparts)
>
> **Functions:** &nbsp; [\_count\_leading\_zeros](#_count_leading_zeros) &nbsp;&nbsp; [\_parse\_significand](#_parse_significand) &nbsp;&nbsp; [\_prepare\_float](#_prepare_float) &nbsp;&nbsp; [\_tidy\_up\_right\_significand](#_tidy_up_right_significand) &nbsp;&nbsp; [add\_leading\_zeros](#add_leading_zeros) &nbsp;&nbsp; [calc\_uint\_bytes](#calc_uint_bytes) &nbsp;&nbsp; [construct\_date](#construct_date) &nbsp;&nbsp; [construct\_datetime](#construct_datetime) &nbsp;&nbsp; [construct\_time](#construct_time) &nbsp;&nbsp; [count\_indents](#count_indents) &nbsp;&nbsp; [count\_leading\_zeros](#count_leading_zeros) &nbsp;&nbsp; [decode\_unicode](#decode_unicode) &nbsp;&nbsp; [deconstruct\_date](#deconstruct_date) &nbsp;&nbsp; [deconstruct\_datetime](#deconstruct_datetime) &nbsp;&nbsp; [deconstruct\_time](#deconstruct_time) &nbsp;&nbsp; [dedent](#dedent) &nbsp;&nbsp; [encode\_unicode](#encode_unicode) &nbsp;&nbsp; [forge\_bin](#forge_bin) &nbsp;&nbsp; [get\_int\_base](#get_int_base) &nbsp;&nbsp; [is\_whole\_number](#is_whole_number) &nbsp;&nbsp; [left\_pad\_int](#left_pad_int) &nbsp;&nbsp; [make\_indent\_str](#make_indent_str) &nbsp;&nbsp; [prettify\_b16](#prettify_b16) &nbsp;&nbsp; [prettify\_grid](#prettify_grid) &nbsp;&nbsp; [split\_float](#split_float) &nbsp;&nbsp; [split\_int](#split_int) &nbsp;&nbsp; [stringify\_bin](#stringify_bin) &nbsp;&nbsp; [strip\_block\_extra\_space](#strip_block_extra_space) &nbsp;&nbsp; [tidy\_up\_float](#tidy_up_float) &nbsp;&nbsp; [tidy\_up\_int](#tidy_up_int)
>
> **Constants:** &nbsp; None

# All Functions
[\_count\_leading\_zeros](#_count_leading_zeros) &nbsp;&nbsp; [\_parse\_significand](#_parse_significand) &nbsp;&nbsp; [\_prepare\_float](#_prepare_float) &nbsp;&nbsp; [\_tidy\_up\_right\_significand](#_tidy_up_right_significand) &nbsp;&nbsp; [add\_leading\_zeros](#add_leading_zeros) &nbsp;&nbsp; [calc\_uint\_bytes](#calc_uint_bytes) &nbsp;&nbsp; [construct\_date](#construct_date) &nbsp;&nbsp; [construct\_datetime](#construct_datetime) &nbsp;&nbsp; [construct\_time](#construct_time) &nbsp;&nbsp; [count\_indents](#count_indents) &nbsp;&nbsp; [count\_leading\_zeros](#count_leading_zeros) &nbsp;&nbsp; [decode\_unicode](#decode_unicode) &nbsp;&nbsp; [deconstruct\_date](#deconstruct_date) &nbsp;&nbsp; [deconstruct\_datetime](#deconstruct_datetime) &nbsp;&nbsp; [deconstruct\_time](#deconstruct_time) &nbsp;&nbsp; [dedent](#dedent) &nbsp;&nbsp; [encode\_unicode](#encode_unicode) &nbsp;&nbsp; [forge\_bin](#forge_bin) &nbsp;&nbsp; [get\_int\_base](#get_int_base) &nbsp;&nbsp; [is\_whole\_number](#is_whole_number) &nbsp;&nbsp; [left\_pad\_int](#left_pad_int) &nbsp;&nbsp; [make\_indent\_str](#make_indent_str) &nbsp;&nbsp; [prettify\_b16](#prettify_b16) &nbsp;&nbsp; [prettify\_grid](#prettify_grid) &nbsp;&nbsp; [split\_float](#split_float) &nbsp;&nbsp; [split\_int](#split_int) &nbsp;&nbsp; [stringify\_bin](#stringify_bin) &nbsp;&nbsp; [strip\_block\_extra\_space](#strip_block_extra_space) &nbsp;&nbsp; [tidy\_up\_float](#tidy_up_float) &nbsp;&nbsp; [tidy\_up\_int](#tidy_up_int)

## \_count\_leading\_zeros
This function accepts a string representing an integer.
This string shouldn't contain a sign symbol,
or any prefix such 0x, 0b, or 0o.
If you want to count leading zeros for an integer representation
that might contain a sign symbol, use the 'count_leading_zeros' function



**Signature:** (val)





**Return Value:** None

[Back to Top](#module-overview)


## \_parse\_significand
No description



**Signature:** (s)





**Return Value:** None

[Back to Top](#module-overview)


## \_prepare\_float
No description



**Signature:** (s)





**Return Value:** None

[Back to Top](#module-overview)


## \_tidy\_up\_right\_significand
No description



**Signature:** (s, width)





**Return Value:** None

[Back to Top](#module-overview)


## add\_leading\_zeros
No description



**Signature:** (val, n)





**Return Value:** None

[Back to Top](#module-overview)


## calc\_uint\_bytes
Return the number of bytes needed for a given integer



**Signature:** (x)





**Return Value:** None

[Back to Top](#module-overview)


## construct\_date
No description



**Signature:** (year\_delta, days\_delta)





**Return Value:** None

[Back to Top](#module-overview)


## construct\_datetime
No description



**Signature:** (year\_delta, ns\_delta, trailing\_zeros, tz\_minutes=None)





**Return Value:** None

[Back to Top](#module-overview)


## construct\_time
No description



**Signature:** (ns\_delta, trailing\_zeros, tz\_minutes=None)





**Return Value:** None

[Back to Top](#module-overview)


## count\_indents
No description



**Signature:** (line, strict=True)





**Return Value:** None

[Back to Top](#module-overview)


## count\_leading\_zeros
No description



**Signature:** (val)





**Return Value:** None

[Back to Top](#module-overview)


## decode\_unicode
Take in input some string that might have Unicode escape sequences.
Output the same string with unicode escape sequences converted into
the actual characters that they represent



**Signature:** (text)





**Return Value:** None

[Back to Top](#module-overview)


## deconstruct\_date
No description



**Signature:** (d)





**Return Value:** None

[Back to Top](#module-overview)


## deconstruct\_datetime
No description



**Signature:** (dt)





**Return Value:** None

[Back to Top](#module-overview)


## deconstruct\_time
No description



**Signature:** (t)





**Return Value:** None

[Back to Top](#module-overview)


## dedent
No description



**Signature:** (line, indents=1)





**Return Value:** None

[Back to Top](#module-overview)


## encode\_unicode
Convert a string into another where non-latin characters are
replaced with Unicode escape sequences



**Signature:** (text, codec='latin-1')





**Return Value:** None

[Back to Top](#module-overview)


## forge\_bin
items are int, bytes, bytearrays, or Nones, returns a bytearray



**Signature:** (\*items)





**Return Value:** None

[Back to Top](#module-overview)


## get\_int\_base
No description



**Signature:** (val)





**Return Value:** None

[Back to Top](#module-overview)


## is\_whole\_number
No description



**Signature:** (number)





**Return Value:** None

[Back to Top](#module-overview)


## left\_pad\_int
No description



**Signature:** (val, width)





**Return Value:** None

[Back to Top](#module-overview)


## make\_indent\_str
The type of 'indents' is int !



**Signature:** (indents)





**Return Value:** None

[Back to Top](#module-overview)


## prettify\_b16
Prettify base16 string. Returns a list of strings, each string representing
a line of 16 bytes



**Signature:** (s)





**Return Value:** None

[Back to Top](#module-overview)


## prettify\_grid
prettify grids, returns a list that can be iterated like this:
for row in result:
    print("  ".join(row))



**Signature:** (grid)





**Return Value:** None

[Back to Top](#module-overview)


## split\_float
Parse a float number (string or decimal.Decimal or float), returns
an instance of this namedtuple:
FloatParts = namedtuple("FloatParts", ["sign", "left_significand", "right_significand", "exponent"])



**Signature:** (s)





**Return Value:** None

[Back to Top](#module-overview)


## split\_int
No description



**Signature:** (val)





**Return Value:** None

[Back to Top](#module-overview)


## stringify\_bin
Good for debug. Stringify some binary data



**Signature:** (b, offset=0, width=None, spaced=False)





**Return Value:** None

[Back to Top](#module-overview)


## strip\_block\_extra\_space
This function is useful for textual Paradict's text and raw.
It strips extra space out from text/raw block
which is either a list of strings or a string.
Return a string.



**Signature:** (block)





**Return Value:** None

[Back to Top](#module-overview)


## tidy\_up\_float
Tidy up a float number (str or float or decimal.Decimal)
Example: 3.141234 -> 3.141_234



**Signature:** (s, width=3)





**Return Value:** None

[Back to Top](#module-overview)


## tidy\_up\_int
Tidy up some int number (str or int)
Example: 300141234 -> 300_141_234
0xFFFFFFFF -> 0xFFFF_FFFF
Returns a string



**Signature:** (val, width=3)





**Return Value:** None

[Back to Top](#module-overview)


