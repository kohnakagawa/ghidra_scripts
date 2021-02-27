from typing import List
import docking.widgets.fieldpanel
import docking.widgets.fieldpanel.internal
import ghidra.app.util.viewer.listingpanel
import ghidra.program.util
import java.lang


class ListingComparisonFieldPanelCoordinator(docking.widgets.fieldpanel.internal.LayoutLockedFieldPanelCoordinator, ghidra.app.util.viewer.listingpanel.DualListingFieldPanelCoordinator):
    """
    Coordinates cursor location and scrolling between the two sides of a ListingCodeComparisonPanel.
    """





    def __init__(self, dualListingPanel: ghidra.app.util.viewer.listingpanel.ListingCodeComparisonPanel):
        """
        Constructor for this dual listing field panel coordinator.
        @param dualListingPanel the dual listing to be controlled by this coordinator.
        """
        ...



    def add(self, fp: docking.widgets.fieldpanel.FieldPanel) -> None:
        """
        Adds the given field panel to the list of panels to coordinate.
        @param fp the field panel to add.
        """
        ...

    def dispose(self) -> None:
        """
        Cleans up resources.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def leftLocationChanged(self, leftLocation: ghidra.program.util.ProgramLocation) -> None: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def remove(self, fp: docking.widgets.fieldpanel.FieldPanel) -> None:
        """
        Removes the given field panel from the list of those to be coordinated.
        """
        ...

    def resetLockedLines(self) -> None:
        """
        Resets the locked line numbers for this field panel coordinator to their default
         of each being zero.
        """
        ...

    def rightLocationChanged(self, rightLocation: ghidra.program.util.ProgramLocation) -> None: ...

    def setCorrelation(self, addressCorrelation: ghidra.program.util.ListingAddressCorrelation) -> None:
        """
        Sets a new address correlation for associating addresses between the left and right sides.
         The field panels can then be coordinated by locking the layouts together whenever the
         current location on one side can be correlated with a location on the other side.
        @param addressCorrelation the correlation to use for locking the two sides together for
         scrolling.
        """
        ...

    def setLockedLines(self, lockedLineNumbers: List[long]) -> None:
        """
        Call this method whenever you want to change the line numbers that are locked together
         for the associated field panels.
        @param lockedLineNumbers the array of locked line numbers that are directly associated with
         the array of field panels.<BR>
         Important: Make sure the line numbers are in the order that matches the field panels in the array.
        """
        ...

    def toString(self) -> unicode: ...

    def viewChanged(self, fp: docking.widgets.fieldpanel.FieldPanel, index: long, xPos: int, yPos: int) -> None: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def correlation(self) -> None: ...  # No getter available.

    @correlation.setter
    def correlation(self, value: ghidra.program.util.ListingAddressCorrelation) -> None: ...
