import ghidra.app.util.bin.format.pdb2.pdbreader
import ghidra.app.util.bin.format.pdb2.pdbreader.symbol
import java.lang


class DataSymbolInternals(ghidra.app.util.bin.format.pdb2.pdbreader.symbol.AbstractSymbolInternals):




    def __init__(self, __a0: ghidra.app.util.bin.format.pdb2.pdbreader.AbstractPdb, __a1: bool): ...



    def emit(self, __a0: java.lang.StringBuilder) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getName(self) -> unicode: ...

    def getOffset(self) -> long: ...

    def getSegment(self) -> int: ...

    def getTypeRecordNumber(self) -> ghidra.app.util.bin.format.pdb2.pdbreader.RecordNumber: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def parse16(__a0: ghidra.app.util.bin.format.pdb2.pdbreader.AbstractPdb, __a1: ghidra.app.util.bin.format.pdb2.pdbreader.PdbByteReader, __a2: bool) -> ghidra.app.util.bin.format.pdb2.pdbreader.symbol.DataSymbolInternals: ...

    @staticmethod
    def parse32(__a0: ghidra.app.util.bin.format.pdb2.pdbreader.AbstractPdb, __a1: ghidra.app.util.bin.format.pdb2.pdbreader.PdbByteReader, __a2: bool) -> ghidra.app.util.bin.format.pdb2.pdbreader.symbol.DataSymbolInternals: ...

    @staticmethod
    def parse3216(__a0: ghidra.app.util.bin.format.pdb2.pdbreader.AbstractPdb, __a1: ghidra.app.util.bin.format.pdb2.pdbreader.PdbByteReader, __a2: bool) -> ghidra.app.util.bin.format.pdb2.pdbreader.symbol.DataSymbolInternals: ...

    @staticmethod
    def parse32St(__a0: ghidra.app.util.bin.format.pdb2.pdbreader.AbstractPdb, __a1: ghidra.app.util.bin.format.pdb2.pdbreader.PdbByteReader, __a2: bool) -> ghidra.app.util.bin.format.pdb2.pdbreader.symbol.DataSymbolInternals: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def name(self) -> unicode: ...

    @property
    def offset(self) -> long: ...

    @property
    def segment(self) -> int: ...

    @property
    def typeRecordNumber(self) -> ghidra.app.util.bin.format.pdb2.pdbreader.RecordNumber: ...