from typing import List
import ghidra.framework.options
import ghidra.program.model.address
import ghidra.program.model.listing
import ghidra.program.util
import java.lang


class PlateFieldLocation(ghidra.program.util.CommentFieldLocation):
    """
    The PlateFieldLocation class contains specific location information
     within the Plate field of a CodeUnitLocation object.
    """





    @overload
    def __init__(self):
        """
        Default constructor needed for restoring
         a plate field location from XML.
        """
        ...

    @overload
    def __init__(self, program: ghidra.program.model.listing.Program, addr: ghidra.program.model.address.Address, componentPath: List[int], row: int, charOffset: int, comment: List[unicode], commentRow: int):
        """
        Construct a new PlateFieldLocation.
        @param program the program of the location
        @param addr the address of the code unit.
        @param componentPath the componentPath of the codeUnit
        @param row the line of the location
        @param charOffset the character position on the row of the location.
        @param comment plate comment text
        @param commentRow The row index into the comments of this location.  This is different
                than the <code>row</code> due to the fact that the PlateField has fictitious borders
                that don't exist in the actual comment.
        """
        ...



    @overload
    def compareTo(self, other: ghidra.program.util.ProgramLocation) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def equals(self, obj: object) -> bool: ...

    def getAddress(self) -> ghidra.program.model.address.Address:
        """
        Returns the address associated with this location.

         <p>
         Note: this may not be the same as the byte address. For example, in a {@link CodeUnit code
         unit} location this may be the minimum address of the code unit that contains the byte
         address.
        """
        ...

    def getByteAddress(self) -> ghidra.program.model.address.Address:
        """
        Returns the byte level address associated with this location.
        """
        ...

    def getCharOffset(self) -> int:
        """
        Returns the character offset in the display item at the (row,col)
        @return the character offset in the display item at the (row,col)
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getColumn(self) -> int:
        """
        Returns the column index of the display piece represented by this location. For most
         locations, there is only one display item per row, in which case this value will be 0.
        """
        ...

    def getComment(self) -> List[unicode]:
        """
        Returns the array of strings that make up the comment.
        """
        ...

    def getCommentRow(self) -> int:
        """
        Returns the index into the String[] returned by {@link #getComment()} that represents
         the comment row that was clicked.  <code>-1</code> will be returned if the border of the
         plate field was clicked.
         <p>
         <b>Note: </b> This value is different than that returned by {@link #getRow()}, as that
                 value represents the screen row clicked.  Further, the PlateField adds screen
                 decoration to the comments, which causes the screen row to differ from the comment
                 row.
        @return the index into the String[] returned by {@link #getComment()} that represents
         the comment row that was clicked.  <code>-1</code> will be returned if the border of the
         plate field was clicked.
        """
        ...

    def getCommentType(self) -> int:
        """
        Returns the comment type.  The type is either CodeUnit.EOL_COMMENT,
           CodeUnit.POST_COMMENT, CodeUnit.PLATE_COMMENT, CodeUnit.PRE_COMMENT,
           or CodeUnit.REPEATABLE_COMMENT.
        """
        ...

    def getComponentPath(self) -> List[int]:
        """
        Returns the componentPath for the {@link CodeUnit code unit}. Null will be returned if the
         object is an {@link Instruction} or a top-level {@link Data} object.
        """
        ...

    @staticmethod
    def getLocation(program: ghidra.program.model.listing.Program, saveState: ghidra.framework.options.SaveState) -> ghidra.program.util.ProgramLocation:
        """
        Get the program location for the given program and save state object.
        @param program the program for the location
        @param saveState the state to restore
        @return the restored program location
        """
        ...

    def getProgram(self) -> ghidra.program.model.listing.Program:
        """
        Returns the program associated with this location.
        """
        ...

    def getRefAddress(self) -> ghidra.program.model.address.Address:
        """
        Returns the "referred to" address if the location is over an address in some field.
        """
        ...

    def getRow(self) -> int:
        """
        Returns the row within the program location.
        @return the row within the program location.
        """
        ...

    def hashCode(self) -> int: ...

    def isValid(self, p: ghidra.program.model.listing.Program) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def restoreState(self, p: ghidra.program.model.listing.Program, obj: ghidra.framework.options.SaveState) -> None: ...

    def saveState(self, obj: ghidra.framework.options.SaveState) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def commentRow(self) -> int: ...
