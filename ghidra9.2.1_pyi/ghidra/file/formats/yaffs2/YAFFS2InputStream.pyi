import ghidra.file.formats.yaffs2
import java.io
import java.lang


class YAFFS2InputStream(object):




    @overload
    def __init__(self, __a0: java.io.InputStream): ...

    @overload
    def __init__(self, __a0: java.io.InputStream, __a1: int): ...



    def close(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getEntryData(self, __a0: long, __a1: long) -> java.io.InputStream: ...

    def getNextHeaderEntry(self) -> ghidra.file.formats.yaffs2.YAFFS2Entry: ...

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

    @property
    def nextHeaderEntry(self) -> ghidra.file.formats.yaffs2.YAFFS2Entry: ...