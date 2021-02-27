import ghidra.util.datastruct
import java.lang


class PropertySetIndexRangeIterator(object, ghidra.util.datastruct.IndexRangeIterator):
    """
    Iterator over Property Set Index ranges that have the same value
    """





    def __init__(self, set: ghidra.util.prop.PropertySet, start: long):
        """
        Constructor for PropertySetIndexRangeIterator.
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hasNext(self) -> bool:
        """
        @see ghidra.util.datastruct.IndexRangeIterator#hasNext()
        """
        ...

    def hashCode(self) -> int: ...

    def next(self) -> ghidra.util.datastruct.IndexRange:
        """
        @see ghidra.util.datastruct.IndexRangeIterator#next()
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
