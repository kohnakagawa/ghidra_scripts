import ghidra.framework.task
import java.lang


class MulticastTaskListener(object, ghidra.framework.task.GTaskListener):
    """
    Used by the GTaskManager to efficiently manage multiple GTaskListeners.

     When an GTaskManager has multiple listeners, instead of having a list of listeners, listeners
     are chained together using MulticastTaskListeners. It avoids the creation of
     an iterator every time a listener method needs to be called.

     For example, the GTaskManager has a single TaskListener variable that it notifies when its state
     changes.  If someone adds a listener, and the current listener is null, then it becomes the
     listener.  If it already has a listener, it will create a new MulticaseTaskListener taking in the
     old listener and the new listener.  When a TaskListener method is called, it simply calls the same
     method on those two listeners.
    """









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
