import ghidra.app.util.bin.format.xcoff
import java.lang


class XCoffFileHeaderFlags(object):
    F_AR16WR: int = 128
    F_AR32W: int = 512
    F_AR32WR: int = 256
    F_DSA: int = 64
    F_DYNLOAD: int = 4096
    F_EXEC: int = 2
    F_FDPR_OPTI: int = 32
    F_FDPR_PROF: int = 16
    F_LNNO: int = 4
    F_LOADONLY: int = 16384
    F_LSYMS: int = 8
    F_RELFLG: int = 1
    F_SHROBJ: int = 8192



    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    @staticmethod
    def isDebug(header: ghidra.app.util.bin.format.xcoff.XCoffFileHeader) -> bool: ...

    @staticmethod
    def isExec(header: ghidra.app.util.bin.format.xcoff.XCoffFileHeader) -> bool: ...

    @staticmethod
    def isStrip(header: ghidra.app.util.bin.format.xcoff.XCoffFileHeader) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
