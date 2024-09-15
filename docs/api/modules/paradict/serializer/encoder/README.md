###### Paradict API Reference
[Home](/docs/api/README.md) | [Project](/README.md) | Module | [Source](/paradict/serializer/encoder.py)

# Module Overview
> Module: **paradict.serializer.encoder**

No docstring.

## Fields
- [**All fields**](/docs/api/modules/paradict/serializer/encoder/fields.md)
    - base64 = `<module 'base64' from '/usr/local/lib/python3.12/base64.py'>`
    - const = `<module 'paradict.const' from '/home/alex/PycharmProjects/paradict/paradict/const/__init__.py'>`
    - errors = `<module 'paradict.errors' from '/home/alex/PycharmProjects/paradict/paradict/errors/__init__.py'>`
    - misc = `<module 'paradict.misc' from '/home/alex/PycharmProjects/paradict/paradict/misc/__init__.py'>`
    - os = `<module 'os' (frozen)>`
    - re = `<module 're' from '/usr/local/lib/python3.12/re/__init__.py'>`

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## Functions
- [**All functions**](/docs/api/modules/paradict/serializer/encoder/funcs.md)
    - [encode\_bin](/docs/api/modules/paradict/serializer/encoder/funcs.md#encode_bin): No docstring.
    - [encode\_bin\_int](/docs/api/modules/paradict/serializer/encoder/funcs.md#encode_bin_int): No docstring.
    - [encode\_bool](/docs/api/modules/paradict/serializer/encoder/funcs.md#encode_bool): No docstring.
    - [encode\_complex](/docs/api/modules/paradict/serializer/encoder/funcs.md#encode_complex): No docstring.
    - [encode\_date](/docs/api/modules/paradict/serializer/encoder/funcs.md#encode_date): Parse date and time with the ISO 8601 format
    - [encode\_datetime](/docs/api/modules/paradict/serializer/encoder/funcs.md#encode_datetime): No docstring.
    - [encode\_float](/docs/api/modules/paradict/serializer/encoder/funcs.md#encode_float): No docstring.
    - [encode\_hex\_int](/docs/api/modules/paradict/serializer/encoder/funcs.md#encode_hex_int): No docstring.
    - [encode\_int](/docs/api/modules/paradict/serializer/encoder/funcs.md#encode_int): No docstring.
    - [encode\_multiline\_str](/docs/api/modules/paradict/serializer/encoder/funcs.md#encode_multiline_str): No docstring.
    - [encode\_null](/docs/api/modules/paradict/serializer/encoder/funcs.md#encode_null): No docstring.
    - [encode\_oct\_int](/docs/api/modules/paradict/serializer/encoder/funcs.md#encode_oct_int): No docstring.
    - [encode\_str](/docs/api/modules/paradict/serializer/encoder/funcs.md#encode_str): No docstring.
    - [encode\_time](/docs/api/modules/paradict/serializer/encoder/funcs.md#encode_time): No docstring.

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## Classes
- [**Context**](/docs/api/modules/paradict/serializer/encoder/class-Context.md): Context(name, collection, indents)
    - name: Alias for field number 0
    - collection: Alias for field number 1
    - indents: Alias for field number 2
- [**Encoder**](/docs/api/modules/paradict/serializer/encoder/class-Encoder.md): Convert a Python dictionary object to Paradict text format
    - [attachments\_dir](/docs/api/modules/paradict/serializer/encoder/class-Encoder.md#properties-table); _getter, setter_
    - [bin\_to\_text](/docs/api/modules/paradict/serializer/encoder/class-Encoder.md#properties-table); _getter, setter_
    - [mode](/docs/api/modules/paradict/serializer/encoder/class-Encoder.md#properties-table); _getter, setter_
    - [root\_dir](/docs/api/modules/paradict/serializer/encoder/class-Encoder.md#properties-table); _getter, setter_
    - [skip\_comments](/docs/api/modules/paradict/serializer/encoder/class-Encoder.md#properties-table); _getter, setter_
    - [type\_ref](/docs/api/modules/paradict/serializer/encoder/class-Encoder.md#properties-table); _getter, setter_
    - [encode](/docs/api/modules/paradict/serializer/encoder/class-Encoder.md#encode): Generator for iteratively encoding data by yielding lines of Paradict text format
    - [\_check\_key](/docs/api/modules/paradict/serializer/encoder/class-Encoder.md#_check_key): No docstring.
    - [\_encode](/docs/api/modules/paradict/serializer/encoder/class-Encoder.md#_encode): No docstring.
    - [\_encode\_bin](/docs/api/modules/paradict/serializer/encoder/class-Encoder.md#_encode_bin): No docstring.
    - [\_encode\_bin\_int](/docs/api/modules/paradict/serializer/encoder/class-Encoder.md#_encode_bin_int): No docstring.
    - [\_encode\_bool](/docs/api/modules/paradict/serializer/encoder/class-Encoder.md#_encode_bool): No docstring.
    - [\_encode\_comment](/docs/api/modules/paradict/serializer/encoder/class-Encoder.md#_encode_comment): No docstring.
    - [\_encode\_complex](/docs/api/modules/paradict/serializer/encoder/class-Encoder.md#_encode_complex): No docstring.
    - [\_encode\_date](/docs/api/modules/paradict/serializer/encoder/class-Encoder.md#_encode_date): No docstring.
    - [\_encode\_datetime](/docs/api/modules/paradict/serializer/encoder/class-Encoder.md#_encode_datetime): No docstring.
    - [\_encode\_dict](/docs/api/modules/paradict/serializer/encoder/class-Encoder.md#_encode_dict): No docstring.
    - [\_encode\_dict\_and\_obj](/docs/api/modules/paradict/serializer/encoder/class-Encoder.md#_encode_dict_and_obj): No docstring.
    - [\_encode\_float](/docs/api/modules/paradict/serializer/encoder/class-Encoder.md#_encode_float): No docstring.
    - [\_encode\_grid](/docs/api/modules/paradict/serializer/encoder/class-Encoder.md#_encode_grid): No docstring.
    - [\_encode\_hex\_int](/docs/api/modules/paradict/serializer/encoder/class-Encoder.md#_encode_hex_int): No docstring.
    - [\_encode\_int](/docs/api/modules/paradict/serializer/encoder/class-Encoder.md#_encode_int): No docstring.
    - [\_encode\_list](/docs/api/modules/paradict/serializer/encoder/class-Encoder.md#_encode_list): No docstring.
    - [\_encode\_null](/docs/api/modules/paradict/serializer/encoder/class-Encoder.md#_encode_null): No docstring.
    - [\_encode\_obj](/docs/api/modules/paradict/serializer/encoder/class-Encoder.md#_encode_obj): No docstring.
    - [\_encode\_oct\_int](/docs/api/modules/paradict/serializer/encoder/class-Encoder.md#_encode_oct_int): No docstring.
    - [\_encode\_set](/docs/api/modules/paradict/serializer/encoder/class-Encoder.md#_encode_set): No docstring.
    - [\_encode\_str](/docs/api/modules/paradict/serializer/encoder/class-Encoder.md#_encode_str): No docstring.
    - [\_encode\_time](/docs/api/modules/paradict/serializer/encoder/class-Encoder.md#_encode_time): No docstring.

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>
