from typing import List
import ghidra.app.util.bin
import ghidra.formats.gfilesystem
import java.io
import java.lang


class ByteArrayProvider(object, ghidra.app.util.bin.ByteProvider):
    """
    An implementation of ByteProvider where the underlying bytes are supplied by a static
     byte array.

     NOTE: Use of this class is discouraged when the byte array could be large.
    """





    @overload
    def __init__(self, bytes: List[int]):
        """
        Constructs a {@link ByteArrayProvider} using the specified byte array
        @param bytes the underlying byte array
        """
        ...

    @overload
    def __init__(self, name: unicode, bytes: List[int]):
        """
        Constructs a {@link ByteArrayProvider} using the specified byte array
        @param name the name of the {@link ByteProvider}
        @param bytes the underlying byte array
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
