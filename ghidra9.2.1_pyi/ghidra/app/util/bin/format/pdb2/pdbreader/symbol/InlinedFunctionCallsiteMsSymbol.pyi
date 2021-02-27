from typing import List
import ghidra.app.util.bin.format.pdb2.pdbreader
import ghidra.app.util.bin.format.pdb2.pdbreader.symbol
import java.lang


class InlinedFunctionCallsiteMsSymbol(ghidra.app.util.bin.format.pdb2.pdbreader.symbol.AbstractMsSymbol):
    PDB_ID: int = 4429



    def __init__(self, __a0: ghidra.app.util.bin.format.pdb2.pdbreader.AbstractPdb, __a1: ghidra.app.util.bin.format.pdb2.pdbreader.PdbByteReader): ...



    def emit(self, __a0: java.lang.StringBuilder) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getBinaryAnnotationOpcodeList(self) -> List[object]: ...

    def getClass(self) -> java.lang.Class: ...

    def getInlineeRecordNumber(self) -> ghidra.app.util.bin.format.pdb2.pdbreader.RecordNumber: ...

    def getPdbId(self) -> int: ...

    def getPointerToInliner(self) -> long: ...

    def getPointerToThisBlockEnd(self) -> long: ...

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
    def binaryAnnotationOpcodeList(self) -> List[object]: ...

    @property
    def inlineeRecordNumber(self) -> ghidra.app.util.bin.format.pdb2.pdbreader.RecordNumber: ...

    @property
    def pdbId(self) -> int: ...

    @property
    def pointerToInliner(self) -> long: ...

    @property
    def pointerToThisBlockEnd(self) -> long: ...