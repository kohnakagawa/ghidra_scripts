import ghidra.util.task
import java.lang


class JohnsonCircuitsAlgorithm(object):
    """
    Finds all circuits (loops) in the given graph.

     Warning: This is a recursive algorithm.  As such, it is limited in how deep
     it can recurse.   Any path that exceeds the #JAVA_STACK_DEPTH_LIMIT will not be found.
    """

    JAVA_STACK_DEPTH_LIMIT: int = 2700



    def __init__(self, g: ghidra.graph.GDirectedGraph, accumulator: ghidra.util.datastruct.Accumulator): ...



    def compute(self, uniqueCircuits: bool, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Finds the circuits in the graph passed at construction time.
        @param uniqueCircuits true signals to return only unique circuits, where no two
                circuits will contain the same vertex
        @param monitor the task monitor
        @throws CancelledException if the monitor is cancelled
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
