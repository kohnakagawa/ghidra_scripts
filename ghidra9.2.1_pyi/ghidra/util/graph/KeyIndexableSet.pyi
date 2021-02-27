from typing import List
import ghidra.util.graph
import java.lang


class KeyIndexableSet(object):
    """
    Interface for sets of graph objects which have keys such as vertices
     and edges.
    """









    def add(self, __a0: ghidra.util.graph.KeyedObject) -> bool: ...

    def capacity(self) -> int:
        """
        Returns the number of KeyedObjects this KeyIndexableSet can
         hold without growing.
        """
        ...

    def contains(self, __a0: ghidra.util.graph.KeyedObject) -> bool: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getKeyedObject(self, key: long) -> object:
        """
        Returns the KeyedObject with the specified key in this KeyIndexableSet.
         Returns null if the Set contains no object with that key.
        """
        ...

    def getModificationNumber(self) -> long:
        """
        The modification number is a counter for the number of changes
         the KeyIndexableSet has undergone since its creation.
        """
        ...

    def hashCode(self) -> int: ...

    def iterator(self) -> ghidra.util.graph.GraphIterator:
        """
        Returns an iterator for this KeyIndexableSet which uses the
         hasNext()/next() style. See GraphIterator.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def remove(self, __a0: ghidra.util.graph.KeyedObject) -> bool: ...

    def size(self) -> int:
        """
        Returns the number of KeyedObjects in this KeyIndexableSet
        """
        ...

    def toArray(self) -> List[object]:
        """
        Returns the elements of this KeyIndexableSet as an array of
         KeyedObjects.
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
    def modificationNumber(self) -> long: ...
