import ghidra.util.datastruct
import ghidra.util.search.memory
import ghidra.util.task
import java.lang


class MemSearcherAlgorithm(object, ghidra.util.search.memory.MemorySearchAlgorithm):
    """
    Search memory using the provided search text.
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def search(self, accumulator: ghidra.util.datastruct.Accumulator, monitor: ghidra.util.task.TaskMonitor) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
