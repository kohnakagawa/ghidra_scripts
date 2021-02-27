import ghidra.graph
import java.lang
import java.util


class GDirectedGraph(ghidra.graph.GImplicitDirectedGraph, object):
    """
    A directed graph

     Unlike GImplicitDirectedGraph, this graph is constructed explicitly
     in memory. Edges and vertices are added and removed like any other
     collection, and these elements represent the entirety of the graph at any
     given time.
    """









    def addEdge(self, __a0: ghidra.graph.GEdge) -> None: ...

    def addVertex(self, __a0: object) -> bool: ...

    @overload
    def containsEdge(self, __a0: ghidra.graph.GEdge) -> bool: ...

    @overload
    def containsEdge(self, __a0: object, __a1: object) -> bool: ...

    def containsVertex(self, __a0: object) -> bool: ...

    def copy(self) -> ghidra.graph.GDirectedGraph:
        """
        Copy this graph.

         <P>
         Note: the vertices and edges in the copy may be the same instances in the
         new graph and not themselves copies.
        @return the new copy
        """
        ...

    def emptyCopy(self) -> ghidra.graph.GDirectedGraph:
        """
        Creates a new instance of this graph with no vertices or edges. This is
         useful when you wish to build a new graph using the same type as this
         graph.
        @return the new copy
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def findEdge(self, __a0: object, __a1: object) -> ghidra.graph.GEdge: ...

    def getClass(self) -> java.lang.Class: ...

    def getEdgeCount(self) -> int:
        """
        Count the number of edges in the graph
        @return the count
        """
        ...

    def getEdges(self) -> java.util.Collection:
        """
        Retrieve all the edges
        @return the edges
        """
        ...

    def getInEdges(self, __a0: object) -> java.util.Collection: ...

    def getIncidentEdges(self, __a0: object) -> java.util.Collection: ...

    def getOutEdges(self, __a0: object) -> java.util.Collection: ...

    def getPredecessors(self, __a0: object) -> java.util.Collection: ...

    def getSuccessors(self, __a0: object) -> java.util.Collection: ...

    def getVertexCount(self) -> int:
        """
        Count the number of vertices in the graph
        @return the count
        """
        ...

    def getVertices(self) -> java.util.Collection:
        """
        Retrieve all the vertices
        @return the vertices
        """
        ...

    def hashCode(self) -> int: ...

    def isEmpty(self) -> bool:
        """
        Test if the graph is empty, i.e., contains no vertices or edges
        @return true if the graph is empty, or false
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def removeEdge(self, __a0: ghidra.graph.GEdge) -> bool: ...

    def removeEdges(self, edges: java.lang.Iterable) -> None:
        """
        Removes the given edges from the graph
        @param edges the edges to remove
        """
        ...

    def removeVertex(self, __a0: object) -> bool: ...

    def removeVertices(self, vertices: java.lang.Iterable) -> None:
        """
        Removes the given vertices from the graph
        @param vertices the vertices to remove
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def edgeCount(self) -> int: ...

    @property
    def edges(self) -> java.util.Collection: ...

    @property
    def empty(self) -> bool: ...

    @property
    def vertexCount(self) -> int: ...

    @property
    def vertices(self) -> java.util.Collection: ...
