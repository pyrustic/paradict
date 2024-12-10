"""binary Paradict: 256 tags from NOP (`\\x00`) to END (`\\xff`)"""


# Nop
NOP = b'\x00'

# ----------- CONTAINERS -------------

# Dict (container)
DICT = b'\x01'
DICT_EMPTY = b'\x02'

# List (container)
LIST = b'\x03'
LIST_EMPTY = b'\x04'

# Set (container)
SET = b'\x05'
SET_EMPTY = b'\x06'

# Extension Object (container)
OBJ = b'\x07'
OBJ_EMPTY = b'\x08'

# ----------- GRID -------------

# Grid (math container)
GRID = b'\x09'
GRID_DIV = b'\x0a'
GRID_EMPTY = b'\x0b'

# ----------- NULL AND BOOL -------------

# Null
NULL = b'\x0c'

# Bool
BOOL_TRUE = b'\x0d'
BOOL_FALSE = b'\x0e'

# ----------- COMPLEX NUMBER -------------

# <tag, real, imaginary>
COMPLEX = b'\x0f'

# ----------- RESERVED TAGS -------------

XA = b'\x10'
XB = b'\x11'
XC = b'\x12'
XD = b'\x13'
XE = b'\x14'

# ----------- DATE -------------

# <tag, year_delta, day_delta>
DATE = b'\x15'

# ----------- TIME -------------

# <tag, nanoseconds_leading_digits, trailing_zeros>
TIME = b'\x16'
# <tag, nanoseconds_leading_digits, trailing_zeros, utc_offset_minutes>
TIME_EXT = b'\x17'

# ----------- DATETIME -------------

# <tag, year_delta, nanoseconds_delta_leading_digits, trailing_zeros>
DATETIME = b'\x18'
# <tag, year_delta, nanoseconds_delta_leading_digits, trailing_zeros, utc_offset_minutes>
DATETIME_EXT = b'\x19'

# ----------- BIN OCT HEX INTEGER NOTATION -------------

# <tag, integer>
RADIX_BIN = b'\x1a'
# <tag, leading_zeros, integer>
RADIX_BIN_EXT = b'\x1b'

# <tag, integer>
RADIX_OCT = b'\x1c'
# <tag, leading_zeros, integer>
RADIX_OCT_EXT = b'\x1d'

# <tag, integer>
RADIX_HEX = b'\x1e'
# <tag, leading_zeros, integer>
RADIX_HEX_EXT = b'\x1f'

# ----------- FLOATING-POINT NUMBER-------------

# <tag, char> where char is a letter (n, x, y, z) for NaN, +inf, -inf, and -0
FLOAT_MISC = b'\x20'

# <tag, left_significand>
FLOAT_1 = b'\x21'
# <tag, left_significand, exponent>
FLOAT_1_EXT = b'\x22'

# <tag, left_significand, right_significand>
FLOAT_2 = b'\x23'
# <tag, left_significand, right_significand, exponent>
FLOAT_2_EXT = b'\x24'

# <tag, left_significand, leading_zeros, right_significand>
FLOAT_3 = b'\x25'
# <tag, left_significand, leading_zeros, right_significand, exponent>
FLOAT_3_EXT = b'\x26'

# ----------- BINARY -------------

# Bin
BIN_EMPTY = b'\x27'
BIN_SHORT = b'\x28'
BIN_MEDIUM = b'\x29'
BIN_LONG = b'\x2a'
BIN_BIG = b'\x2b'
BIN_HEAVY = b'\x2c'

# ----------- INTEGER -------------

# Positive Integer
PINT_8 = b'\x2d'
PINT_16 = b'\x2e'
PINT_24 = b'\x2f'
PINT_32 = b'\x30'
PINT_40 = b'\x31'
PINT_48 = b'\x32'
PINT_56 = b'\x33'
PINT_64 = b'\x34'
PINT_BIG = b'\x35'
PINT_HEAVY = b'\x36'

