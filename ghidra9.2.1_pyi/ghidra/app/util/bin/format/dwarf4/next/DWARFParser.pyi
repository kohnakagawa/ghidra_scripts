import ghidra.app.util.bin.format.dwarf4.next
import java.lang


class DWARFParser(object):
    """
    Performs a DWARF datatype import and a DWARF function import, under the control of the
     DWARFImportOptions.
    """





    def __init__(self, prog: ghidra.app.util.bin.format.dwarf4.next.DWARFProgram, builtInDTM: ghidra.program.model.data.DataTypeManager, monitor: ghidra.util.task.TaskMonitor): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getImportOptions(self) -> ghidra.app.util.bin.format.dwarf4.next.DWARFImportOptions: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def parse(self) -> ghidra.app.util.bin.format.dwarf4.next.DWARFImportSummary:
        """
        Imports DWARF information according to the {@link DWARFImportOptions} set.
         <p>
         {@link DWARFProgram#checkPreconditions(TaskMonitor)} must be called before this.
         <p>
        @return
        @throws IOException
        @throws DWARFException
        @throws CancelledException
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def importOptions(self) -> ghidra.app.util.bin.format.dwarf4.next.DWARFImportOptions: ...
