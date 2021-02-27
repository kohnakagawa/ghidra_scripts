from typing import List
import ghidra.app.util.bin.format.pdb2.pdbreader.symbol
import java.lang


class ArmSwitchTableMsSymbol(ghidra.app.util.bin.format.pdb2.pdbreader.symbol.AbstractMsSymbol):
    PDB_ID: int = 4441




    class EntryType(java.lang.Enum):
        INT1: ghidra.app.util.bin.format.pdb2.pdbreader.symbol.ArmSwitchTableMsSymbol.EntryType = signed byte
        INT1SHL1: ghidra.app.util.bin.format.pdb2.pdbreader.symbol.ArmSwitchTableMsSymbol.EntryType = signed byte scaled by two
        INT2: ghidra.app.util.bin.format.pdb2.pdbreader.symbol.ArmSwitchTableMsSymbol.EntryType = signed two byte
        INT2SHL1: ghidra.app.util.bin.format.pdb2.pdbreader.symbol.ArmSwitchTableMsSymbol.EntryType = signed two byte scaled by two
        INT4: ghidra.app.util.bin.format.pdb2.pdbreader.symbol.ArmSwitchTableMsSymbol.EntryType = signed four byte
        POINTER: ghidra.app.util.bin.format.pdb2.pdbreader.symbol.ArmSwitchTableMsSymbol.EntryType = pointer
        UINT1: ghidra.app.util.bin.format.pdb2.pdbreader.symbol.ArmSwitchTableMsSymbol.EntryType = unsigned byte
        UINT1SHL1: ghidra.app.util.bin.format.pdb2.pdbreader.symbol.ArmSwitchTableMsSymbol.EntryType = unsigned byte scaled by two
        UINT2: ghidra.app.util.bin.format.pdb2.pdbreader.symbol.ArmSwitchTableMsSymbol.EntryType = unsigned two byte
        UINT2SHL1: ghidra.app.util.bin.format.pdb2.pdbreader.symbol.ArmSwitchTableMsSymbol.EntryType = unsigned two byte scaled by two
        UINT4: ghidra.app.util.bin.format.pdb2.pdbreader.symbol.ArmSwitchTableMsSymbol.EntryType = unsigned four byte
        UNKNOWN: ghidra.app.util.bin.format.pdb2.pdbreader.symbol.ArmSwitchTableMsSymbol.EntryType = unknown return
        label: unicode
        value: int







        @overload
        def compareTo(self, __a0: java.lang.Enum) -> int: ...

        @overload
        def compareTo(self, __a0: object) -> int: ...

        def equals(self, __a0: object) -> bool: ...

        @staticmethod
        def fromValue(__a0: int) -> ghidra.app.util.bin.format.pdb2.pdbreader.symbol.ArmSwitchTableMsSymbol.EntryType: ...

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
        def valueOf(__a0: unicode) -> ghidra.app.util.bin.format.pdb2.pdbreader.symbol.ArmSwitchTableMsSymbol.EntryType: ...

        @overload
        @staticmethod
        def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

        @staticmethod
        def values() -> List[ghidra.app.util.bin.format.pdb2.pdbreader.symbol.ArmSwitchTableMsSymbol.EntryType]: ...

        @overload
        def wait(self) -> None: ...

        @overload
        def wait(self, __a0: long) -> None: ...

        @overload
        def wait(self, __a0: long, __a1: int) -> None: ...



    def __init__(self, __a0: ghidra.app.util.bin.format.pdb2.pdbreader.AbstractPdb, __a1: ghidra.app.util.bin.format.pdb2.pdbreader.PdbByteReader): ...



    def emit(self, __a0: java.lang.StringBuilder) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getPdbId(self) -> int: ...

    def getSwitchEntryType(self) -> ghidra.app.util.bin.format.pdb2.pdbreader.symbol.ArmSwitchTableMsSymbol.EntryType: ...

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
    def pdbId(self) -> int: ...

    @property
    def switchEntryType(self) -> ghidra.app.util.bin.format.pdb2.pdbreader.symbol.ArmSwitchTableMsSymbol.EntryType: ...
