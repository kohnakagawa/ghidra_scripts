import ghidra.graph
import ghidra.graph.algo
import java.lang
import java.util


class ChkDominanceAlgorithm(ghidra.graph.algo.AbstractDominanceAlgorithm):
    """
    This algorithm is an implementation of the Cooper, Harvey, Kennedy algorithm.

     The algorithm processes the graph in reverse post-order.  The runtime of
     this algorithm is approximately O(V+E*D) per iteration of the loop, where
     D is the size of the largest dominator set.  The number of iterations is
     bound at d(G) + 3, where d(G) is the "loop
     connectedness" of the graph.
    """





    def __init__(self, g: ghidra.graph.GDirectedGraph, monitor: ghidra.util.task.TaskMonitor):
        """
        Constructor.
        @param g the graph
        @param monitor the monitor
        @throws CancelledException if the algorithm is cancelled
        @throws IllegalArgumentException if there are no source vertices in the graph
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

    @property
    def dominanceTree(self) -> ghidra.graph.GDirectedGraph: ...
