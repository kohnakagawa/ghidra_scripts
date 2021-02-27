import ghidra.util.task
import java.lang


class TrackedTaskListener(object):








    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def taskAdded(self, task: ghidra.util.task.Task) -> None:
        """
        A callback for when a Task is starting to be tracked.
        @param task The task being tracked.
        """
        ...

    def taskRemoved(self, task: ghidra.util.task.Task) -> None:
        """
        A callback when a task is no longer being tracked.
        @param task The task that is no longer tracked.
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
