from typing import List
import ghidra.app.util.bin.format.pdb2.pdbreader
import ghidra.app.util.bin.format.pdb2.pdbreader.symbol
import ghidra.util.task
import java.lang
import java.util


class PdbNewDebugInfo(ghidra.app.util.bin.format.pdb2.pdbreader.PdbDebugInfo):




    def __init__(self, __a0: ghidra.app.util.bin.format.pdb2.pdbreader.AbstractPdb, __a1: int): ...



    def deserialize(self, __a0: bool, __a1: ghidra.util.task.TaskMonitor) -> long: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDebugData(self) -> ghidra.app.util.bin.format.pdb2.pdbreader.DebugData: ...

    def getGlobalSymbolInformation(self) -> ghidra.app.util.bin.format.pdb2.pdbreader.GlobalSymbolInformation: ...

    def getMachineType(self) -> ghidra.app.util.bin.format.pdb2.pdbreader.ImageFileMachine: ...

    def getModuleInformation(self, __a0: int) -> ghidra.app.util.bin.format.pdb2.pdbreader.AbstractModuleInformation: ...

    def getModuleInformationList(self) -> List[object]: ...

    def getModuleSymbolsByOffset(self, __a0: int) -> java.util.Map: ...

    def getNumModules(self) -> int: ...

    def getPublicSymbolInformation(self) -> ghidra.app.util.bin.format.pdb2.pdbreader.PublicSymbolInformation: ...

    def getSectionContributionList(self) -> List[object]: ...

    def getSegmentMapList(self) -> List[object]: ...

    def getSymbolForModuleAndOffsetOfRecord(self, __a0: int, __a1: long) -> ghidra.app.util.bin.format.pdb2.pdbreader.symbol.AbstractMsSymbol: ...

    def getSymbolForOffsetOfRecord(self, __a0: long) -> ghidra.app.util.bin.format.pdb2.pdbreader.symbol.AbstractMsSymbol: ...

    def getSymbolRecords(self) -> ghidra.app.util.bin.format.pdb2.pdbreader.SymbolRecords: ...

    def getSymbolsByOffset(self) -> java.util.Map: ...

    @staticmethod
    def getVersionNumberSize() -> int: ...

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
    def debugData(self) -> ghidra.app.util.bin.format.pdb2.pdbreader.DebugData: ...

    @property
    def machineType(self) -> ghidra.app.util.bin.format.pdb2.pdbreader.ImageFileMachine: ...