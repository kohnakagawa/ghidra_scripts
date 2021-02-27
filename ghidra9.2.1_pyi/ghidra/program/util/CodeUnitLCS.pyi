from typing import List
import generic.algorithms
import ghidra.program.util
import ghidra.util.task
import java.lang


class CodeUnitLCS(generic.algorithms.Lcs):




    def __init__(self, __a0: List[object], __a1: List[object]): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @overload
    def getLcs(self) -> List[object]:
        """
        Returns a list of the longest common subsequence.  This result will be empty if the
         {@link #getSizeLimit()} has been reached.
        @return the list
        """
        ...

    @overload
    def getLcs(self, monitor: ghidra.util.task.TaskMonitor) -> List[object]:
        """
        Returns a list of the longest common subsequence. This result will be empty if the
         {@link #getSizeLimit()} has been reached.
        @param monitor the task monitor
        @return the LCS list
        @throws CancelledException if the monitor is cancelled
        """
        ...

    def getSizeLimit(self) -> int:
        """
        Returns the current size limit, past which no calculations will be performed
        @return the size limit
        @see #setSizeLimit(int)
        """
        ...

    def hashCode(self) -> int: ...

    @overload
    def matches(self, x: ghidra.program.util.CodeUnitContainer, y: ghidra.program.util.CodeUnitContainer) -> bool: ...

    @overload
    def matches(self, x: object, y: object) -> bool:
        """
        Returns true if the value of x and y match
        @param x the x-sequence element of interest
        @param y the y-sequence element of interest
        @return true if <code>x</code> matches <code>y</code>; false otherwise
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setSizeLimit(self, newLimit: int) -> None:
        """
        Changes the size limit of this LCS, past which no calculations will be performed
        @param newLimit the new limit
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
