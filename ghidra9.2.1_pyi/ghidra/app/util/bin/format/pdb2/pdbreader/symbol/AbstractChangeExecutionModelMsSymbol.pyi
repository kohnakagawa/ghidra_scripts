from typing import List
import ghidra.app.util.bin.format.pdb2.pdbreader.symbol
import java.lang


class AbstractChangeExecutionModelMsSymbol(ghidra.app.util.bin.format.pdb2.pdbreader.symbol.AbstractMsSymbol):





    class Model(java.lang.Enum):
        COBOL: ghidra.app.util.bin.format.pdb2.pdbreader.symbol.AbstractChangeExecutionModelMsSymbol.Model = COBOL
        CODE: ghidra.app.util.bin.format.pdb2.pdbreader.symbol.AbstractChangeExecutionModelMsSymbol.Model = CODE
        CODEPAD: ghidra.app.util.bin.format.pdb2.pdbreader.symbol.AbstractChangeExecutionModelMsSymbol.Model = CODEPAD
        DATAPAD: ghidra.app.util.bin.format.pdb2.pdbreader.symbol.AbstractChangeExecutionModelMsSymbol.Model = DATAPAD
        JAVAINT: ghidra.app.util.bin.format.pdb2.pdbreader.symbol.AbstractChangeExecutionModelMsSymbol.Model = JAVAINT
        JUMPTABLE: ghidra.app.util.bin.format.pdb2.pdbreader.symbol.AbstractChangeExecutionModelMsSymbol.Model = JUMPTABLE
        NATIVE: ghidra.app.util.bin.format.pdb2.pdbreader.symbol.AbstractChangeExecutionModelMsSymbol.Model = NATIVE
        PCODE: ghidra.app.util.bin.format.pdb2.pdbreader.symbol.AbstractChangeExecutionModelMsSymbol.Model = PCODE
        PCODE32MACINTOSH: ghidra.app.util.bin.format.pdb2.pdbreader.symbol.AbstractChangeExecutionModelMsSymbol.Model = PCODE for the Mac
        PCODE32MACINTOSH_NATIVE_ENTRY_POINT: ghidra.app.util.bin.format.pdb2.pdbreader.symbol.AbstractChangeExecutionModelMsSymbol.Model = PCODE for the Mac (Native Entry Point)
        SQL: ghidra.app.util.bin.format.pdb2.pdbreader.symbol.AbstractChangeExecutionModelMsSymbol.Model = SQL
        TABLE: ghidra.app.util.bin.format.pdb2.pdbreader.symbol.AbstractChangeExecutionModelMsSymbol.Model = DATA
        UNKNOWN: ghidra.app.util.bin.format.pdb2.pdbreader.symbol.AbstractChangeExecutionModelMsSymbol.Model = UNKNOWN MODEL
        label: unicode
        value: int







        @overload
        def compareTo(self, __a0: java.lang.Enum) -> int: ...

        @overload
        def compareTo(self, __a0: object) -> int: ...

        def equals(self, __a0: object) -> bool: ...

        @staticmethod
        def fromValue(__a0: int) -> ghidra.app.util.bin.format.pdb2.pdbreader.symbol.AbstractChangeExecutionModelMsSymbol.Model: ...

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
        def valueOf(__a0: unicode) -> ghidra.app.util.bin.format.pdb2.pdbreader.symbol.AbstractChangeExecutionModelMsSymbol.Model: ...

        @overload
        @staticmethod
        def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

        @staticmethod
        def values() -> List[ghidra.app.util.bin.format.pdb2.pdbreader.symbol.AbstractChangeExecutionModelMsSymbol.Model]: ...

        @overload
        def wait(self) -> None: ...

        @overload
        def wait(self, __a0: long) -> None: ...

        @overload
        def wait(self, __a0: long, __a1: int) -> None: ...



    def __init__(self, __a0: ghidra.app.util.bin.format.pdb2.pdbreader.AbstractPdb, __a1: ghidra.app.util.bin.format.pdb2.pdbreader.PdbByteReader, __a2: int): ...



    def emit(self, __a0: java.lang.StringBuilder) -> None: ...

    def equals(self, __a0: object) -> bool: ...

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
