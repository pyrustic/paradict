"""Private miscellaneous module for the Paradict binary format"""
from paradict import tags


# Mapping payload sizes in bytes to PINT tags
SIZE_TO_PINT = {1: tags.PINT_8, 2: tags.PINT_16,
                3: tags.PINT_24, 4: tags.PINT_32,
                5: tags.PINT_40, 6: tags.PINT_48,
                7: tags.PINT_56, 8: tags.PINT_64}

# Mapping PINT tags to payload sizes in bytes
PINT_TO_SIZE = {tags.PINT_8: 1, tags.PINT_16: 2,
                tags.PINT_24: 3, tags.PINT_32: 4,
                tags.PINT_40: 5, tags.PINT_48: 6,
                tags.PINT_56: 7, tags.PINT_64: 8}


# Mapping payload sizes in bytes to NINT tags
SIZE_TO_NINT = {1: tags.NINT_8, 2: tags.NINT_16,
                3: tags.NINT_24, 4: tags.NINT_32,
                5: tags.NINT_40, 6: tags.NINT_48,
                7: tags.NINT_56, 8: tags.NINT_64}

# Mapping NINT tags to payload sizes in bytes
NINT_TO_SIZE = {tags.NINT_8: 1, tags.NINT_16: 2,
                tags.NINT_24: 3, tags.NINT_32: 4,
                tags.NINT_40: 5, tags.NINT_48: 6,
                tags.NINT_56: 7, tags.NINT_64: 8}


# Mapping payload sizes in bytes to fixed-length STR tags
SIZE_TO_STR = {1: tags.STR_8, 2: tags.STR_16,
               3: tags.STR_24, 4: tags.STR_32,
               5: tags.STR_40, 6: tags.STR_48,
               7: tags.STR_56, 8: tags.STR_64,
               9: tags.STR_72, 10: tags.STR_80,
               11: tags.STR_88, 12: tags.STR_96,
               13: tags.STR_104, 14: tags.STR_112,
               15: tags.STR_120, 16: tags.STR_128,
               17: tags.STR_136, 18: tags.STR_144,
               19: tags.STR_152, 20: tags.STR_160,
               21: tags.STR_168, 22: tags.STR_176,
               23: tags.STR_184, 24: tags.STR_192,
               25: tags.STR_200, 26: tags.STR_208,
               27: tags.STR_216, 28: tags.STR_224,
               29: tags.STR_232, 30: tags.STR_240,
               31: tags.STR_248, 32: tags.STR_256}

# Mapping fixed-length STR tags to payload sizes in bytes
STR_TO_SIZE = {tags.STR_8: 1, tags.STR_16: 2,
               tags.STR_24: 3, tags.STR_32: 4,
               tags.STR_40: 5, tags.STR_48: 6,
               tags.STR_56: 7, tags.STR_64: 8,
               tags.STR_72: 9, tags.STR_80: 10,
               tags.STR_88:11, tags.STR_96: 12,
               tags.STR_104: 13, tags.STR_112: 14,
               tags.STR_120: 15, tags.STR_128: 16,
               tags.STR_136: 17, tags.STR_144: 18,
               tags.STR_152: 19, tags.STR_160: 20,
               tags.STR_168: 21, tags.STR_176: 22,
               tags.STR_184: 23, tags.STR_192: 24,
               tags.STR_200: 25, tags.STR_208: 26,
               tags.STR_216: 27, tags.STR_224: 28,
               tags.STR_232: 29, tags.STR_240: 30,
               tags.STR_248: 31, tags.STR_256: 32}


# Mapping BIN tags to number of bytes for encoding payload sizes
BIN_TO_SIZE = {tags.BIN_SHORT: 1,
               tags.BIN_MEDIUM: 2,
               tags.BIN_LONG: 3,
               tags.BIN_BIG: 4,
               tags.BIN_HEAVY: 5}

# Mapping number of bytes for encoding payload sizes to BIN tags
SIZE_TO_BIN = {1: tags.BIN_SHORT,
               2: tags.BIN_MEDIUM,
               3: tags.BIN_LONG,
               4: tags.BIN_BIG,
               5: tags.BIN_HEAVY}

# Mapping variable-length STR tags to number of bytes for encoding payload sizes
VARSTR_TO_SIZE = {tags.STR_SHORT: 1,
                  tags.STR_MEDIUM: 2,
                  tags.STR_LONG: 3,
                  tags.STR_BIG: 4,
                  tags.STR_HEAVY: 5}

