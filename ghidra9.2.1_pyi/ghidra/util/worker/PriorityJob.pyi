import ghidra.util.task
import ghidra.util.worker
import java.lang


class PriorityJob(ghidra.util.worker.Job):








    def cancel(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getError(self) -> java.lang.Throwable: ...

    def getPriority(self) -> long: ...

    def hasError(self) -> bool: ...

    def hashCode(self) -> int: ...

    def isCancelled(self) -> bool: ...

    def isCompleted(self) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def run(self, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        The method that gets called by the Worker when this job is selected to be run
         by the Worker.
        """
        ...

    def setCompleted(self) -> None: ...

    def setError(self, t: java.lang.Throwable) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def priority(self) -> long: ...