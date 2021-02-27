from typing import List
import docking.action
import java.lang


class ListingDiffActionManager(object):
    """
    Manages the actions that control a ListingDiff.
    """





    def __init__(self, listingDiff: ghidra.program.util.ListingDiff):
        """
        Constructor for the action manager for a ListingDiff.
        @param listingDiff the ListingDiff that is controlled by this manager's docking actions.
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getActions(self) -> List[docking.action.DockingAction]:
        """
        Gets the actions.
        @return the docking actions.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    def updateActionEnablement(self, isShowing: bool) -> None:
        """
        Update the enablement of the actions created by this manager.
        @param isShowing true indicates that the dual listing diff is currently visible on screen.
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def actions(self) -> List[docking.action.DockingAction]: ...
