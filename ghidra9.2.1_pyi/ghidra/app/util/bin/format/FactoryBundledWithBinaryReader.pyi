from typing import List
import generic.continues
import ghidra.app.util.bin
import java.lang


class FactoryBundledWithBinaryReader(ghidra.app.util.bin.BinaryReader):




    def __init__(self, factory: generic.continues.GenericFactory, provider: ghidra.app.util.bin.ByteProvider, isLittleEndian: bool): ...



    def align(self, alignValue: int) -> int:
        """
        Aligns the current index on the specified alignment value.
         For example, if current index was 123 and align value was
         16, then current index would become 128.
        @param alignValue
        @return the number of bytes required to align
        """
        ...

    def clone(self, newIndex: long) -> ghidra.app.util.bin.BinaryReader:
        """
        Returns a clone of this reader positioned at the new index.
        @param newIndex the new index
        @return a clone of this reader positioned at the new index
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getByteProvider(self) -> ghidra.app.util.bin.ByteProvider:
        """
        Returns the underlying byte provider.
        @return the underlying byte provider
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getFactory(self) -> generic.continues.GenericFactory: ...

    def getPointerIndex(self) -> long:
        """
        Returns the current index value.
        @return the current index value
        """
        ...

    def hashCode(self) -> int: ...

    def isLittleEndian(self) -> bool:
        """
        Returns true if this reader will extract values in little endian,
         otherwise in big endian.
        @return true is little endian, false is big endian
        """
        ...

    @overload
    def isValidIndex(self, index: long) -> bool:
        """
        Returns true if the specified index into
         the underlying byte provider is valid.
        @param index the index in the byte provider
        @return returns true if the specified index is valid
        @exception IOException if an I/O error occurs
        """
        ...

    @overload
    def isValidIndex(self, index: int) -> bool:
        """
        Returns true if the specified index into
         the underlying byte provider is valid.
        @param index the index in the byte provider
        @return returns true if the specified index is valid
        @exception IOException if an I/O error occurs
        """
        ...

    def length(self) -> long:
        """
        Returns the length of the underlying file.
        @return returns the length of the underlying file
        @exception IOException if an I/O error occurs
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def peekNextByte(self) -> int:
        """
        Peeks at the next byte without incrementing
         the current index.
        @return the next byte
        @exception IOException if an I/O error occurs
        """
        ...

    def peekNextInt(self) -> int:
        """
        Peeks at the next integer without incrementing
         the current index.
        @return the next int
        @exception IOException if an I/O error occurs
        """
        ...

    def peekNextLong(self) -> long:
        """
        Peeks at the next long without incrementing
         the current index.
        @return the next long
        @exception IOException if an I/O error occurs
        """
        ...

    def peekNextShort(self) -> int:
        """
        Peeks at the next short without incrementing
         the current index.
        @return the next short
        @exception IOException if an I/O error occurs
        """
        ...

    @overload
    def readAsciiString(self, index: long) -> unicode:
        """
        Reads an Ascii string starting at <code>index</code>, ending
         at the next character outside the range [32..126] or when
         reaching the end of the underlying ByteProvider.
         <p>
         Leading and trailing spaces will be trimmed before the string is returned.
        @param index the index where the Ascii string begins
        @return the trimmed Ascii string
        @exception IOException if an I/O error occurs
        """
        ...

    @overload
    def readAsciiString(self, index: long, length: int) -> unicode:
        """
        Returns an Ascii string of <code>length</code> bytes
         starting at <code>index</code>. This method does not
         care about null-terminators.  Leading and trailing spaces
         will be trimmed before the string is returned.
        @param index the index where the Ascii string begins
        @param length the length of the Ascii string
        @return the trimmed Ascii string
        @exception IOException if an I/O error occurs
        """
        ...

    def readAsciiStringArray(self, index: long, nElements: int) -> List[unicode]:
        """
        Returns the Ascii string array of <code>nElements</code>
         starting at <code>index</code>
        @param index the index where the Ascii Strings begin
        @param nElements the number of array elements
        @return the Ascii String array
        @exception IOException if an I/O error occurs
        """
        ...

    def readByte(self, index: long) -> int:
        """
        Returns the signed BYTE at <code>index</code>.
        @param index the index where the BYTE begins
        @return the signed BYTE
        @exception IOException if an I/O error occurs
        """
        ...

    def readByteArray(self, index: long, nElements: int) -> List[int]:
        """
        Returns the BYTE array of <code>nElements</code>
         starting at <code>index</code>.
        @param index the index where the BYTE begins
        @param nElements the number of array elements
        @return the BYTE array
        @exception IOException if an I/O error occurs
        """
        ...

    def readFixedLenAsciiString(self, index: long, len: int) -> unicode:
        """
        Reads an fixed length Ascii string starting at <code>index</code>.
         <p>
         Does NOT trim the string.
         <p>
        @param index the index where the Ascii string begins
        @param len number of bytes to read
        @return the Ascii string
        @exception IOException if an I/O error occurs
        """
        ...

    def readInt(self, index: long) -> int:
        """
        Returns the signed INTEGER at <code>index</code>.
        @param index the index where the INTEGER begins
        @return the signed INTEGER
        @exception IOException if an I/O error occurs
        """
        ...

    def readIntArray(self, index: long, nElements: int) -> List[int]:
        """
        Returns the INTEGER array of <code>nElements</code>
         starting at <code>index</code>.
        @param index the index where the INTEGER begins
        @param nElements the number of array elements
        @return the INTEGER array
        @exception IOException if an I/O error occurs
        """
        ...

    def readLong(self, index: long) -> long:
        """
        Returns the signed LONG at <code>index</code>.
        @param index the index where the LONG begins
        @return the LONG
        @exception IOException if an I/O error occurs
        """
        ...

    def readLongArray(self, index: long, nElements: int) -> List[long]:
        """
        Returns the LONG array of <code>nElements</code>
         starting at <code>index</code>.
        @param index the index where the LONG begins
        @param nElements the number of array elements
        @return the LONG array
        @exception IOException if an I/O error occurs
        """
        ...

    @overload
    def readNextAsciiString(self) -> unicode:
        """
        Reads the Ascii string at the current index and then increments the current
         index by the length of the Ascii string that was found. This method
         expects the string to be null-terminated.
        @return the null-terminated Ascii string at the current index
        @exception IOException if an I/O error occurs
        """
        ...

    @overload
    def readNextAsciiString(self, length: int) -> unicode:
        """
        Reads an Ascii string of <code>length</code>
         characters starting at the current index and then increments the current
         index by <code>length</code>.
        @return the Ascii string at the current index
        """
        ...

    def readNextByte(self) -> int:
        """
        Reads the byte at the current index and then increments the current
         index by <code>SIZEOF_BYTE</code>.
        @return the byte at the current index
        @exception IOException if an I/O error occurs
        """
        ...

    def readNextByteArray(self, nElements: int) -> List[int]:
        """
        Reads a byte array of <code>nElements</code>
         starting at the current index and then increments the current
         index by <code>SIZEOF_BYTE * nElements</code>.
        @return the byte array starting at the current index
        @exception IOException if an I/O error occurs
        """
        ...

    def readNextInt(self) -> int:
        """
        Reads the integer at the current index and then increments the current
         index by <code>SIZEOF_INT</code>.
        @return the integer at the current index
        @exception IOException if an I/O error occurs
        """
        ...

    def readNextIntArray(self, nElements: int) -> List[int]:
        """
        Reads an integer array of <code>nElements</code>
         starting at the current index and then increments the current
         index by <code>SIZEOF_INT * nElements</code>.
        @return the integer array starting at the current index
        @exception IOException if an I/O error occurs
        """
        ...

    def readNextLong(self) -> long:
        """
        Reads the long at the current index and then increments the current
         index by <code>SIZEOF_LONG</code>.
        @return the long at the current index
        @exception IOException if an I/O error occurs
        """
        ...

    def readNextLongArray(self, nElements: int) -> List[long]:
        """
        Reads a long array of <code>nElements</code>
         starting at the current index and then increments the current
         index by <code>SIZEOF_LONG * nElements</code>.
        @return the long array starting at the current index
        @exception IOException if an I/O error occurs
        """
        ...

    def readNextNullTerminatedAsciiString(self) -> unicode:
        """
        Reads a null terminated Ascii string starting at the current index,
         ending at the first null character or when reaching the
         end of the underlying ByteProvider.
         <p>
         The current index is advanced to the next byte after the null terminator.
         <p>
        @return the null-terminated Ascii string at the current index
        @exception IOException if an I/O error occurs
        """
        ...

    def readNextShort(self) -> int:
        """
        Reads the short at the current index and then increments the current
         index by <code>SIZEOF_SHORT</code>.
        @return the short at the current index
        @exception IOException if an I/O error occurs
        """
        ...

    def readNextShortArray(self, nElements: int) -> List[int]:
        """
        Reads a short array of <code>nElements</code>
         starting at the current index and then increments the current
         index by <code>SIZEOF_SHORT * nElements</code>.
        @return the short array starting at the current index
        @exception IOException if an I/O error occurs
        """
        ...

    @overload
    def readNextUnicodeString(self) -> unicode:
        """
        Reads the Unicode string at the current index and then increments the current
         index by the length of the Unicode string that was found. This method
         expects the string to be double null-terminated ('\0\0').
        @return the null-terminated Ascii string at the current index
        @exception IOException if an I/O error occurs
        """
        ...

    @overload
    def readNextUnicodeString(self, length: int) -> unicode:
        """
        Reads fixed length UTF-16 Unicode string the current index and then increments the current
         {@link #setPointerIndex(int) pointer index} by <code>length</code> elements (length*2 bytes).
        @return the UTF-16 Unicode string at the current index
        @exception IOException if an I/O error occurs
        """
        ...

    def readNextUnsignedByte(self) -> int:
        """
        Reads the unsigned byte at the current index and then increments the current
         index by <code>SIZEOF_BYTE</code>.
        @return the unsigned byte at the current index, as an int
        @exception IOException if an I/O error occurs
        """
        ...

    def readNextUnsignedInt(self) -> long:
        """
        Reads the unsigned integer at the current index and then increments the current
         index by <code>SIZEOF_INT</code>.
        @return the unsigned integer at the current index, as a long
        @exception IOException if an I/O error occurs
        """
        ...

    def readNextUnsignedShort(self) -> int:
        """
        Reads the unsigned short at the current index and then increments the current
         index by <code>SIZEOF_SHORT</code>.
        @return the unsigned short at the current index, as an int
        @exception IOException if an I/O error occurs
        """
        ...

    def readShort(self, index: long) -> int:
        """
        Returns the signed SHORT at <code>index</code>.
        @param index the index where the SHORT begins
        @return the signed SHORT
        @exception IOException if an I/O error occurs
        """
        ...

    def readShortArray(self, index: long, nElements: int) -> List[int]:
        """
        Returns the SHORT array of <code>nElements</code>
         starting at <code>index</code>.
        @param index the index where the SHORT begins
        @param nElements the number of array elements
        @return the SHORT array
        @exception IOException if an I/O error occurs
        """
        ...

    @overload
    def readTerminatedString(self, index: long, termChar: int) -> unicode:
        """
        Reads an Ascii string starting at <code>index</code>, ending
         at the next {@code termChar} character byte or when  reaching the end of
         the underlying ByteProvider.
         <p>
         Does NOT trim the string.
         <p>
        @param index the index where the Ascii string begins
        @return the Ascii string (excluding the terminating character)
        @exception IOException if an I/O error occurs
        """
        ...

    @overload
    def readTerminatedString(self, index: long, termChars: unicode) -> unicode:
        """
        Reads an Ascii string starting at <code>index</code>, ending
         at the next character that is one of the specified {@code termChars} or when
         reaching the end of the underlying ByteProvider.
         <p>
         Does NOT trim the string.
         <p>
        @param index the index where the Ascii string begins
        @return the Ascii string (excluding the terminating character)
        @exception IOException if an I/O error occurs
        """
        ...

    @overload
    def readUnicodeString(self, index: long) -> unicode:
        """
        Reads a null-terminated UTF-16 Unicode string starting
         at <code>index</code> using the pre-specified
         {@link #setLittleEndian(boolean) endianness}.
         <p>
         The end of the string is denoted by a two-byte (ie. short) <code>null</code> character.
         <p>
         Leading and trailing spaces will be trimmed before the string is returned.
         <p>
        @param index the index where the UTF-16 Unicode string begins
        @return the trimmed UTF-16 Unicode string
        @exception IOException if an I/O error occurs
        """
        ...

    @overload
    def readUnicodeString(self, index: long, length: int) -> unicode:
        """
        Reads a fixed length UTF-16 Unicode string of <code>length</code> characters
         starting at <code>index</code>, using the pre-specified
         {@link #setLittleEndian(boolean) endianness}.
         <p>
         This method does not care about null-terminators.
         <p>
         Leading and trailing spaces will be trimmed before the string is returned.
         <p>
        @param index the index where the UTF-16 Unicode string begins
        @param length the number of UTF-16 character elements to read.
        @return the trimmed UTF-16 Unicode string
        @exception IOException if an I/O error occurs
        """
        ...

    def readUnsignedByte(self, index: long) -> int:
        """
        Returns the unsigned BYTE at <code>index</code>.
        @param index the index where the BYTE begins
        @return the unsigned BYTE as an int
        @exception IOException if an I/O error occurs
        """
        ...

    def readUnsignedInt(self, index: long) -> long:
        """
        Returns the unsigned INTEGER at <code>index</code>.
        @param index the index where the INTEGER begins
        @return the unsigned INTEGER as a long
        @exception IOException if an I/O error occurs
        """
        ...

    def readUnsignedShort(self, index: long) -> int:
        """
        Returns the unsigned SHORT at <code>index</code>.
        @param index the index where the SHORT begins
        @return the unsigned SHORT as an int
        @exception IOException if an I/O error occurs
        """
        ...

    def readUnsignedValue(self, index: long, len: int) -> long:
        """
        Returns the unsigned value of the integer (of the specified length) at the specified offset.
        @param index offset the offset from the membuffers origin (the address that it is set at)
        @param len the number of bytes that the integer occupies.  Valid values are 1 (byte), 2 (short),
         4 (int), 8 (long)
        @return unsigned value of requested length, in a long
        @throws IOException
        """
        ...

    def readValue(self, index: long, len: int) -> long:
        """
        Returns the signed value of the integer (of the specified length) at the specified offset.
        @param index offset the offset from the membuffers origin (the address that it is set at)
        @param len the number of bytes that the integer occupies.  Valid values are 1 (byte), 2 (short),
         4 (int), 8 (long)
        @return value of requested length, with sign bit extended, in a long
        @throws IOException
        """
        ...

    def setLittleEndian(self, isLittleEndian: bool) -> None:
        """
        Sets the endian of this binary reader.
        @param isLittleEndian true for little-endian and false for big-endian
        """
        ...

    @overload
    def setPointerIndex(self, index: long) -> None:
        """
        Sets the current index to the specified value.
         The pointer index will allow the reader
         to operate as a psuedo-iterator.
        @param index the byte provider index value
        """
        ...

    @overload
    def setPointerIndex(self, index: int) -> None:
        """
        A convenience method for setting the index using
         an integer.
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
    def factory(self) -> generic.continues.GenericFactory: ...
