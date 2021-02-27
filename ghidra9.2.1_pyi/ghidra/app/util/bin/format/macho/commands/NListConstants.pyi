import java.lang


class NListConstants(object):
    DEBUG_N_BCOMM: int = -30
    DEBUG_N_BINCL: int = -126
    DEBUG_N_BNSYM: int = 46
    DEBUG_N_ECOML: int = -24
    DEBUG_N_ECOMM: int = -28
    DEBUG_N_EINCL: int = -94
    DEBUG_N_ENSYM: int = 78
    DEBUG_N_ENTRY: int = -92
    DEBUG_N_EXCL: int = -62
    DEBUG_N_FNAME: int = 34
    DEBUG_N_FUN: int = 36
    DEBUG_N_GSYM: int = 32
    DEBUG_N_LBRAC: int = -64
    DEBUG_N_LCSYM: int = 40
    DEBUG_N_LENG: int = -2
    DEBUG_N_LSYM: int = -128
    DEBUG_N_OLEVEL: int = -118
    DEBUG_N_OPT: int = 60
    DEBUG_N_OSO: int = 102
    DEBUG_N_PARAMS: int = -122
    DEBUG_N_PSYM: int = -96
    DEBUG_N_RBRAC: int = -32
    DEBUG_N_RSYM: int = 64
    DEBUG_N_SLINE: int = 68
    DEBUG_N_SO: int = 100
    DEBUG_N_SOL: int = -124
    DEBUG_N_SSYM: int = 96
    DEBUG_N_STSYM: int = 38
    DEBUG_N_VERSION: int = -120
    DESC_N_ARM_THUMB_DEF: int = 8
    DESC_N_DESC_DISCARDED: int = 32
    DESC_N_NO_DEAD_STRIP: int = 32
    DESC_N_REF_TO_WEAK: int = 128
    DESC_N_WEAK_DEF: int = 128
    DESC_N_WEAK_REF: int = 64
    DYNAMIC_LOOKUP_ORDINAL: int = -2
    EXECUTABLE_ORDINAL: int = -1
    MASK_N_EXT: int = 1
    MASK_N_PEXT: int = 16
    MASK_N_STAB: int = 224
    MASK_N_TYPE: int = 14
    MAX_LIBRARY_ORDINAL: int = -3
    NO_SECT: int = 0
    REFERENCED_DYNAMICALLY: int = 16
    REFERENCE_FLAG_DEFINED: int = 2
    REFERENCE_FLAG_PRIVATE_DEFINED: int = 3
    REFERENCE_FLAG_PRIVATE_UNDEFINED_LAZY: int = 5
    REFERENCE_FLAG_PRIVATE_UNDEFINED_NON_LAZY: int = 4
    REFERENCE_FLAG_UNDEFINED_LAZY: int = 1
    REFERENCE_FLAG_UNDEFINED_NON_LAZY: int = 0
    REFERENCE_TYPE: int = 7
    SELF_LIBRARY_ORDINAL: int = 0
    TYPE_N_ABS: int = 2
    TYPE_N_INDR: int = 10
    TYPE_N_PBUD: int = 12
    TYPE_N_SECT: int = 14
    TYPE_N_UNDF: int = 0



    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
