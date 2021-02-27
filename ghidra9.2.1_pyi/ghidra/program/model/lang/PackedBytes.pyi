import java.io
import java.lang


class PackedBytes(object):
    """
    A class for dynamically collecting a stream of bytes and then later dumping those bytes to a stream
     It allows the bytes to be edited in the middle of collection
    """





    def __init__(self, startlen: int): ...



    def equals(self, __a0: object) -> bool: ...

    def find(self, start: int, val: int) -> int: ...

    def getByte(self, streampos: int) -> int:
        """
        Inspect the middle of the byte stream accumulated so far
        @param streampos is the index of the byte to inspect
        @return a byte value from the stream
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def insertByte(self, streampos: int, val: int) -> None:
        """
        Overwrite bytes that have already been written into the stream
        @param streampos is the index of the byte to overwrite
        @param val is the value to overwrite with
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def size(self) -> int: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    def write(self, val: int) -> None:
        """
        Dump a single byte to the packed byte stream
        @param val is the byte to be written
        """
        ...

    def writeTo(self, s: java.io.OutputStream) -> None:
        """
        Write the accumulated packed byte stream onto the output stream
        @param s is the output stream receiving the bytes
        @throws IOException
        """
        ...
