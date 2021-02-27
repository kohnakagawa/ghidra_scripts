import ghidra.util.task
import java.lang


class InitializeCircuitsRunnable(object, ghidra.util.task.SwingRunnable):
    """
    A task to find all the loops in a graph.
    """





    def __init__(self, view: ghidra.graph.viewer.VisualGraphView, graph: ghidra.graph.VisualGraph): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def monitoredRun(self, monitor: ghidra.util.task.TaskMonitor) -> None: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def swingRun(self, isCancelled: bool) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