# Mapping number of bytes for encoding payload sizes to variable-length STR tags 
SIZE_TO_VARSTR = {1: tags.STR_SHORT,
                  2: tags.STR_MEDIUM,
                  3: tags.STR_LONG,
                  4: tags.STR_BIG,
                  5: tags.STR_HEAVY}


# Mapping lower and upper alphabet letters to CHAR tags
LETTER_TO_TAG = {"a": tags.CHAR_A, "b": tags.CHAR_B,
                 "c": tags.CHAR_C, "d": tags.CHAR_D,
                 "e": tags.CHAR_E, "f": tags.CHAR_F,
                 "g": tags.CHAR_G, "h": tags.CHAR_H,
                 "i": tags.CHAR_I, "j": tags.CHAR_J,
                 "k": tags.CHAR_K, "l": tags.CHAR_L,
                 "m": tags.CHAR_M, "n": tags.CHAR_N,
                 "o": tags.CHAR_O, "p": tags.CHAR_P,
                 "q": tags.CHAR_Q, "r": tags.CHAR_R,
                 "s": tags.CHAR_S, "t": tags.CHAR_T,
                 "u": tags.CHAR_U, "v": tags.CHAR_V,
                 "w": tags.CHAR_W, "x": tags.CHAR_X,
                 "y": tags.CHAR_Y, "z": tags.CHAR_Z,
                 "A": tags.CHAR_UP_A, "B": tags.CHAR_UP_B,
                 "C": tags.CHAR_UP_C, "D": tags.CHAR_UP_D,
                 "E": tags.CHAR_UP_E, "F": tags.CHAR_UP_F,
                 "G": tags.CHAR_UP_G, "H": tags.CHAR_UP_H,
                 "I": tags.CHAR_UP_I, "J": tags.CHAR_UP_J,
                 "K": tags.CHAR_UP_K, "L": tags.CHAR_UP_L,
                 "M": tags.CHAR_UP_M, "N": tags.CHAR_UP_N,
                 "O": tags.CHAR_UP_O, "P": tags.CHAR_UP_P,
                 "Q": tags.CHAR_UP_Q, "R": tags.CHAR_UP_R,
                 "S": tags.CHAR_UP_S, "T": tags.CHAR_UP_T,
                 "U": tags.CHAR_UP_U, "V": tags.CHAR_UP_V,
                 "W": tags.CHAR_UP_W, "X": tags.CHAR_UP_X,
                 "Y": tags.CHAR_UP_Y, "Z": tags.CHAR_UP_Z}

# Mapping CHAR tags to lower and upper alphabet letters
TAG_TO_LETTER = {tags.CHAR_A: "a", tags.CHAR_B: "b",
                 tags.CHAR_C: "c", tags.CHAR_D: "d",
                 tags.CHAR_E: "e", tags.CHAR_F: "f",
                 tags.CHAR_G: "g", tags.CHAR_H: "h",
                 tags.CHAR_I: "i", tags.CHAR_J: "j",
                 tags.CHAR_K: "k", tags.CHAR_L: "l",
                 tags.CHAR_M: "m", tags.CHAR_N: "n",
                 tags.CHAR_O: "o", tags.CHAR_P: "p",
                 tags.CHAR_Q: "q", tags.CHAR_R: "r",
                 tags.CHAR_S: "s", tags.CHAR_T: "t",
                 tags.CHAR_U: "u", tags.CHAR_V: "v",
                 tags.CHAR_W: "w", tags.CHAR_X: "x",
                 tags.CHAR_Y: "y", tags.CHAR_Z: "z",
                 tags.CHAR_UP_A: "A", tags.CHAR_UP_B: "B",
                 tags.CHAR_UP_C: "C", tags.CHAR_UP_D: "D",
                 tags.CHAR_UP_E: "E", tags.CHAR_UP_F: "F",
                 tags.CHAR_UP_G: "G", tags.CHAR_UP_H: "H",
                 tags.CHAR_UP_I: "I", tags.CHAR_UP_J: "J",
                 tags.CHAR_UP_K: "K", tags.CHAR_UP_L: "L",
                 tags.CHAR_UP_M: "M", tags.CHAR_UP_N: "N",
                 tags.CHAR_UP_O: "O", tags.CHAR_UP_P: "P",
                 tags.CHAR_UP_Q: "Q", tags.CHAR_UP_R: "R",
                 tags.CHAR_UP_S: "S", tags.CHAR_UP_T: "T",
                 tags.CHAR_UP_U: "U", tags.CHAR_UP_V: "V",
                 tags.CHAR_UP_W: "W", tags.CHAR_UP_X: "X",
                 tags.CHAR_UP_Y: "Y", tags.CHAR_UP_Z: "Z"}
