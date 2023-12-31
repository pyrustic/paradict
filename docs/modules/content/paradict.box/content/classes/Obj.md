Back to [All Modules](https://github.com/pyrustic/paradict/blob/master/docs/modules/README.md#readme)

# Module Overview

**paradict.box**
 
Boxes to hold comments, grids, hexadecimal integers, et cetera

> **Classes:** &nbsp; [BinInt](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.box/content/classes/BinInt.md#class-binint) &nbsp;&nbsp; [Command](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.box/content/classes/Command.md#class-command) &nbsp;&nbsp; [Comment](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.box/content/classes/Comment.md#class-comment) &nbsp;&nbsp; [CommentID](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.box/content/classes/CommentID.md#class-commentid) &nbsp;&nbsp; [Grid](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.box/content/classes/Grid.md#class-grid) &nbsp;&nbsp; [HexInt](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.box/content/classes/HexInt.md#class-hexint) &nbsp;&nbsp; [Obj](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.box/content/classes/Obj.md#class-obj) &nbsp;&nbsp; [OctInt](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.box/content/classes/OctInt.md#class-octint)
>
> **Functions:** &nbsp; None
>
> **Constants:** &nbsp; None

# Class Obj
Box to hold an Extension Object. Such objects behave like a dictionary.
An object builder is passed as argument to the right functions, thus,
the object is consumed/used to build a new valid data value

## Base Classes
dict

## Class Attributes
No class attributes.

## Class Properties


# All Methods
[\_\_init\_\_](#__init__) &nbsp;&nbsp; [fromkeys](#fromkeys) &nbsp;&nbsp; [get](#get) &nbsp;&nbsp; [popitem](#popitem) &nbsp;&nbsp; [setdefault](#setdefault)

## \_\_init\_\_
Initialize self.  See help(type(self)) for accurate signature.

**Inherited from:** dict

**Signature:** (self, /, \*args, \*\*kwargs)





**Return Value:** None

[Back to Top](#module-overview)


## fromkeys
Create a new dictionary with keys from iterable and values set to value.

**Inherited from:** dict

**Signature:** (type, iterable, value=None, /)





**Return Value:** None

[Back to Top](#module-overview)


## get
Return the value for key if key is in the dictionary, else default.

**Inherited from:** dict

**Signature:** (self, key, default=None, /)





**Return Value:** None

[Back to Top](#module-overview)


## popitem
Remove and return a (key, value) pair as a 2-tuple.

Pairs are returned in LIFO (last-in, first-out) order.
Raises KeyError if the dict is empty.

**Inherited from:** dict

**Signature:** (self, /)





**Return Value:** None

[Back to Top](#module-overview)


## setdefault
Insert key with a value of default if key is not in the dictionary.

Return the value for key if key is in the dictionary, else default.

**Inherited from:** dict

**Signature:** (self, key, default=None, /)





**Return Value:** None

[Back to Top](#module-overview)



