from typing import List
import generic.continues
import ghidra.app.util.bin
import ghidra.app.util.bin.format.macho
import ghidra.app.util.bin.format.ubi
import java.lang


class FatHeader(object):
    """
    Represents a fat_header structure.
    """

    FAT_CIGAM: int = -1095041334
    FAT_MAGIC: int = -889275714



    def __init__(self):
        """
        DO NOT USE THIS CONSTRUCTOR, USE create*(GenericFactory ...) FACTORY METHODS INSTEAD.
        """
        ...



    @staticmethod
    def createFatHeader(factory: generic.continues.GenericFactory, provider: ghidra.app.util.bin.ByteProvider) -> ghidra.app.util.bin.format.ubi.FatHeader: ...

    def equals(self, __a0: object) -> bool: ...

    def getArchitectures(self) -> List[ghidra.app.util.bin.format.ubi.FatArch]: ...

    def getClass(self) -> java.lang.Class: ...

    def getFatArchitectureCount(self) -> int: ...

    def getMachHeaders(self) -> List[ghidra.app.util.bin.format.macho.MachHeader]: ...

    def getMagic(self) -> int: ...

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
    def architectures(self) -> List[object]: ...

    @property
    def fatArchitectureCount(self) -> int: ...

    @property
    def machHeaders(self) -> List[object]: ...

    @property
    def magic(self) -> int: ...
