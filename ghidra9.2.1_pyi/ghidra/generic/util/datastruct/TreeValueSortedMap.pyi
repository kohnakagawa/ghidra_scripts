from typing import Iterator
from typing import List
import ghidra.generic.util.datastruct
import java.lang
import java.util
import java.util.function


class TreeValueSortedMap(java.util.AbstractMap, ghidra.generic.util.datastruct.ValueSortedMap):
    """
    A tree-based implementation of a value-sorted map

     The underlying implementation is currently an unbalanced binary tree whose nodes also comprise a
     doubly-linked list. Currently, it is not thread safe.

     Note this implementation isn't terribly smart, as it makes no efforts to balance the tree. It is
     also not thread safe.
    """







    def __iter__(self): ...

    def ceilingEntryByValue(self, __a0: object) -> java.util.Map.Entry: ...

    def clear(self) -> None: ...

    def compute(self, __a0: object, __a1: java.util.function.BiFunction) -> object: ...

    def computeIfAbsent(self, __a0: object, __a1: java.util.function.Function) -> object: ...

    def computeIfPresent(self, __a0: object, __a1: java.util.function.BiFunction) -> object: ...

    def containsKey(self, key: object) -> bool: ...

    def containsValue(self, value: object) -> bool: ...

    @staticmethod
    def copyOf(__a0: java.util.Map) -> java.util.Map: ...

    @staticmethod
    def createWithComparator(comparator: java.util.Comparator) -> ghidra.generic.util.datastruct.TreeValueSortedMap:
        """
        Create a tree using a custom comparator to order the values
        @param comparator the comparator, providing a total ordering of the values
        """
        ...

    @staticmethod
    def createWithNaturalOrder() -> ghidra.generic.util.datastruct.TreeValueSortedMap:
        """
        Create a tree using the values' natural ordering
        """
        ...

    @staticmethod
    def entry(__a0: object, __a1: object) -> java.util.Map.Entry: ...

    def entrySet(self) -> ghidra.generic.util.datastruct.TreeValueSortedMap:
        """
        {@inheritDoc}
        @see ValueSortedTreeMapEntrySet
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def floorEntryByValue(self, __a0: object) -> java.util.Map.Entry: ...

    def forEach(self, __a0: java.util.function.BiConsumer) -> None: ...

    def getClass(self) -> java.lang.Class: ...

    def getOrDefault(self, __a0: object, __a1: object) -> object: ...

    def hashCode(self) -> int: ...

    def headMapByValue(self, __a0: object, __a1: bool) -> ghidra.generic.util.datastruct.ValueSortedMap: ...

    def higherEntryByValue(self, __a0: object) -> java.util.Map.Entry: ...

    def isEmpty(self) -> bool: ...

    def keySet(self) -> ghidra.generic.util.datastruct.TreeValueSortedMap:
        """
        {@inheritDoc}
        @see ValueSortedTreeMapKeySet
        """
        ...

    def lowerEntryByValue(self, __a0: object) -> java.util.Map.Entry: ...

    def merge(self, __a0: object, __a1: object, __a2: java.util.function.BiFunction) -> object: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @overload
    @staticmethod
    def of() -> java.util.Map: ...

    @overload
    @staticmethod
    def of(__a0: object, __a1: object) -> java.util.Map: ...

    @overload
    @staticmethod
    def of(__a0: object, __a1: object, __a2: object, __a3: object) -> java.util.Map: ...

    @overload
    @staticmethod
    def of(__a0: object, __a1: object, __a2: object, __a3: object, __a4: object, __a5: object) -> java.util.Map: ...

    @overload
    @staticmethod
    def of(__a0: object, __a1: object, __a2: object, __a3: object, __a4: object, __a5: object, __a6: object, __a7: object) -> java.util.Map: ...

    @overload
    @staticmethod
    def of(__a0: object, __a1: object, __a2: object, __a3: object, __a4: object, __a5: object, __a6: object, __a7: object, __a8: object, __a9: object) -> java.util.Map: ...

    @overload
    @staticmethod
    def of(__a0: object, __a1: object, __a2: object, __a3: object, __a4: object, __a5: object, __a6: object, __a7: object, __a8: object, __a9: object, __a10: object, __a11: object) -> java.util.Map: ...

    @overload
    @staticmethod
    def of(__a0: object, __a1: object, __a2: object, __a3: object, __a4: object, __a5: object, __a6: object, __a7: object, __a8: object, __a9: object, __a10: object, __a11: object, __a12: object, __a13: object) -> java.util.Map: ...

    @overload
    @staticmethod
    def of(__a0: object, __a1: object, __a2: object, __a3: object, __a4: object, __a5: object, __a6: object, __a7: object, __a8: object, __a9: object, __a10: object, __a11: object, __a12: object, __a13: object, __a14: object, __a15: object) -> java.util.Map: ...

    @overload
    @staticmethod
    def of(__a0: object, __a1: object, __a2: object, __a3: object, __a4: object, __a5: object, __a6: object, __a7: object, __a8: object, __a9: object, __a10: object, __a11: object, __a12: object, __a13: object, __a14: object, __a15: object, __a16: object, __a17: object) -> java.util.Map: ...

    @overload
    @staticmethod
    def of(__a0: object, __a1: object, __a2: object, __a3: object, __a4: object, __a5: object, __a6: object, __a7: object, __a8: object, __a9: object, __a10: object, __a11: object, __a12: object, __a13: object, __a14: object, __a15: object, __a16: object, __a17: object, __a18: object, __a19: object) -> java.util.Map: ...

    @staticmethod
    def ofEntries(__a0: List[java.util.Map.Entry]) -> java.util.Map: ...

    def put(self, __a0: object, __a1: object) -> object: ...

    def putAll(self, m: java.util.Map) -> None: ...

    def putIfAbsent(self, __a0: object, __a1: object) -> object: ...

    @overload
    def remove(self, key: object) -> V: ...

    @overload
    def remove(self, __a0: object, __a1: object) -> bool: ...

    @overload
    def replace(self, __a0: object, __a1: object) -> object: ...

    @overload
    def replace(self, __a0: object, __a1: object, __a2: object) -> bool: ...

    def replaceAll(self, __a0: java.util.function.BiFunction) -> None: ...

    def size(self) -> int: ...

    def subMapByValue(self, __a0: object, __a1: bool, __a2: object, __a3: bool) -> ghidra.generic.util.datastruct.ValueSortedMap: ...

    def tailMapByValue(self, __a0: object, __a1: bool) -> ghidra.generic.util.datastruct.ValueSortedMap: ...

    def toString(self) -> unicode: ...

    def update(self, __a0: object) -> bool: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def empty(self) -> bool: ...
