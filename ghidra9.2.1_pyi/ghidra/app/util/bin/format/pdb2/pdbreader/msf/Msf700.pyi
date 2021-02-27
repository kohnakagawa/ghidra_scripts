import ghidra.app.util.bin.format.pdb2.pdbreader.msf
import java.lang


class Msf700(ghidra.app.util.bin.format.pdb2.pdbreader.msf.AbstractMsf):




    def __init__(self, __a0: java.io.RandomAccessFile, __a1: ghidra.app.util.bin.format.pdb2.pdbreader.PdbReaderOptions): ...



    def close(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getNumStreams(self) -> int: ...

    def getPageSize(self) -> int: ...

    def getPageSizeOffset(self) -> int: ...

    def getStream(self, __a0: int) -> ghidra.app.util.bin.format.pdb2.pdbreader.msf.MsfStream: ...

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
    def pageSizeOffset(self) -> int: ...
