import ghidra.app.util.bin.format
import ghidra.app.util.bin.format.ubi
import java.lang


class FatArch(object):
    """
    Represents a fat_arch structure.
    """





    def __init__(self):
        """
        DO NOT USE THIS CONSTRUCTOR, USE create*(GenericFactory ...) FACTORY METHODS INSTEAD.
        """
        ...



    @staticmethod
    def createFatArch(reader: ghidra.app.util.bin.format.FactoryBundledWithBinaryReader) -> ghidra.app.util.bin.format.ubi.FatArch: ...

    def equals(self, __a0: object) -> bool: ...

    def getAlign(self) -> int:
        """
        Returns the alignment as a power of 2.
        @return the alignment as a power of 2
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getCpuSubType(self) -> int:
        """
        @see CpuSubTypes
        """
        ...

    def getCpuType(self) -> int:
        """
        @see CpuTypes
        """
        ...

    def getOffset(self) -> int:
        """
        Returns the file offset to this object file.
        @return the file offset to this object file
        """
        ...

    def getSize(self) -> int:
        """
        Returns the size of this object file.
        @return the size of this object file
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
    def align(self) -> int: ...

    @property
    def cpuSubType(self) -> int: ...

    @property
    def cpuType(self) -> int: ...

    @property
    def offset(self) -> int: ...

    @property
    def size(self) -> int: ...
