from typing import List
import ghidra.app.util.bin
import ghidra.formats.gfilesystem
import java.io
import java.lang


class RandomAccessMutableByteProvider(ghidra.app.util.bin.RandomAccessByteProvider, ghidra.app.util.bin.MutableByteProvider):
    """
    An implementation of ByteProvider where the underlying
     bytes are supplied by a random access file.
    """





    @overload
    def __init__(self, file: java.io.File):
        """
        Constructs a byte provider using the specified file
        @param file the file to open for random access
        @throws FileNotFoundException if the file does not exist
        """
        ...

    @overload
    def __init__(self, file: java.io.File, permissions: unicode):
        """
        Constructs a byte provider using the specified file and permissions string
        @param file the file to open for random access
        @param permissions indicating permissions used for open
        @throws FileNotFoundException if the file does not exist
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

    def length(self) -> long: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def readByte(self, index: long) -> int: ...

    def readBytes(self, index: long, length: long) -> List[int]: ...

    def setFSRL(self, fsrl: ghidra.formats.gfilesystem.FSRL) -> None:
        """
        Sets the {@link FSRL} of this {@link ByteProvider}
        @param fsrl the {@link FSRL} to assign to this byte provider
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    def writeByte(self, index: long, value: int) -> None: ...

    def writeBytes(self, index: long, values: List[int]) -> None: ...
