# Paradict binary format specification
<b>This document is the Paradict binary format specification.</b>

**Paradict** is a multi-format [serialization](https://en.wikipedia.org/wiki/Serialization) solution for serializing and deserializing a [dictionary](https://en.wikipedia.org/wiki/Associative_array) data structure in bulk or in a streaming fashion.

> Learn more: [https://github.com/pyrustic/paradict](https://github.com/pyrustic/paradict#readme)

## Table of contents
- [Overview](#overview)
- [Types of tags](#types-of-tags)
    - [Primitive](#primitive)
    - [Composite](#composite)
    - [Signal](#signal)
    - [Constant](#constant)
- [Keep-alive byte](#keep-alive-byte)
- [Null value](#null-value)
- [Numbers](#numbers)
    - [Integers](#integers)
    - [Floating-point numbers](#floating-point-numbers)
    - [Complex numbers](#complex-numbers)
- [Grid type](#grid-type)
- [Booleans](#booleans)
- [Strings](#strings)
- [Date and time](#date-and-time)
    - [Date](#date)
    - [Time](#time)
    - [Datetime](#datetime)
- [Embedded binary data](#embedded-binary-data)
- [Collections](#collections)
    - [Dictionary](#dictionary)
    - [List](#list)
    - [Set](#set)
- [Extension object](#extension-object)
- [Table of the 256 tags](#table-of-the-256-tags)

# Overview
Paradict can serialize a rich set of datatypes ranging from numbers to datetimes.

At the high level of the [binary](https://en.wikipedia.org/wiki/Byte) representation is the **message** which represents a **dictionary** data structure and at the low level is the **datum** which is often a 2-tuple composed of a **tag** and its **payload** which may be non-existent.

To extend the already rich set of data types, Paradict offers an extension mechanism which consists of a dict-like data structure (the extension Object) to hold the data elements which will be consumed by an object builder to create a new data item.

> The Paradict binary format follows the [little endian](https://en.wikipedia.org/wiki/Endianness) convention for packing bytes.

## Datum
Paradict defines [256 one-byte tags](#table-of-the-256-tags) to create datums following this format:

```text
tag [payload_length] [payload] [END]
```

As indicated above, a datum may consist of only a tag or embed its payload, or even end with the `END` tag.

> To learn more about datum composition, check the [types of tags](##types-of-tags).


## Datatypes
Here are the data types that can be represented with Paradict:

- **dict**: dictionary data structure.
- **list**: list data structure.
- **set**: set data structure.
- **obj**: object type for extension.
- **grid**: grid data structure for storing matrix-like data.
- **bool**: boolean type (true and false).
- **str**: ordinary string with escape sequences.
- **bin**: binary datatype.
- **int**: integer datatype.
- **float**: floating-point numbers.
- **complex**: complex numbers.
- **datetime**: [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) datetime (with time offsets).
- **date**: ISO 8601 date.
- **time**: ISO 8601 time (with time offsets).

> Paradict supports **null** for representing the intentional absence of any value.

## Compactness
To achieve advanced compactness, most of the datatypes presented above each have a family of tags to process their subtypes. For example, for the **int** datatype, there is no `INT` tag, but there is `PINT_x` and `NINT_x` to represent positive and negative integers where the suffix `x` is the number of bits allocated to the payload.

<p align="right"><a href="#readme">Back to top</a></p>

# Types of tags
There are four types of tags with different roles: **Primitive**, **Composite**, **Signal**, and **Constant**.

## Primitive
A **Primitive** tag enables the creation of datum whose payload does not consist of other datum. 

Primitives are:
> `BIN_x` `STR_x` `PINT_x` `NINT_x`

## Composite
A **Composite** tag enables the creation of datum whose payload consists of other datum.

Composites are:
> `DICT` `LIST` `SET` `OBJ` `GRID` `COMPLEX` `RADIX_x` `DATE` `TIME` `DATETIME` `FLOAT_MISC` `FLOAT_1` `FLOAT_1_EXT` `FLOAT_2` `FLOAT_2_EXT` `FLOAT_3` `FLOAT_3_EXT`

## Signal
A **Signal** tag enables the creation of datum that doesn't contain a payload and only serves as a signal intended to be consumed by the deserializer.

Signals are:
> `NOP` `GRID_DIV` `END`

## Constant
A **Constant** tag enables the creation of datum that doesn't contain a payload because it already serves as a placeholder for a predefined constant.

Constants are:
> `DICT_EMPTY` `LIST_EMPTY` `SET_EMPTY` `OBJ_EMPTY` `GRID_EMPTY` `NULL` `BOOL_x` `BIN_EMPTY` `CHAR_x` `CONST_x`

<p align="right"><a href="#readme">Back to top</a></p>

# Keep-alive byte
`NOP` represents the [keep-alive](https://en.wikipedia.org/wiki/Keepalive) byte whose value is **0x00**.

# Null value
The `NULL` tag represents the **null** value to indicate the intentional absence of any value.

<p align="right"><a href="#readme">Back to top</a></p>

# Numbers
Numbers are either **integers**, **floating-point** or **complex** numbers.

## Integers
Three families of tags enable the creation of integer datums: integer constants (`CONST_0` to `CONST_99`), positive integers (`PINT_8` to `PINT_HEAVY`), and negative integers (`NINT_8` to `NINT_HEAVY`).

In addition to the default [decimal system](https://en.wikipedia.org/wiki/Decimal), there is also support for alternative numeral systems such as binary, octal, and hexadecimal through the `RADIX_x` tag family.

### Constants
There are **100** tags of type Constant to represent positive integers from **0** to **99**. These tags belong to the `CONST_x` tag family where `x` is a number (0 to 99).

### Positive integers
For compactness, positive integers are not supported by a specific tag but by a family of primitive tags namely `PINT_x` where `x` refers to the length in bits of the unsigned integer payload.

|Tag | Format | Range |
|---|---|---|
|`PINT_8`|tag **+** 8-bit payload|100 to (2^8)-1|
|`PINT_16`|tag **+** 16-bit payload|2^8 to (2^16)-1|
|`PINT_24`|tag **+** 24-bit payload|2^16 to (2^24)-1|
|`PINT_32`|tag **+** 32-bit payload|2^24 to (2^32)-1|
|`PINT_40`|tag **+** 40-bit payload|2^32 to (2^40)-1|
|`PINT_48`|tag **+** 48-bit payload|2^40 to (2^48)-1|
|`PINT_56`|tag **+** 56-bit payload|2^48 to (2^56)-1|
|`PINT_64`|tag **+** 64-bit payload|2^56 to (2^64)-1|
|`PINT_BIG`|tag **+** 1-byte PL **+** payload|2^64 to (2^2048)-1|
|`PINT_HEAVY`|tag **+** 2-byte PL **+** payload|2^2048 to (2^524288)-1|

> **PL** stands for **payload length**. This is an unsigned integer to store the length of the payload in `PINT_BIG` and `PINT_HEAVY` datums. Note that it is the **payload length minus 1** that is actually stored.

### Negative integers
For compactness, negative integers are not supported by a specific tag but by a family of primitive tags namely `NINT_x` where `x` refers to the length in bits of the unsigned integer payload.

|Tag | Format | Range |
|---|---|---|
|`NINT_8`|tag **+** 8-bit payload|100 to (2^8)-1|
|`NINT_16`|tag **+** 16-bit payload|2^8 to (2^16)-1|
|`NINT_24`|tag **+** 24-bit payload|2^16 to (2^24)-1|
|`NINT_32`|tag **+** 32-bit payload|2^24 to (2^32)-1|
|`NINT_40`|tag **+** 40-bit payload|2^32 to (2^40)-1|
|`NINT_48`|tag **+** 48-bit payload|2^40 to (2^48)-1|
|`NINT_56`|tag **+** 56-bit payload|2^48 to (2^56)-1|
|`NINT_64`|tag **+** 64-bit payload|2^56 to (2^64)-1|
|`NINT_BIG`|tag **+** 1-byte PL **+** payload|2^64 to (2^2048)-1|
|`NINT_HEAVY`|tag **+** 2-byte PL **+** payload|2^2048 to (2^524288)-1|

> **PL** stands for **payload length**. This is an unsigned integer to store the length of the payload in `NINT_BIG` and `NINT_HEAVY` datums. Note that it is the **payload length minus 1** that is actually stored.

### Binary, octal, and hexadecimal integer
In addition to the default [decimal system](https://en.wikipedia.org/wiki/Decimal), there is also support for alternative numeral systems such as binary, octal, and hexadecimal through the `RADIX_x` tag family.

The `RADIX_x` tag family, of type Composite, specifies the [radix](https://en.wikipedia.org/wiki/Radix) of the associated payload.

|Tag|Radix|Format|
|---|---|---|
|`RADIX_BIN`|2|tag **+** payload|
|`RADIX_BIN_EXT`|2|tag **+** n **+** payload|
|`RADIX_OCT`|8|tag **+** payload|
|`RADIX_OCT_EXT`|8|tag **+** n **+** payload|
|`RADIX_HEX`|16|tag **+** payload|
|`RADIX_HEX_EXT`|16|tag **+** n **+** payload|

> The **payload** is an integer datum and **n** is the count of [leading zeros](https://en.wikipedia.org/wiki/Leading_zero) expected when the number is rendered using the specified radix.

## Floating-point numbers
There is a set of Composite tags for storing floating-point numbers.

Floating point numbers can be represented using ordinary or [scientific notation](https://en.wikipedia.org/wiki/Scientific_notation#E_notation). Whether these numbers are processed with binary (efficiency) or decimal (precision) floating-point representation depends on custom configurations defined for the deserializer.

|Tag|Format|
|---|---|
|`FLOAT_1`|tag **+** left significand|
|`FLOAT_1_EXT`|tag **+** left significand **+** exponent|
|`FLOAT_2`|tag **+** left significand **+** right significand|
|`FLOAT_2_EXT`|tag **+** left significand **+** right significand **+** exponent|
|`FLOAT_3`|tag **+** left significand **+** leading zeros **+** right significand|
|`FLOAT_3_EXT`|tag **+** left significand **+** leading zeros **+** right significand **+** exponent|

Assume the floating-point number `-3.014E-5`. It can be divided into four parts:
- left significand: **-3**
- leading zeros (right significand): **1**
- right significand: **14**
- exponent: **-5**

> The tag family being of type Composite, the four parts listed above should be packed as integer datums.

### Constant values
Floating-point numbers have four constant values that can be represented with the `FLOAT_MISC` tag, of type Composite, followed by an alphabetical tag:

|Datum|Constant value|
|---|---|
|`FLOAT_MISC` **+** `CHAR_N`|NaN|
|`FLOAT_MISC` **+** `CHAR_X`|+Infinity|
|`FLOAT_MISC` **+** `CHAR_Y`|-Infinity|
|`FLOAT_MISC` **+** `CHAR_Z`|-0.0|


## Complex numbers
A complex number is packed with the `COMPLEX` tag, of type Composite, followed by two integer datums that represent the real and imaginary parts of the number, respectively.

> **Format:** tag **+** real datum **+** imaginary datum

<p align="right"><a href="#readme">Back to top</a></p>

# Grid type
The grid consists of rows made up of numbers. All rows are the same length.

A grid is packed with the `GRID` tag, of type Composite, followed by integer datums and closed with the `END` tag. The `GRID_DIV` tag is placed at the end of the first row if there are **at least 2 rows** in the grid. The position of the `GRID_DIV` tag will then be used by the deserializer to determine the row length.

> **Format:** tag **+** first row of integer datums **+** `GRID_DIV` **+** integer datums **+** `END`

> The `GRID_EMPTY` tag represents an empty grid.

<p align="right"><a href="#readme">Back to top</a></p>

# Booleans
The `BOOL_TRUE` and `BOOL_FALSE` tags, of type Constant, represent the two [Boolean](https://en.wikipedia.org/wiki/Boolean_data_type) type values.

<p align="right"><a href="#readme">Back to top</a></p>

# Strings
A string is a sequence of zero or more [Unicode](https://en.wikipedia.org/wiki/Unicode) characters that supports escape sequences.

For compactness, regular strings aren't covered by a specific tag but by a family of Primitive tags namely `STR_x` where `x` hints to the length of the string payload.

> The `STR_EMPTY` tag represents an empty string.

### STR_8 to STR_256
There are 32 tags from `STR_8` to `STR_256` all suffixed with a multiple of 8. These suffixes indicate the length in bits of the string payload following the tag.

> **Format:** tag **+** payload

### STR_SHORT, STR_MEDIUM, STR_LONG, and STR_HEAVY
Strings that cannot be packed with `STR_8` to `STR_256` tags can be packed with `STR_SHORT`, `STR_MEDIUM`, `STR_LONG`, and `STR_HEAVY`.

These tags are followed by 2 items: one to four bytes (also known as the **Z** bytes) to store the length of the payload, and then the payload itself.

The following table shows for each tag the **Z** number of bytes (unsigned integer) to store the payload length.

|Tag|Z|Payload length|
|---|---|---|
|`STR_SHORT`|1|33 to 2^8 bytes|
|`STR_MEDIUM`|2|(2^8)+1 to 2^16 bytes|
|`STR_LONG`|3|(2^16)+1 to 2^24 bytes|
|`STR_BIG`|4|(2^24)+1 to 2^32 bytes|
|`STR_HEAVY`|5|(2^32)+1 to 2^40 bytes|

> Assuming the payload length is **n**, it is **n minus 1** that would actually be stored in the **Z** bytes.

> **Format:** tag **+** Z **+** payload

<p align="right"><a href="#readme">Back to top</a></p>

# Date and time
Paradict supports date, time, and datetime types compatible with [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601).

For compactness, Paradict uses a reference datetime (also known as Paradict Epoch) to generate deltas which become the temporal information to be stored in temporal datums. 

> **Paradict Epoch:** `2020-01-01T00:00:00Z`

## Date
A date is packed with the `DATE` tag, of type Composite, followed by the year delta and the day delta. The year and the day deltas are integer datums calculated relative to the Paradict Epoch.

> **Format:** `DATE` **+** year delta **+** day delta

## Time
A time is packed with the `TIME` tag, of type Composite, followed by the nanosecond delta and **n**, the number of trailing zeros. The nanosecond delta is an integer datum calculated relative to the Paradict Epoch but stripped of its trailing zeros. The **n** number of trailing zeros is an integer datum.

> **Format:** `TIME` **+** nanosecond delta **+** n trailing zeros

### Time with UTC offset
Time with [UTC offset](https://en.wikipedia.org/wiki/UTC_offset) is packed with the `TIME_EXT` tag, of type Composite, followed by the nanosecond delta, the **n** number of trailing zeros, and the UTC offset in minutes.

The nanosecond delta is an integer datum calculated relative to the Paradict Epoch but stripped of its trailing zeros. The **n** number of trailing zeros and the UTC offset in minutes are integer datums.

> **Format:** `TIME_EXT` **+** nanosecond delta **+** n trailing zeros **+** utc offset in minutes

## Datetime
A datetime is packed with the `DATETIME` tag, of type Composite, followed by the year delta, the nanosecond delta, and the **n** number of trailing zeros. 

The year and the nanosecond deltas are integer datums calculated relative to the Paradict Epoch. The nanosecond delta is stripped of its trailing zeros. The **n** number of trailing zeros is an integer datum.

> **Format:** `DATETIME` **+** year delta **+** nanosecond delta **+** n trailing zeros

### Datetime with UTC offset
Datetime with [UTC offset](https://en.wikipedia.org/wiki/UTC_offset) is packed with the `DATETIME_EXT` tag, of type Composite, followed by the year delta, the nanosecond delta, the **n** number of trailing zeros, and the UTC offset in minutes.

The year and the nanosecond deltas are integer datums calculated relative to the Paradict Epoch. The nanosecond delta is stripped of its trailing zeros. The **n** number of trailing zeros and the UTC offset in minutes are integer datums.

> **Format:** `DATETIME_EXT` **+** year delta **+** nanosecond delta **+** n trailing zeros **+** utc offset in minutes


<p align="right"><a href="#readme">Back to top</a></p>

# Embedded binary data
An embedded binary data is a sequence of bytes that is packed with the Primitive `BIN_x` tag where `x` is a hint to the length of the payload. The tag is followed by **Z** number of bytes to store the length of the following payload.

> The `BIN_EMPTY` tag, of type Constant, represents an empty binary data.

|Tag|Z|Payload length|
|---|---|---|
|`BIN_SHORT`|1|1 to 2^8 bytes|
|`BIN_MEDIUM`|2|(2^8)+1 to 2^16 bytes|
|`BIN_LONG`|3|(2^16)+1 to 2^24 bytes|
|`BIN_BIG`|4|(2^24)+1 to 2^32 bytes|
|`BIN_HEAVY`|5|(2^32)+1 to 2^40 bytes|

> Assuming the payload length is **n**, it is **n minus 1** that would actually be stored in the **Z** bytes.

> **Format:** tag **+** Z **+** payload

<p align="right"><a href="#readme">Back to top</a></p>

# Collections
Although Paradict's root data structure is a dictionary, lists, sets, and dictionaries can be nested within it at arbitrary depth.

## Dictionary
The dictionary data structure can contain any other datatype. It is packed with the `DICT` tag that is followed by an arbitrary number of key-value pairs. Such datum ultimately ends with the `END` tag, of type Signal. 

> Key-value pairs are a succession of pairs of datums, each pair consisting of two datums representing a unique key and a value, respectively.

> The types allowed for keys are numbers and strings datum.

> Empty dict are represented with the `DICT_EMPTY` tag, of type Constant.

> **Format:** tag **+** key-value datums pairs... **+** `END`


## List
The **list** data structure can contain any other datatype. A list is packed with the `LIST` tag, of type Composite, followed by an arbitrary number of datums. Such datum ultimately ends with the `END` tag, of type Signal.


> Empty dict are represented with the `LIST_EMPTY` tag, of type Constant.

> **Format:** tag **+** datums... **+** `END`


## Set
The **set** data structure can contain any other datatype except:
- another data structure such as another set, a dict, a list,
- an extension object,
- a grid.

A set is packed with the `SET` tag, of type Composite, followed by an arbitrary number of datums. Such datum ultimately ends with the `END` tag, of type Signal.


> Empty dict are represented with the `SET_EMPTY` tag, of type Constant.

> **Format:** tag **+** datums... **+** `END`

<p align="right"><a href="#readme">Back to top</a></p>

# Extension object
To extend the already rich set of data types, Paradict offers an extension mechanism which consists of a dict-like data structure (the extension Object) to hold the data elements which will be consumed by an object builder to create a new data item.

The extension Object data structure can contain any other datatype. It is packed with the `OBJ` tag that is followed by an arbitrary number of key-value pairs. Such datum ultimately ends with the `END` tag, of type Signal. 

> Key-value pairs are a succession of pairs of datums, each pair consisting of two datums representing a unique key and a value, respectively.

> The types allowed for keys are numbers and strings datum.

> An empty extension Object is represented with the `OBJ_EMPTY` tag, of type Constant.

> **Format:** tag **+** key-value datums pairs... **+** `END`

<p align="right"><a href="#readme">Back to top</a></p>

# Table of the 256 tags
Following is the tag-byte mapping:

|Tag|Byte|Type|Note|
|---|---|---|---|
|`NOP`|0x00|signal| |
|`DICT`|0x01|composite|container|
|`DICT_EMPTY`|0x02|constant| |
|`LIST`|0x03|composite|container|
|`LIST_EMPTY`|0x04|constant| |
|`SET`|0x05|composite|container|
|`SET_EMPTY`|0x06|constant| |
|`OBJ`|0x07|composite|extension container|
|`OBJ_EMPTY`|0x08|constant| |
|`GRID`|0x09|composite|math container|
|`GRID_DIV`|0x0A|signal| |
|`GRID_EMPTY`|0x0B|constant| |
|`NULL`|0x0C|composite| |
|`BOOL_TRUE`|0x0D|composite| |
|`BOOL_FALSE`|0x0E|composite| |
|`COMPLEX`|0x0F|composite|complex numbers|
|`XA`|0x10|?|reserved tag|
|`XB`|0x11|?|reserved tag|
|`XC`|0x12|?|reserved tag|
|`XD`|0x13|?|reserved tag|
|`XE`|0x14|?|reserved tag|
|`DATE`|0x15|composite| |
|`TIME`|0x16|composite| |
|`TIME_EXT`|0x17|composite|time with UTC offsets|
|`DATETIME`|0x18|composite| |
|`DATETIME_EXT`|0x19|composite|datetime with UTC offsets|
|`RADIX_BIN`|0x1A|composite|binary notation for int|
|`RADIX_BIN_EXT`|0x1B|primitive| |
|`RADIX_OCT`|0x1C|composite|octal notation for int|
|`RADIX_OCT_EXT`|0x1D|composite| |
|`RADIX_HEX`|0x1E|composite|hex notation for int|
|`RADIX_HEX_EXT`|0x1F|composite| |
|`FLOAT_MISC`|0x20|composite|for +/-inf, NaN, and -0|
|`FLOAT_1`|0x21|composite| |
|`FLOAT_1_EXT`|0x22|composite|float with exponent|
|`FLOAT_2`|0x23|composite| |
|`FLOAT_2_EXT`|0x24|composite|float with exponent|
|`FLOAT_3`|0x25|composite| |
|`FLOAT_3_EXT`|0x26|composite|float with exponent|
|`BIN_EMPTY`|0x27|constant| |
|`BIN_SHORT`|0x28|primitive| |
|`BIN_MEDIUM`|0x29|primitive| |
|`BIN_LONG`|0x2A|primitive| |
|`BIN_BIG`|0x2B|primitive| |
|`BIN_HEAVY`|0x2C|primitive| |
|`PINT_8`|0x2D|primitive|positive integer|
|`PINT_16`|0x2E|primitive| |
|`PINT_24`|0x2F|primitive| |
|`PINT_32`|0x30|primitive| |
|`PINT_40`|0x31|primitive| |
|`PINT_48`|0x32|primitive| |
|`PINT_56`|0x33|primitive| |
|`PINT_64`|0x34|primitive| |
|`PINT_BIG`|0x35|primitive| |
|`PINT_HEAVY`|0x36|primitive| |
|`NINT_8`|0x37|primitive|negative integer|
|`NINT_16`|0x38|primitive| |
|`NINT_24`|0x39|primitive| |
|`NINT_32`|0x3A|primitive| |
|`NINT_40`|0x3B|primitive| |
|`NINT_48`|0x3C|primitive| |
|`NINT_56`|0x3D|primitive| |
|`NINT_64`|0x3E|primitive| |
|`NINT_BIG`|0x3F|primitive| |
|`NINT_HEAVY`|0x40|primitive| |
|`STR_8`|0x41|primitive|string|
|`STR_16`|0x42|primitive| |
|`STR_24`|0x43|primitive| |
|`STR_32`|0x44|primitive| |
|`STR_40`|0x45|primitive| |
|`STR_48`|0x46|primitive| |
|`STR_56`|0x47|primitive| |
|`STR_64`|0x48|primitive| |
|`STR_72`|0x49|primitive| |
|`STR_80`|0x4A|primitive| |
|`STR_88`|0x4B|primitive| |
|`STR_96`|0x4C|primitive| |
|`STR_104`|0x4D|primitive| |
|`STR_112`|0x4E|primitive| |
|`STR_120`|0x4F|primitive| |
|`STR_128`|0x50|primitive| |
|`STR_136`|0x51|primitive| |
|`STR_144`|0x52|primitive| |
|`STR_152`|0x53|primitive| |
|`STR_160`|0x54|primitive| |
|`STR_168`|0x55|primitive| |
|`STR_176`|0x56|primitive| |
|`STR_184`|0x57|primitive| |
|`STR_192`|0x58|primitive| |
|`STR_200`|0x59|primitive| |
|`STR_208`|0x5A|primitive| |
|`STR_216`|0x5B|primitive| |
|`STR_224`|0x5C|primitive| |
|`STR_232`|0x5D|primitive| |
|`STR_240`|0x5E|primitive| |
|`STR_248`|0x5F|primitive| |
|`STR_256`|0x60|primitive| |
|`STR_EMPTY`|0x61|constant| |
|`STR_SHORT`|0x62|primitive| |
|`STR_MEDIUM`|0x63|primitive| |
|`STR_LONG`|0x64|primitive| |
|`STR_BIG`|0x65|primitive| |
|`STR_HEAVY`|0x66|primitive| |
|`CHAR_A`|0x67|constant|lowercase character|
|`CHAR_B`|0x68|constant| |
|`CHAR_C`|0x69|constant| |
|`CHAR_D`|0x6A|constant| |
|`CHAR_E`|0x6B|constant| |
|`CHAR_F`|0x6C|constant| |
|`CHAR_G`|0x6D|constant| |
|`CHAR_H`|0x6E|constant| |
|`CHAR_I`|0x6F|constant| |
|`CHAR_J`|0x70|constant| |
|`CHAR_K`|0x71|constant| |
|`CHAR_L`|0x72|constant| |
|`CHAR_M`|0x73|constant| |
|`CHAR_N`|0x74|constant| |
|`CHAR_O`|0x75|constant| |
|`CHAR_P`|0x76|constant| |
|`CHAR_Q`|0x77|constant| |
|`CHAR_R`|0x78|constant| |
|`CHAR_S`|0x79|constant| |
|`CHAR_T`|0x7A|constant| |
|`CHAR_U`|0x7B|constant| |
|`CHAR_V`|0x7C|constant| |
|`CHAR_W`|0x7D|constant| |
|`CHAR_X`|0x7E|constant| |
|`CHAR_Y`|0x7F|constant| |
|`CHAR_Z`|0x80|constant| |
|`CHAR_UP_A`|0x81|constant|uppercase character|
|`CHAR_UP_B`|0x82|constant| |
|`CHAR_UP_C`|0x83|constant| |
|`CHAR_UP_D`|0x84|constant| |
|`CHAR_UP_E`|0x85|constant| |
|`CHAR_UP_F`|0x86|constant| |
|`CHAR_UP_G`|0x87|constant| |
|`CHAR_UP_H`|0x88|constant| |
|`CHAR_UP_I`|0x89|constant| |
|`CHAR_UP_J`|0x8A|constant| |
|`CHAR_UP_K`|0x8B|constant| |
|`CHAR_UP_L`|0x8C|constant| |
|`CHAR_UP_M`|0x8D|constant| |
|`CHAR_UP_N`|0x8E|constant| |
|`CHAR_UP_O`|0x8F|constant| |
|`CHAR_UP_P`|0x90|constant| |
|`CHAR_UP_Q`|0x91|constant| |
|`CHAR_UP_R`|0x92|constant| |
|`CHAR_UP_S`|0x93|constant| |
|`CHAR_UP_T`|0x94|constant| |
|`CHAR_UP_U`|0x95|constant| |
|`CHAR_UP_V`|0x96|constant| |
|`CHAR_UP_W`|0x97|constant| |
|`CHAR_UP_X`|0x98|constant| |
|`CHAR_UP_Y`|0x99|constant| |
|`CHAR_UP_Z`|0x9A|constant| |
|`CONST_0`|0x9B|constant|constant number|
|`CONST_1`|0x9C|constant| |
|`CONST_2`|0x9D|constant| |
|`CONST_3`|0x9E|constant| |
|`CONST_4`|0x9F|constant| |
|`CONST_5`|0xA0|constant| |
|`CONST_6`|0xA1|constant| |
|`CONST_7`|0xA2|constant| |
|`CONST_8`|0xA3|constant| |
|`CONST_9`|0xA4|constant| |
|`CONST_10`|0xA5|constant| |
|`CONST_11`|0xA6|constant| |
|`CONST_12`|0xA7|constant| |
|`CONST_13`|0xA8|constant| |
|`CONST_14`|0xA9|constant| |
|`CONST_15`|0xAA|constant| |
|`CONST_16`|0xAB|constant| |
|`CONST_17`|0xAC|constant| |
|`CONST_18`|0xAD|constant| |
|`CONST_19`|0xAE|constant| |
|`CONST_20`|0xAF|constant| |
|`CONST_21`|0xB0|constant| |
|`CONST_22`|0xB1|constant| |
|`CONST_23`|0xB2|constant| |
|`CONST_24`|0xB3|constant| |
|`CONST_25`|0xB4|constant| |
|`CONST_26`|0xB5|constant| |
|`CONST_27`|0xB6|constant| |
|`CONST_28`|0xB7|constant| |
|`CONST_29`|0xB8|constant| |
|`CONST_30`|0xB9|constant| |
|`CONST_31`|0xBA|constant| |
|`CONST_32`|0xBB|constant| |
|`CONST_33`|0xBC|constant| |
|`CONST_34`|0xBD|constant| |
|`CONST_35`|0xBE|constant| |
|`CONST_36`|0xBF|constant| |
|`CONST_37`|0xC0|constant| |
|`CONST_38`|0xC1|constant| |
|`CONST_39`|0xC2|constant| |
|`CONST_40`|0xC3|constant| |
|`CONST_41`|0xC4|constant| |
|`CONST_42`|0xC5|constant| |
|`CONST_43`|0xC6|constant| |
|`CONST_44`|0xC7|constant| |
|`CONST_45`|0xC8|constant| |
|`CONST_46`|0xC9|constant| |
|`CONST_47`|0xCA|constant| |
|`CONST_48`|0xCB|constant| |
|`CONST_49`|0xCC|constant| |
|`CONST_50`|0xCD|constant| |
|`CONST_51`|0xCE|constant| |
|`CONST_52`|0xCF|constant| |
|`CONST_53`|0xD0|constant| |
|`CONST_54`|0xD1|constant| |
|`CONST_55`|0xD2|constant| |
|`CONST_56`|0xD3|constant| |
|`CONST_57`|0xD4|constant| |
|`CONST_58`|0xD5|constant| |
|`CONST_59`|0xD6|constant| |
|`CONST_60`|0xD7|constant| |
|`CONST_61`|0xD8|constant| |
|`CONST_62`|0xD9|constant| |
|`CONST_63`|0xDA|constant| |
|`CONST_64`|0xDB|constant| |
|`CONST_65`|0xDC|constant| |
|`CONST_66`|0xDD|constant| |
|`CONST_67`|0xDE|constant| |
|`CONST_68`|0xDF|constant| |
|`CONST_69`|0xE0|constant| |
|`CONST_70`|0xE1|constant| |
|`CONST_71`|0xE2|constant| |
|`CONST_72`|0xE3|constant| |
|`CONST_73`|0xE4|constant| |
|`CONST_74`|0xE5|constant| |
|`CONST_75`|0xE6|constant| |
|`CONST_76`|0xE7|constant| |
|`CONST_77`|0xE8|constant| |
|`CONST_78`|0xE9|constant| |
|`CONST_79`|0xEA|constant| |
|`CONST_80`|0xEB|constant| |
|`CONST_81`|0xEC|constant| |
|`CONST_82`|0xED|constant| |
|`CONST_83`|0xEE|constant| |
|`CONST_84`|0xEF|constant| |
|`CONST_85`|0xF0|constant| |
|`CONST_86`|0xF1|constant| |
|`CONST_87`|0xF2|constant| |
|`CONST_88`|0xF3|constant| |
|`CONST_89`|0xF4|constant| |
|`CONST_90`|0xF5|constant| |
|`CONST_91`|0xF6|constant| |
|`CONST_92`|0xF7|constant| |
|`CONST_93`|0xF8|constant| |
|`CONST_94`|0xF9|constant| |
|`CONST_95`|0xFA|constant| |
|`CONST_96`|0xFB|constant| |
|`CONST_97`|0xFC|constant| |
|`CONST_98`|0xFD|constant| |
|`CONST_99`|0xFE|constant| |
|`END`|0xFF|signal|used by containers|


> `XA`, `XB`, `XC`, `XD`, and `XE` are reserved tags.

<br>
<br>
<br>

[Back to top](#readme)

