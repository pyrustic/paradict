Back to [All Modules](https://github.com/pyrustic/paradict/blob/master/docs/modules/README.md#readme)

# Module Overview

**paradict.box**
 
Boxes to hold comments, grids, hexadecimal integers, et cetera

> **Classes:** &nbsp; [BinInt](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.box/content/classes/BinInt.md#class-binint) &nbsp;&nbsp; [Comment](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.box/content/classes/Comment.md#class-comment) &nbsp;&nbsp; [CommentID](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.box/content/classes/CommentID.md#class-commentid) &nbsp;&nbsp; [Grid](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.box/content/classes/Grid.md#class-grid) &nbsp;&nbsp; [HexInt](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.box/content/classes/HexInt.md#class-hexint) &nbsp;&nbsp; [Obj](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.box/content/classes/Obj.md#class-obj) &nbsp;&nbsp; [OctInt](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.box/content/classes/OctInt.md#class-octint)
>
> **Functions:** &nbsp; None
>
> **Constants:** &nbsp; None

# Class Grid
Box to hold a grid. A grid is made of numbers and should
be consistent (rows should be of same size)

Example:
    # a grid with 2 rows and 3 columns
    my_grid = Grid([(0, 1, 0),
                    (1, 0, 1)])

## Base Classes
list

## Class Attributes
No class attributes.

## Class Properties


# All Methods
[\_\_init\_\_](#__init__) &nbsp;&nbsp; [append](#append) &nbsp;&nbsp; [clear](#clear) &nbsp;&nbsp; [copy](#copy) &nbsp;&nbsp; [count](#count) &nbsp;&nbsp; [extend](#extend) &nbsp;&nbsp; [index](#index) &nbsp;&nbsp; [insert](#insert) &nbsp;&nbsp; [pop](#pop) &nbsp;&nbsp; [remove](#remove) &nbsp;&nbsp; [reverse](#reverse) &nbsp;&nbsp; [sort](#sort)

## \_\_init\_\_
Initialize self.  See help(type(self)) for accurate signature.

**Inherited from:** list

**Signature:** (self, /, \*args, \*\*kwargs)





**Return Value:** None

[Back to Top](#module-overview)


## append
Append object to the end of the list.

**Inherited from:** list

**Signature:** (self, object, /)





**Return Value:** None

[Back to Top](#module-overview)


## clear
Remove all items from list.

**Inherited from:** list

**Signature:** (self, /)





**Return Value:** None

[Back to Top](#module-overview)


## copy
Return a shallow copy of the list.

**Inherited from:** list

**Signature:** (self, /)





**Return Value:** None

[Back to Top](#module-overview)


## count
Return number of occurrences of value.

**Inherited from:** list

**Signature:** (self, value, /)





**Return Value:** None

[Back to Top](#module-overview)


## extend
Extend list by appending elements from the iterable.

**Inherited from:** list

**Signature:** (self, iterable, /)





**Return Value:** None

[Back to Top](#module-overview)


## index
Return first index of value.

Raises ValueError if the value is not present.

**Inherited from:** list

**Signature:** (self, value, start=0, stop=9223372036854775807, /)





**Return Value:** None

[Back to Top](#module-overview)


## insert
Insert object before index.

**Inherited from:** list

**Signature:** (self, index, object, /)





**Return Value:** None

[Back to Top](#module-overview)


## pop
Remove and return item at index (default last).

Raises IndexError if list is empty or index is out of range.

**Inherited from:** list

**Signature:** (self, index=-1, /)





**Return Value:** None

[Back to Top](#module-overview)


## remove
Remove first occurrence of value.

Raises ValueError if the value is not present.

**Inherited from:** list

**Signature:** (self, value, /)





**Return Value:** None

[Back to Top](#module-overview)


## reverse
Reverse *IN PLACE*.

**Inherited from:** list

**Signature:** (self, /)





**Return Value:** None

[Back to Top](#module-overview)


## sort
Sort the list in ascending order and return None.

The sort is in-place (i.e. the list itself is modified) and stable (i.e. the
order of two equal elements is maintained).

If a key function is given, apply it once to each list item and sort them,
ascending or descending, according to their function values.

The reverse flag can be set to sort in descending order.

**Inherited from:** list

**Signature:** (self, /, \*, key=None, reverse=False)





**Return Value:** None

[Back to Top](#module-overview)



