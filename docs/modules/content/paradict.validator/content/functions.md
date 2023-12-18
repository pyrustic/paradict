Back to [All Modules](https://github.com/pyrustic/paradict/blob/master/docs/modules/README.md#readme)

# Module Overview

**paradict.validator**
 
Data validation module

> **Classes:** &nbsp; [Spec](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.validator/content/classes/Spec.md#class-spec) &nbsp;&nbsp; [Validator](https://github.com/pyrustic/paradict/blob/master/docs/modules/content/paradict.validator/content/classes/Validator.md#class-validator)
>
> **Functions:** &nbsp; [validate](#validate)
>
> **Constants:** &nbsp; VALID_DATATYPES

# All Functions
[validate](#validate)

## validate
This function returns True if the given data
successfully validates against the given schema



**Signature:** (data, schema, type\_ref=None)

|Parameter|Description|
|---|---|
|data|some Python object (like a dict, a list, ...) that is part or include datatypes defined in VALID_DATATYPES.|
|schema|a valid schema. It might be a collection containing Spec instances and/or type-strings. The benefit of using Spec is that you can add a checker function that will serve as an extra programmatic validation.|
|type\_ref|optional TypeRef object|





**Return Value:** Returns True or False

[Back to Top](#module-overview)


