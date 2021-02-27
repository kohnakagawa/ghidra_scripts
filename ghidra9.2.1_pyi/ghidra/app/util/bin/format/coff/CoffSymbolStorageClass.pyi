import java.lang


class CoffSymbolStorageClass(object):
    C_ALIAS: int = 105
    C_ARG: int = 9
    C_AUTO: int = 1
    C_AUTOARG: int = 19
    C_BLOCK: int = 100
    C_EFCN: int = 107
    C_ENTAG: int = 15
    C_EOS: int = 102
    C_EXT: int = 2
    C_EXTDEF: int = 5
    C_FCN: int = 101
    C_FIELD: int = 18
    C_FILE: int = 103
    C_HIDDEN: int = 106
    C_LABEL: int = 6
    C_LASTENT: int = 20
    C_LINE: int = 104
    C_MOE: int = 16
    C_MOS: int = 8
    C_MOU: int = 11
    C_NULL: int = 0
    C_REG: int = 4
    C_REGPARAM: int = 17
    C_STAT: int = 3
    C_STRTAG: int = 10
    C_TPDEF: int = 13
    C_ULABEL: int = 7
    C_UNTAG: int = 12
    C_USTATIC: int = 14



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
