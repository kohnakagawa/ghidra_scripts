from typing import List
import ghidra.graph
import ghidra.graph.algo
import java.lang
import java.util


class GraphNavigator(object):
    """
    The methods on this interface are meant to enable graph traversal in a way that allows
     the underlying graph to be walked from top-down or bottom-up.
    """









    @staticmethod
    def bottomUpNavigator() -> ghidra.graph.algo.GraphNavigator:
        """
        Creates a bottom-down navigator, which is one that traverses the graph from the sink
         to the source.
        @return the navigator
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getEdges(self, __a0: ghidra.graph.GDirectedGraph, __a1: object) -> java.util.Collection: ...

    def getEnd(self, __a0: ghidra.graph.GEdge) -> object: ...

    def getPredecessors(self, __a0: ghidra.graph.GDirectedGraph, __a1: object) -> java.util.Collection: ...

    def getSinks(self, graph: ghidra.graph.GDirectedGraph) -> java.util.Set:
        """
        Gets the exit vertices of the given graph.  If this is a top-down navigator, then the
         sinks are returned; otherwise, the sources are returned.
        @param graph the graph
        @return the exits
        """
        ...

    def getSources(self, graph: ghidra.graph.GDirectedGraph) -> java.util.Set:
        """
        Gets the root vertices of the given graph.  If this is a top-down navigator, then the
         sources are returned; otherwise, the sinks are returned.
        @param graph the graph
        @return the roots
        """
        ...

    def getSuccessors(self, __a0: ghidra.graph.GDirectedGraph, __a1: object) -> java.util.Collection: ...

    def getVerticesInPostOrder(self, graph: ghidra.graph.GDirectedGraph) -> List[V]:
        """
        Returns all vertices in the given graph in the depth-first order.   The order will
         be post-order for a top-down navigator and pre-order for a bottom-up navigator.
        @param graph the graph
        @return the ordered vertices
        """
        ...

    def hashCode(self) -> int: ...

    def isTopDown(self) -> bool:
        """
        Returns true if this navigator processes nodes from the top down; false if nodes are
         processed from the bottom up.
        @return true if this navigator processes nodes from the top down; false if nodes are
         		   processed from the bottom up.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @staticmethod
    def topDownNavigator() -> ghidra.graph.algo.GraphNavigator:
        """
        Creates a top-down navigator, which is one that traverses the graph from the source
         to the sink.
        @return the navigator
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def topDown(self) -> bool: ...
