import java.lang


class XCoffSymbolStorageClassCSECT(object):
    XMC_BS: int = 9
    XMC_DB: int = 2
    XMC_DS: int = 10
    XMC_GL: int = 6
    XMC_PR: int = 0
    XMC_RO: int = 1
    XMC_RW: int = 5
    XMC_SV: int = 8
    XMC_SV3264: int = 18
    XMC_SV64: int = 17
    XMC_TB: int = 13
    XMC_TC: int = 3
    XMC_TC0: int = 15
    XMC_TD: int = 16
    XMC_TI: int = 12
    XMC_UA: int = 4
    XMC_UC: int = 11
    XMC_XO: int = 7



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
