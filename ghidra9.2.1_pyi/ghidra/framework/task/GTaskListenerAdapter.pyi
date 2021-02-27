import ghidra.framework.task
import java.lang


class GTaskListenerAdapter(object, ghidra.framework.task.GTaskListener):
    """
    A Dummy implementation to that listeners can subclass this and not have to fill in methods they
     don't need.
    """





    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def initialize(self) -> None: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def suspendedStateChanged(self, suspended: bool) -> None: ...

    def taskCompleted(self, task: ghidra.framework.task.GScheduledTask, result: ghidra.framework.task.GTaskResult) -> None: ...

    def taskGroupCompleted(self, taskGroup: ghidra.framework.task.GTaskGroup) -> None: ...

    def taskGroupScheduled(self, group: ghidra.framework.task.GTaskGroup) -> None: ...

    def taskGroupStarted(self, taskGroup: ghidra.framework.task.GTaskGroup) -> None: ...

    def taskScheduled(self, scheduledTask: ghidra.framework.task.GScheduledTask) -> None: ...

    def taskStarted(self, task: ghidra.framework.task.GScheduledTask) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
