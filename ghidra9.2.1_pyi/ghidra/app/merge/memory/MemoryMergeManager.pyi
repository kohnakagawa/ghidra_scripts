from typing import List
import ghidra.app.merge
import ghidra.util.task
import java.lang


class MemoryMergeManager(object, ghidra.app.merge.MergeResolver):
    """
    Merge memory blocks that have changes to the name, permissions or comments.
    """





    def __init__(self, mergeManager: ghidra.app.merge.ProgramMultiUserMergeManager, resultProgram: ghidra.program.model.listing.Program, myProgram: ghidra.program.model.listing.Program, originalProgram: ghidra.program.model.listing.Program, latestProgram: ghidra.program.model.listing.Program):
        """
        Constructor
        @param mergeManager merge manager
        @param resultProgram program where changes will be applied to
        @param myProgram source program with changes that will be applied to
         result program
        @param originalProgram original program that was checked out
        @param latestProgram latest program that was checked in; the result
         program and latest program are initially identical
        """
        ...



    def apply(self) -> None: ...

    def cancel(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDescription(self) -> unicode: ...

    def getName(self) -> unicode: ...

    def getPhases(self) -> List[unicode]: ...

    def hashCode(self) -> int: ...

    def merge(self, monitor: ghidra.util.task.TaskMonitor) -> None: ...

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
    def description(self) -> unicode: ...

    @property
    def name(self) -> unicode: ...

    @property
    def phases(self) -> List[unicode]: ...
