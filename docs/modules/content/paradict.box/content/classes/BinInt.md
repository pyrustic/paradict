Back to [All Modules](https://github.com/pyrustic/paradict/blob/master/docs/modules/README.md#readme)

# Module Overview

**paradict.box**
 
Boxes to hold comments, grids, hexadecimal integers, et cetera

> **Classes:** &nbsp; [BinInt](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.box/content/classes/BinInt.md#class-binint) &nbsp;&nbsp; [Comment](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.box/content/classes/Comment.md#class-comment) &nbsp;&nbsp; [CommentID](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.box/content/classes/CommentID.md#class-commentid) &nbsp;&nbsp; [Grid](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.box/content/classes/Grid.md#class-grid) &nbsp;&nbsp; [HexInt](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.box/content/classes/HexInt.md#class-hexint) &nbsp;&nbsp; [Obj](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.box/content/classes/Obj.md#class-obj) &nbsp;&nbsp; [OctInt](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.box/content/classes/OctInt.md#class-octint)
>
> **Functions:** &nbsp; None
>
> **Constants:** &nbsp; None

# Class BinInt
Box to hold binary integer

## Base Classes
int

## Class Attributes
denominator (inherited from int) &nbsp;&nbsp; imag (inherited from int) &nbsp;&nbsp; numerator (inherited from int) &nbsp;&nbsp; real (inherited from int)

## Class Properties


# All Methods
[as\_integer\_ratio](#as_integer_ratio) &nbsp;&nbsp; [bit\_length](#bit_length) &nbsp;&nbsp; [from\_bytes](#from_bytes) &nbsp;&nbsp; [to\_bytes](#to_bytes)

## as\_integer\_ratio
Return integer ratio.

Return a pair of integers, whose ratio is exactly equal to the original int
and with a positive denominator.

>>> (10).as_integer_ratio()
(10, 1)
>>> (-10).as_integer_ratio()
(-10, 1)
>>> (0).as_integer_ratio()
(0, 1)

**Inherited from:** int

**Signature:** (self, /)





**Return Value:** None

[Back to Top](#module-overview)


## bit\_length
Number of bits necessary to represent self in binary.

>>> bin(37)
'0b100101'
>>> (37).bit_length()
6

**Inherited from:** int

**Signature:** (self, /)





**Return Value:** None

[Back to Top](#module-overview)


## from\_bytes
Return the integer represented by the given array of bytes.

bytes
  Holds the array of bytes to convert.  The argument must either
  support the buffer protocol or be an iterable object producing bytes.
  Bytes and bytearray are examples of built-in objects that support the
  buffer protocol.
byteorder
  The byte order used to represent the integer.  If byteorder is 'big',
  the most significant byte is at the beginning of the byte array.  If
  byteorder is 'little', the most significant byte is at the end of the
  byte array.  To request the native byte order of the host system, use
  `sys.byteorder' as the byte order value.
signed
  Indicates whether two's complement is used to represent the integer.

**Inherited from:** int

**Signature:** (type, /, bytes, byteorder, \*, signed=False)





**Return Value:** None

[Back to Top](#module-overview)


## to\_bytes
Return an array of bytes representing an integer.

length
  Length of bytes object to use.  An OverflowError is raised if the
  integer is not representable with the given number of bytes.
byteorder
  The byte order used to represent the integer.  If byteorder is 'big',
  the most significant byte is at the beginning of the byte array.  If
  byteorder is 'little', the most significant byte is at the end of the
  byte array.  To request the native byte order of the host system, use
  `sys.byteorder' as the byte order value.
signed
  Determines whether two's complement is used to represent the integer.
  If signed is False and a negative integer is given, an OverflowError
  is raised.

**Inherited from:** int

**Signature:** (self, /, length, byteorder, \*, signed=False)





**Return Value:** None

[Back to Top](#module-overview)



