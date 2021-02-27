import java.lang


class XCoffSymbolStorageClass(object):
    C_BCOMM: int = 135
    C_BINCL: int = 108
    C_BLOCK: int = 100
    C_BSTAT: int = 143
    C_DECL: int = 140
    C_ECOML: int = 136
    C_ECOMM: int = 127
    C_EINCL: int = 109
    C_ENTRY: int = 141
    C_ESTAT: int = 144
    C_EXT: int = 2
    C_FCN: int = 101
    C_FILE: int = 103
    C_FUN: int = 142
    C_GSYM: int = 128
    C_HIDEXT: int = 107
    C_INFO: int = 100
    C_LSYM: int = 129
    C_NULL: int = 0
    C_PSYM: int = 130
    C_RPSYM: int = 132
    C_RSYM: int = 131
    C_STAT: int = 3
    C_STSYM: int = 133
    C_TCSYM: int = 134
    C_WEAKEXT: int = 111



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
