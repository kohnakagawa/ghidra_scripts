import ghidra.app.util.bin.format.dwarf4.next
import ghidra.util.task
import java.lang


class DIEAMonitoredIterator(object):
    """
    Handles the details of iterating all the DIEAggregate of a DWARF program.

     DWARF programs are made of multiple compilation units (CUs), and each CU has
     DebugInfoEntrys that are grouped together into aggregates (DIEAs).

     In normal operation, to iterate the DIEAs, each CU's DIEs are loaded into memory,
     iterated, and then thrown away before going to the next CU.

     There are typically no DIE references between CUs, but if there are,
     DWARFImportOptions#isPreloadAllDIEs() needs to be turned on by the user before
     analysis begins.
    """





    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    @staticmethod
    def iterable(prog: ghidra.app.util.bin.format.dwarf4.next.DWARFProgram, monitorMessage: unicode, monitor: ghidra.util.task.TaskMonitor) -> java.lang.Iterable:
        """
        Create an iterable to allow for-each usage of this iterator.
        @param prog {@link DWARFProgram} that holds the DIEs.
        @param monitorMessage String to display in the TaskMonitor.
        @param monitor {@link TaskMonitor}
        @return Iterable that can be used in a for-each loop.
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
