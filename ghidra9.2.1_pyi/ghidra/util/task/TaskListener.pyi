import ghidra.util.task
import java.lang


class TaskListener(object):
    """
    Listener that is notified when a thread completes its task.
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def taskCancelled(self, task: ghidra.util.task.Task) -> None:
        """
        Notification that the task was canceled.
        @param task the task that was running and was canceled
        """
        ...

    def taskCompleted(self, task: ghidra.util.task.Task) -> None:
        """
        Notification that the task completed.
        @param task the task that was running and is now completed
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
