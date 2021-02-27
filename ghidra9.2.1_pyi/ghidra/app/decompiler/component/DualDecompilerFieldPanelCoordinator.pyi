from typing import List
import docking.widgets.fieldpanel
import docking.widgets.fieldpanel.internal
import ghidra.program.util
import java.lang


class DualDecompilerFieldPanelCoordinator(docking.widgets.fieldpanel.internal.LineLockedFieldPanelCoordinator):




    def __init__(self, dualDecompilerPanel: ghidra.app.decompiler.component.DecompilerCodeComparisonPanel): ...



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
