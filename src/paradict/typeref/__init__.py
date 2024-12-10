"""TypeRef for type specs and customization"""
import datetime
from decimal import Decimal
from collections import OrderedDict
from paradict import xtypes, errors
from paradict.const import Datatype

__all__ = ["TypeRef"]


class TypeRef:
    """This class represents a mechanism for customizing
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
    """
    def __init__(self, adapters=None,

                 dict_type=None, list_type=None, set_type=None,
                 obj_type=None,

                 dict_types=None, list_types=None, set_types=None,
                 obj_types=None,

                 bin_type=None, bool_type=None,
                 complex_type=None, date_type=None, datetime_type=None,
                 float_type=None, grid_type=None,
                 int_type=None, str_type=None, time_type=None,

                 bin_types=None, bool_types=None,
                 complex_types=None, date_types=None, datetime_types=None,
                 float_types=None, grid_types=None,
                 int_types=None, str_types=None, time_types=None):

        # adapters
        self._adapters = adapters if adapters else dict()

        # containers for deserialization
        self._dict_type = dict_type if dict_type else dict
        self._list_type = list_type if list_type else list
        self._set_type = set_type if set_type else set
        self._obj_type = obj_type if obj_type else xtypes.Obj

        # datatypes for deserialization
        self._bin_type = bin_type if bin_type else bytes
        self._bool_type = bool_type if bool_type else bool
        self._complex_type = complex_type if complex_type else complex
        self._date_type = date_type if date_type else datetime.date
        self._datetime_type = datetime_type if datetime_type else datetime.datetime
        self._float_type = float_type if float_type else float
        self._grid_type = grid_type if grid_type else xtypes.Grid
        self._int_type = int_type if int_type else int
        self._str_type = str_type if str_type else str
        self._time_type = time_type if time_type else datetime.time

        # serializable containers
        self._dict_types = dict_types if dict_types else [dict, OrderedDict]
        self._list_types = list_types if list_types else [list, tuple]
        self._set_types = set_types if set_types else [set]
        self._obj_types = obj_types if obj_types else [xtypes.Obj]

        # serializable data types
        self._bin_types = bin_types if bin_types else [bytes, bytearray]
        self._bool_types = bool_types if bool_types else [bool]
        self._complex_types = complex_types if complex_types else [complex]
        self._date_types = date_types if date_types else [datetime.date]
        self._datetime_types = datetime_types if datetime_types else [datetime.datetime]
        self._float_types = float_types if float_types else [float, Decimal]
        self._grid_types = grid_types if grid_types else [xtypes.Grid]
        self._int_types = int_types if int_types else [int, xtypes.HexInt, xtypes.BinInt, xtypes.OctInt]
        self._str_types = str_types if str_types else [str]
        self._time_types = time_types if time_types else [datetime.time]

        # setup
        self._mapping = self._create_map()

    # adapters
    @property
    def adapters(self):
        return self._adapters

    @adapters.setter
    def adapters(self, val):
        self._adapters = val

    # types for containers

    @property
    def dict_type(self):
        return self._dict_type

    @dict_type.setter
    def dict_type(self, val):
        self._dict_type = val
        self._update_types(Datatype.DICT, val)

    @property
    def list_type(self):
        return self._list_type

    @list_type.setter
    def list_type(self, val):
        self._list_type = val
        self._update_types(Datatype.LIST, val)

    @property
    def set_type(self):
        return self._set_type

    @set_type.setter
    def set_type(self, val):
        self._set_type = val
        self._update_types(Datatype.SET, val)

    @property
    def obj_type(self):
        return self._obj_type

    @obj_type.setter
    def obj_type(self, val):
        self._obj_type = val
        self._update_types(Datatype.OBJ, val)

    @property
    def dict_types(self):
        return self._dict_types

    @dict_types.setter
    def dict_types(self, val):
        self._dict_types = val

    @property
    def list_types(self):
        return self._list_types

    @list_types.setter
    def list_types(self, val):
        self._list_types = val

    @property
    def set_types(self):
        return self._set_types

    @set_types.setter
    def set_types(self, val):
        self._set_types = val

    @property
    def obj_types(self):
        return self._obj_types

    @obj_types.setter
    def obj_types(self, val):
        self._obj_types = val

    # types for values

    @property
    def bin_type(self):
        return self._bin_type

    @bin_type.setter
    def bin_type(self, val):
        self._bin_type = val
        self._update_types(Datatype.BIN, val)

    @property
    def bool_type(self):
        return self._bool_type

    @bool_type.setter
    def bool_type(self, val):
        self._bool_type = val
        self._update_types(Datatype.BOOL, val)

    @property
    def complex_type(self):
        return self._complex_type

    @complex_type.setter
    def complex_type(self, val):
        self._complex_type = val
        self._update_types(Datatype.COMPLEX, val)

    @property
    def date_type(self):
        return self._date_type

    @date_type.setter
    def date_type(self, val):
        self._date_type = val
        self._update_types(Datatype.DATE, val)

    @property
    def datetime_type(self):
        return self._datetime_type

    @datetime_type.setter
    def datetime_type(self, val):
        self._datetime_type = val
        self._update_types(Datatype.DATETIME, val)

    @property
    def float_type(self):
        return self._float_type

    @float_type.setter
    def float_type(self, val):
        self._float_type = val
        self._update_types(Datatype.FLOAT, val)

    @property
    def grid_type(self):
        return self._grid_type

    @grid_type.setter
    def grid_type(self, val):
        self._grid_type = val
        self._update_types(Datatype.GRID, val)

    @property
    def int_type(self):
        return self._int_type

    @int_type.setter
    def int_type(self, val):
        self._int_type = val
        self._update_types(Datatype.INT, val)

    @property
    def str_type(self):
        return self._str_type

    @str_type.setter
    def str_type(self, val):
        self._str_type = val
        self._update_types(Datatype.STR, val)

    @property
    def time_type(self):
        return self._time_type

    @time_type.setter
    def time_type(self, val):
        self._time_type = val
        self._update_types(Datatype.TIME, val)

    @property
    def bin_types(self):
        return self._bin_types

    @bin_types.setter
    def bin_types(self, val):
        self._bin_types = val

    @property
    def bool_types(self):
        return self._bool_types

    @bool_types.setter
    def bool_types(self, val):
        self._bool_types = val

    @property
    def complex_types(self):
        return self._complex_types

    @complex_types.setter
    def complex_types(self, val):
        self._complex_types = val

    @property
    def date_types(self):
        return self._date_types

    @date_types.setter
    def date_types(self, val):
        self._date_types = val

    @property
    def datetime_types(self):
        return self._datetime_types

    @datetime_types.setter
    def datetime_types(self, val):
        self._datetime_types = val

    @property
    def float_types(self):
        return self._float_types

    @float_types.setter
    def float_types(self, val):
        self._float_types = val

    @property
    def grid_types(self):
        return self._grid_types

    @grid_types.setter
    def grid_types(self, val):
        self._grid_types = val

    @property
    def int_types(self):
        return self._int_types

    @int_types.setter
    def int_types(self, val):
        self._int_types = val

    @property
    def str_types(self):
        return self._str_types

    @str_types.setter
    def str_types(self, val):
        self._str_types = val

    @property
    def time_types(self):
        return self._time_types

    @time_types.setter
    def time_types(self, val):
        self._time_types = val

    def adapt(self, value):
        """Checks the 'adapters' attribute to find out if there is
        an adapter function registered for the type of the data argument.
        Then, calls the adapter on the value.

        [param]
        - value: the data value to adapt is an arbitrary Python object

        [return]
        Returns the adapted value or the same value if no adapter is registered for its type"""
        if not self._adapters:
            return value
        t = type(value)
        try:
            return self._adapters[t](value)
        except KeyError as e:
            return value

    def check(self, dtype):
        """This function accepts as argument a Python type, and return
        a Datatype instance if the type is supported/registered, else returns None"""
        try:
            return self._mapping[dtype]
        except KeyError as e:
            pass

    def _create_map(self):
        categories = {Datatype.DICT: self._dict_types, Datatype.LIST: self._list_types,
                      Datatype.SET: self._set_types, Datatype.OBJ: self._obj_types,
                      Datatype.BIN: self._bin_types,
                      Datatype.BOOL: self._bool_types, Datatype.COMPLEX: self._complex_types,
                      Datatype.DATE: self._date_types, Datatype.DATETIME: self._datetime_types,
                      Datatype.FLOAT: self._float_types, Datatype.GRID: self._grid_types,
                      Datatype.INT: self._int_types,
                      Datatype.STR: self._str_types,
                      Datatype.TIME: self._time_types}
        mapping = dict()
        for name, datatypes in categories.items():
            for datatype in datatypes:
                mapping[datatype] = name
        return mapping

    def _update_types(self, name, datatype):
        if name == Datatype.DICT and datatype not in self._dict_types:
            self._dict_types.insert(0, datatype)
        elif name == Datatype.LIST and datatype not in self._list_types:
            self._list_types.insert(0, datatype)
        elif name == Datatype.SET and datatype not in self._set_types:
            self._set_types.insert(0, datatype)
        elif name == Datatype.OBJ and datatype not in self._obj_types:
            self._obj_types.insert(0, datatype)
        elif name == Datatype.BIN and datatype not in self._bin_types:
            self._bin_types.insert(0, datatype)
        elif name == Datatype.BOOL and datatype not in self._bool_types:
            self._bool_types.insert(0, datatype)
        elif name == Datatype.COMPLEX and datatype not in self._complex_types:
            self._complex_types.insert(0, datatype)
        elif name == Datatype.DATE and datatype not in self._date_types:
            self._date_types.insert(0, datatype)
        elif name == Datatype.DATETIME and datatype not in self._datetime_types:
            self._datetime_types.insert(0, datatype)
        elif name == Datatype.FLOAT and datatype not in self._float_types:
            self._float_types.insert(0, datatype)
        elif name == Datatype.GRID and datatype not in self._grid_types:
            self._grid_types.insert(0, datatype)
        elif name == Datatype.INT and datatype not in self._int_types:
            self._int_types.insert(0, datatype)
        elif name == Datatype.STR and datatype not in self._str_types:
            self._str_types.insert(0, datatype)
        elif name == Datatype.TIME and datatype not in self._time_types:
            self._time_types.insert(0, datatype)
        else:
            msg = "Unknown datatype named '{}'".format(name)
            raise errors.Error(msg)
