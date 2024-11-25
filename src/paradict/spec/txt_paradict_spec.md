
# Paradict textual format specification
<b>This document is the Paradict textual format specification.</b>

**Paradict** is a multi-format [serialization](https://en.wikipedia.org/wiki/Serialization) solution for serializing and deserializing a [dictionary](https://en.wikipedia.org/wiki/Associative_array) data structure in bulk or in a streaming fashion.

> Learn more: [https://github.com/pyrustic/paradict](https://github.com/pyrustic/paradict#readme)

## Table of contents
- [Overview](#overview)
- [Data and config modes](data-and-config-modes)
- [Null value](#null-value)
- [Numbers](#numbers)
    - [Integers](#integers)
    - [Floating-point numbers](#floating-point-numbers)
    - [Complex numbers](#complex-numbers)
- [Grid type](#grid-type)
- [Booleans](#booleans)
- [Strings](#strings)
    - [Ordinary string](#ordinary-string)
    - [Raw string](#raw-string)
- [Comments](#comments)
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


# Overview
Paradict can textually represent a rich set of datatypes ranging from numbers to datetimes.

At the high level of the textual representation is the **message** which represents a dictionary data structure and at the low level is the **line** of text. A line of text can represent either complete data, such as a number, or a portion of some data that spans multiple lines, such as a multiline string.

To extend the already rich set of data types, Paradict offers an extension mechanism which consists of a dict-like data structure (the extension Object) to hold the data elements which will be consumed by an object builder to create a new data item.

> Paradict textual format must be encoded in UTF-8.

## Datatypes
Here are the data types that can be represented with Paradict:

- **dict**: dictionary data structure.
- **list**: list data structure.
- **set**: set data structure.
- **obj**: object type for extension.
- **grid**: grid data structure for storing matrix-like data.
- **bool**: boolean type (true and false).
- **str**: ordinary string with escape sequences.
- **raw**: raw string without escape sequences.
- **bin**: binary datatype.
- **int**: integer datatype.
- **float**: float datatype.
- **complex**: complex number.
- **datetime**: [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) datetime (with time offsets).
- **date**: ISO 8601 date.
- **time**: ISO 8601 time (with time offsets).

> Paradict supports **null** for representing the intentional absence of any value.

## Indentation
For human readability, data expected to span multiple lines is first introduced with a **tag** (the data type in parentheses) under which the data is placed with the correct number of **4-space indents**.

Example:
```text
poem = (text)
    This is a multiline
    poem.
    ---
books = (dict)
    sci_fi = (list)
        "Book A"
        "Book B"
    thriller = (list)
        "Book C"
        "Book D"
```

> **Valid tags**: `(dict)`, `(list)`, `(set)`, `(obj)`, `(grid)`, `(text)`, `(raw)`, `(int)`, `(float)`, `(bin)`.

<p align="right"><a href="#readme">Back to top</a></p>

# Data and config modes
The Paradict textual format has two modes:
- **data mode** to formally represent data (bidirectional mapping to binary format).
- **config mode** for configuration files only.

These modes differ based on the data type of dictionary keys and the character utilized to separate each key from its corresponding value.

## Data mode
**Data mode** allows numbers and strings as keys, so keys that aren't numbers must be enclosed in quotes. The character between a key and its value is a colon (**:**).

Example:

```text
'my key 1': 'value 1'
```

> A key that is a string must be surrounded by double or single quotes depending on whether escape sequences will be taken into account or not. Unlike a value (string on the other side of the equals sign), a key must escape the quotes inside itself.

## Config mode
**Config mode** only allows strings as keys, making it unnecessary to enclose keys in quotes. The character between a key and its value is the equal sign (**=**).

> A key shouldn't contain a space or the equal sign (**=**). 

Example:

```text
my_key_1 = 'value 1'
```

<p align="right"><a href="#readme">Back to top</a></p>

# Null value
The `null` keyword represents the **null** value to indicate the intentional absence of any value.

Example:
```text
my_key = null
```

<p align="right"><a href="#readme">Back to top</a></p>

# Numbers
Numbers are either **integers**, **floating-point** or **complex** numbers. They may contain underscores to improve readability. However, underscores aren't allowed in some specific places:
- at the beginning or end of the number,
- on either side of a notation prefix.

> The range of valid numeric values is discussed in the Paradict binary format specification. 

## Integers
An integer can be represented in [decimal](https://en.wikipedia.org/wiki/Decimal) (default), hexadecimal, octal, and binary notation.

Example:
```text
int = 4_294_967_295
hex_int = 0xffff_ffff
oct_int = 0o37_777_777_777
bin_int = 0b1111_1111_1111_1111_1111_1111_1111_1111
```

### Multi-line integers
A integer can span multiple lines.

Example:
```text
number = (int)
    -1_000_000_000_000_000_000_000_000_000_000
    _000_000_000_000_000_000_000_000
```

## Floating-point numbers
Floating point numbers can be represented using regular or [scientific notation](https://en.wikipedia.org/wiki/Scientific_notation#E_notation). Whether these numbers are processed with binary (efficient) or decimal (precision) floating point representation depends on custom configurations defined for the deserializer.

Example:
```text
float = 3.14
sci_notation_float = 3.147_378E-10
```

### Multi-line floating-point numbers
A floating-point number can span multiple lines.

Example:
```text
number = (float)
    -1.000_000_000_000_000_000_000_000_000_000
    _000_000_000_000_000_000_000_111E-10
```

## Complex numbers
A complex number is suffixed with `i`.

Example:
```text
my_complex = -1.2+3.4i
```

<p align="right"><a href="#readme">Back to top</a></p>

# Grid type
A grid is made up of lines made up of numbers. Each line represents a row whose size is the same as that of the other rows. As a grid can span multiple lines, it is introduced with the `(grid)` tag. At least one space separates numbers on the same line.

Example:
```text
matrix_1 = (grid)
    0 1 0 1
    1 0 1 0
matrix = (grid)
    3.14      -1.2+3.4i   123
    2_000_000 0xFFFF_FFFF 456
```

> The numbers must be left aligned so as not to alter the indents.

<p align="right"><a href="#readme">Back to top</a></p>

# Booleans
The keywords `true` and `false` represent the two values of the Boolean type.

Example:
```text
my_bool_1 = true
my_bool_2 = false
```

<p align="right"><a href="#readme">Back to top</a></p>

# Strings
A string is a sequence of zero or more [Unicode](https://en.wikipedia.org/wiki/Unicode) characters. This sequence can be labeled as **ordinary** or **raw**.

## Ordinary string
A regular string supports escape sequences and can be defined on a single-line in double-quotes or span multiple lines.

### Single-line string
A single-line string is defined on its own line surrounded by double quotes.

> A quote that is part of a string must not be escaped by backlash character.

### Multiline string
A multi-line string is text that spans multiple lines. Such a string is introduced with the `(text)` tag and therefore indented.

Example:
```text
single_line_str = "hello \n world !"
multiline_str = (text)
    Hello
    world !
    ---
```

> The last three consecutive dashes starting an empty line indicate the end of a multiline string.

## Raw string
Raw strings don't support escape sequences and can be defined on a single-line in single-quotes or span multiple lines.

### Single-line string
A single-line string is defined on its own line surrounded by single quotes.

> The backlash character has no special effect in a raw string.

### Multi-line string
A multi-line raw string is text that spans multiple lines. Such a string is introduced with the `(raw)` tag and therefore indented.

Example:
```text
single_line_str = 'hello world !'
multiline_str = (raw)
    Hello
    world !
    ---
```

> The last three consecutive dashes starting an empty line indicate the end of a multi-line string.

<p align="right"><a href="#readme">Back to top</a></p>
    
# Comments
A comment starts on its own line with a hash character (**#**).

```text
# this is a comment
my_key = (list)
    # this is a comment
    "item 1"
    "item 2"
extension_obj = (obj)
    # this is a comment
    key = "val"
```
> Comments are ignored by the parser.

<p align="right"><a href="#readme">Back to top</a></p>

# Date and time
Paradict supports date, time, and datetime types compatible with [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601).

## Date
A date follows the `YYYY-MM-DD` format. 

Example:
```text
my_date = 2025-12-25
```
## Time
A time follows the `hh:mm:ss[.mmm]` format. A time offset from [UTC](https://en.wikipedia.org/wiki/Coordinated_Universal_Time) can be appended to the time following the `±[hh]:[mm]` format. However, time offset might be represented with the letter `Z` to indicate the [Zulu time zone](https://en.wikipedia.org/wiki/Military_time_zone).

Example:
```text
my_time_1 = 16:20:59
my_time_2 = 08:15:31Z
my_time_3 = 08:05:28+02:30
```

## Datetime
A datetime follows the `YYYY-MM-DDThh:mm:ss[.mmm]` format. A time offset from [UTC](https://en.wikipedia.org/wiki/Coordinated_Universal_Time) can be appended to the datetime following the `±[hh]:[mm]` format. However, time offset might be represented with the letter `Z` to indicate the [Zulu time zone](https://en.wikipedia.org/wiki/Military_time_zone).

Example:
```text
my_time_1 = 2025-12-25T16:20:59
my_time_2 = 2025-12-25T08:15:31Z
my_time_3 = 2025-12-25T08:05:28+02:30
```

<p align="right"><a href="#readme">Back to top</a></p>

# Embedded binary data
Embedded binary data is a sequence of characters as it would be encoded using [RFC 4648](https://datatracker.ietf.org/doc/html/rfc4648#section-8)'s Base16 encoding. For readability, this sequence can span multiple lines if needed, with each line containing 16 pairs of characters.

The encoded binary data is introduced with the `(bin)` tag.

Example:

```test
embedded_binary_data = (bin)
    48 65 6C 6C 6F 20 57 6F 72 6C 64 20 21 20 48 65
    6C 6C 6F 20 57 6F 72 6C 64 20 21
```
> Aligning 16 pairs of characters per line as seen above is just for readability as the deserializer will remove spaces and newlines. 

<p align="right"><a href="#readme">Back to top</a></p>

# Collections
Although Paradict's root data structure is a dictionary, lists, sets, and dictionaries can be nested within it at arbitrary depth.

## Dictionary
The dictionary data structure can contain any other datatype. It is introduced with the `(dict)` tag.

> The **config** and **data** modes of Paradict differ based on the data type of dictionary keys and the character utilized to separate each key from its corresponding value.

Example:
```text
my_dict = (dict)
    color_1 = 'red'
    color_2 = 'green'
    color_3 = 'blue'
```

## List
The **list** data structure can contain any other datatype. It is introduced with the `(list)` tag.

Example:
```text
my_list = (list)
    'red'
    'green'
    'blue'
```

## Set
The **set** data structure (introduced with the `(set)` tag) can contain any other datatype except:
- another data structure such as another set, a dict, a list,
- an extension object,
- a grid.

Example:
```text
my_set = (set)
    'red'
    'green'
    'blue'
```

<p align="right"><a href="#readme">Back to top</a></p>

# Extension object
To extend the already rich set of data types, Paradict offers an extension mechanism which consists of a dict-like data structure (the extension Object) to hold the data elements which will be consumed by an object builder to create a new data item.

The extension Object is introduced with the `(obj)` tag.

Example:
```text
my_complex = (obj)
    type = 'complex'
    real_part = 1.23
    imag_part = 3.14
```

<br>
<br>
<br>

[Back to top](#readme)
