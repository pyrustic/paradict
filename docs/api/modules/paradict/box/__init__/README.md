###### Paradict API Reference
[Home](/docs/api/README.md) | [Project](/README.md) | Module | [Source](/src/paradict/box/__init__.py)

# Module Overview
> Module: **paradict.box.\_\_init\_\_**

Boxes to hold grids, hexadecimal integers, et cetera

## Classes
- [**BinInt**](/docs/api/modules/paradict/box/__init__/class-BinInt.md): Box to hold binary integer
    - [as\_integer\_ratio](/docs/api/modules/paradict/box/__init__/class-BinInt.md#fields-table) = `<method 'as_integer_ratio' of 'int' objects>`
    - [bit\_count](/docs/api/modules/paradict/box/__init__/class-BinInt.md#fields-table) = `<method 'bit_count' of 'int' objects>`
    - [bit\_length](/docs/api/modules/paradict/box/__init__/class-BinInt.md#fields-table) = `<method 'bit_length' of 'int' objects>`
    - [conjugate](/docs/api/modules/paradict/box/__init__/class-BinInt.md#fields-table) = `<method 'conjugate' of 'int' objects>`
    - [denominator](/docs/api/modules/paradict/box/__init__/class-BinInt.md#fields-table) = `<attribute 'denominator' of 'int' objects>`
    - [from\_bytes](/docs/api/modules/paradict/box/__init__/class-BinInt.md#fields-table) = `<built-in method from_bytes of type object at 0xa3af20>`
    - [imag](/docs/api/modules/paradict/box/__init__/class-BinInt.md#fields-table) = `<attribute 'imag' of 'int' objects>`
    - [is\_integer](/docs/api/modules/paradict/box/__init__/class-BinInt.md#fields-table) = `<method 'is_integer' of 'int' objects>`
    - [numerator](/docs/api/modules/paradict/box/__init__/class-BinInt.md#fields-table) = `<attribute 'numerator' of 'int' objects>`
    - [real](/docs/api/modules/paradict/box/__init__/class-BinInt.md#fields-table) = `<attribute 'real' of 'int' objects>`
    - [to\_bytes](/docs/api/modules/paradict/box/__init__/class-BinInt.md#fields-table) = `<method 'to_bytes' of 'int' objects>`
- [**Grid**](/docs/api/modules/paradict/box/__init__/class-Grid.md): Box to hold a grid. A grid is made of numbers and should be consistent (rows should be of same size)
    - [\_abc\_impl](/docs/api/modules/paradict/box/__init__/class-Grid.md#fields-table) = `<_abc._abc_data object at 0x7f990f827d00>`
    - [append](/docs/api/modules/paradict/box/__init__/class-Grid.md#append): S.append(value) -- append value to the end of the sequence
    - [clear](/docs/api/modules/paradict/box/__init__/class-Grid.md#clear): S.clear() -> None -- remove all items from S
    - [copy](/docs/api/modules/paradict/box/__init__/class-Grid.md#copy): No docstring.
    - [count](/docs/api/modules/paradict/box/__init__/class-Grid.md#count): S.count(value) -> integer -- return number of occurrences of value
    - [extend](/docs/api/modules/paradict/box/__init__/class-Grid.md#extend): S.extend(iterable) -- extend sequence by appending elements from the iterable
    - [index](/docs/api/modules/paradict/box/__init__/class-Grid.md#index): S.index(value, [start, [stop]]) -> integer -- return first index of value. Raises ValueError if the value is not present.
    - [insert](/docs/api/modules/paradict/box/__init__/class-Grid.md#insert): S.insert(index, value) -- insert value before index
    - [pop](/docs/api/modules/paradict/box/__init__/class-Grid.md#pop): S.pop([index]) -> item -- remove and return item at index (default last). Raise IndexError if list is empty or index is out of r...
    - [remove](/docs/api/modules/paradict/box/__init__/class-Grid.md#remove): S.remove(value) -- remove first occurrence of value. Raise ValueError if the value is not present.
    - [reverse](/docs/api/modules/paradict/box/__init__/class-Grid.md#reverse): S.reverse() -- reverse *IN PLACE*
    - [sort](/docs/api/modules/paradict/box/__init__/class-Grid.md#sort): No docstring.
    - [\_UserList\_\_cast](/docs/api/modules/paradict/box/__init__/class-Grid.md#_userlist__cast): No docstring.
- [**HexInt**](/docs/api/modules/paradict/box/__init__/class-HexInt.md): Box to hold hexadecimal integer
    - [as\_integer\_ratio](/docs/api/modules/paradict/box/__init__/class-HexInt.md#fields-table) = `<method 'as_integer_ratio' of 'int' objects>`
    - [bit\_count](/docs/api/modules/paradict/box/__init__/class-HexInt.md#fields-table) = `<method 'bit_count' of 'int' objects>`
    - [bit\_length](/docs/api/modules/paradict/box/__init__/class-HexInt.md#fields-table) = `<method 'bit_length' of 'int' objects>`
    - [conjugate](/docs/api/modules/paradict/box/__init__/class-HexInt.md#fields-table) = `<method 'conjugate' of 'int' objects>`
    - [denominator](/docs/api/modules/paradict/box/__init__/class-HexInt.md#fields-table) = `<attribute 'denominator' of 'int' objects>`
    - [from\_bytes](/docs/api/modules/paradict/box/__init__/class-HexInt.md#fields-table) = `<built-in method from_bytes of type object at 0xa3af20>`
    - [imag](/docs/api/modules/paradict/box/__init__/class-HexInt.md#fields-table) = `<attribute 'imag' of 'int' objects>`
    - [is\_integer](/docs/api/modules/paradict/box/__init__/class-HexInt.md#fields-table) = `<method 'is_integer' of 'int' objects>`
    - [numerator](/docs/api/modules/paradict/box/__init__/class-HexInt.md#fields-table) = `<attribute 'numerator' of 'int' objects>`
    - [real](/docs/api/modules/paradict/box/__init__/class-HexInt.md#fields-table) = `<attribute 'real' of 'int' objects>`
    - [to\_bytes](/docs/api/modules/paradict/box/__init__/class-HexInt.md#fields-table) = `<method 'to_bytes' of 'int' objects>`
- [**Obj**](/docs/api/modules/paradict/box/__init__/class-Obj.md): Box to hold an Extension Object. Such objects behave like a dictionary. An object builder is passed as argument to the right fun...
    - [\_MutableMapping\_\_marker](/docs/api/modules/paradict/box/__init__/class-Obj.md#fields-table) = `<object object at 0x7f99105141d0>`
    - [\_abc\_impl](/docs/api/modules/paradict/box/__init__/class-Obj.md#fields-table) = `<_abc._abc_data object at 0x7f990f827c00>`
    - [clear](/docs/api/modules/paradict/box/__init__/class-Obj.md#clear): D.clear() -> None.  Remove all items from D.
    - [copy](/docs/api/modules/paradict/box/__init__/class-Obj.md#copy): No docstring.
    - [fromkeys](/docs/api/modules/paradict/box/__init__/class-Obj.md#fromkeys): No docstring.
    - [get](/docs/api/modules/paradict/box/__init__/class-Obj.md#get): D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.
    - [items](/docs/api/modules/paradict/box/__init__/class-Obj.md#items): D.items() -> a set-like object providing a view on D's items
    - [keys](/docs/api/modules/paradict/box/__init__/class-Obj.md#keys): D.keys() -> a set-like object providing a view on D's keys
    - [pop](/docs/api/modules/paradict/box/__init__/class-Obj.md#pop): D.pop(k[,d]) -> v, remove specified key and return the corresponding value. If key is not found, d is returned if given, otherwi...
    - [popitem](/docs/api/modules/paradict/box/__init__/class-Obj.md#popitem): D.popitem() -> (k, v), remove and return some (key, value) pair as a 2-tuple; but raise KeyError if D is empty.
    - [setdefault](/docs/api/modules/paradict/box/__init__/class-Obj.md#setdefault): D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D
    - [update](/docs/api/modules/paradict/box/__init__/class-Obj.md#update): D.update([E, ]**F) -> None.  Update D from mapping/iterable E and F. If E present and has a .keys() method, does:     for k in E...
    - [values](/docs/api/modules/paradict/box/__init__/class-Obj.md#values): D.values() -> an object providing a view on D's values
- [**OctInt**](/docs/api/modules/paradict/box/__init__/class-OctInt.md): Box to hold octal integer
    - [as\_integer\_ratio](/docs/api/modules/paradict/box/__init__/class-OctInt.md#fields-table) = `<method 'as_integer_ratio' of 'int' objects>`
    - [bit\_count](/docs/api/modules/paradict/box/__init__/class-OctInt.md#fields-table) = `<method 'bit_count' of 'int' objects>`
    - [bit\_length](/docs/api/modules/paradict/box/__init__/class-OctInt.md#fields-table) = `<method 'bit_length' of 'int' objects>`
    - [conjugate](/docs/api/modules/paradict/box/__init__/class-OctInt.md#fields-table) = `<method 'conjugate' of 'int' objects>`
    - [denominator](/docs/api/modules/paradict/box/__init__/class-OctInt.md#fields-table) = `<attribute 'denominator' of 'int' objects>`
    - [from\_bytes](/docs/api/modules/paradict/box/__init__/class-OctInt.md#fields-table) = `<built-in method from_bytes of type object at 0xa3af20>`
    - [imag](/docs/api/modules/paradict/box/__init__/class-OctInt.md#fields-table) = `<attribute 'imag' of 'int' objects>`
    - [is\_integer](/docs/api/modules/paradict/box/__init__/class-OctInt.md#fields-table) = `<method 'is_integer' of 'int' objects>`
    - [numerator](/docs/api/modules/paradict/box/__init__/class-OctInt.md#fields-table) = `<attribute 'numerator' of 'int' objects>`
    - [real](/docs/api/modules/paradict/box/__init__/class-OctInt.md#fields-table) = `<attribute 'real' of 'int' objects>`
    - [to\_bytes](/docs/api/modules/paradict/box/__init__/class-OctInt.md#fields-table) = `<method 'to_bytes' of 'int' objects>`

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>
