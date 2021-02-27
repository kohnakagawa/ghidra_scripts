from typing import List
import ghidra.program.model.listing
import ghidra.program.util
import java.lang


class ProgramTableModel(object):
    """
    An interface for translating table rows and columns
     into program locations and selections.
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getProgram(self) -> ghidra.program.model.listing.Program:
        """
        Returns the program associated with this ProgramTableModel.
        @return the program associated with this ProgramTableModel.
        """
        ...

    def getProgramLocation(self, row: int, column: int) -> ghidra.program.util.ProgramLocation:
        """
        Returns a program location corresponding the given row and column.
         Motivation:
         Given a table that has a column that contains addresses.
         If the user clicks on this column, then it would be nice
         to have the CodeBrowser navigate to this address.
        @param row the row
        @param column the column
        @return a program location corresponding the given row and column
        """
        ...

    def getProgramSelection(self, rows: List[int]) -> ghidra.program.util.ProgramSelection:
        """
        Returns a program selection corresponding to the
         specified row index array. This array will contain
         the currently selected rows.
        @param rows the currently selected rows.
        @return a program selection
        """
        ...

    def hashCode(self) -> int: ...

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
    def program(self) -> ghidra.program.model.listing.Program: ...
