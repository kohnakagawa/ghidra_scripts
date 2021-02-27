import java.lang


class DWARFSourceLanguage(object):
    """
    DWARF source lang consts from www.dwarfstd.org/doc/DWARF4.pdf.

     TODO: The PDF also lists the default lower bound for array dw_tag_subrange_type
     attributes based on this value.
    """

    DW_LANG_Ada83: int = 3
    DW_LANG_Ada95: int = 13
    DW_LANG_C: int = 2
    DW_LANG_C89: int = 1
    DW_LANG_C99: int = 12
    DW_LANG_C_plus_plus: int = 4
    DW_LANG_Cobol74: int = 5
    DW_LANG_Cobol85: int = 6
    DW_LANG_D: int = 19
    DW_LANG_Fortran77: int = 7
    DW_LANG_Fortran90: int = 8
    DW_LANG_Fortran95: int = 14
    DW_LANG_Java: int = 11
    DW_LANG_Modula2: int = 10
    DW_LANG_ObjC: int = 16
    DW_LANG_ObjC_plus_plus: int = 17
    DW_LANG_PL1: int = 15
    DW_LANG_Pascal83: int = 9
    DW_LANG_Python: int = 20
    DW_LANG_UPC: int = 18
    DW_LANG_hi_user: int = 65535
    DW_LANG_lo_user: int = 32768



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
