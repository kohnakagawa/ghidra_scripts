from typing import List
import ghidra.graph
import ghidra.graph.algo
import java.lang


class DepthFirstSorter(object):
    """
    Processes the given graph depth first and records that order of the vertices.
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @overload
    @staticmethod
    def postOrder(g: ghidra.graph.GDirectedGraph) -> List[V]:
        """
        Returns the vertices of the given graph in post-order, which is the order the vertices
         are last visited when performing a depth-first traversal.
        @param g the graph
        @return the vertices in post-order
        """
        ...

    @overload
    @staticmethod
    def postOrder(g: ghidra.graph.GDirectedGraph, navigator: ghidra.graph.algo.GraphNavigator) -> List[V]:
        """
        Returns the vertices of the given graph in post-order, which is the order the vertices
         are last visited when performing a depth-first traversal.
        @param g the graph
        @param navigator the knower of the direction the graph should be traversed
        @return the vertices in post-order
        """
        ...

    @overload
    @staticmethod
    def preOrder(g: ghidra.graph.GDirectedGraph) -> List[V]:
        """
        Returns the vertices of the given graph in pre-order, which is the order the vertices
         are encountered when performing a depth-first traversal.
        @param g the graph
        @return the vertices in pre-order
        """
        ...

    @overload
    @staticmethod
    def preOrder(g: ghidra.graph.GDirectedGraph, navigator: ghidra.graph.algo.GraphNavigator) -> List[V]:
        """
        Returns the vertices of the given graph in pre-order, which is the order the vertices
         are encountered when performing a depth-first traversal.
        @param g the graph
        @param navigator the knower of the direction the graph should be traversed
        @return the vertices in pre-order
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
