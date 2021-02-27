import java.lang


class DWARFEndianity(object):
    """
    DWARF Endianity consts from www.dwarfstd.org/doc/DWARF4.pdf
    """

    DW_END_big: int = 1
    DW_END_default: int = 0
    DW_END_hi_user: int = 255
    DW_END_little: int = 2
    DW_END_lo_user: int = 64



    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getEndianity(endian: long, defaultisBigEndian: bool) -> bool:
        """
        Get the endianity given a DWARFEndianity value.
        @param endian DWARFEndianity value to check
        @param defaultisBigEndian true if by default is big endian and false otherwise
        @return true if big endian and false if little endian
        @throws IllegalArgumentException if an unknown endian value is given
        """
        ...

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
