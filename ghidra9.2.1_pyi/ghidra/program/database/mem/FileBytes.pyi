from typing import List
import java.lang


class FileBytes(object):
    """
    FileBytes provides access to the all the byte values (both original and modified) from an
     imported file.
    """





    def __init__(self, adapter: ghidra.program.database.mem.FileBytesAdapter, record: db.Record): ...



    def equals(self, obj: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getFileOffset(self) -> long:
        """
        Returns the offset in the original file from where these bytes originated. Normally this will
         be 0, but in the case where the program is actually a piece in some other file (e.g. tar,zip),
         this will be the offset into the file corresponding to the first byte in this FileBytes object.
        @return the offset in the original file from where these bytes originated.
        """
        ...

    def getFilename(self) -> unicode:
        """
        Returns the name of the file that supplied the bytes.
        @return the name of the file that supplied the bytes.
        """
        ...

    def getModifiedByte(self, offset: long) -> int:
        """
        Returns the (possibly modified) byte at the given offset for this file bytes object.
        @param offset the offset into the file bytes for the byte to retrieve.
        @return the (possibly modified) byte at the given offset for this file bytes object.
        @throws IOException if there is a problem reading the database.
        @throws IndexOutOfBoundsException if the given offset is invalid.
        """
        ...

    @overload
    def getModifiedBytes(self, offset: long, b: List[int]) -> int:
        """
        Tries to get b.length (possibly modified) bytes from this FileBytes entry at the given offset into the file
          bytes.  May return fewer bytes if the requested length is beyond the end of the file bytes.
        @param offset the offset into the files bytes to start.
        @param b the byte array to populate.
        @return the number of bytes actually populated.
        @throws IOException if there is an error reading from the database
        """
        ...

    @overload
    def getModifiedBytes(self, offset: long, b: List[int], off: int, length: int) -> int:
        """
        Tries to get length (possibly modified) bytes from the files starting at the given offset and put them
         into the given byte array at the specified offset into the byte array.  May return
         fewer bytes if the requested length is beyond the end of the file bytes.
        @param offset the offset into the files bytes to start.
        @param b the byte array to populate.
        @param off the offset into the byte array.
        @param length the number of bytes to get.
        @return the number of bytes actually populated.
        @throws IOException if there is an error reading from the database
        @throws IndexOutOfBoundsException if the destination offset and length would exceed the
         size of the buffer b.
        """
        ...

    def getOriginalByte(self, offset: long) -> int:
        """
        Returns the original byte value at the given offset for this file bytes object.
        @param offset the offset into the file bytes for the byte to retrieve.
        @return the original byte at the given offset for this file bytes object.
        @throws IOException if there is a problem reading the database.
        @throws IndexOutOfBoundsException if the given offset is invalid.
        """
        ...

    @overload
    def getOriginalBytes(self, offset: long, b: List[int]) -> int:
        """
        Tries to get b.length original bytes from this FileBytes entry at the given offset into the file
          bytes.  May return fewer bytes if the requested length is beyond the end of the file bytes.
        @param offset the offset into the files bytes to start.
        @param b the byte array to populate.
        @return the number of bytes actually populated.
        @throws IOException if there is an error reading from the database
        """
        ...

    @overload
    def getOriginalBytes(self, offset: long, b: List[int], off: int, length: int) -> int:
        """
        Tries to get length (original) bytes from the files starting at the given offset and put them
         into the given byte array at the specified offset into the byte array.  May return
         fewer bytes if the requested length is beyond the end of the file bytes.
        @param offset the offset into the files bytes to start.
        @param b the byte array to populate.
        @param off the offset into the byte array.
        @param length the number of bytes to get.
        @return the number of bytes actually populated.
        @throws IOException if there is an error reading from the database
        @throws IndexOutOfBoundsException if the destination offset and length would exceed the
         size of the buffer b.
        """
        ...

    def getSize(self) -> long:
        """
        Returns the number of bytes from the original source file that are stored in the database.
        @return the number of bytes from the original source file that are stored in the database.
        """
        ...

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

    @property
    def fileOffset(self) -> long: ...

    @property
    def filename(self) -> unicode: ...

    @property
    def size(self) -> long: ...
