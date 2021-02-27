import java.lang


class ElfProgramHeaderConstants(object):
    PF_MASKOS: int = 267386880
    PF_MASKPROC: int = -268435456
    PF_R: int = 4
    PF_W: int = 2
    PF_X: int = 1
    PT_DYNAMIC: int = 2
    PT_GNU_EH_FRAME: int = 1685382480
    PT_GNU_RELRO: int = 1685382482
    PT_GNU_STACK: int = 1685382481
    PT_INTERP: int = 3
    PT_LOAD: int = 1
    PT_NOTE: int = 4
    PT_NULL: int = 0
    PT_PHDR: int = 6
    PT_SHLIB: int = 5
    PT_SUNWBSS: int = 1879048186
    PT_SUNWSTACK: int = 1879048187
    PT_TLS: int = 7







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