# Negative Integer
NINT_8 = b'\x37'
NINT_16 = b'\x38'
NINT_24 = b'\x39'
NINT_32 = b'\x3a'
NINT_40 = b'\x3b'
NINT_48 = b'\x3c'
NINT_56 = b'\x3d'
NINT_64 = b'\x3e'
NINT_BIG = b'\x3f'
NINT_HEAVY = b'\x40'

# ----------- STRING -------------

# String
STR_8 = b'\x41'
STR_16 = b'\x42'
STR_24 = b'\x43'
STR_32 = b'\x44'
STR_40 = b'\x45'
STR_48 = b'\x46'
STR_56 = b'\x47'
STR_64 = b'\x48'
STR_72 = b'\x49'
STR_80 = b'\x4a'
STR_88 = b'\x4b'
STR_96 = b'\x4c'
STR_104 = b'\x4d'
STR_112 = b'\x4e'
STR_120 = b'\x4f'
STR_128 = b'\x50'
STR_136 = b'\x51'
STR_144 = b'\x52'
STR_152 = b'\x53'
STR_160 = b'\x54'
STR_168 = b'\x55'
STR_176 = b'\x56'
STR_184 = b'\x57'
STR_192 = b'\x58'
STR_200 = b'\x59'
STR_208 = b'\x5a'
STR_216 = b'\x5b'
STR_224 = b'\x5c'
STR_232 = b'\x5d'
STR_240 = b'\x5e'
STR_248 = b'\x5f'
STR_256 = b'\x60'
STR_EMPTY = b'\x61'
STR_SHORT = b'\x62'
STR_MEDIUM = b'\x63'
STR_LONG = b'\x64'
STR_BIG = b'\x65'
STR_HEAVY = b'\x66'

# ----------- ALPHABET -------------

# a to z
CHAR_A = b'\x67'
CHAR_B = b'\x68'
CHAR_C = b'\x69'
CHAR_D = b'\x6a'
CHAR_E = b'\x6b'
CHAR_F = b'\x6c'
CHAR_G = b'\x6d'
CHAR_H = b'\x6e'
CHAR_I = b'\x6f'
CHAR_J = b'\x70'
CHAR_K = b'\x71'
CHAR_L = b'\x72'
CHAR_M = b'\x73'
CHAR_N = b'\x74'
CHAR_O = b'\x75'
CHAR_P = b'\x76'
CHAR_Q = b'\x77'
CHAR_R = b'\x78'
CHAR_S = b'\x79'
CHAR_T = b'\x7a'
CHAR_U = b'\x7b'
CHAR_V = b'\x7c'
CHAR_W = b'\x7d'
CHAR_X = b'\x7e'
CHAR_Y = b'\x7f'
CHAR_Z = b'\x80'

# A to Z (uppercase)
CHAR_UP_A = b'\x81'
CHAR_UP_B = b'\x82'
CHAR_UP_C = b'\x83'
CHAR_UP_D = b'\x84'
CHAR_UP_E = b'\x85'
CHAR_UP_F = b'\x86'
CHAR_UP_G = b'\x87'
CHAR_UP_H = b'\x88'
CHAR_UP_I = b'\x89'
CHAR_UP_J = b'\x8a'
CHAR_UP_K = b'\x8b'
CHAR_UP_L = b'\x8c'
CHAR_UP_M = b'\x8d'
CHAR_UP_N = b'\x8e'
CHAR_UP_O = b'\x8f'
CHAR_UP_P = b'\x90'
CHAR_UP_Q = b'\x91'
CHAR_UP_R = b'\x92'
CHAR_UP_S = b'\x93'
CHAR_UP_T = b'\x94'
CHAR_UP_U = b'\x95'
CHAR_UP_V = b'\x96'
CHAR_UP_W = b'\x97'
CHAR_UP_X = b'\x98'
CHAR_UP_Y = b'\x99'
CHAR_UP_Z = b'\x9a'

