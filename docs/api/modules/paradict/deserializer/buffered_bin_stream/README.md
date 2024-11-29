###### Paradict API Reference
[Home](/docs/api/README.md) | [Project](/README.md) | Module | [Source](/src/paradict/deserializer/buffered_bin_stream.py)

# Module Overview
> Module: **paradict.deserializer.buffered\_bin\_stream**

A FIFO queue for processing binary Paradict data

## Classes
- [**BufferedBinStream**](/docs/api/modules/paradict/deserializer/buffered_bin_stream/class-BufferedBinStream.md): A FIFO queue for processing binary Paradict data
    - [buffer](/docs/api/modules/paradict/deserializer/buffered_bin_stream/class-BufferedBinStream.md#properties-table); _getter_
    - [get](/docs/api/modules/paradict/deserializer/buffered_bin_stream/class-BufferedBinStream.md#get): No docstring.
    - [get\_all](/docs/api/modules/paradict/deserializer/buffered_bin_stream/class-BufferedBinStream.md#get_all): Generator for iteratively getting each tag-payload tuple composing the raw data stored in the buffer
    - [is\_empty](/docs/api/modules/paradict/deserializer/buffered_bin_stream/class-BufferedBinStream.md#is_empty): No docstring.
    - [put](/docs/api/modules/paradict/deserializer/buffered_bin_stream/class-BufferedBinStream.md#put): Store binary data in the buffer. This data will then be iteratively extracted by the 'get' method
    - [\_clear\_status](/docs/api/modules/paradict/deserializer/buffered_bin_stream/class-BufferedBinStream.md#_clear_status): No docstring.
    - [\_read](/docs/api/modules/paradict/deserializer/buffered_bin_stream/class-BufferedBinStream.md#_read): No docstring.
    - [\_read\_buffer](/docs/api/modules/paradict/deserializer/buffered_bin_stream/class-BufferedBinStream.md#_read_buffer): No docstring.
    - [\_update\_expected\_width\_var](/docs/api/modules/paradict/deserializer/buffered_bin_stream/class-BufferedBinStream.md#_update_expected_width_var): No docstring.
    - [\_update\_tag\_var](/docs/api/modules/paradict/deserializer/buffered_bin_stream/class-BufferedBinStream.md#_update_tag_var): No docstring.

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>
