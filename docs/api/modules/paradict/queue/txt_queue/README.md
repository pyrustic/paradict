###### Paradict API Reference
[Home](/docs/api/README.md) | [Project](/README.md) | Module | [Source](/paradict/queue/txt_queue.py)

# Module Overview
> Module: **paradict.queue.txt\_queue**

A FIFO queue for processing textual Paradict data

## Classes
- [**TxtQueue**](/docs/api/modules/paradict/queue/txt_queue/class-TxtQueue.md): A FIFO queue for processing textual Paradict data
    - [buffer](/docs/api/modules/paradict/queue/txt_queue/class-TxtQueue.md#properties-table); _getter_
    - [dequeue](/docs/api/modules/paradict/queue/txt_queue/class-TxtQueue.md#dequeue): Generator for iteratively getting each line composing the         textual data stored in the buffer.         Note that lines yie...
    - [enqueue](/docs/api/modules/paradict/queue/txt_queue/class-TxtQueue.md#enqueue): Store textual data in the buffer. This data will then be iteratively         extracted by the 'get' method, line by line.       ...
    - [\_read](/docs/api/modules/paradict/queue/txt_queue/class-TxtQueue.md#_read): No docstring.

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>
