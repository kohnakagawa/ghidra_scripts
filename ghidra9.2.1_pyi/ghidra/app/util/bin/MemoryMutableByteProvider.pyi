from typing import List
import ghidra.app.util.bin
import ghidra.formats.gfilesystem
import ghidra.program.model.address
import java.io
import java.lang


class MemoryMutableByteProvider(ghidra.app.util.bin.MemoryByteProvider, ghidra.app.util.bin.MutableByteProvider):
    """
    A Byte Provider implementation based on Memory.
    """





    @overload
    def __init__(self, memory: ghidra.program.model.mem.Memory, baseAddress: ghidra.program.model.address.Address):
        """
        Constructs a new provider relative to the base address.
        @param memory the memory
        @param baseAddress the relative base address
        """
        ...

    @overload
    def __init__(self, memory: ghidra.program.model.mem.Memory, space: ghidra.program.model.address.AddressSpace):
        """
        Constructs a new provider for a specific address space.
        @param memory the memory
        """
        ...



    def close(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getAbsolutePath(self) -> unicode: ...

    def getAddress(self, index: long) -> ghidra.program.model.address.Address:
        """
        Converts an index into this ByteProvider into an {@link Address}.
         <p>
        @param index absolute index in this ByteProvider to convert into an Address
        @return {@link Address}
        @throws AddressOutOfBoundsException if wrapping is not supported by the
         corresponding address space and the addition causes an out-of-bounds
         error
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getFSRL(self) -> ghidra.formats.gfilesystem.FSRL: ...

    def getFile(self) -> java.io.File: ...

    def getInputStream(self, index: long) -> java.io.InputStream: ...

    def getName(self) -> unicode: ...

    def hashCode(self) -> int: ...

    def isValidIndex(self, index: long) -> bool: ...

    def length(self) -> long: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def readByte(self, index: long) -> int: ...

    def readBytes(self, index: long, length: long) -> List[int]: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    def writeByte(self, index: long, value: int) -> None: ...

    def writeBytes(self, index: long, values: List[int]) -> None: ...
