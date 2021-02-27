import ghidra.program.model.listing
import java.lang


class DWARFFunctionImporter(object):
    """
    Iterates through all DIEAs in a DWARFProgram and creates Ghidra functions
     and variables.
    """





    def __init__(self, prog: ghidra.app.util.bin.format.dwarf4.next.DWARFProgram, dwarfDTM: ghidra.app.util.bin.format.dwarf4.next.DWARFDataTypeManager, importOptions: ghidra.app.util.bin.format.dwarf4.next.DWARFImportOptions, importSummary: ghidra.app.util.bin.format.dwarf4.next.DWARFImportSummary, monitor: ghidra.util.task.TaskMonitor): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def hasDWARFProgModule(prog: ghidra.program.model.listing.Program, progModuleName: unicode) -> bool: ...

    def hashCode(self) -> int: ...

    def importFunctions(self) -> None: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
