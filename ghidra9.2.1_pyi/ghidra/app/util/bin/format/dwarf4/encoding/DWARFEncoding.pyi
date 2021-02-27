import java.lang


class DWARFEncoding(object):
    """
    DWARF attribute encoding consts from www.dwarfstd.org/doc/DWARF4.pdf
    """

    DW_ATE_UTF: int = 16
    DW_ATE_address: int = 1
    DW_ATE_boolean: int = 2
    DW_ATE_complex_float: int = 3
    DW_ATE_decimal_float: int = 15
    DW_ATE_edited: int = 12
    DW_ATE_float: int = 4
    DW_ATE_hi_user: int = 255
    DW_ATE_imaginary_float: int = 9
    DW_ATE_lo_user: int = 128
    DW_ATE_numeric_string: int = 11
    DW_ATE_packed_decimal: int = 10
    DW_ATE_signed: int = 5
    DW_ATE_signed_char: int = 6
    DW_ATE_signed_fixed: int = 13
    DW_ATE_unsigned: int = 7
    DW_ATE_unsigned_char: int = 8
    DW_ATE_unsigned_fixed: int = 14
    DW_ATE_void: int = 0



    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getTypeName(encoding: int) -> unicode: ...

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
