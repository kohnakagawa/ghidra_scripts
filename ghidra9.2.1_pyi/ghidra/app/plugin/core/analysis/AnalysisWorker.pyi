import ghidra.program.model.listing
import ghidra.util.task
import java.lang


class AnalysisWorker(object):








    def analysisWorkerCallback(self, __a0: ghidra.program.model.listing.Program, __a1: object, __a2: ghidra.util.task.TaskMonitor) -> bool: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getWorkerName(self) -> unicode: ...

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

    @property
    def workerName(self) -> unicode: ...
