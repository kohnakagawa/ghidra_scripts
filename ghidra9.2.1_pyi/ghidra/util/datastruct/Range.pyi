import ghidra.util.datastruct
import java.lang


class Range(object, java.lang.Comparable):
    """
    A class for holding a minimum and maximum signed int values that define a range.
    """

    max: int
    min: int



    def __init__(self, min: int, max: int):
        """
        Creates a range whose extent is from min to max.
        @param min the minimum extent.
        @param max the maximum extent (inclusive).
        @throws IllegalArgumentException if max is less than min.
        """
        ...



    @overload
    def compareTo(self, other: ghidra.util.datastruct.Range) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def contains(self, value: int) -> bool:
        """
        Returns true if the value is within the ranges extent.
        @param value the value to check.
        """
        ...

    def equals(self, obj: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def size(self) -> long:
        """
        Returns the range's size.
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
