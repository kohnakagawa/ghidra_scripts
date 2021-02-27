from typing import List
import ghidra.app.merge
import ghidra.util.task
import java.lang


class PropertyListMergeManager(object, ghidra.app.merge.MergeResolver):
    """
    Manages options changes and conflicts between the latest versioned
     Program and the Program that is being checked into version control.
    """





    def __init__(self, mergeManager: ghidra.app.merge.ProgramMultiUserMergeManager, resultProgram: ghidra.program.model.listing.Program, myProgram: ghidra.program.model.listing.Program, originalProgram: ghidra.program.model.listing.Program, latestProgram: ghidra.program.model.listing.Program):
        """
        Construct a new PropertyListMergeManager.
        @param mergeManager manages each stage of the merge/resolve conflict process
        @param resultProgram latest version of the Program that is the
         destination for changes that will be applied from the source program
        @param myProgram source of changes to apply to the result
         program
        @param originalProgram program that was originally checked out
        @param latestProgram program that that is the latest version; the
         resultProgram and latestProgram start out the same
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
