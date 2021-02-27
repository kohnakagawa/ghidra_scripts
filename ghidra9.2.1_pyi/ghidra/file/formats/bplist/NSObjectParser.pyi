import ghidra.app.util.bin
import ghidra.file.formats.bplist
import java.lang


class NSObjectParser(object):




    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def parseObject(__a0: ghidra.app.util.bin.BinaryReader, __a1: int, __a2: ghidra.file.formats.bplist.BinaryPropertyListTrailer) -> ghidra.file.formats.bplist.NSObject: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
