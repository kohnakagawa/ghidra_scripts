from typing import List
import generic.stl
import ghidra.program.model.listing
import java.lang


class VariableStorageConflicts(object):




    def __init__(self, __a0: List[object], __a1: List[object], __a2: bool, __a3: ghidra.util.task.TaskMonitor): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getOverlappingVariables(self) -> List[generic.stl.Pair]: ...

    def hasOverlapConflict(self) -> bool: ...

    def hasParameterConflict(self) -> bool: ...

    def hashCode(self) -> int: ...

    def isConflicted(self, var1: ghidra.program.model.listing.Variable, var2: ghidra.program.model.listing.Variable) -> bool:
        """
        Check to see if either var1 or var2 is contained within the conflicted/overlapping
         set of variables.  In general, one of the specified variables should be null.
        @param var1 a variable which corresponds to function1 at time of construction or null
        @param var2 a variable which corresponds to function2 at time of construction or null
        @return true if either variable is contained within the conflicted/overlapping
         set of variables.
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

    @property
    def overlappingVariables(self) -> List[object]: ...
