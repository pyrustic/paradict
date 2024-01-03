Back to [All Modules](https://github.com/pyrustic/paradict/blob/master/docs/modules/README.md#readme)

# Module Overview

**paradict**
 
No description

> **Classes:** &nbsp; [ConfigFile](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/classes/ConfigFile.md#class-configfile) &nbsp;&nbsp; [Decoder](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/classes/Decoder.md#class-decoder) &nbsp;&nbsp; [Document](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/classes/Document.md#class-document) &nbsp;&nbsp; [Encoder](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/classes/Encoder.md#class-encoder) &nbsp;&nbsp; [FileDoc](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/classes/FileDoc.md#class-filedoc) &nbsp;&nbsp; [Packer](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/classes/Packer.md#class-packer) &nbsp;&nbsp; [TypeRef](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/classes/TypeRef.md#class-typeref) &nbsp;&nbsp; [Unpacker](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/classes/Unpacker.md#class-unpacker) &nbsp;&nbsp; [Validator](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/classes/Validator.md#class-validator)
>
> **Functions:** &nbsp; [decode](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/functions.md#decode) &nbsp;&nbsp; [dump](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/functions.md#dump) &nbsp;&nbsp; [encode](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/functions.md#encode) &nbsp;&nbsp; [forge\_bin](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/functions.md#forge_bin) &nbsp;&nbsp; [load](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/functions.md#load) &nbsp;&nbsp; [pack](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/functions.md#pack) &nbsp;&nbsp; [split\_kv](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/functions.md#split_kv) &nbsp;&nbsp; [stringify\_bin](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/functions.md#stringify_bin) &nbsp;&nbsp; [unpack](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/functions.md#unpack) &nbsp;&nbsp; [validate](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict/content/functions.md#validate)
>
> **Constants:** &nbsp; None

# Class TypeRef
This class represents a mechanism for customizing
Python types allowed for (de)serializing data with Paradict classes and functions.
For example, one might want to only use Python OrderedDict instead of the regular
dict. In this case, just create a TypeRef instance, and make sure that you
set the dict_type attribute via the construction or a property.

```python
type_ref = TypeRef(dict_type=OrderedDict)
```

Still with this class, one could 'adapt' some exotic datatype so it will
conform with Python datatypes allowed in Paradict (de)serialization.
To do so, set the adapters attribute like this:

```python
adapters = {MyExoticType1: adapterFunction1, MyExoticType2: adapterFunction2}
type_ref = TypeRef(adapters=adapters)
```

## Base Classes
object

## Class Attributes
No class attributes.

## Class Properties
|Property|Type|Description|Inherited from|
|---|---|---|---|
|adapters|getter|None||
|adapters|setter|None||
|bin_int_type|getter|None||
|bin_int_type|setter|None||
|bin_int_types|getter|None||
|bin_int_types|setter|None||
|bin_type|getter|None||
|bin_type|setter|None||
|bin_types|getter|None||
|bin_types|setter|None||
|bool_type|getter|None||
|bool_type|setter|None||
|bool_types|getter|None||
|bool_types|setter|None||
|comment_id_type|getter|None||
|comment_id_type|setter|None||
|comment_id_types|getter|None||
|comment_id_types|setter|None||
|comment_type|getter|None||
|comment_type|setter|None||
|comment_types|getter|None||
|comment_types|setter|None||
|complex_type|getter|None||
|complex_type|setter|None||
|complex_types|getter|None||
|complex_types|setter|None||
|date_type|getter|None||
|date_type|setter|None||
|date_types|getter|None||
|date_types|setter|None||
|datetime_type|getter|None||
|datetime_type|setter|None||
|datetime_types|getter|None||
|datetime_types|setter|None||
|dict_type|getter|None||
|dict_type|setter|None||
|dict_types|getter|None||
|dict_types|setter|None||
|float_type|getter|None||
|float_type|setter|None||
|float_types|getter|None||
|float_types|setter|None||
|grid_type|getter|None||
|grid_type|setter|None||
|grid_types|getter|None||
|grid_types|setter|None||
|hex_int_type|getter|None||
|hex_int_type|setter|None||
|hex_int_types|getter|None||
|hex_int_types|setter|None||
|int_type|getter|None||
|int_type|setter|None||
|int_types|getter|None||
|int_types|setter|None||
|list_type|getter|None||
|list_type|setter|None||
|list_types|getter|None||
|list_types|setter|None||
|obj_type|getter|None||
|obj_type|setter|None||
|obj_types|getter|None||
|obj_types|setter|None||
|oct_int_type|getter|None||
|oct_int_type|setter|None||
|oct_int_types|getter|None||
|oct_int_types|setter|None||
|set_type|getter|None||
|set_type|setter|None||
|set_types|getter|None||
|set_types|setter|None||
|str_type|getter|None||
|str_type|setter|None||
|str_types|getter|None||
|str_types|setter|None||
|time_type|getter|None||
|time_type|setter|None||
|time_types|getter|None||
|time_types|setter|None||



# All Methods
[\_\_init\_\_](#__init__) &nbsp;&nbsp; [adapt](#adapt) &nbsp;&nbsp; [check](#check) &nbsp;&nbsp; [\_create\_map](#_create_map) &nbsp;&nbsp; [\_update\_types](#_update_types)

## \_\_init\_\_
Initialize self.  See help(type(self)) for accurate signature.



**Signature:** (self, adapters=None, dict\_type=None, list\_type=None, set\_type=None, obj\_type=None, dict\_types=None, list\_types=None, set\_types=None, obj\_types=None, bin\_type=None, bin\_int\_type=None, bool\_type=None, complex\_type=None, date\_type=None, datetime\_type=None, comment\_type=None, comment\_id\_type=None, float\_type=None, grid\_type=None, hex\_int\_type=None, int\_type=None, oct\_int\_type=None, str\_type=None, time\_type=None, bin\_types=None, bin\_int\_types=None, bool\_types=None, complex\_types=None, date\_types=None, datetime\_types=None, comment\_types=None, comment\_id\_types=None, float\_types=None, grid\_types=None, hex\_int\_types=None, int\_types=None, oct\_int\_types=None, str\_types=None, time\_types=None)





**Return Value:** None

[Back to Top](#module-overview)


## adapt
Checks the 'adapters' attribute to find out if there is
an adapter function registered for the type of the data argument.
Then, calls the adapter on the data.



**Signature:** (self, data)

|Parameter|Description|
|---|---|
|data|the data to adapt is an arbitrary Python object|





**Return Value:** Returns the adapted data or the same data if no adapter is registered for its type

[Back to Top](#module-overview)


## check
This function accepts as argument a Python type, and return
its Paradict string type if it exists, else returns None



**Signature:** (self, datatype)





**Return Value:** None

[Back to Top](#module-overview)


## \_create\_map
No description



**Signature:** (self)





**Return Value:** None

[Back to Top](#module-overview)


## \_update\_types
No description



**Signature:** (self, name, datatype)





**Return Value:** None

[Back to Top](#module-overview)



