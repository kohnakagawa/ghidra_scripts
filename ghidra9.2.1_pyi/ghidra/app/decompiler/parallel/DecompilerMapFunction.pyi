import ghidra.app.decompiler
import ghidra.program.model.listing
import ghidra.util.task
import java.lang


class DecompilerMapFunction(object):








    def equals(self, __a0: object) -> bool: ...

    def evaluate(self, decompiler: ghidra.app.decompiler.DecompInterface, function: ghidra.program.model.listing.Function, monitor: ghidra.util.task.TaskMonitor) -> float: ...

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
