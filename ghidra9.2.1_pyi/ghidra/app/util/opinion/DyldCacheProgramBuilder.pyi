import ghidra.app.util.bin
import ghidra.app.util.importer
import ghidra.app.util.opinion
import ghidra.program.database.mem
import ghidra.program.model.listing
import ghidra.util.task
import java.lang


class DyldCacheProgramBuilder(ghidra.app.util.opinion.MachoProgramBuilder):
    """
    Builds up a DYLD Cache Program by parsing the DYLD Cache headers.
    """









    @overload
    @staticmethod
    def buildProgram(program: ghidra.program.model.listing.Program, provider: ghidra.app.util.bin.ByteProvider, fileBytes: ghidra.program.database.mem.FileBytes, log: ghidra.app.util.importer.MessageLog, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Builds up a Mach-O {@link Program}.
        @param program The {@link Program} to build up.
        @param provider The {@link ByteProvider} that contains the Mach-O's bytes.
        @param fileBytes Where the Mach-O's bytes came from.
        @param log The log.
        @param monitor A cancelable task monitor.
        @throws Exception if a problem occurs.
        """
        ...

    @overload
    @staticmethod
    def buildProgram(program: ghidra.program.model.listing.Program, provider: ghidra.app.util.bin.ByteProvider, fileBytes: ghidra.program.database.mem.FileBytes, shouldProcessSymbols: bool, shouldCreateDylibSections: bool, addRelocationEntries: bool, log: ghidra.app.util.importer.MessageLog, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Builds up a DYLD Cache {@link Program}.
        @param program The {@link Program} to build up
        @param provider The {@link ByteProvider} that contains the DYLD Cache's bytes
        @param fileBytes Where the Mach-O's bytes came from
        @param shouldProcessSymbols True if symbols should be processed; otherwise, false
        @param shouldCreateDylibSections True if memory blocks should be created for DYLIB sections;
           otherwise, false
        @param addRelocationEntries True to create a relocation entry for each fixed up pointer in pointer chain
        @param log The log
        @param monitor A cancelable task monitor
        @throws Exception if a problem occurs
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

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
