from typing import List
import ghidra.formats.gfilesystem
import java.io
import java.lang


class ByteProvider(java.io.Closeable, object):
    """
    An interface for a generic random-access byte provider.
    """









    def close(self) -> None:
        """
        Releases any resources the {@link ByteProvider} may have occupied
        @throws IOException if an I/O error occurs
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getAbsolutePath(self) -> unicode:
        """
        Returns the absolute path (similar to, but not a, URI) to the {@link ByteProvider}.
         For example, the complete path to the file.
        @return the absolute path to the {@link ByteProvider} or null if not associated with a
           {@link File}.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getFSRL(self) -> ghidra.formats.gfilesystem.FSRL:
        """
        Returns the {@link FSRL} of the underlying file for this byte provider,
         or null if this byte provider is not associated with a file.
        @return The {@link FSRL} of the underlying {@link File}, or null if no associated
           {@link File}.
        """
        ...

    def getFile(self) -> java.io.File:
        """
        Returns the underlying {@link File} for this {@link ByteProvider}, or null if this
         {@link ByteProvider} is not associated with a {@link File}.
        @return the underlying file for this byte provider
        """
        ...

    def getInputStream(self, index: long) -> java.io.InputStream:
        """
        Returns an input stream to the underlying byte provider starting at the specified index.
         <p>
         The caller is responsible for closing the returned {@link InputStream} instance.
         <p>
        @param index where in the {@link ByteProvider} to start the {@link InputStream}
        @return the {@link InputStream}
        @throws IOException if an I/O error occurs
        """
        ...

    def getName(self) -> unicode:
        """
        Returns the name of the {@link ByteProvider}. For example, the underlying file name.
        @return the name of the {@link ByteProvider} or null if there is no name
        """
        ...

    def hashCode(self) -> int: ...

    def isValidIndex(self, index: long) -> bool:
        """
        Returns true if the specified index is valid.
        @param index the index in the byte provider to check
        @return true if the specified index is valid
        """
        ...

    def length(self) -> long:
        """
        Returns the length of the {@link ByteProvider}
        @return the length of the {@link ByteProvider}
        @throws IOException if an I/O error occurs
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def readByte(self, index: long) -> int:
        """
        Reads a byte at the specified index
        @param index the index of the byte to read
        @return the byte read from the specified index
        @throws IOException if an I/O error occurs
        """
        ...

    def readBytes(self, index: long, length: long) -> List[int]:
        """
        Reads a byte array at the specified index
        @param index the index of the byte to read
        @param length the number of bytes to read
        @return the byte array read from the specified index
        @throws IOException if an I/O error occurs
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

    @property
    def absolutePath(self) -> unicode: ...

    @property
    def file(self) -> java.io.File: ...

    @property
    def name(self) -> unicode: ...
