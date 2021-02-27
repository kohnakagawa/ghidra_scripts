from typing import Iterator
from typing import List
import java.lang
import java.util
import java.util.function
import java.util.stream


class LongArrayList(object, List[object]):
    """
    An ArrayList for longs.
    """

    MIN_SIZE: int = 4



    @overload
    def __init__(self):
        """
        Creates a new LongArrayList
        """
        ...

    @overload
    def __init__(self, arr: List[long]):
        """
        Creates a new Long ArrayList using the values in the given array
        @param arr array of longs to initialize to.
        """
        ...

    @overload
    def __init__(self, list: ghidra.util.datastruct.LongArrayList):
        """
        Creates a new LongArrayList that is equivalent to the specified LongArrayList.
         It creates a copy of the specified list.
        @param list the list to be copied.
        """
        ...

    def __iter__(self): ...

    @overload
    def add(self, value: long) -> None: ...

    @overload
    def add(self, value: long) -> None: ...

    @overload
    def add(self, __a0: object) -> bool: ...

    @overload
    def add(self, index: int, value: long) -> None:
        """
        @see java.util.List#add(int, java.lang.Object)
        """
        ...

    @overload
    def add(self, index: int, value: long) -> None:
        """
        @see java.util.List#add(int, java.lang.Object)
        """
        ...

    @overload
    def add(self, __a0: int, __a1: object) -> None: ...

    @overload
    def addAll(self, c: java.util.Collection) -> bool: ...

    @overload
    def addAll(self, index: int, c: java.util.Collection) -> bool: ...

    def clear(self) -> None:
        """
        @see LongArraySubList#clear()
        """
        ...

    def contains(self, value: object) -> bool: ...

    def containsAll(self, c: java.util.Collection) -> bool: ...

    @staticmethod
    def copyOf(__a0: java.util.Collection) -> List[object]: ...

    def equals(self, __a0: object) -> bool: ...

    def forEach(self, __a0: java.util.function.Consumer) -> None: ...

    def get(self, index: int) -> long:
        """
        @see java.util.List#get(int)
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getLongValue(self, index: int) -> long: ...

    def hashCode(self) -> int: ...

    def indexOf(self, value: object) -> int: ...

    def isEmpty(self) -> bool: ...

    def iterator(self) -> Iterator[long]: ...

    def lastIndexOf(self, value: object) -> int: ...

    @overload
    def listIterator(self) -> java.util.ListIterator: ...

    @overload
    def listIterator(self, index: int) -> java.util.ListIterator: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @overload
    @staticmethod
    def of() -> List[object]: ...

    @overload
    @staticmethod
    def of(__a0: List[object]) -> List[object]: ...

    @overload
    @staticmethod
    def of(__a0: object) -> List[object]: ...

    @overload
    @staticmethod
    def of(__a0: object, __a1: object) -> List[object]: ...

    @overload
    @staticmethod
    def of(__a0: object, __a1: object, __a2: object) -> List[object]: ...

    @overload
    @staticmethod
    def of(__a0: object, __a1: object, __a2: object, __a3: object) -> List[object]: ...

    @overload
    @staticmethod
    def of(__a0: object, __a1: object, __a2: object, __a3: object, __a4: object) -> List[object]: ...

    @overload
    @staticmethod
    def of(__a0: object, __a1: object, __a2: object, __a3: object, __a4: object, __a5: object) -> List[object]: ...

    @overload
    @staticmethod
    def of(__a0: object, __a1: object, __a2: object, __a3: object, __a4: object, __a5: object, __a6: object) -> List[object]: ...

    @overload
    @staticmethod
    def of(__a0: object, __a1: object, __a2: object, __a3: object, __a4: object, __a5: object, __a6: object, __a7: object) -> List[object]: ...

    @overload
    @staticmethod
    def of(__a0: object, __a1: object, __a2: object, __a3: object, __a4: object, __a5: object, __a6: object, __a7: object, __a8: object) -> List[object]: ...

    @overload
    @staticmethod
    def of(__a0: object, __a1: object, __a2: object, __a3: object, __a4: object, __a5: object, __a6: object, __a7: object, __a8: object, __a9: object) -> List[object]: ...

    def parallelStream(self) -> java.util.stream.Stream: ...

    def removeAll(self, c: java.util.Collection) -> bool: ...

    def removeIf(self, __a0: java.util.function.Predicate) -> bool: ...

    def replaceAll(self, __a0: java.util.function.UnaryOperator) -> None: ...

    def retainAll(self, c: java.util.Collection) -> bool: ...

    def reverse(self) -> None: ...

    @overload
    def set(self, index: int, value: long) -> long:
        """
        @see LongArraySubList#set(int, long)
        """
        ...

    @overload
    def set(self, __a0: int, __a1: object) -> object: ...

    def size(self) -> int:
        """
        @see LongArraySubList#size()
        """
        ...

    def spliterator(self) -> java.util.Spliterator: ...

    def stream(self) -> java.util.stream.Stream: ...

    def subList(self, startIndex: int, endIndex: int) -> List[long]: ...

    @overload
    def toArray(self) -> List[long]:
        """
        @see LongArraySubList#toArray()
        """
        ...

    @overload
    def toArray(self, a: List[long]) -> List[long]: ...

    @overload
    def toArray(self, a: List[object]) -> List[object]: ...

    @overload
    def toArray(self, __a0: java.util.function.IntFunction) -> List[object]: ...

    @overload
    def toLongArray(self) -> List[long]: ...

    @overload
    def toLongArray(self, start: int, length: int) -> List[long]: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def empty(self) -> bool: ...
