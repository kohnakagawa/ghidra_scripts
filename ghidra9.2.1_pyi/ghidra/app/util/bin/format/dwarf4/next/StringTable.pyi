import ghidra.app.util.bin
import ghidra.app.util.bin.format.dwarf4.next
import java.lang


class StringTable(object):
    """
    A offset-to-String string table backed by a simple byte array (encoded as UTF-8).

     Requested strings are instantiated when requested.
    """





    def __init__(self, bytes: List[int]):
        """
        Creates a StringTable using the bytes contained in the supplied array.
        """
        ...



    def add(self, offset: int, s: unicode) -> None:
        """
        Modifies the string table to add a string at a specified offset, growing the
         internal byte[] storage as necessary to accommodate the string at the offset.
         <p>
         Used for unit tests to construct a custom string table for test cases.
         <p>
        @param offset where to place the string in the table
        @param s string to insert into table
        """
        ...

    def clear(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getByteCount(self) -> int: ...

    def getClass(self) -> java.lang.Class: ...

    def getStringAtOffset(self, offset: long) -> unicode:
        """
        Returns the string found at <code>offset</code>, or throws an {@link IOException}
         if the offset is out of bounds.
        @param offset
        @return a string, never null.
        @throws IOException if not found
        """
        ...

    def hashCode(self) -> int: ...

    def isValid(self, offset: long) -> bool:
        """
        Returns true if the specified offset is a valid offset for this string table.
         <p>
        @param offset
        @return
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def readStringTable(bp: ghidra.app.util.bin.ByteProvider) -> ghidra.app.util.bin.format.dwarf4.next.StringTable:
        """
        Create a {@link StringTable} by reading the entire contents of a {@link ByteProvider}
         into memory.
         <p>
         If the specified {@link ByteProvider} is null, an empty string table will be constructed.
         <p>
        @param bp
        @return
        @throws IOException
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
    def byteCount(self) -> int: ...
