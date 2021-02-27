from typing import List
import ghidra.app.util.bin
import ghidra.formats.gfilesystem
import java.io
import java.lang


class InputStreamByteProvider(object, ghidra.app.util.bin.ByteProvider):
    """
    A ByteProvider implementation that wraps an InputStream, allowing
     data to be read, as long as there are no operations that request data from a previous
     offset.

     In other words, this ByteProvider can only be used to read data at ever increasing
     offsets.

    """





    def __init__(self, inputStream: java.io.InputStream, length: long):
        """
        Constructs a {@link InputStreamByteProvider} from the specified {@link InputStream}
        @param inputStream the underlying {@link InputStream}
        @param length the length of the {@link InputStreamByteProvider}
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

    def getUnderlyingInputStream(self) -> java.io.InputStream: ...

    def hashCode(self) -> int: ...

    def isValidIndex(self, index: long) -> bool: ...

    def length(self) -> long: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def readByte(self, index: long) -> int: ...

    def readBytes(self, index: long, len: long) -> List[int]: ...

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

    @property
    def underlyingInputStream(self) -> java.io.InputStream: ...
