from typing import List
import ghidra.framework.options
import ghidra.program.model.address
import ghidra.program.model.listing
import ghidra.program.util
import java.lang


class VariableXRefHeaderFieldLocation(ghidra.program.util.VariableXRefFieldLocation):




    @overload
    def __init__(self):
        """
        Should only be used for XML restoring.
        """
        ...

    @overload
    def __init__(self, program: ghidra.program.model.listing.Program, var: ghidra.program.model.listing.Variable, charOffset: int, refAddr: ghidra.program.model.address.Address):
        """
        Creates a variable xref field program location
        @param program the program of the location
        @param var the variable
        @param charOffset the character offset
        @param refAddr the xref address
        """
        ...



    @overload
    def compareTo(self, pl: ghidra.program.util.ProgramLocation) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def equals(self, object: object) -> bool: ...

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

    def getIndex(self) -> int:
        """
        Returns the index of the XREF in the list.
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

    def getReferenceAddress(self) -> ghidra.program.model.address.Address:
        """
        Returns the reference address at this location.
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
