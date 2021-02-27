from typing import List
import ghidra.app.util.bin
import ghidra.formats.gfilesystem
import java.io
import java.lang


class MemBufferByteProvider(object, ghidra.app.util.bin.ByteProvider):
    """
    MemBufferByteProvider provide a ByteProvider backed by
     a MemBuffer.
    """





    def __init__(self, buffer: ghidra.program.model.mem.MemBuffer):
        """
        Constructor
        @param buffer memory buffer
        """
        ...



    def close(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getAbsolutePath(self) -> unicode: ...

    def getClass(self) -> java.lang.Class: ...

    def getFSRL(self) -> ghidra.formats.gfilesystem.FSRL: ...

    def getFile(self) -> java.io.File: ...

    def getInputStream(self, index: long) -> java.io.InputStream: ...

    def getName(self) -> unicode: ...

    def hashCode(self) -> int: ...

    def isValidIndex(self, index: long) -> bool: ...

    def length(self) -> long:
        """
        Return maximum length since actual length is unknown
        @return maximum possible length
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def readByte(self, index: long) -> int: ...

    def readBytes(self, index: long, length: long) -> List[int]: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def FSRL(self) -> ghidra.formats.gfilesystem.FSRL: ...

    @property
    def absolutePath(self) -> unicode: ...

    @property
    def file(self) -> java.io.File: ...

    @property
    def name(self) -> unicode: ...
