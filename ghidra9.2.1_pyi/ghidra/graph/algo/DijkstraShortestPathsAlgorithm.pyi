import java.lang
import java.util


class DijkstraShortestPathsAlgorithm(object):
    """
    Dijkstra's shortest-path algorithm


     This implementation computes the shortest paths between two vertices using Dijkstra's
     single-source shortest path finding algorithm. Any time a new source is given, it explores all
     destinations in the graph up to a maximum distance from the source. Thus, this implementation is
     best applied when many queries are anticipated from relatively few sources.
    """





    @overload
    def __init__(self, graph: ghidra.graph.GImplicitDirectedGraph):
        """
        Use Dijkstra's algorithm on the given graph

         <p>
         This constructor assumes the graph's edges are {@link GWeightedEdge}s. If not, you will
         likely encounter a {@link ClassCastException}.
        @param graph the graph
        """
        ...

    @overload
    def __init__(self, graph: ghidra.graph.GImplicitDirectedGraph, maxDistance: float):
        """
        Use Dijkstra's algorithm on the given graph with the given maximum distance

         <p>
         This constructor assumes the graph's edges are {@link GWeightedEdge}s. If not, you will
         likely encounter a {@link ClassCastException}.
        @param graph the graph
        @param maxDistance the maximum distance, or null for no maximum
        """
        ...

    @overload
    def __init__(self, graph: ghidra.graph.GImplicitDirectedGraph, metric: ghidra.graph.GEdgeWeightMetric):
        """
        Use Dijstra's algorithm on the given graph with a custom edge weight metric
        @param graph the graph
        @param metric the function to compute the weight of an edge
        """
        ...

    @overload
    def __init__(self, graph: ghidra.graph.GImplicitDirectedGraph, maxDistance: float, metric: ghidra.graph.GEdgeWeightMetric):
        """
        Use Dijstra's algorithm on the given graph with the given maximum distance and a custom edge
         weight metric
        @param graph the graph
        @param maxDistance the maximum distance, or null for no maximum
        @param metric the function to compute the weight of an edge
        """
        ...



    def computeOptimalPaths(self, __a0: object, __a1: object) -> java.util.Collection: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDistancesFromSource(self, __a0: object) -> java.util.Map: ...

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
