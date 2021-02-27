import ghidra.util.task
import java.lang


class VtTask(ghidra.util.task.Task):








    def addTaskListener(self, __a0: ghidra.util.task.TaskListener) -> None: ...

    def canCancel(self) -> bool: ...

    def cancel(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getErrorDetails(self) -> unicode: ...

    def getStatusTextAlignment(self) -> int: ...

    def getTaskTitle(self) -> unicode: ...

    def hasErrors(self) -> bool: ...

    def hasProgress(self) -> bool: ...

    def hashCode(self) -> int: ...

    def isModal(self) -> bool: ...

    def logErrors(self) -> None: ...

    def monitoredRun(self, __a0: ghidra.util.task.TaskMonitor) -> None: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def run(self, __a0: ghidra.util.task.TaskMonitor) -> None: ...

    def setHasProgress(self, __a0: bool) -> None: ...

    def showErrors(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    def wasCancelled(self) -> bool: ...

    def wasSuccessfull(self) -> bool: ...

    @property
    def errorDetails(self) -> unicode: ...
