###### Paradict API Reference
[Home](/docs/api/README.md) | [Project](/README.md) | Module | [Source](/paradict/queue/bin_queue.py)

# Module Overview
> Module: **paradict.queue.bin\_queue**

A FIFO queue for processing binary Paradict data

## Classes
- [**BinQueue**](/docs/api/modules/paradict/queue/bin_queue/class-BinQueue.md): A FIFO queue for processing binary Paradict data
    - [buffer](/docs/api/modules/paradict/queue/bin_queue/class-BinQueue.md#properties-table); _getter_
    - [dequeue](/docs/api/modules/paradict/queue/bin_queue/class-BinQueue.md#dequeue): Generator for iteratively getting each tag-payload tuple composing the raw data stored in the buffer
    - [enqueue](/docs/api/modules/paradict/queue/bin_queue/class-BinQueue.md#enqueue): Store binary data in the buffer. This data will then be iteratively extracted by the 'get' method
    - [\_clear\_status](/docs/api/modules/paradict/queue/bin_queue/class-BinQueue.md#_clear_status): No docstring.
    - [\_read](/docs/api/modules/paradict/queue/bin_queue/class-BinQueue.md#_read): No docstring.
    - [\_read\_buffer](/docs/api/modules/paradict/queue/bin_queue/class-BinQueue.md#_read_buffer): No docstring.
    - [\_update\_expected\_width\_var](/docs/api/modules/paradict/queue/bin_queue/class-BinQueue.md#_update_expected_width_var): No docstring.
    - [\_update\_tag\_var](/docs/api/modules/paradict/queue/bin_queue/class-BinQueue.md#_update_tag_var): No docstring.

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>
