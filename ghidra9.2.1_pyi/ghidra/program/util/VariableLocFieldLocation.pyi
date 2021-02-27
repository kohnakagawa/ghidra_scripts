from typing import List
import ghidra.framework.options
import ghidra.program.model.address
import ghidra.program.model.listing
import ghidra.program.util
import java.lang


class VariableLocFieldLocation(ghidra.program.util.VariableLocation):
    """
    The VariableLocFieldLocation class provides specific information
     about the stack variable offset field within a program location.
    """





    @overload
    def __init__(self):
        """
        Should only be used by XML restoration.
        """
        ...

    @overload
    def __init__(self, program: ghidra.program.model.listing.Program, var: ghidra.program.model.listing.Variable, charOffset: int):
        """
        Construct a new VariableLocFieldLocation object.
         Variable function entry point is the assumed listing location (i.e., referent code unit).
         Care should be taken if variable corresponds to an EXTERNAL function.
        @param program the program of the location
        @param var the variable which has its location (stack offset) in the field.
        @param charOffset the position within the variable location (stack offset) string for this location.
        """
        ...

    @overload
    def __init__(self, program: ghidra.program.model.listing.Program, locationAddr: ghidra.program.model.address.Address, var: ghidra.program.model.listing.Variable, charOffset: int):
        """
        Construct a new VariableLocFieldLocation object.
        @param program the program of the location
        @param locationAddr the address of the listing location (i.e., referent code unit)
        @param var the variable which has its location (stack offset) in the field.
        @param charOffset the position within the variable location (stack offset) string for this location.
        """
        ...



    @overload
    def compareTo(self, pl: ghidra.program.util.ProgramLocation) -> int: ...

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

    def getLoc(self) -> unicode:
        """
        Gets the location string. (For stack variables this is the offset as a string.)
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

    def getVariable(self) -> ghidra.program.model.listing.Variable:
        """
        Get the variable associated with this variable location
        @return associated function variable
        """
        ...

    def hashCode(self) -> int: ...

    def isLocationFor(self, var: ghidra.program.model.listing.Variable) -> bool:
        """
        Checks to see if this location is for the indicated variable.
        @param var the variable
        @return true if this location is for the specified variable.
        """
        ...

    def isParameter(self) -> bool: ...

    def isReturn(self) -> bool: ...

    def isValid(self, p: ghidra.program.model.listing.Program) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def restoreState(self, program1: ghidra.program.model.listing.Program, obj: ghidra.framework.options.SaveState) -> None: ...

    def saveState(self, obj: ghidra.framework.options.SaveState) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def loc(self) -> unicode: ...
