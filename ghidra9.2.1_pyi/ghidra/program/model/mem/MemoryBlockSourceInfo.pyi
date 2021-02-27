import ghidra.program.model.address
import ghidra.program.model.mem
import java.lang
import java.util


class MemoryBlockSourceInfo(object):
    """
    Describes the source of bytes for a memory block.
    """









    def contains(self, address: ghidra.program.model.address.Address) -> bool:
        """
        Returns true if this SourceInfo object applies to the given address;
        @param address the address to test if this is its SourceInfo
        @return true if this SourceInfo object applies to the given address;
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getByteMappingScheme(self) -> java.util.Optional:
        """
        Returns an {@link Optional} {@link ByteMappingScheme} employed if this is a byte-mapped
         memory block.  Otherwise, the Optional is empty.
        @return an {@link Optional} {@link ByteMappingScheme} employed if this is a byte-mapped memory block.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getDescription(self) -> unicode:
        """
        Returns a description of this SourceInfo object.
        @return a description of this SourceInfo object.
        """
        ...

    def getFileBytes(self) -> java.util.Optional:
        """
        Returns an {@link Optional} {@link FileBytes} object if a FileBytes object is the byte
         source for this SourceInfo.  Otherwise, the Optional will be empty.
        @return the {@link FileBytes} object if it is the byte source for this section
        """
        ...

    @overload
    def getFileBytesOffset(self) -> long:
        """
        Returns the offset into the {@link FileBytes} object where this section starts getting its bytes or
         -1 if this SourceInfo does not have an associated {@link FileBytes}
        @return the offset into the {@link FileBytes} object where this section starts getting its bytes.
        """
        ...

    @overload
    def getFileBytesOffset(self, address: ghidra.program.model.address.Address) -> long:
        """
        Returns the offset into the {@link FileBytes} object for the given address or
         -1 if this MemoryBlockSourceInfo does not have an associated {@link FileBytes} or the address doesn't
         belong to this MemoryBlockSourceInfo.
        @param address the address for which to get an offset into the {@link FileBytes} object.
        @return the offset into the {@link FileBytes} object for the given address.
        """
        ...

    def getLength(self) -> long:
        """
        Returns the length of this block byte source.
        @return the length of this block byte source.
        """
        ...

    def getMappedRange(self) -> java.util.Optional:
        """
        Returns an {@link Optional} {@link AddressRange} for the mapped addresses if this is a mapped
         memory block (bit mapped or byte mapped). Otherwise, the Optional is empty.
        @return an {@link Optional} {@link AddressRange} for the mapped addresses if this is a mapped
         memory block
        """
        ...

    def getMaxAddress(self) -> ghidra.program.model.address.Address:
        """
        Returns the end address where this byte source is mapped.
        @return the end address where this byte source is mapped.
        """
        ...

    def getMemoryBlock(self) -> ghidra.program.model.mem.MemoryBlock:
        """
        Returns the containing Memory Block
        @return the containing Memory Block
        """
        ...

    def getMinAddress(self) -> ghidra.program.model.address.Address:
        """
        Returns the start address where this byte source is mapped.
        @return the start address where this byte source is mapped.
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
    def byteMappingScheme(self) -> java.util.Optional: ...

    @property
    def description(self) -> unicode: ...

    @property
    def fileBytes(self) -> java.util.Optional: ...

    @property
    def fileBytesOffset(self) -> long: ...

    @property
    def length(self) -> long: ...

    @property
    def mappedRange(self) -> java.util.Optional: ...

    @property
    def maxAddress(self) -> ghidra.program.model.address.Address: ...

    @property
    def memoryBlock(self) -> ghidra.program.model.mem.MemoryBlock: ...

    @property
    def minAddress(self) -> ghidra.program.model.address.Address: ...
