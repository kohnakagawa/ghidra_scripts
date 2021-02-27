from typing import List
import ghidra.app.util.bin
import ghidra.formats.gfilesystem
import java.io
import java.lang


class MutableByteProvider(ghidra.app.util.bin.ByteProvider, object):
    """
    An interface for a generic random-access byte provider, plus mutation methods.
    """









    def close(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getAbsolutePath(self) -> unicode: ...

    def getClass(self) -> java.lang.Class: ...

    def getFSRL(self) -> ghidra.formats.gfilesystem.FSRL: ...

    def getFile(self) -> java.io.File: ...

    def getInputStream(self, __a0: long) -> java.io.InputStream: ...

    def getName(self) -> unicode: ...

    def hashCode(self) -> int: ...

    def isValidIndex(self, __a0: long) -> bool: ...

    def length(self) -> long: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def readByte(self, __a0: long) -> int: ...

    def readBytes(self, __a0: long, __a1: long) -> List[int]: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    def writeByte(self, index: long, value: int) -> None:
        """
        Writes a byte at the specified index.
        @param index the index to write the byte
        @param value the value to write at the specified index
        @throws IOException if an I/O error occurs
        """
        ...

    def writeBytes(self, index: long, values: List[int]) -> None:
        """
        Writes a byte array at the specified index.
        @param index the index to write the byte array
        @param values the values to write at the specified index
        @throws IOException if an I/O error occurs
        """
        ...

    @property
    def FSRL(self) -> ghidra.formats.gfilesystem.FSRL: ...

    @property
    def absolutePath(self) -> unicode: ...

    @property
    def file(self) -> java.io.File: ...

    @property
    def name(self) -> unicode: ...
