from typing import List
import ghidra.app.merge.listing
import ghidra.app.merge.tool
import ghidra.program.model.address
import ghidra.program.model.symbol
import ghidra.program.util
import ghidra.util.task
import java.lang


class ExternalFunctionMerger(ghidra.app.merge.listing.AbstractFunctionMerger, ghidra.app.merge.listing.ListingMerger):
    """
    Class for merging external function and label changes. This class can merge external function
     and label changes that were made to the checked out version. It can determine
     where there are conflicts between the latest checked in version and my
     checked out version. It can then allow the user to manually merge the conflicting
     functions and labels. External functions do not have bodies.
     However their signatures, stacks and variables do get merged.
     This class extends the AbstractFunctionMerger to handle merging of function changes when both
     My and Latest have changed functions.
     Note: Externals are uniquely identified by symbol ID and the name (including namespace is
     also used to match externals when the external is transitioned from a label to a function
     and vice versa.
     Important: This class is intended to be used only for a single program
     version merge. It should be constructed, followed by an autoMerge(), and lastly
     each external with a conflict should have mergeConflicts() called on it.
    """

    KEEP_BOTH_ADDS: int = 4
    KEEP_BOTH_BUTTON_NAME: unicode = u'KeepBothVersionsRB'
    KEEP_LATEST_ADD: int = 1
    KEEP_MY_ADD: int = 2
    MERGE_BOTH_ADDS: int = 8
    MERGE_BOTH_BUTTON_NAME: unicode = u'MergeBothVersionsRB'



    def __init__(self, listingMergeManager: ghidra.app.merge.listing.ListingMergeManager, showListingPanel: bool):
        """
        Manages changes and conflicts for externals between the latest versioned
         program and the modified program being checked into version control.
        @param listingMergeManager the top level merge manager for merging a program version.
        @param showListingPanel true to show the listing panel.
        """
        ...



    def allChoicesAreResolved(self) -> bool: ...

    def apply(self) -> bool: ...

    def autoMerge(self, progressMin: int, progressMax: int, monitor: ghidra.util.task.TaskMonitor) -> None: ...

    def cancel(self) -> None: ...

    def dispose(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getConflictCount(self, addr: ghidra.program.model.address.Address) -> int: ...

    def getConflictType(self) -> unicode: ...

    def getConflicts(self) -> ghidra.program.model.address.AddressSetView: ...

    def getDescription(self) -> unicode: ...

    def getName(self) -> unicode: ...

    def getNumConflictsResolved(self) -> int: ...

    def hasConflict(self, addr: ghidra.program.model.address.Address) -> bool: ...

    def hashCode(self) -> int: ...

    def init(self) -> None: ...

    @overload
    def mergeConflicts(self, chosenConflictOption: int, listingConflictInfoPanel: ghidra.app.merge.listing.ConflictInfoPanel, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Performs a manual merge of external program conflicts.
        @param chosenConflictOption ASK_USER means interactively resolve conflicts.
         JUnit testing also allows setting this to LATEST, MY, or ORIGINAL to force
         selection of a particular version change.
        @param monitor task monitor for informing the user of progress.
        @throws CancelledException if the user cancels the merge.
        """
        ...

    @overload
    def mergeConflicts(self, listingPanel: ghidra.app.merge.tool.ListingMergePanel, addr: ghidra.program.model.address.Address, conflictOption: int, monitor: ghidra.util.task.TaskMonitor) -> None: ...

    def mergeConflictsForAdd(self, externalLocations: List[ghidra.program.model.symbol.ExternalLocation], chosenConflictOption: int, monitor: ghidra.util.task.TaskMonitor) -> None: ...

    def mergeFunction(self, externalLocations: List[ghidra.program.model.symbol.ExternalLocation], currentChosenOption: int, monitor: ghidra.util.task.TaskMonitor) -> None: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def refreshResultPanel(self, externalLocations: List[ghidra.program.model.symbol.ExternalLocation]) -> None: ...

    def replaceExternalDataType(self, resultExternalLocation: ghidra.program.model.symbol.ExternalLocation, fromExternalLocation: ghidra.program.model.symbol.ExternalLocation, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        <CODE>replaceExternalDataType</CODE> replaces the data type of the
         external label in program1 with the data type of the external label in program2
         at the specified external space address.
        @param resultExternalLocation
        @param fromExternalLocation
        @param monitor the task monitor for notifying the user of this merge's progress.
        @throws CancelledException
        """
        ...

    def replaceExternalLocation(self, toExternalLocation: ghidra.program.model.symbol.ExternalLocation, fromExternalLocation: ghidra.program.model.symbol.ExternalLocation, programMerge: ghidra.program.util.ProgramMerge, monitor: ghidra.util.task.TaskMonitor) -> ghidra.program.model.symbol.ExternalLocation: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def conflictType(self) -> unicode: ...

    @property
    def conflicts(self) -> ghidra.program.model.address.AddressSetView: ...

    @property
    def description(self) -> unicode: ...

    @property
    def name(self) -> unicode: ...

    @property
    def numConflictsResolved(self) -> int: ...
