###### Paradict API Reference
[Home](/docs/api/README.md) | [Project](/README.md) | Module | [Source](/src/paradict/deserializer/scanner.py)

# Module Overview
> Module: **paradict.deserializer.scanner**

No docstring.

## Fields
- [**All fields**](/docs/api/modules/paradict/deserializer/scanner/fields.md)
    - BIN\_TO\_SIZE = `{b'(': 1, b')': 2, b'*': 3, b'+': 4, b',': 5}`
    - NINT\_TO\_SIZE = `{b'7': 1, b'8': 2, b'9': 3, b':': 4, b';': 5, b'<': 6, b'=': 7, b'>': 8}`
    - PINT\_TO\_SIZE = `{b'-': 1, b'.': 2, b'/': 3, b'0': 4, b'1': 5, b'2': 6, b'3': 7, b'4': 8}`
    - STR\_TO\_SIZE = `{b'A': 1, b'B': 2, b'C': 3, b'D': 4, b'E': 5, b'F': 6, b'G': 7, b'H': 8, b'I': 9, b'J': 10, b'K': 11, b'L': 12, b'M': 13, b'N': 14, b'O': 15, b'P': 16, b'Q': 17, b'R': 18, b'S': 19, b'T': 20, b'U': 21, b'V': 22, b'W': 23, b'X': 24, b'Y': 25, b'Z': 26, b'[': 27, b'\\': 28, b']': 29, b'^': 30, b'_': 31, b'`': 32}`
    - VARSTR\_TO\_SIZE = `{b'b': 1, b'c': 2, b'd': 3, b'e': 4, b'f': 5}`
    - os = `<module 'os' (frozen)>`
    - paradict = `<module 'paradict' from '/home/alex/PycharmProjects/paradict/src/paradict/__init__.py'>`
    - tags = `<module 'paradict.tags' from '/home/alex/PycharmProjects/paradict/src/paradict/tags/__init__.py'>`

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## Functions
- [**All functions**](/docs/api/modules/paradict/deserializer/scanner/funcs.md)
    - [get\_slice\_for\_fixed\_length\_datum](/docs/api/modules/paradict/deserializer/scanner/funcs.md#get_slice_for_fixed_length_datum): This function returns the slice object for datums with fixed-length payload
    - [get\_slice\_for\_variable\_length\_datum](/docs/api/modules/paradict/deserializer/scanner/funcs.md#get_slice_for_variable_length_datum): This function is used to generate a slice object for tags with variable-length payload such as: STR_SHORT, STR_MEDIUM, STR_LONG,...
    - [process\_bin](/docs/api/modules/paradict/deserializer/scanner/funcs.md#process_bin): No docstring.
    - [process\_nint\_big](/docs/api/modules/paradict/deserializer/scanner/funcs.md#process_nint_big): No docstring.
    - [process\_nint\_heavy](/docs/api/modules/paradict/deserializer/scanner/funcs.md#process_nint_heavy): No docstring.
    - [process\_nintx](/docs/api/modules/paradict/deserializer/scanner/funcs.md#process_nintx): No docstring.
    - [process\_pint\_big](/docs/api/modules/paradict/deserializer/scanner/funcs.md#process_pint_big): No docstring.
    - [process\_pint\_heavy](/docs/api/modules/paradict/deserializer/scanner/funcs.md#process_pint_heavy): No docstring.
    - [process\_pintx](/docs/api/modules/paradict/deserializer/scanner/funcs.md#process_pintx): No docstring.
    - [process\_str](/docs/api/modules/paradict/deserializer/scanner/funcs.md#process_str): No docstring.
    - [process\_strx](/docs/api/modules/paradict/deserializer/scanner/funcs.md#process_strx): No docstring.
    - [process\_tag](/docs/api/modules/paradict/deserializer/scanner/funcs.md#process_tag): No docstring.
    - [read\_payload\_size](/docs/api/modules/paradict/deserializer/scanner/funcs.md#read_payload_size): Read the expected size of payload Note that nb is the number of bytes encoding the size of payload
    - [scan](/docs/api/modules/paradict/deserializer/scanner/funcs.md#scan): Scan a binary Paradict file object, yielding a tag with the slice object of its associated payload

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>
