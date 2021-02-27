import ghidra.app.util.bin.format.pdb2.pdbreader
import ghidra.app.util.bin.format.pdb2.pdbreader.symbol
import java.lang


class GlobalDataHLSL32ExtMsSymbol(ghidra.app.util.bin.format.pdb2.pdbreader.symbol.AbstractGlobalDataHLSLMsSymbol):
    PDB_ID: int = 4452



    def __init__(self, __a0: ghidra.app.util.bin.format.pdb2.pdbreader.AbstractPdb, __a1: ghidra.app.util.bin.format.pdb2.pdbreader.PdbByteReader): ...



    def emit(self, __a0: java.lang.StringBuilder) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getBindSlot(self) -> long: ...

    def getBindSpace(self) -> long: ...

    def getClass(self) -> java.lang.Class: ...

    def getDataOffset(self) -> long: ...

    def getName(self) -> unicode: ...

    def getPdbId(self) -> int: ...

    def getRegisterIndex(self) -> long: ...

    def getRegisterType(self) -> ghidra.app.util.bin.format.pdb2.pdbreader.symbol.HLSLRegisterType: ...

    def getTypeRecordNumber(self) -> ghidra.app.util.bin.format.pdb2.pdbreader.RecordNumber: ...

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
    def bindSlot(self) -> long: ...

    @property
    def bindSpace(self) -> long: ...

    @property
    def pdbId(self) -> int: ...

    @property
    def registerIndex(self) -> long: ...
