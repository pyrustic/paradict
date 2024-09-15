###### Paradict API Reference
[Home](/docs/api/README.md) | [Project](/README.md) | Module | [Source](/paradict/validator/__init__.py)

# Module Overview
> Module: **paradict.validator.\_\_init\_\_**

Data validation module

## Fields
- [**All fields**](/docs/api/modules/paradict/validator/__init__/fields.md)
    - VALID\_DATATYPES = `('dict', 'list', 'set', 'obj', 'bin', 'bool', 'complex', 'date', 'datetime', 'float', 'grid', 'int', 'str', 'time')`

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## Functions
- [**All functions**](/docs/api/modules/paradict/validator/__init__/funcs.md)
    - [is\_valid](/docs/api/modules/paradict/validator/__init__/funcs.md#is_valid): This function returns True if the given data successfully validates against the given schema
    - [validate](/docs/api/modules/paradict/validator/__init__/funcs.md#validate): This function validate some data against a schema. Might raise a ValidationError.

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>

## Classes
- [**Spec**](/docs/api/modules/paradict/validator/__init__/class-Spec.md): A Spec can be used to form a schema along with string-types. The particularity of a Spec is that it can carry a checker that is ...
    - [checker](/docs/api/modules/paradict/validator/__init__/class-Spec.md#properties-table); _getter_
    - [datatype](/docs/api/modules/paradict/validator/__init__/class-Spec.md#properties-table); _getter_
- [**Validator**](/docs/api/modules/paradict/validator/__init__/class-Validator.md): Class to validate data against a schema
    - [schema](/docs/api/modules/paradict/validator/__init__/class-Validator.md#properties-table); _getter_
    - [type\_ref](/docs/api/modules/paradict/validator/__init__/class-Validator.md#properties-table); _getter_
    - [validate](/docs/api/modules/paradict/validator/__init__/class-Validator.md#validate): Validate data. Might raise a validation error
    - [\_ensure\_spec](/docs/api/modules/paradict/validator/__init__/class-Validator.md#_ensure_spec): No docstring.
    - [\_validate](/docs/api/modules/paradict/validator/__init__/class-Validator.md#_validate): No docstring.
    - [\_validate\_datatype](/docs/api/modules/paradict/validator/__init__/class-Validator.md#_validate_datatype): No docstring.
    - [\_validate\_dict](/docs/api/modules/paradict/validator/__init__/class-Validator.md#_validate_dict): No docstring.
    - [\_validate\_list](/docs/api/modules/paradict/validator/__init__/class-Validator.md#_validate_list): Schema SHOULD be a list
    - [\_validate\_obj](/docs/api/modules/paradict/validator/__init__/class-Validator.md#_validate_obj): No docstring.
    - [\_validate\_set](/docs/api/modules/paradict/validator/__init__/class-Validator.md#_validate_set): Schema SHOULD be a set

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>
