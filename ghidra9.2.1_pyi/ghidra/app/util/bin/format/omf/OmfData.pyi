from typing import List
import ghidra.app.util.bin
import java.lang


class OmfData(java.lang.Comparable, object):
    """
    Object representing data loaded directly into the final image.
    """









    def compareTo(self, __a0: object) -> int: ...

    def equals(self, __a0: object) -> bool: ...

    def getByteArray(self, reader: ghidra.app.util.bin.BinaryReader) -> List[int]:
        """
        Create a byte array holding the data represented by this object. The length
         of the byte array should exactly match the value returned by getLength()
        @param reader is for pulling bytes directly from the binary image
        @return allocated and filled byte array
        @throws IOException for problems accessing data through the reader
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getDataOffset(self) -> long:
        """
        @return the starting offset, within the loaded image, of this data
        """
        ...

    def getLength(self) -> int:
        """
        @return the length of this data in bytes
        """
        ...

    def hashCode(self) -> int: ...

    def isAllZeroes(self) -> bool:
        """
        @return true if this is a block entirely of zeroes
        """
        ...

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
    def allZeroes(self) -> bool: ...

    @property
    def dataOffset(self) -> long: ...

    @property
    def length(self) -> int: ...
