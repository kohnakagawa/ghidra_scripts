import ghidra.util.graph
import java.lang


class Edge(object, ghidra.util.graph.KeyedObject, java.lang.Comparable):
    """
    An Edge joins a pair of vertices.
     The from and to vertex of an edge can not be changed.
    """





    def __init__(self, from_: ghidra.util.graph.Vertex, to: ghidra.util.graph.Vertex):
        """
        @param from The from or parent vertex.
        @param to The to or child vertex.
        """
        ...



    @overload
    def compareTo(self, edge: ghidra.util.graph.Edge) -> int:
        """
        Compare one edge to another. Based on time of creation.
        """
        ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def equals(self, obj: object) -> bool:
        """
        Overides equals method by comparing keys.
        """
        ...

    def from(self) -> ghidra.util.graph.Vertex:
        """
        Returns from vertex.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def key(self) -> long:
        """
        Returns the key of this edge.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def to(self) -> ghidra.util.graph.Vertex:
        """
        Returns to vertex.
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
