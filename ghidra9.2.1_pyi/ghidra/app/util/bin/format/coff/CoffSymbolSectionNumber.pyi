import java.lang


class CoffSymbolSectionNumber(object):
    N_ABS: int = -1
    N_BSS: int = 3
    N_DATA: int = 2
    N_DEBUG: int = -2
    N_TEXT: int = 1
    N_UNDEf: int = 0



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
