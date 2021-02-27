import ghidra.graph.job
import ghidra.util.task
import java.lang


class AbstractGraphVisibilityTransitionJob(ghidra.graph.job.AbstractAnimatorJob):
    """
    A job that provides an animator and callbacks for transitioning the visibility of
     graph vertices.  The opacity value will change from 0 to 1 over the course of the job.
     Subclasses can decide how to use the opacity value as it changes.   For example, a
     subclass can fade in or out the vertices provided to the job.
    """









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

    def setPercentComplete(self, percentComplete: float) -> None:
        """
        Callback from our animator.
        """
        ...

    def shortcut(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def percentComplete(self) -> None: ...  # No getter available.

    @percentComplete.setter
    def percentComplete(self, value: float) -> None: ...
