from typing import List
import ghidra.util.graph
import java.lang


class EdgeSet(object, ghidra.util.graph.KeyIndexableSet):
    """
    Container class for a set of edges (ghidra.util.graph.Edge).
    """









    def add(self, __a0: ghidra.util.graph.KeyedObject) -> bool: ...

    def capacity(self) -> int:
        """
        Returns the number of edges this edge set can hold without growing.
        """
        ...

    def contains(self, __a0: ghidra.util.graph.KeyedObject) -> bool: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getKeyedObject(self, key: long) -> ghidra.util.graph.Edge: ...

    def getModificationNumber(self) -> long:
        """
        Used to test if edges have been added or removed from this edge set.
        """
        ...

    def hashCode(self) -> int: ...

    def iterator(self) -> ghidra.util.graph.GraphIterator:
        """
        Returns an iterator for this EdgeSet.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def remove(self, __a0: ghidra.util.graph.KeyedObject) -> bool: ...

    def size(self) -> int:
        """
        Returns the current number of edges within this edge set.
        """
        ...

    def toArray(self) -> List[ghidra.util.graph.Edge]:
        """
        @return array of Edges contained in this EdgeSet
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
