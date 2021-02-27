import ghidra.util.datastruct
import java.lang


class ValueRange(object, java.lang.Comparable):
    """
    Associates an integer value with a numeric range.
    """





    def __init__(self, start: long, end: long, value: int):
        """
        Constructor for numeric range with an associated value.
        @param start beginning of the range
        @param end end of the range
        @param value the value to associate with the range.
        """
        ...



    @overload
    def compareTo(self, otherRange: ghidra.util.datastruct.ValueRange) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def contains(self, index: long) -> bool:
        """
        Determines whether or not the indicated index is in the range.
        @param index the index to check
        @return true if the index is in this range.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getEnd(self) -> long:
        """
        Returns the end of the range.
        """
        ...

    def getStart(self) -> long:
        """
        Returns the beginning of the range.
        """
        ...

    def getValue(self) -> int:
        """
        Returns the value associated with the range.
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def end(self) -> long: ...

    @property
    def start(self) -> long: ...

    @property
    def value(self) -> int: ...
