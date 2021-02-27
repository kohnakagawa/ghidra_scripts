import ghidra.program.model.address
import ghidra.program.model.mem
import java.lang


class AddressSourceInfo(object):
    """
    Provides information about the source of a byte value at an address including the file it
     came from, the offset into that file, and the original value of that byte.
    """





    def __init__(self, memory: ghidra.program.model.mem.Memory, address: ghidra.program.model.address.Address, block: ghidra.program.model.mem.MemoryBlock): ...



    def equals(self, __a0: object) -> bool: ...

    def getAddress(self) -> ghidra.program.model.address.Address:
        """
        Returns the address for which this object provides byte source information.
        @return the address for which this object provides byte source information.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getFileName(self) -> unicode:
        """
        Returns the filename of the originally imported file that provided the byte value for the
         associated address or null if there is no source information for this location.
        @return the filename of the originally imported file that provided the byte value for the
         associated address or null if there is no source information for this location.
        """
        ...

    def getFileOffset(self) -> long:
        """
        Returns the offset into the originally imported file that provided the byte value for the
         associated address or -1 if there is no source information for this location.
        @return the offset into the originally imported file that provided the byte value for the
         associated address.
        """
        ...

    def getMemoryBlockSourceInfo(self) -> ghidra.program.model.mem.MemoryBlockSourceInfo:
        """
        Returns the {@link MemoryBlockSourceInfo} for the region surround this info's location.
        @return the {@link MemoryBlockSourceInfo} for the region surround this info's location.
        """
        ...

    def getOriginalValue(self) -> int:
        """
        Returns the original byte value from the imported file that provided the byte value for the
         associated address or 0 if there is no source information for this location.
        @return the original byte value from the imported file that provided the byte value for the
         associated address or 0 if there is no source information for this location.
        @throws IOException if an io error occurs reading the program database.
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
    def address(self) -> ghidra.program.model.address.Address: ...

    @property
    def fileName(self) -> unicode: ...

    @property
    def fileOffset(self) -> long: ...

    @property
    def memoryBlockSourceInfo(self) -> ghidra.program.model.mem.MemoryBlockSourceInfo: ...

    @property
    def originalValue(self) -> int: ...
