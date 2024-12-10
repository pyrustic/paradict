"""Data validation module"""
from paradict.typeref import TypeRef
from paradict.errors import Error, ValidationError


__all__ = ["VALID_DATATYPES", "is_valid", "validate", "Spec", "Validator"]


VALID_DATATYPES = ("dict", "list", "set", "obj", "bin",
                   "bool", "complex", "date", "datetime",
                   "float", "grid", "int", "str", "time")


def is_valid(data, schema, type_ref=None):
    """This function returns True if the given data
    successfully validates against the given schema

    [params]
    - data: some Python object (like a dict, a list, ...) that is
    part or include datatypes defined in VALID_DATATYPES.
    - schema: a valid schema. It might be a collection containing
    Spec instances and/or type-strings. The benefit of using Spec is
    that you can add a checker function that will serve as an extra
    programmatic validation.
    - type_ref: optional TypeRef object

    [returns]
    Returns True or False"""
    validator = Validator(schema, type_ref=type_ref)
    try:
        validator.validate(data)
    except ValidationError as e:
        return False
    else:
        return True


def validate(data, schema, type_ref=None):
    """This function validate some data against a schema.
    Might raise a ValidationError.

    [params]
    - data: some Python object (like a dict, a list, ...) that is
    part or include datatypes defined in VALID_DATATYPES.
    - schema: a valid schema. It might be a collection containing
    Spec instances and/or type-strings. The benefit of using Spec is
    that you can add a checker function that will serve as an extra
    programmatic validation.
    - type_ref: optional TypeRef object

    [raises]
    - ValidationError: Raised when an issue is encountered while validating the data
    """
    validator = Validator(schema, type_ref=type_ref)
    validator.validate(data)


class Spec:
    """A Spec can be used to form a schema along with string-types.
    The particularity of a Spec is that it can carry a checker that
    is a function to serve as an extra programmatic validation"""
    def __init__(self, datatype, checker=None):
        """
        Init
        [params]
        - datatype: a string representing a valid datatype.
        Check the VALID_DATATYPES variable to discover valid types.
        - checker: an optional function that will be called with passed
        as argument, the specific data it should check. This function
        should return a boolean to validate this piece of data

        [raises]
        - ValidationError: raised if the datatype isn't a valid one
        """
        if datatype not in VALID_DATATYPES:
            msg = "Only these datatypes are valid: {}"
            msg = msg.format(" ".join(VALID_DATATYPES))
            raise ValidationError(msg)
        self._datatype = datatype
        self._checker = checker

    @property
    def datatype(self):
        return self._datatype

    @property
    def checker(self):
        return self._checker


class Validator:
    """Class to validate data against a schema"""
    def __init__(self, schema, type_ref=None):
        """
        Init

        [param]
        - schema: the schema
        - type_ref: optional TypeRef instance
        """
        self._schema = schema
        self._type_ref = type_ref if type_ref else TypeRef()


    @property
    def schema(self):
        return self._schema

    @property
    def type_ref(self):
        return self._type_ref

    def validate(self, data):
        """Validate data. Might raise a validation error"""
        if not self._validate(data, self._schema):
            raise ValidationError

    def _validate(self, target, schema):
        if target is None:
            return True
        target = self._type_ref.adapt(target)
        t = type(schema)
        if t in self._type_ref.str_types:
            return self._validate_datatype(target, schema)
        if t is Spec:
            return self._ensure_spec(target, schema)
        if t in self._type_ref.list_types:
            return self._validate_list(target, schema)
        if t in self._type_ref.set_types:
            return self._validate_set(target, schema)
        if t in self._type_ref.dict_types:
            return self._validate_dict(target, schema)
        if t in self._type_ref.obj_types:
            return self._validate_obj(target, schema)
        msg = "Invalid schema"
        raise ValidationError(msg)

    def _validate_list(self, target, schema):
        """Schema SHOULD be a list"""
        if type(target) not in self._type_ref.list_types:
            return False
        if not schema:
            return True
        for item in target:
            matched = False
            for expected_type in schema:
                if self._validate(item, expected_type):
                    matched = True
                    break
            if not matched:
                return False
        return True

    def _validate_set(self, target, schema):
        """Schema SHOULD be a set"""
        if type(target) not in self._type_ref.set_types:
            return False
        if not schema:
            return True
        for item in target:
            matched = False
            for expected_type in schema:
                if self._validate(item, expected_type):
                    matched = True
                    break
            if not matched:
                return False
        return True

    def _validate_dict(self, target, schema):
        if type(target) not in self._type_ref.dict_types:
            return False
        if not schema:
            return True
        for key, val in target.items():
            try:
                r = self._validate(val, schema[key])
            except KeyError as e:
                return False
            else:
                if not r:
                    return False
        return True

    def _validate_obj(self, target, schema):
        if type(target) not in self._type_ref.obj_types:
            return False
        if not schema:
            return True
        for key, val in target.items():
            try:
                r = self._validate(val, schema[key])
            except KeyError as e:
                return False
            else:
                if not r:
                    return False
        return True

    def _validate_datatype(self, target, datatype):
        valid_types_map = {"dict": self._type_ref.dict_types,
                           "list": self._type_ref.list_types,
                           "set": self._type_ref.set_types,
                           "obj": self._type_ref.obj_types,
                           "bin": self._type_ref.bin_types,
                           "bool": self._type_ref.bool_types,
                           "complex": self._type_ref.complex_types,
                           "date": self._type_ref.date_types,
                           "datetime": self._type_ref.datetime_types,
                           "float": self._type_ref.float_types,
                           "grid": self._type_ref.grid_types,
                           "int": self._type_ref.int_types,
                           "str": self._type_ref.str_types,
                           "time": self._type_ref.time_types}
        try:
            valid_types = valid_types_map[datatype]
        except KeyError as e:
            msg = "Unknown data type '{}'".format(datatype)
            raise ValidationError(msg)
        for valid_type in valid_types:
            if type(target) == valid_type:
                return True
        return False

    def _ensure_spec(self, target, spec):
        if not self._validate_datatype(target, spec.datatype):
            return False
        if not spec.checker:
            return True
        try:
            return bool(spec.checker(target))
        except Exception as e:
            msg = "Error while running a checker"
            raise ValidationError(msg)
