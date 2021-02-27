from typing import List
import ghidra.framework.options
import ghidra.program.model.address
import ghidra.program.model.listing
import ghidra.program.util
import java.lang


class FunctionParameterNameFieldLocation(ghidra.program.util.FunctionParameterFieldLocation):
    """
    A FunctionSignatureFieldLocation that indicates the user clicked on a function
     parameter name.
    """





    @overload
    def __init__(self):
        """
        Default constructor needed for restoring
         a program location from XML
        """
        ...

    @overload
    def __init__(self, program: ghidra.program.model.listing.Program, locationAddr: ghidra.program.model.address.Address, functionAddr: ghidra.program.model.address.Address, charOffset: int, signature: unicode, parameter: ghidra.program.model.listing.Parameter):
        """
        Construct a new FunctionParameterNameFieldLocation object.
        @param program the program of the location
        @param locationAddr the address of the listing location (i.e., referent code unit)
        @param functionAddr the function address
        @param charOffset the position within the function signature string for this location.
        @param signature the function signature string at this location.
        @param parameter the function parameter at this location.
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

    def getOrdinal(self) -> int: ...

    def getParameter(self) -> ghidra.program.model.listing.Parameter:
        """
        Returns the parameter associated with this location.  This value can be null if the
         parameters are deleted from the function associated with the address of the parameter.
        @return the parameter
        """
        ...

    def getParameterName(self) -> unicode: ...

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

    def getSignature(self) -> unicode:
        """
        Return the function signature string at this location.
        """
        ...

    def hashCode(self) -> int: ...

    def isFieldBasedPositioning(self) -> bool: ...

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
    def parameterName(self) -> unicode: ...
