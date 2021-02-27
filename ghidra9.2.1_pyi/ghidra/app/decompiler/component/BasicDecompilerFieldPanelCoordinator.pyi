from typing import List
import docking.widgets.fieldpanel
import ghidra.app.decompiler.component
import ghidra.program.util
import java.lang


class BasicDecompilerFieldPanelCoordinator(ghidra.app.decompiler.component.DualDecompilerFieldPanelCoordinator):
    """
    A basic coordinator that locks two decompiler panels together at the first line so that
     scrolling one side also scrolls the other. It also allows the cursor locations to track
     together based on the line number or to move independent of each other.
    """





    def __init__(self, dualDecompilerPanel: ghidra.app.decompiler.component.BasicDecompilerCodeComparisonPanel, syncLineLocation: bool):
        """
        Constructs a dual decompiler coordinator that scrolls the two panels together so that
         they are locked together at the first line.
        @param dualDecompilerPanel the dual decompiler panel being controlled by this coordinator
        @param syncLineLocation true means synchronize the cursors in the two decompiler panels
         to the same line number and offset if possible. false means the the cursors move
         independently of each other.
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

    def leftLocationChanged(self, leftProgramLocation: ghidra.program.util.ProgramLocation) -> None: ...

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

    def rightLocationChanged(self, rightProgramLocation: ghidra.program.util.ProgramLocation) -> None: ...

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
