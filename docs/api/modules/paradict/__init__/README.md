###### Paradict API Reference
[Home](/docs/api/README.md) | [Project](/README.md) | Module | [Source](/src/paradict/__init__.py)

# Module Overview
> Module: **paradict.\_\_init\_\_**

No docstring.

## Fields
- [**All fields**](/docs/api/modules/paradict/__init__/fields.md)
    - CONFIG\_MODE = `'c'`
    - DATA\_MODE = `'d'`

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## Functions
- [**All functions**](/docs/api/modules/paradict/__init__/funcs.md)
    - [decode](/docs/api/modules/paradict/__init__/funcs.md#decode): Convert some textual Paradict data into a Python dictionary
    - [decode\_from](/docs/api/modules/paradict/__init__/funcs.md#decode_from): Open a textual Paradict file then read its contents into Python dict
    - [encode](/docs/api/modules/paradict/__init__/funcs.md#encode): Serialize a Python dict object with the Paradict binary format
    - [encode\_into](/docs/api/modules/paradict/__init__/funcs.md#encode_into): Serialize a Python dict object with the Paradict text format then write it to a file
    - [forge\_bin](/docs/api/modules/paradict/__init__/funcs.md#forge_bin): items are int, bytes, bytearrays, or Nones, returns a bytearray
    - [is\_valid](/docs/api/modules/paradict/__init__/funcs.md#is_valid): This function returns True if the given data successfully validates against the given schema
    - [pack](/docs/api/modules/paradict/__init__/funcs.md#pack): Serialize a Python dict object with the Paradict binary format
    - [pack\_into](/docs/api/modules/paradict/__init__/funcs.md#pack_into): Serialize a Python data object with the Paradict binary format then dump it in a file
    - [scan](/docs/api/modules/paradict/__init__/funcs.md#scan): Scan a binary Paradict file object, yielding a tag with the slice object of its associated payload
    - [split\_kv](/docs/api/modules/paradict/__init__/funcs.md#split_kv): Split a non-empty string into key val. The string should follow one of these format: - data_mode format: key: value - config_mod...
    - [stringify\_bin](/docs/api/modules/paradict/__init__/funcs.md#stringify_bin): Good for debug. Stringify some binary data
    - [unpack](/docs/api/modules/paradict/__init__/funcs.md#unpack): Convert some binary Paradict data into a Python dictionary
    - [unpack\_from](/docs/api/modules/paradict/__init__/funcs.md#unpack_from): Open a binary Paradict file then unpack its contents into Python dict

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## Classes
- [**Datatype**](/docs/api/modules/paradict/__init__/class-Datatype.md): Create a collection of name/value pairs.
    - DICT = `1`
    - LIST = `2`
    - SET = `3`
    - OBJ = `4`
    - GRID = `5`
    - BOOL = `6`
    - STR = `7`
    - BIN = `8`
    - INT = `9`
    - FLOAT = `10`
    - COMPLEX = `11`
    - DATE = `12`
    - TIME = `13`
    - DATETIME = `14`
- [**Decoder**](/docs/api/modules/paradict/__init__/class-Decoder.md): Class to convert some textual Paradict data into a Python dict
    - [data](/docs/api/modules/paradict/__init__/class-Decoder.md#properties-table); _getter_
    - [obj\_builder](/docs/api/modules/paradict/__init__/class-Decoder.md#properties-table); _getter, setter_
    - [queue](/docs/api/modules/paradict/__init__/class-Decoder.md#properties-table); _getter, setter_
    - [receiver](/docs/api/modules/paradict/__init__/class-Decoder.md#properties-table); _getter, setter_
    - [root\_dir](/docs/api/modules/paradict/__init__/class-Decoder.md#properties-table); _getter, setter_
    - [type\_ref](/docs/api/modules/paradict/__init__/class-Decoder.md#properties-table); _getter, setter_
    - [feed](/docs/api/modules/paradict/__init__/class-Decoder.md#feed): Feed the decoder engine with some string.         The string might represent a line in the textual Paradict data,         or an ...
    - [\_check\_key](/docs/api/modules/paradict/__init__/class-Decoder.md#_check_key): No docstring.
    - [\_check\_line](/docs/api/modules/paradict/__init__/class-Decoder.md#_check_line): Check the validity of the indent in the line Returns the indent-less version of line
    - [\_check\_multiline\_tag](/docs/api/modules/paradict/__init__/class-Decoder.md#_check_multiline_tag): No docstring.
    - [\_cleanup\_stack](/docs/api/modules/paradict/__init__/class-Decoder.md#_cleanup_stack): No docstring.
    - [\_consume\_bin\_block](/docs/api/modules/paradict/__init__/class-Decoder.md#_consume_bin_block): No docstring.
    - [\_consume\_grid\_block](/docs/api/modules/paradict/__init__/class-Decoder.md#_consume_grid_block): No docstring.
    - [\_consume\_obj\_block](/docs/api/modules/paradict/__init__/class-Decoder.md#_consume_obj_block): No docstring.
    - [\_consume\_raw\_block](/docs/api/modules/paradict/__init__/class-Decoder.md#_consume_raw_block): No docstring.
    - [\_consume\_str\_block](/docs/api/modules/paradict/__init__/class-Decoder.md#_consume_str_block): No docstring.
    - [\_decode\_bin](/docs/api/modules/paradict/__init__/class-Decoder.md#_decode_bin): No docstring.
    - [\_decode\_bool](/docs/api/modules/paradict/__init__/class-Decoder.md#_decode_bool): No docstring.
    - [\_decode\_complex\_number](/docs/api/modules/paradict/__init__/class-Decoder.md#_decode_complex_number): No docstring.
    - [\_decode\_container](/docs/api/modules/paradict/__init__/class-Decoder.md#_decode_container): No docstring.
    - [\_decode\_date](/docs/api/modules/paradict/__init__/class-Decoder.md#_decode_date): No docstring.
    - [\_decode\_datetime](/docs/api/modules/paradict/__init__/class-Decoder.md#_decode_datetime): No docstring.
    - [\_decode\_float](/docs/api/modules/paradict/__init__/class-Decoder.md#_decode_float): No docstring.
    - [\_decode\_int](/docs/api/modules/paradict/__init__/class-Decoder.md#_decode_int): No docstring.
    - [\_decode\_load\_func](/docs/api/modules/paradict/__init__/class-Decoder.md#_decode_load_func): No docstring.
    - [\_decode\_null](/docs/api/modules/paradict/__init__/class-Decoder.md#_decode_null): No docstring.
    - [\_decode\_str](/docs/api/modules/paradict/__init__/class-Decoder.md#_decode_str): No docstring.
    - [\_decode\_time](/docs/api/modules/paradict/__init__/class-Decoder.md#_decode_time): No docstring.
    - [\_decode\_value](/docs/api/modules/paradict/__init__/class-Decoder.md#_decode_value): No docstring.
    - [\_get\_context](/docs/api/modules/paradict/__init__/class-Decoder.md#_get_context): No docstring.
    - [\_get\_parent\_context](/docs/api/modules/paradict/__init__/class-Decoder.md#_get_parent_context): No docstring.
    - [\_interpret](/docs/api/modules/paradict/__init__/class-Decoder.md#_interpret): No docstring.
    - [\_process](/docs/api/modules/paradict/__init__/class-Decoder.md#_process): No docstring.
    - [\_update\_context](/docs/api/modules/paradict/__init__/class-Decoder.md#_update_context): No docstring.
    - [\_update\_dict\_container](/docs/api/modules/paradict/__init__/class-Decoder.md#_update_dict_container): No docstring.
    - [\_update\_list\_container](/docs/api/modules/paradict/__init__/class-Decoder.md#_update_list_container): No docstring.
    - [\_update\_obj\_container](/docs/api/modules/paradict/__init__/class-Decoder.md#_update_obj_container): No docstring.
    - [\_update\_parent\_context](/docs/api/modules/paradict/__init__/class-Decoder.md#_update_parent_context): No docstring.
    - [\_update\_set\_container](/docs/api/modules/paradict/__init__/class-Decoder.md#_update_set_container): No docstring.
    - [\_update\_stack](/docs/api/modules/paradict/__init__/class-Decoder.md#_update_stack): No docstring.
- [**Encoder**](/docs/api/modules/paradict/__init__/class-Encoder.md): Convert a Python dictionary object to Paradict text format
    - [attachments\_dir](/docs/api/modules/paradict/__init__/class-Encoder.md#properties-table); _getter, setter_
    - [bin\_to\_text](/docs/api/modules/paradict/__init__/class-Encoder.md#properties-table); _getter, setter_
    - [mode](/docs/api/modules/paradict/__init__/class-Encoder.md#properties-table); _getter, setter_
    - [root\_dir](/docs/api/modules/paradict/__init__/class-Encoder.md#properties-table); _getter, setter_
    - [type\_ref](/docs/api/modules/paradict/__init__/class-Encoder.md#properties-table); _getter, setter_
    - [encode](/docs/api/modules/paradict/__init__/class-Encoder.md#encode): Generator for iteratively encoding data by yielding lines of Paradict text format
    - [\_check\_key](/docs/api/modules/paradict/__init__/class-Encoder.md#_check_key): No docstring.
    - [\_encode](/docs/api/modules/paradict/__init__/class-Encoder.md#_encode): No docstring.
    - [\_encode\_bin](/docs/api/modules/paradict/__init__/class-Encoder.md#_encode_bin): No docstring.
    - [\_encode\_bin\_int](/docs/api/modules/paradict/__init__/class-Encoder.md#_encode_bin_int): No docstring.
    - [\_encode\_bool](/docs/api/modules/paradict/__init__/class-Encoder.md#_encode_bool): No docstring.
    - [\_encode\_complex](/docs/api/modules/paradict/__init__/class-Encoder.md#_encode_complex): No docstring.
    - [\_encode\_date](/docs/api/modules/paradict/__init__/class-Encoder.md#_encode_date): No docstring.
    - [\_encode\_datetime](/docs/api/modules/paradict/__init__/class-Encoder.md#_encode_datetime): No docstring.
    - [\_encode\_dict](/docs/api/modules/paradict/__init__/class-Encoder.md#_encode_dict): No docstring.
    - [\_encode\_dict\_and\_obj](/docs/api/modules/paradict/__init__/class-Encoder.md#_encode_dict_and_obj): No docstring.
    - [\_encode\_float](/docs/api/modules/paradict/__init__/class-Encoder.md#_encode_float): No docstring.
    - [\_encode\_grid](/docs/api/modules/paradict/__init__/class-Encoder.md#_encode_grid): No docstring.
    - [\_encode\_hex\_int](/docs/api/modules/paradict/__init__/class-Encoder.md#_encode_hex_int): No docstring.
    - [\_encode\_int](/docs/api/modules/paradict/__init__/class-Encoder.md#_encode_int): No docstring.
    - [\_encode\_list](/docs/api/modules/paradict/__init__/class-Encoder.md#_encode_list): No docstring.
    - [\_encode\_null](/docs/api/modules/paradict/__init__/class-Encoder.md#_encode_null): No docstring.
    - [\_encode\_obj](/docs/api/modules/paradict/__init__/class-Encoder.md#_encode_obj): No docstring.
    - [\_encode\_oct\_int](/docs/api/modules/paradict/__init__/class-Encoder.md#_encode_oct_int): No docstring.
    - [\_encode\_set](/docs/api/modules/paradict/__init__/class-Encoder.md#_encode_set): No docstring.
    - [\_encode\_str](/docs/api/modules/paradict/__init__/class-Encoder.md#_encode_str): No docstring.
    - [\_encode\_time](/docs/api/modules/paradict/__init__/class-Encoder.md#_encode_time): No docstring.
- [**Packer**](/docs/api/modules/paradict/__init__/class-Packer.md): Class to convert some binary Python dict into Paradict binary format
    - [auto\_index](/docs/api/modules/paradict/__init__/class-Packer.md#properties-table); _getter_
    - [dict\_only](/docs/api/modules/paradict/__init__/class-Packer.md#properties-table); _getter_
    - [index\_dict](/docs/api/modules/paradict/__init__/class-Packer.md#properties-table); _getter_
    - [type\_ref](/docs/api/modules/paradict/__init__/class-Packer.md#properties-table); _getter, setter_
    - [pack](/docs/api/modules/paradict/__init__/class-Packer.md#pack): Generator for iteratively packing data by yielding bytes datum forged in Paradict binary format
    - [\_pack](/docs/api/modules/paradict/__init__/class-Packer.md#_pack): No docstring.
    - [\_pack\_bin](/docs/api/modules/paradict/__init__/class-Packer.md#_pack_bin): No docstring.
    - [\_pack\_bin\_int](/docs/api/modules/paradict/__init__/class-Packer.md#_pack_bin_int): No docstring.
    - [\_pack\_bool](/docs/api/modules/paradict/__init__/class-Packer.md#_pack_bool): No docstring.
    - [\_pack\_complex](/docs/api/modules/paradict/__init__/class-Packer.md#_pack_complex): No docstring.
    - [\_pack\_date](/docs/api/modules/paradict/__init__/class-Packer.md#_pack_date): No docstring.
    - [\_pack\_datetime](/docs/api/modules/paradict/__init__/class-Packer.md#_pack_datetime): No docstring.
    - [\_pack\_dict](/docs/api/modules/paradict/__init__/class-Packer.md#_pack_dict): No docstring.
    - [\_pack\_float](/docs/api/modules/paradict/__init__/class-Packer.md#_pack_float): No docstring.
    - [\_pack\_grid](/docs/api/modules/paradict/__init__/class-Packer.md#_pack_grid): No docstring.
    - [\_pack\_hex\_int](/docs/api/modules/paradict/__init__/class-Packer.md#_pack_hex_int): No docstring.
    - [\_pack\_int](/docs/api/modules/paradict/__init__/class-Packer.md#_pack_int): No docstring.
    - [\_pack\_list](/docs/api/modules/paradict/__init__/class-Packer.md#_pack_list): No docstring.
    - [\_pack\_null](/docs/api/modules/paradict/__init__/class-Packer.md#_pack_null): No docstring.
    - [\_pack\_obj](/docs/api/modules/paradict/__init__/class-Packer.md#_pack_obj): No docstring.
    - [\_pack\_oct\_int](/docs/api/modules/paradict/__init__/class-Packer.md#_pack_oct_int): No docstring.
    - [\_pack\_set](/docs/api/modules/paradict/__init__/class-Packer.md#_pack_set): No docstring.
    - [\_pack\_str](/docs/api/modules/paradict/__init__/class-Packer.md#_pack_str): No docstring.
    - [\_pack\_time](/docs/api/modules/paradict/__init__/class-Packer.md#_pack_time): No docstring.
- [**TypeRef**](/docs/api/modules/paradict/__init__/class-TypeRef.md): This class represents a mechanism for customizing Python types allowed for (de)serializing data with Paradict classes and functi...
    - [adapters](/docs/api/modules/paradict/__init__/class-TypeRef.md#properties-table); _getter, setter_
    - [bin\_type](/docs/api/modules/paradict/__init__/class-TypeRef.md#properties-table); _getter, setter_
    - [bin\_types](/docs/api/modules/paradict/__init__/class-TypeRef.md#properties-table); _getter, setter_
    - [bool\_type](/docs/api/modules/paradict/__init__/class-TypeRef.md#properties-table); _getter, setter_
    - [bool\_types](/docs/api/modules/paradict/__init__/class-TypeRef.md#properties-table); _getter, setter_
    - [complex\_type](/docs/api/modules/paradict/__init__/class-TypeRef.md#properties-table); _getter, setter_
    - [complex\_types](/docs/api/modules/paradict/__init__/class-TypeRef.md#properties-table); _getter, setter_
    - [date\_type](/docs/api/modules/paradict/__init__/class-TypeRef.md#properties-table); _getter, setter_
    - [date\_types](/docs/api/modules/paradict/__init__/class-TypeRef.md#properties-table); _getter, setter_
    - [datetime\_type](/docs/api/modules/paradict/__init__/class-TypeRef.md#properties-table); _getter, setter_
    - [datetime\_types](/docs/api/modules/paradict/__init__/class-TypeRef.md#properties-table); _getter, setter_
    - [dict\_type](/docs/api/modules/paradict/__init__/class-TypeRef.md#properties-table); _getter, setter_
    - [dict\_types](/docs/api/modules/paradict/__init__/class-TypeRef.md#properties-table); _getter, setter_
    - [float\_type](/docs/api/modules/paradict/__init__/class-TypeRef.md#properties-table); _getter, setter_
    - [float\_types](/docs/api/modules/paradict/__init__/class-TypeRef.md#properties-table); _getter, setter_
    - [grid\_type](/docs/api/modules/paradict/__init__/class-TypeRef.md#properties-table); _getter, setter_
    - [grid\_types](/docs/api/modules/paradict/__init__/class-TypeRef.md#properties-table); _getter, setter_
    - [int\_type](/docs/api/modules/paradict/__init__/class-TypeRef.md#properties-table); _getter, setter_
    - [int\_types](/docs/api/modules/paradict/__init__/class-TypeRef.md#properties-table); _getter, setter_
    - [list\_type](/docs/api/modules/paradict/__init__/class-TypeRef.md#properties-table); _getter, setter_
    - [list\_types](/docs/api/modules/paradict/__init__/class-TypeRef.md#properties-table); _getter, setter_
    - [obj\_type](/docs/api/modules/paradict/__init__/class-TypeRef.md#properties-table); _getter, setter_
    - [obj\_types](/docs/api/modules/paradict/__init__/class-TypeRef.md#properties-table); _getter, setter_
    - [set\_type](/docs/api/modules/paradict/__init__/class-TypeRef.md#properties-table); _getter, setter_
    - [set\_types](/docs/api/modules/paradict/__init__/class-TypeRef.md#properties-table); _getter, setter_
    - [str\_type](/docs/api/modules/paradict/__init__/class-TypeRef.md#properties-table); _getter, setter_
    - [str\_types](/docs/api/modules/paradict/__init__/class-TypeRef.md#properties-table); _getter, setter_
    - [time\_type](/docs/api/modules/paradict/__init__/class-TypeRef.md#properties-table); _getter, setter_
    - [time\_types](/docs/api/modules/paradict/__init__/class-TypeRef.md#properties-table); _getter, setter_
    - [adapt](/docs/api/modules/paradict/__init__/class-TypeRef.md#adapt): Checks the 'adapters' attribute to find out if there is an adapter function registered for the type of the data argument. Then, ...
    - [check](/docs/api/modules/paradict/__init__/class-TypeRef.md#check): This function accepts as argument a Python type, and return a Datatype instance if the type is supported/registered, else return...
    - [\_create\_map](/docs/api/modules/paradict/__init__/class-TypeRef.md#_create_map): No docstring.
    - [\_update\_types](/docs/api/modules/paradict/__init__/class-TypeRef.md#_update_types): No docstring.
- [**Unpacker**](/docs/api/modules/paradict/__init__/class-Unpacker.md): Class to convert some binary Paradict data into a Python dict
    - [data](/docs/api/modules/paradict/__init__/class-Unpacker.md#properties-table); _getter_
    - [obj\_builder](/docs/api/modules/paradict/__init__/class-Unpacker.md#properties-table); _getter, setter_
    - [queue](/docs/api/modules/paradict/__init__/class-Unpacker.md#properties-table); _getter, setter_
    - [receiver](/docs/api/modules/paradict/__init__/class-Unpacker.md#properties-table); _getter, setter_
    - [type\_ref](/docs/api/modules/paradict/__init__/class-Unpacker.md#properties-table); _getter, setter_
    - [feed](/docs/api/modules/paradict/__init__/class-Unpacker.md#feed): Feed in arbitrary chunks of data
    - [process](/docs/api/modules/paradict/__init__/class-Unpacker.md#process): Pass in a tag and its associated payload
    - [\_cleanup\_stack](/docs/api/modules/paradict/__init__/class-Unpacker.md#_cleanup_stack): No docstring.
    - [\_consume\_block](/docs/api/modules/paradict/__init__/class-Unpacker.md#_consume_block): No docstring.
    - [\_create\_alpha\_context](/docs/api/modules/paradict/__init__/class-Unpacker.md#_create_alpha_context): No docstring.
    - [\_create\_beta\_context](/docs/api/modules/paradict/__init__/class-Unpacker.md#_create_beta_context): No docstring.
    - [\_create\_context](/docs/api/modules/paradict/__init__/class-Unpacker.md#_create_context): No docstring.
    - [\_get\_context](/docs/api/modules/paradict/__init__/class-Unpacker.md#_get_context): No docstring.
    - [\_interpret](/docs/api/modules/paradict/__init__/class-Unpacker.md#_interpret): No docstring.
    - [\_remove\_block](/docs/api/modules/paradict/__init__/class-Unpacker.md#_remove_block): No docstring.
    - [\_remove\_context](/docs/api/modules/paradict/__init__/class-Unpacker.md#_remove_context): No docstring.
    - [\_unpack\_bin](/docs/api/modules/paradict/__init__/class-Unpacker.md#_unpack_bin): No docstring.
    - [\_unpack\_bin\_int](/docs/api/modules/paradict/__init__/class-Unpacker.md#_unpack_bin_int): No docstring.
    - [\_unpack\_bool](/docs/api/modules/paradict/__init__/class-Unpacker.md#_unpack_bool): No docstring.
    - [\_unpack\_complex](/docs/api/modules/paradict/__init__/class-Unpacker.md#_unpack_complex): No docstring.
    - [\_unpack\_date](/docs/api/modules/paradict/__init__/class-Unpacker.md#_unpack_date): No docstring.
    - [\_unpack\_datetime](/docs/api/modules/paradict/__init__/class-Unpacker.md#_unpack_datetime): No docstring.
    - [\_unpack\_float](/docs/api/modules/paradict/__init__/class-Unpacker.md#_unpack_float): No docstring.
    - [\_unpack\_float\_misc](/docs/api/modules/paradict/__init__/class-Unpacker.md#_unpack_float_misc): No docstring.
    - [\_unpack\_grid](/docs/api/modules/paradict/__init__/class-Unpacker.md#_unpack_grid): No docstring.
    - [\_unpack\_hex\_int](/docs/api/modules/paradict/__init__/class-Unpacker.md#_unpack_hex_int): No docstring.
    - [\_unpack\_int](/docs/api/modules/paradict/__init__/class-Unpacker.md#_unpack_int): No docstring.
    - [\_unpack\_null](/docs/api/modules/paradict/__init__/class-Unpacker.md#_unpack_null): No docstring.
    - [\_unpack\_obj](/docs/api/modules/paradict/__init__/class-Unpacker.md#_unpack_obj): No docstring.
    - [\_unpack\_oct\_int](/docs/api/modules/paradict/__init__/class-Unpacker.md#_unpack_oct_int): No docstring.
    - [\_unpack\_payload](/docs/api/modules/paradict/__init__/class-Unpacker.md#_unpack_payload): No docstring.
    - [\_unpack\_str](/docs/api/modules/paradict/__init__/class-Unpacker.md#_unpack_str): No docstring.
    - [\_unpack\_time](/docs/api/modules/paradict/__init__/class-Unpacker.md#_unpack_time): No docstring.
    - [\_update\_context](/docs/api/modules/paradict/__init__/class-Unpacker.md#_update_context): No docstring.
- [**Validator**](/docs/api/modules/paradict/__init__/class-Validator.md): Class to validate data against a schema
    - [schema](/docs/api/modules/paradict/__init__/class-Validator.md#properties-table); _getter_
    - [type\_ref](/docs/api/modules/paradict/__init__/class-Validator.md#properties-table); _getter_
    - [validate](/docs/api/modules/paradict/__init__/class-Validator.md#validate): Validate data. Might raise a validation error
    - [\_ensure\_spec](/docs/api/modules/paradict/__init__/class-Validator.md#_ensure_spec): No docstring.
    - [\_validate](/docs/api/modules/paradict/__init__/class-Validator.md#_validate): No docstring.
    - [\_validate\_datatype](/docs/api/modules/paradict/__init__/class-Validator.md#_validate_datatype): No docstring.
    - [\_validate\_dict](/docs/api/modules/paradict/__init__/class-Validator.md#_validate_dict): No docstring.
    - [\_validate\_list](/docs/api/modules/paradict/__init__/class-Validator.md#_validate_list): Schema SHOULD be a list
    - [\_validate\_obj](/docs/api/modules/paradict/__init__/class-Validator.md#_validate_obj): No docstring.
    - [\_validate\_set](/docs/api/modules/paradict/__init__/class-Validator.md#_validate_set): Schema SHOULD be a set

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>
