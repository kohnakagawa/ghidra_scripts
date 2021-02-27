from typing import List
import ghidra.app.util.bin.format.ne
import java.lang


class SegmentTable(object):
    """
    A class to represent the new-executable segment table.
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getSegments(self) -> List[ghidra.app.util.bin.format.ne.Segment]:
        """
        Returns an array of the segments defined in this segment table.
        @return an array of the segments defined in this segment table
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
    def segments(self) -> List[ghidra.app.util.bin.format.ne.Segment]: ...
