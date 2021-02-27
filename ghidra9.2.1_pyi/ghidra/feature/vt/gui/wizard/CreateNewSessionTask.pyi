import ghidra.util.task
import java.lang


class CreateNewSessionTask(ghidra.util.task.Task):




    def __init__(self, __a0: ghidra.feature.vt.gui.plugin.VTController, __a1: docking.wizard.WizardState): ...



    def addTaskListener(self, __a0: ghidra.util.task.TaskListener) -> None: ...

    def canCancel(self) -> bool: ...

    def cancel(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getStatusTextAlignment(self) -> int: ...

    def getTaskTitle(self) -> unicode: ...

    def hasProgress(self) -> bool: ...

    def hashCode(self) -> int: ...

    def isModal(self) -> bool: ...

    def monitoredRun(self, __a0: ghidra.util.task.TaskMonitor) -> None: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def run(self, __a0: ghidra.util.task.TaskMonitor) -> None: ...

    def setHasProgress(self, __a0: bool) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
