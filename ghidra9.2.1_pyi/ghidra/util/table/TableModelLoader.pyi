import ghidra.util.datastruct
import ghidra.util.task
import java.lang


class TableModelLoader(object):
    """
    Allows clients to create a table model that will call them back via this interface so
     that they may perform their own loading.
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def load(self, accumulator: ghidra.util.datastruct.Accumulator, monitor: ghidra.util.task.TaskMonitor) -> None: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
