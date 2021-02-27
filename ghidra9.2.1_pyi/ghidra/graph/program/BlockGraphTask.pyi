import ghidra.util.task
import java.lang


class BlockGraphTask(ghidra.util.task.Task):




    def __init__(self, __a0: unicode, __a1: bool, __a2: bool, __a3: bool, __a4: bool, __a5: ghidra.framework.plugintool.PluginTool, __a6: ghidra.program.util.ProgramSelection, __a7: ghidra.program.util.ProgramLocation, __a8: ghidra.program.model.block.CodeBlockModel, __a9: ghidra.service.graph.GraphDisplayProvider): ...



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

    def setCodeLimitPerBlock(self, __a0: int) -> None: ...

    def setHasProgress(self, __a0: bool) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def codeLimitPerBlock(self) -> None: ...  # No getter available.

    @codeLimitPerBlock.setter
    def codeLimitPerBlock(self, value: int) -> None: ...