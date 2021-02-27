import ghidra.util
import java.lang


class LongIteratorImpl(object, ghidra.util.LongIterator):
    """
    Class to iterate over indexes of a PropertyMap.
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hasNext(self) -> bool:
        """
        Returns true if the iterator has more indexes.
        """
        ...

    def hasPrevious(self) -> bool:
        """
        Return true if the iterator has a previous index.
        """
        ...

    def hashCode(self) -> int: ...

    def next(self) -> long:
        """
        Returns the next index in the iterator.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def previous(self) -> long:
        """
        Returns the previous index in the iterator.
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
