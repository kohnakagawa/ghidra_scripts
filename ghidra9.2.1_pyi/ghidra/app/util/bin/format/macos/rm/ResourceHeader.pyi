import ghidra.app.util.bin
import ghidra.app.util.bin.format.macos.asd
import ghidra.app.util.bin.format.macos.rm
import ghidra.program.model.data
import java.lang


class ResourceHeader(ghidra.app.util.bin.format.macos.asd.Entry, ghidra.app.util.bin.StructConverter):




    @overload
    def __init__(self, provider: ghidra.app.util.bin.ByteProvider): ...

    @overload
    def __init__(self, reader: ghidra.app.util.bin.BinaryReader, entry: ghidra.app.util.bin.format.macos.asd.EntryDescriptor): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getEntryDescriptor(self) -> ghidra.app.util.bin.format.macos.asd.EntryDescriptor: ...

    def getMap(self) -> ghidra.app.util.bin.format.macos.rm.ResourceMap: ...

    def getResourceDataLength(self) -> int:
        """
        Returns the length of the resource data.
        @return the length of the resource data
        """
        ...

    def getResourceDataOffset(self) -> int:
        """
        Returns the offset from the beginning of resource fork
         to resource data.
        @return offset to resource data
        """
        ...

    def getResourceMapLength(self) -> int:
        """
        Returns the length of the resource map.
        @return the length of the resource map
        """
        ...

    def getResourceMapOffset(self) -> int:
        """
        Returns the offset from the beginning of resource fork
         to resource map.
        @return offset to resource map
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toDataType(self) -> ghidra.program.model.data.DataType: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def map(self) -> ghidra.app.util.bin.format.macos.rm.ResourceMap: ...

    @property
    def resourceDataLength(self) -> int: ...

    @property
    def resourceDataOffset(self) -> int: ...

    @property
    def resourceMapLength(self) -> int: ...

    @property
    def resourceMapOffset(self) -> int: ...
