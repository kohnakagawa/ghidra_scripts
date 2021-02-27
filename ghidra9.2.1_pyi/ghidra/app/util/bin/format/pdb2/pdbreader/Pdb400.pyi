import ghidra.app.util.bin.format.pdb2.pdbreader
import ghidra.app.util.bin.format.pdb2.pdbreader.type
import ghidra.app.util.datatype.microsoft
import ghidra.util.task
import java.io
import java.lang


class Pdb400(ghidra.app.util.bin.format.pdb2.pdbreader.AbstractPdb):








    def close(self) -> None: ...

    def deserialize(self, __a0: ghidra.util.task.TaskMonitor) -> None: ...

    def dumpDirectory(self, __a0: java.io.Writer) -> None: ...

    def dumpSubStreams(self, __a0: java.io.Writer) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getAge(self) -> int: ...

    def getClass(self) -> java.lang.Class: ...

    def getDebugInfo(self) -> ghidra.app.util.bin.format.pdb2.pdbreader.PdbDebugInfo: ...

    def getGuid(self) -> ghidra.app.util.datatype.microsoft.GUID: ...

    def getIdentifiers(self) -> ghidra.app.util.bin.format.pdb2.pdbreader.PdbIdentifiers: ...

    def getItemProgramInterface(self) -> ghidra.app.util.bin.format.pdb2.pdbreader.AbstractTypeProgramInterface: ...

    def getNameFromNameIndex(self, __a0: int) -> unicode: ...

    def getNameIndexFromName(self, __a0: unicode) -> int: ...

    def getNameStringFromOffset(self, __a0: int) -> unicode: ...

    def getPdbReaderMetrics(self) -> ghidra.app.util.bin.format.pdb2.pdbreader.PdbReaderMetrics: ...

    def getPdbReaderOptions(self) -> ghidra.app.util.bin.format.pdb2.pdbreader.PdbReaderOptions: ...

    def getSignature(self) -> int: ...

    def getSymbolParser(self) -> ghidra.app.util.bin.format.pdb2.pdbreader.SymbolParser: ...

    def getSymbolRecords(self) -> ghidra.app.util.bin.format.pdb2.pdbreader.SymbolRecords: ...

    def getTargetProcessor(self) -> ghidra.app.util.bin.format.pdb2.pdbreader.Processor: ...

    def getTypeParser(self) -> ghidra.app.util.bin.format.pdb2.pdbreader.TypeParser: ...

    def getTypeProgramInterface(self) -> ghidra.app.util.bin.format.pdb2.pdbreader.AbstractTypeProgramInterface: ...

    @overload
    def getTypeRecord(self, __a0: ghidra.app.util.bin.format.pdb2.pdbreader.RecordNumber) -> ghidra.app.util.bin.format.pdb2.pdbreader.type.AbstractMsType: ...

    @overload
    def getTypeRecord(self, __a0: ghidra.app.util.bin.format.pdb2.pdbreader.RecordNumber, __a1: java.lang.Class) -> ghidra.app.util.bin.format.pdb2.pdbreader.type.AbstractMsType: ...

    def getVersionNumber(self) -> int: ...

    def hasMinimalDebugInfo(self) -> bool: ...

    def hashCode(self) -> int: ...

    def isDeserialized(self) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def parseSegment(self, __a0: ghidra.app.util.bin.format.pdb2.pdbreader.PdbByteReader) -> int: ...

    def setTargetProcessor(self, __a0: ghidra.app.util.bin.format.pdb2.pdbreader.Processor) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
