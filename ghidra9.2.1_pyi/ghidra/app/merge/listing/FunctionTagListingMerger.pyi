import ghidra.app.merge.listing
import ghidra.app.merge.tool
import ghidra.program.model.address
import ghidra.util.task
import java.lang


class FunctionTagListingMerger(ghidra.app.merge.listing.AbstractListingMerger):
    """
    Handles merging of function tags when they are added/removed from
     functions.

     Most merging can be done automatically; the exception being when a
     tag has been added to a function by one user, but deleted from the
     program by another.

     Note that there are other tag related conflict cases, but they are
     handled by the FunctionTagMerger, which handles all aspects of
     creation/deletion/editing of tags independent of functions.

     THIS CLASS ONLY DEALS WITH FUNCTION-RELATED ADDS/REMOVES.

     The specific cases handled by the class are described below:

      - X and Y are tags
      - ** indicates a conflict

     		User A	|	Add X	Add Y	Delete X	Delete Y
     				|
     User B		|
     -------------------------------------------------------
     Add X		|	X		X,Y			**			X
     				|
     Add Y		|	X,Y		Y			Y			**
     				|
     Delete X		|	**		Y			-			-
     				|
     Delete Y		|	X		**			-			-
    """





    def __init__(self, listingMergeMgr: ghidra.app.merge.listing.ListingMergeManager):
        """
        Constructor.
        @param listingMergeMgr the listing merge manager that owns this merger.
        """
        ...



    def apply(self) -> bool: ...

    def autoMerge(self, progressMin: int, progressMax: int, monitor: ghidra.util.task.TaskMonitor) -> None: ...

    def cancel(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getConflictCount(self, addr: ghidra.program.model.address.Address) -> int: ...

    def getConflictType(self) -> unicode: ...

    def getConflicts(self) -> ghidra.program.model.address.AddressSetView: ...

    def getNumConflictsResolved(self) -> int: ...

    def hasConflict(self, addr: ghidra.program.model.address.Address) -> bool: ...

    def hashCode(self) -> int: ...

    def init(self) -> None:
        """
        PUBLIC METHODS
        """
        ...

    def mergeConflicts(self, listingPanel: ghidra.app.merge.tool.ListingMergePanel, addr: ghidra.program.model.address.Address, chosenConflictOption: int, monitor: ghidra.util.task.TaskMonitor) -> None: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setConflictResolution(self, option: int) -> None:
        """
        Stores the users' selection for how to handle a conflict.
        @param option user option, from {@link ListingMergeConstants}
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def conflictResolution(self) -> None: ...  # No getter available.

    @conflictResolution.setter
    def conflictResolution(self, value: int) -> None: ...

    @property
    def conflictType(self) -> unicode: ...

    @property
    def conflicts(self) -> ghidra.program.model.address.AddressSetView: ...

    @property
    def numConflictsResolved(self) -> int: ...
