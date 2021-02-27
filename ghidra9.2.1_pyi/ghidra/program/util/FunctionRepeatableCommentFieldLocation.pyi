from typing import List
import ghidra.framework.options
import ghidra.program.model.address
import ghidra.program.model.listing
import ghidra.program.util
import java.lang


class FunctionRepeatableCommentFieldLocation(ghidra.program.util.FunctionLocation):
    """
    The FunctionRepeatableCommentFieldLocation class provides specific information
     about the Function Repeatable Comment field within a program location.
    """





    @overload
    def __init__(self):
        """
        Default constructor needed for restoring
         a program location from XML
        """
        ...

    @overload
    def __init__(self, program: ghidra.program.model.listing.Program, functionAddr: ghidra.program.model.address.Address, comment: List[unicode], row: int, col: int):
        """
        Construct a new FunctionRepeatableCommentFieldLocation object.
        @param program the program of the location
        @param functionAddr the function address (must not be an EXTERNAL function)
        @param comment the function comment array String at this location.
        @param row row number (index into the comment array)
        @param col character position within the comment, indexed by row
        """
        ...

    @overload
    def __init__(self, program: ghidra.program.model.listing.Program, locationAddr: ghidra.program.model.address.Address, functionAddr: ghidra.program.model.address.Address, comment: List[unicode], row: int, charOffset: int):
        """
        Construct a new FunctionRepeatableCommentFieldLocation object.
        @param program the program of the location
        @param locationAddr the address of the listing location (i.e., referent code unit)
        @param functionAddr the function address
        @param comment the function comment array String at this location.
        @param row row number (index into the comment array)
        @param charOffset character position within the comment, indexed by row
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
        Return the function comment string at this location.
        """
        ...

    def getComponentPath(self) -> List[int]:
        """
        Returns the componentPath for the {@link CodeUnit code unit}. Null will be returned if the
         object is an {@link Instruction} or a top-level {@link Data} object.
        """
        ...

    def getFunctionAddress(self) -> ghidra.program.model.address.Address:
        """
        Return the Function symbol address which may differ from the "location address" when
         a function is indirectly inferred via a reference.  WARNING: The {@link #getAddress()} should
         not be used to obtain the function address!
        @return the function address corresponding to this program location
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
    def comment(self) -> List[unicode]: ...
