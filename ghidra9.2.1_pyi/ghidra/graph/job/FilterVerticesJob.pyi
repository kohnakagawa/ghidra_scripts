import ghidra.graph.job
import ghidra.util.task
import java.lang


class FilterVerticesJob(ghidra.graph.job.AbstractGraphVisibilityTransitionJob):
    """
    Uses the given filter to fade out vertices that do not pass.  Vertices that pass the filter
     will be included in the graph.  Not only will passing vertices be included, but so too
     will any vertices reachable from those vertices.

     This job will update the graph so that any previously filtered vertices will be put
     back into the graph.
    """





    def __init__(self, viewer: ghidra.graph.viewer.GraphViewer, graph: ghidra.graph.graphs.FilteringVisualGraph, filter: java.util.function.Predicate, remove: bool):
        """
        Constructor
        @param viewer the viewer upon which to operate
        @param graph the graph to filter
        @param filter the predicate used to determine what passes the filter
        @param remove true signals to remove the vertices from the view; false signals to leave
                       them visible, but faded to show that they failed the filter
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
