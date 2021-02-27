from typing import List
import ghidra.util.graph
import java.lang


class VertexSet(object, ghidra.util.graph.KeyIndexableSet):
    """
    VertexSet is a container class for objects of type Vertex. It is
     designed to be used in conjunction with EdgeSet as part of DirectedGraph.
    """









    def add(self, __a0: ghidra.util.graph.KeyedObject) -> bool: ...

    def capacity(self) -> int:
        """
        Return the number of vertices this VertexSet may hold without growing.
        """
        ...

    def contains(self, __a0: ghidra.util.graph.KeyedObject) -> bool: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getKeyedObject(self, key: long) -> ghidra.util.graph.Vertex: ...

    def getModificationNumber(self) -> long:
        """
        Get the number of times this VertexSet has changed
        """
        ...

    def hashCode(self) -> int: ...

    def iterator(self) -> ghidra.util.graph.GraphIterator:
        """
        Return an iterator over all of the vertices in this VertexSet.
         The iterator becomes invalid and throws a ConcurrentModificationException
         if any changes are made to the VertexSet after the iterator is created.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def remove(self, __a0: ghidra.util.graph.KeyedObject) -> bool: ...

    def size(self) -> int:
        """
        Return The number of vertices in this VertexSet.
        """
        ...

    def toArray(self) -> List[ghidra.util.graph.Vertex]:
        """
        Return the elements of this VertexSet as an Vertex[].
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
