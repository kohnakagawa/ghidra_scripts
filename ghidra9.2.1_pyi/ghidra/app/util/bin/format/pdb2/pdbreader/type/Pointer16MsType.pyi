import ghidra.app.util.bin.format.pdb2.pdbreader
import ghidra.app.util.bin.format.pdb2.pdbreader.type
import java.lang


class Pointer16MsType(ghidra.app.util.bin.format.pdb2.pdbreader.type.AbstractPointerMsType):
    PDB_ID: int = 2



    def __init__(self, __a0: ghidra.app.util.bin.format.pdb2.pdbreader.AbstractPdb, __a1: ghidra.app.util.bin.format.pdb2.pdbreader.PdbByteReader): ...



    @overload
    def emit(self, __a0: java.lang.StringBuilder) -> None: ...

    @overload
    def emit(self, __a0: java.lang.StringBuilder, __a1: ghidra.app.util.bin.format.pdb2.pdbreader.type.AbstractMsType.Bind) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getLength(self) -> long: ...

    def getMemberPointerType(self) -> ghidra.app.util.bin.format.pdb2.pdbreader.type.AbstractPointerMsType.MemberPointerType: ...

    def getName(self) -> unicode: ...

    def getPdbId(self) -> int: ...

    def getPointerMode(self) -> ghidra.app.util.bin.format.pdb2.pdbreader.type.AbstractPointerMsType.PointerMode: ...

    def getPointerType(self) -> ghidra.app.util.bin.format.pdb2.pdbreader.type.AbstractPointerMsType.PointerType: ...

    def getRecordNumber(self) -> ghidra.app.util.bin.format.pdb2.pdbreader.RecordNumber: ...

    def getSize(self) -> long: ...

    def getUnderlyingRecordNumber(self) -> ghidra.app.util.bin.format.pdb2.pdbreader.RecordNumber: ...

    def getUnderlyingType(self) -> ghidra.app.util.bin.format.pdb2.pdbreader.type.AbstractMsType: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def parseExtendedPointerInfo(self, __a0: ghidra.app.util.bin.format.pdb2.pdbreader.PdbByteReader, __a1: int, __a2: ghidra.app.util.bin.format.pdb2.pdbreader.StringParseType) -> None: ...

    def setRecordNumber(self, __a0: ghidra.app.util.bin.format.pdb2.pdbreader.RecordNumber) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def pdbId(self) -> int: ...
