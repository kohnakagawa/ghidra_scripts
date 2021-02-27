import ghidra.program.model.address
import java.lang


class ByteMappingScheme(object):
    """
    ByteMappingScheme facilitate byte mapping/decimation scheme for a mapped sub-block to
     an underlying source memory region.
    """





    def __init__(self, mappedByteCount: int, mappedSourceByteCount: int):
        """
        Construct byte mapping scheme specified as a ratio of mapped bytes to source bytes.
        @param mappedByteCount number of mapped bytes per mappedSourcebyteCount (1..127).  This
         value must be less-than or equal to schemeSrcByteCount.
        @param mappedSourceByteCount number of source bytes for mapping ratio (1..127)
        @throws IllegalArgumentException if invalid mapping scheme specified
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getMappedByteCount(self) -> int:
        """
        Get the mapped-byte-count (left-hand value in mapping ratio)
        @return mapped-byte-count
        """
        ...

    def getMappedSourceAddress(self, mappedSourceBaseAddress: ghidra.program.model.address.Address, offsetInSubBlock: long) -> ghidra.program.model.address.Address:
        """
        Calculate the mapped source address for a specified offset with the mapped sub-block.
        @param mappedSourceBaseAddress mapped source base address for sub-block
        @param offsetInSubBlock byte offset within sub-block to be mapped into source
        @return mapped source address
        @throws AddressOverflowException if offset in sub-block produces a wrap condition in
         the mapped source address space.
        """
        ...

    def getMappedSourceByteCount(self) -> int:
        """
        Get the mapped-source-byte-count (right-hand value in mapping ratio)
        @return mapped-source-byte-count
        """
        ...

    def hashCode(self) -> int: ...

    def isOneToOneMapping(self) -> bool:
        """
        Determine this scheme corresponds to a 1:1 byte mapping
        @return true if 1:1 mapping else false
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
    def mappedByteCount(self) -> int: ...

    @property
    def mappedSourceByteCount(self) -> int: ...

    @property
    def oneToOneMapping(self) -> bool: ...
