import ghidra.util.datastruct
import java.lang


class IndexRangeIterator(object):
    """
    Iterator interface for index ranges.
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hasNext(self) -> bool:
        """
        Returns true if there are more index ranges.
        @return true if there are more index ranges.
        """
        ...

    def hashCode(self) -> int: ...

    def next(self) -> ghidra.util.datastruct.IndexRange:
        """
        Returns the next index range.
        @return the next index range.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
