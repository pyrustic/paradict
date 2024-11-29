###### Paradict API Reference
[Home](/docs/api/README.md) | [Project](/README.md) | Module | [Source](/src/paradict/deserializer/buffered_text_stream.py)

# Module Overview
> Module: **paradict.deserializer.buffered\_text\_stream**

A FIFO queue for processing textual Paradict data

## Classes
- [**BufferedTextStream**](/docs/api/modules/paradict/deserializer/buffered_text_stream/class-BufferedTextStream.md): A FIFO queue for processing textual Paradict data
    - [get](/docs/api/modules/paradict/deserializer/buffered_text_stream/class-BufferedTextStream.md#get): No docstring.
    - [get\_all](/docs/api/modules/paradict/deserializer/buffered_text_stream/class-BufferedTextStream.md#get_all): Generator for iteratively getting each line composing the         textual data stored in the buffer.         Note that lines yie...
    - [is\_empty](/docs/api/modules/paradict/deserializer/buffered_text_stream/class-BufferedTextStream.md#is_empty): No docstring.
    - [put](/docs/api/modules/paradict/deserializer/buffered_text_stream/class-BufferedTextStream.md#put): Store textual data in the buffer. This data will then be iteratively         extracted by the 'get' method, line by line.       ...

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>
