import ghidra.util
import java.io
import java.lang


class Writeable(object):
    """
    An interface for writing out class state information.
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

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

    def write(self, raf: java.io.RandomAccessFile, dc: ghidra.util.DataConverter) -> None:
        """
        Writes this object to the specified random access file using
         the data converter to handle endianness.
        @param raf the random access file
        @param dc the data converter
        @throws IOException if an I/O error occurs
        """
        ...
