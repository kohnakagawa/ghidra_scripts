import ghidra.app.plugin.core.searchtext
import ghidra.program.util
import ghidra.util.task
import java.lang


class Searcher(object):








    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getSearchOptions(self) -> ghidra.app.plugin.core.searchtext.SearchOptions: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def search(self) -> ghidra.program.util.ProgramLocation: ...

    def setMonitor(self, __a0: ghidra.util.task.TaskMonitor) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def monitor(self) -> None: ...  # No getter available.

    @monitor.setter
    def monitor(self, value: ghidra.util.task.TaskMonitor) -> None: ...

    @property
    def searchOptions(self) -> ghidra.app.plugin.core.searchtext.SearchOptions: ...
