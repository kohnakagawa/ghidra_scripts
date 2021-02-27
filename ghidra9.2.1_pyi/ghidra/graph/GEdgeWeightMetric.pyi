import ghidra.graph
import java.lang


class GEdgeWeightMetric(object):
    """
    A callback to get the weight of an edge

     Analogous to Java's Comparator, this provides a means to override the weight of an edge
     in a graph, or provide a weight in the absence of a natural weight, when executing various graph
     algorithms, e.g., shortest path.
    """

    NATURAL_METRIC: ghidra.graph.GEdgeWeightMetric = ghidra.graph.GEdgeWeightMetric$$Lambda$1108/0x00000008013af040@786dcd37
    UNIT_METRIC: ghidra.graph.GEdgeWeightMetric = ghidra.graph.GEdgeWeightMetric$$Lambda$1107/0x00000008013afc40@2372cfdd







    def computeWeight(self, __a0: ghidra.graph.GEdge) -> float: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    @staticmethod
    def naturalMetric() -> ghidra.graph.GEdgeWeightMetric:
        """
        Use the natural weight of each edge

         The metric assumes every edge is a {@link GWeightedEdge}. If not, you will likely encounter
         a {@link ClassCastException}.
        @return the metric
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @staticmethod
    def unitMetric() -> ghidra.graph.GEdgeWeightMetric:
        """
        Measure every edge as having a weight of 1
        @return the metric
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
