import ghidra.app.util.bin.format.xcoff
import java.lang


class XCoffFileHeaderMagic(object):
    MAGIC_XCOFF32: int = 479
    MAGIC_XCOFF64: int = 503
    MAGIC_XCOFF64_OLD: int = 495



    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    @staticmethod
    def is32bit(header: ghidra.app.util.bin.format.xcoff.XCoffFileHeader) -> bool: ...

    @staticmethod
    def is64bit(header: ghidra.app.util.bin.format.xcoff.XCoffFileHeader) -> bool: ...

    @staticmethod
    def isMatch(magic: int) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
