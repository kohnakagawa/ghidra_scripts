import ghidra.app.util.bin.format.pe
import ghidra.app.util.importer
import ghidra.program.model.listing
import ghidra.util.task
import java.lang


class PeMarkupable(object):
    """
    Common interface for standardizing the markup of a PE structure.
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def markup(self, program: ghidra.program.model.listing.Program, isBinary: bool, monitor: ghidra.util.task.TaskMonitor, log: ghidra.app.util.importer.MessageLog, ntHeader: ghidra.app.util.bin.format.pe.NTHeader) -> None:
        """
        Marks up a PE structure.
        @param program The program to markup.
        @param isBinary True if the program is binary; otherwise, false.
        @param monitor The monitor.
        @param log The log.
        @param ntHeader The PE's NT Header structure.
        @throws DuplicateNameException
        @throws CodeUnitInsertionException
        @throws IOException
        @throws MemoryAccessException
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
