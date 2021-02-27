import ghidra.graph
import ghidra.graph.algo
import java.lang
import java.util


class ChkPostDominanceAlgorithm(ghidra.graph.algo.ChkDominanceAlgorithm):
    """
    This is ChkDominanceAlgorithm with reverse graph traversal, which allows the
     algorithm to calculate post dominance.
    """





    def __init__(self, g: ghidra.graph.GDirectedGraph, monitor: ghidra.util.task.TaskMonitor):
        """
        Constructor.
        @param g the graph
        @param monitor the monitor
        @throws CancelledException if the algorithm is cancelled
        """
        ...



    def clear(self) -> None:
        """
        Releases cached values used by internal data structures
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDominanceTree(self) -> ghidra.graph.GDirectedGraph:
        """
        Returns the dominance tree for the given graph, which is tree where each
         node's children are those nodes it *immediately* dominates (a idom b).
        @return the dominance tree
        """
        ...

    def getDominated(self, __a0: object) -> java.util.Set: ...

    def getDominators(self, __a0: object) -> java.util.Set: ...

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
