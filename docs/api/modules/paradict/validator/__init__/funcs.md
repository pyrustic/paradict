###### Paradict API Reference
[Home](/docs/api/README.md) | [Project](/README.md) | [Module](/docs/api/modules/paradict/validator/__init__/README.md) | [Source](/paradict/validator/__init__.py)

# Functions within module
> Module: [paradict.validator.\_\_init\_\_](/docs/api/modules/paradict/validator/__init__/README.md)

Here are functions exposed in the module:
- [validate](#validate)

## validate
This function returns True if the given data
successfully validates against the given schema

```python
def validate(data, schema, type_ref=None):
    ...
```

| Parameter | Description |
| --- | --- |
| data | some Python object (like a dict, a list, ...) that is part or include datatypes defined in VALID_DATATYPES. |
| schema | a valid schema. It might be a collection containing Spec instances and/or type-strings. The benefit of using Spec is that you can add a checker function that will serve as an extra programmatic validation. |
| type\_ref | optional TypeRef object |

### Value to return
Returns True or False

<p align="right"><a href="#paradict-api-reference">Back to top</a></p>
