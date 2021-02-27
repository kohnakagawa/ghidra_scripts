from typing import List
import ghidra.app.util.bin.format.pdb2.pdbreader.symbol
import java.lang


class AbstractRegisterDimensionalityDARMsSymbol(ghidra.app.util.bin.format.pdb2.pdbreader.symbol.AbstractDefinedSingleAddressRangeMsSymbol):





    class MemorySpace(java.lang.Enum):
        DATA: ghidra.app.util.bin.format.pdb2.pdbreader.symbol.AbstractRegisterDimensionalityDARMsSymbol.MemorySpace = DATA
        INVALID: ghidra.app.util.bin.format.pdb2.pdbreader.symbol.AbstractRegisterDimensionalityDARMsSymbol.MemorySpace = INVALID MEMORY SPACE
        READWRITERESOURCE: ghidra.app.util.bin.format.pdb2.pdbreader.symbol.AbstractRegisterDimensionalityDARMsSymbol.MemorySpace = RWRESOURCE
        RESOURCE: ghidra.app.util.bin.format.pdb2.pdbreader.symbol.AbstractRegisterDimensionalityDARMsSymbol.MemorySpace = RESOURCE
        SAMPLER: ghidra.app.util.bin.format.pdb2.pdbreader.symbol.AbstractRegisterDimensionalityDARMsSymbol.MemorySpace = SAMPLER
        label: unicode
        value: int







        @overload
        def compareTo(self, __a0: java.lang.Enum) -> int: ...

        @overload
        def compareTo(self, __a0: object) -> int: ...

        def equals(self, __a0: object) -> bool: ...

        @staticmethod
        def fromValue(__a0: int) -> ghidra.app.util.bin.format.pdb2.pdbreader.symbol.AbstractRegisterDimensionalityDARMsSymbol.MemorySpace: ...

        def getClass(self) -> java.lang.Class: ...

        def getDeclaringClass(self) -> java.lang.Class: ...

        def hashCode(self) -> int: ...

        def name(self) -> unicode: ...

        def notify(self) -> None: ...

        def notifyAll(self) -> None: ...

        def ordinal(self) -> int: ...

        def toString(self) -> unicode: ...

        @overload
        @staticmethod
        def valueOf(__a0: unicode) -> ghidra.app.util.bin.format.pdb2.pdbreader.symbol.AbstractRegisterDimensionalityDARMsSymbol.MemorySpace: ...

        @overload
        @staticmethod
        def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

        @staticmethod
        def values() -> List[ghidra.app.util.bin.format.pdb2.pdbreader.symbol.AbstractRegisterDimensionalityDARMsSymbol.MemorySpace]: ...

        @overload
        def wait(self) -> None: ...

        @overload
        def wait(self, __a0: long) -> None: ...

        @overload
        def wait(self, __a0: long, __a1: int) -> None: ...



    def __init__(self, __a0: ghidra.app.util.bin.format.pdb2.pdbreader.AbstractPdb, __a1: ghidra.app.util.bin.format.pdb2.pdbreader.PdbByteReader): ...



    def emit(self, __a0: java.lang.StringBuilder) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getAddressGapList(self) -> List[object]: ...

    def getAddressRange(self) -> ghidra.app.util.bin.format.pdb2.pdbreader.symbol.AddressRange: ...

    def getClass(self) -> java.lang.Class: ...

    def getPdbId(self) -> int: ...

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
