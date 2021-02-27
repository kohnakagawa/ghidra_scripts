from typing import Iterator
import ghidra.util.datastruct
import java.lang
import java.util
import java.util.function


class RedBlackTree(object, java.lang.Iterable):
    """
    A RedBlack Tree implementation with K type keys and place to store V type values.
    """





    def __init__(self):
        """
        Creates a new RedBlackKeySet that can store keys between 0 and n.
        """
        ...

    def __iter__(self): ...

    def containsKey(self, __a0: java.lang.Comparable) -> bool: ...

    def deleteEntry(self, p: ghidra.util.datastruct.RedBlackEntry) -> None:
        """
        Delete node p, and then rebalance the tree.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def forEach(self, __a0: java.util.function.Consumer) -> None: ...

    def getClass(self) -> java.lang.Class: ...

    def getEntry(self, __a0: java.lang.Comparable) -> ghidra.util.datastruct.RedBlackEntry: ...

    def getEntryGreaterThanEqual(self, __a0: java.lang.Comparable) -> ghidra.util.datastruct.RedBlackEntry: ...

    def getEntryLessThanEqual(self, __a0: java.lang.Comparable) -> ghidra.util.datastruct.RedBlackEntry: ...

    def getFirst(self) -> ghidra.util.datastruct.RedBlackEntry:
        """
        Returns the first entry in this set.
        """
        ...

    def getLast(self) -> ghidra.util.datastruct.RedBlackEntry:
        """
        Returns the last entry in this set.
        """
        ...

    def getOrCreateEntry(self, __a0: java.lang.Comparable) -> ghidra.util.datastruct.RedBlackEntry: ...

    def hashCode(self) -> int: ...

    def isEmpty(self) -> bool:
        """
        Test if the set is empty.
        @return true if the set is empty.
        """
        ...

    @overload
    def iterator(self) -> java.util.ListIterator: ...

    @overload
    def iterator(self, forward: bool) -> java.util.ListIterator: ...

    @overload
    def iterator(self, firstEntry: ghidra.util.datastruct.RedBlackEntry, forward: bool) -> java.util.ListIterator: ...

    @overload
    def iterator(self, __a0: java.lang.Comparable, __a1: bool) -> java.util.ListIterator: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def put(self, __a0: java.lang.Comparable, __a1: object) -> object: ...

    def remove(self, __a0: java.lang.Comparable) -> object: ...

    def removeAll(self) -> None:
        """
        Removes all entries from the set.
        """
        ...

    def removeNode(self, node: ghidra.util.datastruct.RedBlackEntry) -> None: ...

    def size(self) -> int:
        """
        Returns the number keys in this set.
        """
        ...

    def spliterator(self) -> java.util.Spliterator: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def empty(self) -> bool: ...

    @property
    def first(self) -> ghidra.util.datastruct.RedBlackEntry: ...

    @property
    def last(self) -> ghidra.util.datastruct.RedBlackEntry: ...
