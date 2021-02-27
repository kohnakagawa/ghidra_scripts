import java.lang


class LongIterator(object):
    """
    Iterator over a set of Java-type long values.
    """

    EMPTY: ghidra.util.LongIterator = ghidra.util.LongIterator$1@6a8f44d2







    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hasNext(self) -> bool:
        """
        Return true if there is a next long in this iterator.
        """
        ...

    def hasPrevious(self) -> bool:
        """
        Return true if there a previous long in this iterator.
        """
        ...

    def hashCode(self) -> int: ...

    def next(self) -> long:
        """
        Get the next long value in this iterator.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def previous(self) -> long:
        """
        Get the previous long value in this iterator.
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
