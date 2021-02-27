from typing import List
import ghidra.app.util.bin
import ghidra.formats.gfilesystem
import java.io
import java.lang


class RandomAccessByteProvider(object, ghidra.app.util.bin.ByteProvider):
    """
    An implementation of ByteProvider where the underlying
     bytes are supplied by a random access file.

     Note: this implementation is not thread-safe, and using an instance of this
     class from multiple threads will result in reading incorrect data and/or
     ArrayIndexOutOfBoundsExceptions.

     See SynchronizedByteProvider as a solution.
    """





    @overload
    def __init__(self, file: java.io.File):
        """
        Constructs a {@link ByteProvider} using the specified {@link File}.
        @param file the {@link File} to open for random access
        @throws IOException if the {@link File} does not exist or other error
        """
        ...

    @overload
    def __init__(self, file: java.io.File, permissions: unicode):
        """
        Constructs a {@link ByteProvider} using the specified {@link File} and permissions
        @param file the {@link File} to open for random access
        @param permissions indicating permissions used for open
        @throws IOException if the {@link File} does not exist or other error
        """
        ...

    @overload
    def __init__(self, file: java.io.File, fsrl: ghidra.formats.gfilesystem.FSRL):
        """
        Constructs a {@link ByteProvider} using the specified {@link File} and {@link FSRL}
        @param file the {@link File} to open for random access
        @param fsrl the {@link FSRL} to use for the {@link File}'s path
        @throws IOException if the {@link File} does not exist or other error
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

    @property
    def FSRL(self) -> ghidra.formats.gfilesystem.FSRL: ...

    @FSRL.setter
    def FSRL(self, value: ghidra.formats.gfilesystem.FSRL) -> None: ...

    @property
    def absolutePath(self) -> unicode: ...

    @property
    def file(self) -> java.io.File: ...

    @property
    def name(self) -> unicode: ...
