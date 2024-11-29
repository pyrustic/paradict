###### Paradict API Reference
[Home](/docs/api/README.md) | [Project](/README.md) | [Module](/docs/api/modules/paradict/deserializer/scanner/README.md) | [Source](/src/paradict/deserializer/scanner.py)

# Functions within module
> Module: [paradict.deserializer.scanner](/docs/api/modules/paradict/deserializer/scanner/README.md)

Here are functions exposed in the module:
- [get\_slice\_for\_fixed\_length\_datum](#get_slice_for_fixed_length_datum)
- [get\_slice\_for\_variable\_length\_datum](#get_slice_for_variable_length_datum)
- [process\_bin](#process_bin)
- [process\_nint\_big](#process_nint_big)
- [process\_nint\_heavy](#process_nint_heavy)
- [process\_nintx](#process_nintx)
- [process\_pint\_big](#process_pint_big)
- [process\_pint\_heavy](#process_pint_heavy)
- [process\_pintx](#process_pintx)
- [process\_str](#process_str)
- [process\_strx](#process_strx)
- [process\_tag](#process_tag)
- [read\_payload\_size](#read_payload_size)
- [scan](#scan)

## get\_slice\_for\_fixed\_length\_datum
This function returns the slice object for
datums with fixed-length payload

```python
def get_slice_for_fixed_length_datum(file, payload_size):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## get\_slice\_for\_variable\_length\_datum
This function is used to generate a slice object for
tags with variable-length payload such as:
STR_SHORT, STR_MEDIUM, STR_LONG, STR_BIG, STR_HEAVY,
BIN_SHORT, BIN_MEDIUM, BIN_LONG, BIN_BIG, and BIN_HEAVY.

nb is the number of bytes encoding the size of payload

This function returns a slice object

```python
def get_slice_for_variable_length_datum(file, nb):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## process\_bin
No docstring

```python
def process_bin(file, tag):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## process\_nint\_big
No docstring

```python
def process_nint_big(file, tag):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## process\_nint\_heavy
No docstring

```python
def process_nint_heavy(file, tag):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## process\_nintx
No docstring

```python
def process_nintx(file, tag):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## process\_pint\_big
No docstring

```python
def process_pint_big(file, tag):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## process\_pint\_heavy
No docstring

```python
def process_pint_heavy(file, tag):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## process\_pintx
No docstring

```python
def process_pintx(file, tag):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## process\_str
No docstring

```python
def process_str(file, tag):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## process\_strx
No docstring

```python
def process_strx(file, tag):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## process\_tag
No docstring

```python
def process_tag(file, tag):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## read\_payload\_size
Read the expected size of payload
Note that nb is the number of bytes encoding the size of payload

```python
def read_payload_size(file, nb):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## scan
Scan a binary Paradict file object, yielding a tag with
the slice object of its associated payload

```python
def scan(file):
    ...
```

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>
