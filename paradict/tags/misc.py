"""Private miscellaneous module for the Paradict binary format"""
from paradict import tags


__all__ = []


# Mapping bytes number to INT tags. Eg: 1 byte int belongs to tags.INT_8
SIZE_TO_PINT = {1: tags.PINT_8, 2: tags.PINT_16,
                3: tags.PINT_24, 4: tags.PINT_32,
                5: tags.PINT_40, 6: tags.PINT_48,
                7: tags.PINT_56, 8: tags.PINT_64}


# Mapping bytes number to NINT tags. Eg: 1 byte nint belongs to tags.NINT_8
SIZE_TO_NINT = {1: tags.NINT_8, 2: tags.NINT_16,
                3: tags.NINT_24, 4: tags.NINT_32,
                5: tags.NINT_40, 6: tags.NINT_48,
                7: tags.NINT_56, 8: tags.NINT_64}


# Mapping bytes number to string tags. Eg: 1 byte string belongs to tags.STR_8
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


# Mapping lower and upper alphabet letters to their tags. Eg: "a" -> tags.LOWER_A
ALPHABET = {"a": tags.CHAR_A, "b": tags.CHAR_B,
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
