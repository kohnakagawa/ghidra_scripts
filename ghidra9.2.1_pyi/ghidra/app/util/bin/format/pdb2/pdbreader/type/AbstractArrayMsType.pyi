import ghidra.app.util.bin.format.pdb2.pdbreader
import ghidra.app.util.bin.format.pdb2.pdbreader.type
import java.lang


class AbstractArrayMsType(ghidra.app.util.bin.format.pdb2.pdbreader.type.AbstractMsType):




    def __init__(self, __a0: ghidra.app.util.bin.format.pdb2.pdbreader.AbstractPdb, __a1: ghidra.app.util.bin.format.pdb2.pdbreader.PdbByteReader, __a2: int, __a3: ghidra.app.util.bin.format.pdb2.pdbreader.StringParseType, __a4: bool): ...



    @overload
    def emit(self, __a0: java.lang.StringBuilder) -> None: ...

    @overload
    def emit(self, __a0: java.lang.StringBuilder, __a1: ghidra.app.util.bin.format.pdb2.pdbreader.type.AbstractMsType.Bind) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getElementType(self) -> ghidra.app.util.bin.format.pdb2.pdbreader.type.AbstractMsType: ...

    def getElementTypeRecordNumber(self) -> ghidra.app.util.bin.format.pdb2.pdbreader.RecordNumber: ...

    def getIndexType(self) -> ghidra.app.util.bin.format.pdb2.pdbreader.type.AbstractMsType: ...

    def getLength(self) -> long: ...

    def getName(self) -> unicode: ...

    def getPdbId(self) -> int: ...

    def getRecordNumber(self) -> ghidra.app.util.bin.format.pdb2.pdbreader.RecordNumber: ...

    def getSize(self) -> long: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setRecordNumber(self, __a0: ghidra.app.util.bin.format.pdb2.pdbreader.RecordNumber) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def elementType(self) -> ghidra.app.util.bin.format.pdb2.pdbreader.type.AbstractMsType: ...

    @property
    def elementTypeRecordNumber(self) -> ghidra.app.util.bin.format.pdb2.pdbreader.RecordNumber: ...

    @property
    def indexType(self) -> ghidra.app.util.bin.format.pdb2.pdbreader.type.AbstractMsType: ...

    @property
    def name(self) -> unicode: ...

    @property
    def size(self) -> long: ...
