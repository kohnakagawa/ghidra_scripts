import ghidra.app.util.bin.format.pef
import ghidra.app.util.importer
import ghidra.program.model.data
import ghidra.program.model.listing
import ghidra.util.task
import java.lang


class RelocLgSetOrBySection(ghidra.app.util.bin.format.pef.Relocation):
    """
    See Apple's -- PEFBinaryFormat.h
    """









    def apply(self, importState: ghidra.app.util.bin.format.pef.ImportStateCache, relocState: ghidra.app.util.bin.format.pef.RelocationState, header: ghidra.app.util.bin.format.pef.ContainerHeader, program: ghidra.program.model.listing.Program, log: ghidra.app.util.importer.MessageLog, monitor: ghidra.util.task.TaskMonitor) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getIndex(self) -> int: ...

    def getOpcode(self) -> int: ...

    def getSizeInBytes(self) -> int: ...

    def getSubopcode(self) -> int: ...

    def hashCode(self) -> int: ...

    def isMatch(self) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toDataType(self) -> ghidra.program.model.data.DataType: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def index(self) -> int: ...

    @property
    def match(self) -> bool: ...

    @property
    def sizeInBytes(self) -> int: ...

    @property
    def subopcode(self) -> int: ...
