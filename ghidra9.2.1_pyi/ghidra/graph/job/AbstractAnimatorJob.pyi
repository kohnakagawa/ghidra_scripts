import ghidra.graph.job
import ghidra.util.task
import java.lang


class AbstractAnimatorJob(object, ghidra.graph.job.GraphJob):
    TOO_BIG_TO_ANIMATE: int = 125



    def __init__(self): ...



    def canShortcut(self) -> bool: ...

    def dispose(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def execute(self, listener: ghidra.graph.job.GraphJobListener) -> None: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def isFinished(self) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setBusyListener(self, listener: ghidra.util.task.BusyListener) -> None: ...

    def shortcut(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def busyListener(self) -> None: ...  # No getter available.

    @busyListener.setter
    def busyListener(self, value: ghidra.util.task.BusyListener) -> None: ...

    @property
    def finished(self) -> bool: ...
