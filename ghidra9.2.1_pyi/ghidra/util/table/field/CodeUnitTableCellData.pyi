from typing import List
import ghidra.util.table.field
import java.lang


class CodeUnitTableCellData(object, java.lang.Comparable):
    """
    A class that knows how to render CodeUnits in 1 or more lines
    """





    def __init__(self, location: ghidra.program.util.ProgramLocation, codeUnitFormat: ghidra.program.model.listing.CodeUnitFormat, codeUnitOffset: int, codeUnitCount: int):
        """
        Constructor
        @param location the location of the code unit to display
        @param codeUnitFormat the format needed to render the code unit
        @param codeUnitOffset relative code-unit offset from the specified address
         		   (this is not a byte-offset, it is expressed in terms of number of code-units).
        @param codeUnitCount number of code-units to be displayed
        """
        ...



    @overload
    def compareTo(self, data: ghidra.util.table.field.CodeUnitTableCellData) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDisplayString(self) -> unicode:
        """
        Get the visual representation for the code unit at or containing the address
         associated with this cell's row
        @return the display string
        """
        ...

    def getDisplayStrings(self) -> List[unicode]: ...

    def getHTMLDisplayString(self) -> unicode:
        """
        Get the visual representation as HTML for the code unit at or containing the
         address associated with this cell's row
        @return the display string
        """
        ...

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
    def displayStrings(self) -> List[object]: ...

    @property
    def offcut(self) -> bool: ...
