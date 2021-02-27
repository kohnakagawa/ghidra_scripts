import java.lang


class GraphIterator(object):
    """
    Interface for VertexSet and EdgeSet iterators.
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hasNext(self) -> bool:
        """
        Return true if the iterator has more elements
        """
        ...

    def hashCode(self) -> int: ...

    def next(self) -> object:
        """
        Returns next element in the iteration.
        @throws ConcurrentModificationException if the backing set
         has been modified since the iterator was created.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def remove(self) -> bool:
        """
        Removes the object from the backing set safely
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
