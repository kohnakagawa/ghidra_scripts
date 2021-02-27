import ghidra.graph.job
import ghidra.graph.viewer.layout
import ghidra.util.task
import java.lang
import java.util


class AbstractFunctionGraphTransitionJob(ghidra.graph.job.AbstractGraphTransitionJob):








    def calculateDefaultLayoutLocations(self, __a0: java.util.Set) -> ghidra.graph.viewer.layout.LayoutPositions: ...

    def canShortcut(self) -> bool: ...

    def dispose(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def execute(self, __a0: ghidra.graph.job.GraphJobListener) -> None: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def isFinished(self) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setBusyListener(self, __a0: ghidra.util.task.BusyListener) -> None: ...

    def setPercentComplete(self, __a0: float) -> None: ...

    def shortcut(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
