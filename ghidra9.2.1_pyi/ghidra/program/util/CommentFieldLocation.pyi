from typing import List
import ghidra.framework.options
import ghidra.program.model.address
import ghidra.program.model.listing
import ghidra.program.util
import java.lang


class CommentFieldLocation(ghidra.program.util.CodeUnitLocation):
    """
    The CommentFieldLocation class contains specific location information
     within the COMMENTS field of a CodeUnitLocation object.
    """





    @overload
    def __init__(self):
        """
        Default constructor needed for restoring
         a comment field location from XML.
        """
        ...

    @overload
    def __init__(self, program: ghidra.program.model.listing.Program, addr: ghidra.program.model.address.Address, componentPath: List[int], comment: List[unicode], type: int, row: int, charOffset: int):
        """
        Construct a new CommentFieldLocation.
        @param program the program of the location
        @param addr address of the location; should not be null
         hierarchy names; this parameter may be null
        @param componentPath if not null, it is the array of indexes that point
         to a specific data type inside of another data type
        @param comment The array of strings that make up the comment
        @param type The type of this comment.
                          Can be either CodeUnit.PRE_COMMENT, CodeUnit.POST_COMMENT,
                          CodeUnit.PLATE_COMMENT, CodeUnit.EOL_COMMENT, or CodeUnit.REPEATABLE_COMMENT.
        @param row The index of the string that contains the exact location.
        @param charOffset The position within the string that specifies the exact location.
        @exception IllegalArgumentException Thrown if type is not one of the comment values given in <CODE>CodeUnit</CODE>
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

    def toString(self) -> unicode:
        """
        Returns a String representation of this location.
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def comment(self) -> List[unicode]: ...

    @property
    def commentType(self) -> int: ...
