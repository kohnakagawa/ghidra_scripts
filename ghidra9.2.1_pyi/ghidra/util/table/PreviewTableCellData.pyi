import ghidra.program.util
import ghidra.util.table
import java.lang


class PreviewTableCellData(object, java.lang.Comparable):
    """
    A generic data type used by table models in order to signal that the data should render
     a preview for a given ProgramLocation, where the preview is what is displayed in
     the Listing.
    """





    def __init__(self, location: ghidra.program.util.ProgramLocation, codeUnitFormat: ghidra.program.model.listing.CodeUnitFormat):
        """
        Constructor
        @param location the location for the preview
        @param codeUnitFormat the format needed to render preview data
        """
        ...



    @overload
    def compareTo(self, data: ghidra.util.table.PreviewTableCellData) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDisplayString(self) -> unicode:
        """
        Get the preview for the code unit at or containing the address associated with this cell's row.
        @return the preview string.
        """
        ...

    def getHTMLDisplayString(self) -> unicode:
        """
        Get the preview as HTML for the code unit at or containing the address associated with this cell's row.
        @return the preview string.
        """
        ...

    def getProgramLocation(self) -> ghidra.program.util.ProgramLocation: ...

    def hashCode(self) -> int: ...

    def isOffcut(self) -> bool: ...

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
    def HTMLDisplayString(self) -> unicode: ...

    @property
    def displayString(self) -> unicode: ...

    @property
    def offcut(self) -> bool: ...

    @property
    def programLocation(self) -> ghidra.program.util.ProgramLocation: ...
