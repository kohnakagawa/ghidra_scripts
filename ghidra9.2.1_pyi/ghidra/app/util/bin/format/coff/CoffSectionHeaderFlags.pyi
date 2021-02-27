import java.lang


class CoffSectionHeaderFlags(object):
    STYP_BSS: long = 0x80L
    STYP_COPY: long = 0x10L
    STYP_DATA: long = 0x40L
    STYP_DEBUG: long = 0x2000L
    STYP_DSECT: long = 0x1L
    STYP_EXCEPT: long = 0x100L
    STYP_GROUP: long = 0x4L
    STYP_INFO: long = 0x200L
    STYP_LIB: long = 0x800L
    STYP_LOADER: long = 0x1000L
    STYP_NOLOAD: long = 0x2L
    STYP_OVER: long = 0x400L
    STYP_OVRFLO: long = 0x8000L
    STYP_PAD: long = 0x8L
    STYP_REG: long = 0x0L
    STYP_TEXT: long = 0x20L
    STYP_TYPECHK: long = 0x4000L



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
