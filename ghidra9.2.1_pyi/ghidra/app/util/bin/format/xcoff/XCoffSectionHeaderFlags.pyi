import java.lang


class XCoffSectionHeaderFlags(object):
    STYP_BSS: int = 128
    STYP_DATA: int = 64
    STYP_DEBUG: int = 8192
    STYP_EXCEPT: int = 128
    STYP_INFO: int = 512
    STYP_LOADER: int = 4096
    STYP_OVRFLO: int = 32768
    STYP_PAD: int = 8
    STYP_TEXT: int = 32
    STYP_TYPCHK: int = 16384



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
