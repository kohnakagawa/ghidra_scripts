from typing import List
import ghidra.program.model.address
import ghidra.program.model.mem
import java.lang


class MemBuffer(object):
    """
    MemBuffer provides an array like interface into memory at a
     specific address.  Bytes can be retrieved by using a positive
     offset from the current position.  Depending on the implementation,
     the offset may be restricted to a specific positive range.  If the
     implementation does have a restriction, then a MemoryAccessException
     will be thrown, except for the #getBytes(byte[], int)
     method which will return 0.

     The purpose of this class is to
     allow an efficient implementation that buffers memory accesses and
     does not have to keep translating addresses.  This was designed to
     be passed to a language parser.  One advantage of MemBuffer over a
     byte array is that if necessary the actual Memory and Address can
     be retrieved in case all of the necessary bytes are not local.

     This interface does not provide methods to reposition the memory
     buffer.  This is so that it is clear that methods accepting this
     base class are not to mess which the base Address for this object.

     Memory-backed access is an optional implementation dependent
     capability.  In addition, the use of the relative offset is
     implementation dependent, but in general those implementations
     which are backed by memory may choose to wrap the offset
     when computing the corresponding memory address.  The treatment
     of the offset argument should be consistent across the various
     methods for a given implementation.
    """









    def equals(self, __a0: object) -> bool: ...

    def getAddress(self) -> ghidra.program.model.address.Address:
        """
        Get the Address which corresponds to the offset 0.
        @return the current address of offset 0.
        """
        ...

    def getBigInteger(self, offset: int, size: int, signed: bool) -> long:
        """
        returns the value at the given offset, taking into account the endianess.
        @param offset the offset from the membuffers origin (the address that it is set at)
        @param size the number of bytes to include in the value
        @param signed true if value should be treated as a signed twos-compliment value.
        @return the value at the given offset, taking into account the endianess.
        @throws MemoryAccessException if the request size value cannot be read at the specified offset
        """
        ...

    def getByte(self, offset: int) -> int:
        """
        Get one byte from memory at the current position plus offset.
        @param offset the displacement from the current position.
        @return the data at offset from the current position.
        @throws MemoryAccessException if memory cannot be read at the specified offset
        """
        ...

    def getBytes(self, b: List[int], offset: int) -> int:
        """
        Reads <code>b.length</code> bytes from this memory buffer
         starting at the address of this memory buffer plus the given memoryBufferOffset
         from that position.  The actual number of bytes may be fewer
         if bytes can't be read.
        @param b the buffer into which bytes will be placed
        @param offset the offset <b>in this memory buffer</b> from which to
                start reading bytes.
        @return the number of bytes read which may be fewer than b.length if
         available bytes are exhausted or no bytes are available at the specified
         offset.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getInt(self, offset: int) -> int:
        """
        returns the int at the given offset, taking into account the endianess.
        @param offset the offset from the membuffers origin (the address that it is set at)
        @return the int at the given offset, taking into account the endianess.
        @throws MemoryAccessException if a 4-byte integer value cannot be read at the specified offset
        """
        ...

    def getLong(self, offset: int) -> long:
        """
        returns the long at the given offset, taking into account the endianess.
        @param offset the offset from the membuffers origin (the address that it is set at)
        @return the long at the given offset, taking into account the endianess.
        @throws MemoryAccessException if a 8-byte long value cannot be read at the specified offset
        """
        ...

    def getMemory(self) -> ghidra.program.model.mem.Memory:
        """
        Get the Memory object actually used by the MemBuffer.
        @return the Memory used by this MemBuffer.
        """
        ...

    def getShort(self, offset: int) -> int:
        """
        returns the short at the given offset, taking into account the endianess.
        @param offset the offset from the membuffers origin (the address that it is set at)
        @return the short at the given offset, taking into account the endianess.
        @throws MemoryAccessException if a 2-byte short value cannot be read at the specified offset
        """
        ...

    def getUnsignedByte(self, offset: int) -> int:
        """
        Get one unsigned byte from memory at the current position plus offset.
        @param offset the displacement from the current position.
        @return the byte data at offset from the current position, as a {@code int} value.
        @throws MemoryAccessException if memory cannot be read at the specified offset
        """
        ...

    def getUnsignedInt(self, offset: int) -> long:
        """
        Returns the unsigned int at the given offset, taking into account the endianess.
        @param offset the offset from the membuffers origin (the address that it is set at)
        @return the unsigned int at the given offset, as a {@code long}, taking into account the endianess.
        @throws MemoryAccessException if a 4-byte integer value cannot be read at the specified offset
        """
        ...

    def getUnsignedShort(self, offset: int) -> int:
        """
        Returns the unsigned short at the given offset, taking into account the endian-ness.
        @param offset the offset from the membuffers origin (the address that it is set at)
        @return the unsigned short at the given offset, as a {@code int}, taking into account the endianess.
        @throws MemoryAccessException if a 2-byte short value cannot be read at the specified offset
        """
        ...

    def getVarLengthInt(self, offset: int, len: int) -> int:
        """
        Returns the signed value of the integer (of the specified length) at the specified offset.
        @param offset the offset from the membuffers origin (the address that it is set at)
        @param len the number of bytes that the integer occupies (ie. 2 bytes == short int, 4
         bytes == 32bit int, etc), valid lens are 1, 2 and 4.
        @return int integer value
        @throws MemoryAccessException
        """
        ...

    def getVarLengthUnsignedInt(self, offset: int, len: int) -> long:
        """
        Returns the unsigned value of the integer (of the specified length) at the specified offset.
        @param offset the offset from the membuffers origin (the address that it is set at)
        @param len the number of bytes that the integer occupies (ie. 2 bytes == short int, 4
         bytes == 32bit int, etc), valid lens are 1, 2 and 4.
        @return long integer value
        @throws MemoryAccessException
        """
        ...

    def hashCode(self) -> int: ...

    def isBigEndian(self) -> bool:
        """
        Returns true if the underlying bytes are in big-endian order, false if they are little endian.
        @return true if the underlying bytes are in big-endian order, false if they are little endian.
        """
        ...

    def isInitializedMemory(self) -> bool:
        """
        Returns true if this buffer's starting address has valid data.
        @return boolean true if first byte of memory buffer can be read
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
    def address(self) -> ghidra.program.model.address.Address: ...

    @property
    def bigEndian(self) -> bool: ...

    @property
    def initializedMemory(self) -> bool: ...

    @property
    def memory(self) -> ghidra.program.model.mem.Memory: ...
