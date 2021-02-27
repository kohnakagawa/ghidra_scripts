import ghidra.app.util.bin.format.dwarf4
import java.lang


class DWARFRange(object, java.lang.Comparable):
    """
    Holds the start (inclusive) and end (exclusive) addresses of a range.
    """





    def __init__(self, start: long, end: long):
        """
        Constructs a new {@link DWARFRange} using start and end values.
        @param start long starting address, inclusive
        @param end long ending address, exclusive
        """
        ...



    @overload
    def compareTo(self, other: ghidra.app.util.bin.format.dwarf4.DWARFRange) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getFrom(self) -> long:
        """
        Returns starting address.
        @return long starting address
        """
        ...

    def getTo(self) -> long:
        """
        Returns ending address, exclusive.
        @return long ending address, exclusive.
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
    def from(self) -> long: ...

    @property
    def to(self) -> long: ...
