import ghidra.app.util.bin.format.pdb2.pdbreader
import ghidra.app.util.bin.format.pdb2.pdbreader.type
import java.lang


class AbstractMemberMsType(ghidra.app.util.bin.format.pdb2.pdbreader.type.AbstractMsType, ghidra.app.util.bin.format.pdb2.pdbreader.type.MsTypeField):




    @overload
    def __init__(self, __a0: ghidra.app.util.bin.format.pdb2.pdbreader.AbstractPdb, __a1: ghidra.app.util.bin.format.pdb2.pdbreader.PdbByteReader): ...

    @overload
    def __init__(self, __a0: ghidra.app.util.bin.format.pdb2.pdbreader.AbstractPdb, __a1: unicode, __a2: long, __a3: ghidra.app.util.bin.format.pdb2.pdbreader.RecordNumber, __a4: ghidra.app.util.bin.format.pdb2.pdbreader.type.ClassFieldMsAttributes): ...



    @overload
    def emit(self, __a0: java.lang.StringBuilder) -> None: ...

    @overload
    def emit(self, __a0: java.lang.StringBuilder, __a1: ghidra.app.util.bin.format.pdb2.pdbreader.type.AbstractMsType.Bind) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getAttribute(self) -> ghidra.app.util.bin.format.pdb2.pdbreader.type.ClassFieldMsAttributes: ...

    def getClass(self) -> java.lang.Class: ...

    def getFieldTypeRecordNumber(self) -> ghidra.app.util.bin.format.pdb2.pdbreader.RecordNumber: ...

    def getLength(self) -> long: ...

    def getName(self) -> unicode: ...

    def getOffset(self) -> long: ...

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
    def attribute(self) -> ghidra.app.util.bin.format.pdb2.pdbreader.type.ClassFieldMsAttributes: ...

    @property
    def fieldTypeRecordNumber(self) -> ghidra.app.util.bin.format.pdb2.pdbreader.RecordNumber: ...

    @property
    def name(self) -> unicode: ...

    @property
    def offset(self) -> long: ...