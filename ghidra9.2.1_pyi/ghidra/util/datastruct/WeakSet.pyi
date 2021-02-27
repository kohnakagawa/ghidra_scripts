from typing import Iterator
import java.lang
import java.util
import java.util.function
import java.util.stream


class WeakSet(object, java.lang.Iterable):




    def __init__(self): ...

    def __iter__(self): ...

    def add(self, t: object) -> None:
        """
        Add the given object to the set
        @param t the object to add
        """
        ...

    def clear(self) -> None:
        """
        Remove all elements from this data structure
        """
        ...

    def contains(self, t: object) -> bool:
        """
        Returns true if the given object is in this data structure
        @return true if the given object is in this data structure
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def forEach(self, __a0: java.util.function.Consumer) -> None: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def isEmpty(self) -> bool:
        """
        Return whether this data structure is empty
        @return whether this data structure is empty
        """
        ...

    def iterator(self) -> java.util.Iterator: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def remove(self, t: object) -> None:
        """
        Remove the given object from the data structure
        @param t the object to remove
        """
        ...

    def size(self) -> int:
        """
        Return the number of objects contained within this data structure
        @return the size
        """
        ...

    def spliterator(self) -> java.util.Spliterator: ...

    def stream(self) -> java.util.stream.Stream:
        """
        Returns a stream of the values of this collection.
        @return a stream of the values of this collection.
        """
        ...

    def toString(self) -> unicode: ...

    def values(self) -> java.util.Collection:
        """
        Returns a Collection view of this set.  The returned Collection is backed by this set.
        @return a Collection view of this set.  The returned Collection is backed by this set.
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def empty(self) -> bool: ...
