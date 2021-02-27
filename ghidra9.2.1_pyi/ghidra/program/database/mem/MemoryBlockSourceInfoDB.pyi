import ghidra.program.model.address
import ghidra.program.model.mem
import java.lang
import java.util


class MemoryBlockSourceInfoDB(object, ghidra.program.model.mem.MemoryBlockSourceInfo):
    """
    Class for describing the source of bytes for a memory block.
    """









    def contains(self, address: ghidra.program.model.address.Address) -> bool: ...

    def equals(self, __a0: object) -> bool: ...

    def getByteMappingScheme(self) -> java.util.Optional: ...

    def getClass(self) -> java.lang.Class: ...

    def getDescription(self) -> unicode: ...

    def getFileBytes(self) -> java.util.Optional: ...

    @overload
    def getFileBytesOffset(self) -> long: ...

    @overload
    def getFileBytesOffset(self, address: ghidra.program.model.address.Address) -> long: ...

    def getLength(self) -> long: ...

    def getMappedRange(self) -> java.util.Optional: ...

    def getMaxAddress(self) -> ghidra.program.model.address.Address: ...

    def getMemoryBlock(self) -> ghidra.program.model.mem.MemoryBlock: ...

    def getMinAddress(self) -> ghidra.program.model.address.Address: ...

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
