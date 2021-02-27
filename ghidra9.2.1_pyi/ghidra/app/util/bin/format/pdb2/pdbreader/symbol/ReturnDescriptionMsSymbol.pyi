from typing import List
import ghidra.app.util.bin.format.pdb2.pdbreader.symbol
import java.lang


class ReturnDescriptionMsSymbol(ghidra.app.util.bin.format.pdb2.pdbreader.symbol.AbstractMsSymbol):
    PDB_ID: int = 13




    class Style(java.lang.Enum):
        INDIRECT_CALLER_ALLOCATED_FAR: ghidra.app.util.bin.format.pdb2.pdbreader.symbol.ReturnDescriptionMsSymbol.Style = indirect caller-allocated far
        INDIRECT_CALLER_ALLOCATED_NEAR: ghidra.app.util.bin.format.pdb2.pdbreader.symbol.ReturnDescriptionMsSymbol.Style = indirected caller-allocated near
        INDIRECT_RETURNEE_ALLOCATED_FAR: ghidra.app.util.bin.format.pdb2.pdbreader.symbol.ReturnDescriptionMsSymbol.Style = indirect returnee allocated far
        INDIRECT_RETURNEE_ALLOCATED_NEAR: ghidra.app.util.bin.format.pdb2.pdbreader.symbol.ReturnDescriptionMsSymbol.Style = indirect returnee allocated near
        RETURN_DATA_IN_REGISTERS: ghidra.app.util.bin.format.pdb2.pdbreader.symbol.ReturnDescriptionMsSymbol.Style = return data in registers
        UNKNOWN: ghidra.app.util.bin.format.pdb2.pdbreader.symbol.ReturnDescriptionMsSymbol.Style = unknown return
        UNUSED: ghidra.app.util.bin.format.pdb2.pdbreader.symbol.ReturnDescriptionMsSymbol.Style = unused
        VOID: ghidra.app.util.bin.format.pdb2.pdbreader.symbol.ReturnDescriptionMsSymbol.Style = void return
        label: unicode
        value: int







        @overload
        def compareTo(self, __a0: java.lang.Enum) -> int: ...

        @overload
        def compareTo(self, __a0: object) -> int: ...

        def equals(self, __a0: object) -> bool: ...

        @staticmethod
        def fromValue(__a0: int) -> ghidra.app.util.bin.format.pdb2.pdbreader.symbol.ReturnDescriptionMsSymbol.Style: ...

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
        def valueOf(__a0: unicode) -> ghidra.app.util.bin.format.pdb2.pdbreader.symbol.ReturnDescriptionMsSymbol.Style: ...

        @overload
        @staticmethod
        def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

        @staticmethod
        def values() -> List[ghidra.app.util.bin.format.pdb2.pdbreader.symbol.ReturnDescriptionMsSymbol.Style]: ...

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

    def getStyle(self) -> ghidra.app.util.bin.format.pdb2.pdbreader.symbol.ReturnDescriptionMsSymbol.Style: ...

    def hashCode(self) -> int: ...

    def isReturneeCleansUpStack(self) -> bool: ...

    def isVarargsPushedRightToLeft(self) -> bool: ...

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
    def returneeCleansUpStack(self) -> bool: ...

    @property
    def style(self) -> ghidra.app.util.bin.format.pdb2.pdbreader.symbol.ReturnDescriptionMsSymbol.Style: ...

    @property
    def varargsPushedRightToLeft(self) -> bool: ...
