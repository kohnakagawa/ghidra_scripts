from typing import Iterator
import java.lang


class ListLinked(object):
    """
    A better linked list implementation than provided by java.util.

     TODO: Looks like the main benefit is a non-failing iterator.  In JDK 1.5
     this may not be needed.  1.5 has better Iterators in the collections classes.
    """









    def add(self, o: object) -> Iterator[object]:
        """
        Add object to end of the list, any existing iterators remain valid
        @param o -- Object to be added
        @return Iterator to new object
        """
        ...

    def clear(self) -> None:
        """
        Get rid of all entries on the linked list.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def insertAfter(self, itr: Iterator[object], o: object) -> Iterator[object]:
        """
        Insert new object AFTER object pointed to by iterator, other Iterators remain valid
        @param itr Iterator to existing object
        @param o New object to add
        @return Iterator to new object
        """
        ...

    def insertBefore(self, itr: Iterator[object], o: object) -> Iterator[object]:
        """
        Insert new object BEFORE object pointed to by iterator, other Iterators remain valid
        @param itr Iterator to existing object
        @param o New object to add
        @return Iterator to new object
        """
        ...

    def iterator(self) -> Iterator[object]:
        """
        @return an iterator over this linked list
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def remove(self, itr: Iterator[object]) -> None:
        """
        Remove object from list indicated by Iterator, all iterators that point to objects other
         than this one remain valid
        @param itr Iterator to object to be removed
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