# ----------- CONSTANTS INTEGERS -------------

# Const 0 to 99
CONST_0 = b'\x9b'
CONST_1 = b'\x9c'
CONST_2 = b'\x9d'
CONST_3 = b'\x9e'
CONST_4 = b'\x9f'
CONST_5 = b'\xa0'
CONST_6 = b'\xa1'
CONST_7 = b'\xa2'
CONST_8 = b'\xa3'
CONST_9 = b'\xa4'
CONST_10 = b'\xa5'
CONST_11 = b'\xa6'
CONST_12 = b'\xa7'
CONST_13 = b'\xa8'
CONST_14 = b'\xa9'
CONST_15 = b'\xaa'
CONST_16 = b'\xab'
CONST_17 = b'\xac'
CONST_18 = b'\xad'
CONST_19 = b'\xae'
CONST_20 = b'\xaf'
CONST_21 = b'\xb0'
CONST_22 = b'\xb1'
CONST_23 = b'\xb2'
CONST_24 = b'\xb3'
CONST_25 = b'\xb4'
CONST_26 = b'\xb5'
CONST_27 = b'\xb6'
CONST_28 = b'\xb7'
CONST_29 = b'\xb8'
CONST_30 = b'\xb9'
CONST_31 = b'\xba'
CONST_32 = b'\xbb'
CONST_33 = b'\xbc'
CONST_34 = b'\xbd'
CONST_35 = b'\xbe'
CONST_36 = b'\xbf'
CONST_37 = b'\xc0'
CONST_38 = b'\xc1'
CONST_39 = b'\xc2'
CONST_40 = b'\xc3'
CONST_41 = b'\xc4'
CONST_42 = b'\xc5'
CONST_43 = b'\xc6'
CONST_44 = b'\xc7'
CONST_45 = b'\xc8'
CONST_46 = b'\xc9'
CONST_47 = b'\xca'
CONST_48 = b'\xcb'
CONST_49 = b'\xcc'
CONST_50 = b'\xcd'
CONST_51 = b'\xce'
CONST_52 = b'\xcf'
CONST_53 = b'\xd0'
CONST_54 = b'\xd1'
CONST_55 = b'\xd2'
CONST_56 = b'\xd3'
CONST_57 = b'\xd4'
CONST_58 = b'\xd5'
CONST_59 = b'\xd6'
CONST_60 = b'\xd7'
CONST_61 = b'\xd8'
CONST_62 = b'\xd9'
CONST_63 = b'\xda'
CONST_64 = b'\xdb'
CONST_65 = b'\xdc'
CONST_66 = b'\xdd'
CONST_67 = b'\xde'
CONST_68 = b'\xdf'
CONST_69 = b'\xe0'
CONST_70 = b'\xe1'
CONST_71 = b'\xe2'
CONST_72 = b'\xe3'
CONST_73 = b'\xe4'
CONST_74 = b'\xe5'
CONST_75 = b'\xe6'
CONST_76 = b'\xe7'
CONST_77 = b'\xe8'
CONST_78 = b'\xe9'
CONST_79 = b'\xea'
CONST_80 = b'\xeb'
CONST_81 = b'\xec'
CONST_82 = b'\xed'
CONST_83 = b'\xee'
CONST_84 = b'\xef'
CONST_85 = b'\xf0'
CONST_86 = b'\xf1'
CONST_87 = b'\xf2'
CONST_88 = b'\xf3'
CONST_89 = b'\xf4'
CONST_90 = b'\xf5'
CONST_91 = b'\xf6'
CONST_92 = b'\xf7'
CONST_93 = b'\xf8'
CONST_94 = b'\xf9'
CONST_95 = b'\xfa'
CONST_96 = b'\xfb'
CONST_97 = b'\xfc'
CONST_98 = b'\xfd'
CONST_99 = b'\xfe'

# ----------- -------------

# The End !
END = b'\xff'
