import ghidra.app.util.bin
import java.lang


class DexConstants(object):
    DEX_MAGIC_BASE: unicode = u'dex\n'
    DEX_VERSION_009: unicode = u'009'
    DEX_VERSION_035: unicode = u'035'
    DEX_VERSION_036: unicode = u'036'
    DEX_VERSION_037: unicode = u'037'
    DEX_VERSION_038: unicode = u'038'
    DEX_VERSION_039: unicode = u'039'
    DEX_VERSION_LENGTH: int = 4
    ENDIAN_CONSTANT: int = 305419896
    MACHINE: unicode = u'1'
    REVERSE_ENDIAN_CONSTANT: int = 2018915346
    kClassesDex: unicode = u'classes.dex'



    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    @staticmethod
    def isDexFile(__a0: ghidra.app.util.bin.ByteProvider) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
