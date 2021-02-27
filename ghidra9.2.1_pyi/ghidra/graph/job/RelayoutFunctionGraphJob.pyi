import ghidra.graph.job
import ghidra.graph.viewer.layout
import ghidra.util.task
import java.lang
import java.util


class RelayoutFunctionGraphJob(ghidra.graph.job.AbstractGraphTransitionJob):




    def __init__(self, viewer: ghidra.graph.viewer.GraphViewer, useAnimation: bool): ...



    def calculateDefaultLayoutLocations(self, verticesToIgnore: java.util.Set) -> ghidra.graph.viewer.layout.LayoutPositions:
        """
        Calculates default vertex locations for the current graph by using the current layout,
         excluding those vertices in the given <i>ignore</i> set.  The graph,
         layout and vertices will be unaltered.
        @param verticesToIgnore The set of vertices which should be excluded from the layout process
        @return The mapping of all arranged vertices to their respective locations
        """
        ...

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
