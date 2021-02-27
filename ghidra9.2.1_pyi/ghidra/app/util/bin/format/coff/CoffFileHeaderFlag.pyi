import java.lang


class CoffFileHeaderFlag(object):
    F_AR16WR: int = 128
    F_AR32W: int = 512
    F_AR32WR: int = 256
    F_EXEC: int = 2
    F_LNNO: int = 4
    F_LSYMS: int = 8
    F_MINMAL: int = 16
    F_NODF: int = 1024
    F_PATCH: int = 1024
    F_RELFLG: int = 1
    F_SWABD: int = 64
    F_UPDATE: int = 32



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
