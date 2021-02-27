import ghidra.app.util.bin
import java.lang


class OdexConstants(object):
    ODEX_MAGIC_35: unicode = u'dey\n035\x00'
    ODEX_MAGIC_36: unicode = u'dey\n036\x00'
    ODEX_MAGIC_37: unicode = u'dey\n037\x00'
    ODEX_MAGIC_LENGTH: int = 8



    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    @staticmethod
    def isOdexFile(__a0: ghidra.app.util.bin.ByteProvider) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
