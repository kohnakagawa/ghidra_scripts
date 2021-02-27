from typing import List
import ghidra.framework.options
import ghidra.program.model.address
import ghidra.program.model.listing
import ghidra.program.util
import java.lang


class BytesFieldLocation(ghidra.program.util.CodeUnitLocation):
    """
    The BytesFieldLocation class provides specific information
      about the BYTES field within a program location.
    """





    @overload
    def __init__(self):
        """
        Default constructor needed for restoring
         a byte field location from XML.
        """
        ...

    @overload
    def __init__(self, program: ghidra.program.model.listing.Program, addr: ghidra.program.model.address.Address):
        """
        Creates a new BytesFieldLocation for the given address.
         The address will be adjusted to the beginning of the code unit containing
         that address(if it exists).  The original address can be retrieved using
         the "getByteAddress()" method.
        @param program the program that this location is related.
        @param addr the address of the byte for this location.
        """
        ...

    @overload
    def __init__(self, program: ghidra.program.model.listing.Program, addr: ghidra.program.model.address.Address, byteAddress: ghidra.program.model.address.Address, componentPath: List[int], columnInByte: int):
        """
        Create a new BytesFieldLocation which represents a specific byte address.
        @param program the program for this location.
        @param addr the address of the code unit containing this location.
        @param byteAddress the address of this location which can be the address of a specific
         byte within a code unit.
        @param componentPath the data component path which is specified as an array of indexes
         where each index indicates the index into nested structures. For instructions or
         simple data, this should be null.
        @param columnInByte the character position in the the bytes
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

    def getAddressForByte(self) -> ghidra.program.model.address.Address: ...

    def getByteAddress(self) -> ghidra.program.model.address.Address:
        """
        Returns the byte level address associated with this location.
        """
        ...

    def getByteIndex(self) -> int:
        """
        Returns the index of byte that represents the current program location.
         Sources that do not get this specific should simply return 0.
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
        This is overridden here because previous versions used to store the byte index in the
         column field.  So if anyone was incorrectly using getColumn() to get the byte index,
         then this override will allow that to keep working.
        """
        ...

    def getColumnInByte(self) -> int:
        """
        Returns the character position within the byte specified by getByteIndex().  Normally,
         this is 1,2, or 3 corresponding to before the byte, between the nibbles of the byte or
         past the byte.  Sometimes, extra delimiters may exist allowing the position to be
         greater than 3.
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

    def restoreState(self, program1: ghidra.program.model.listing.Program, obj: ghidra.framework.options.SaveState) -> None:
        """
        Restore this program location using the given program and save state object.
        @param program1 program to restore from
        @param obj the save state to restore from
        """
        ...

    def saveState(self, obj: ghidra.framework.options.SaveState) -> None:
        """
        Save this program location to the given save state object.
        @param obj the save state object for saving the location
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def addressForByte(self) -> ghidra.program.model.address.Address: ...

    @property
    def byteIndex(self) -> int: ...

    @property
    def column(self) -> int: ...

    @property
    def columnInByte(self) -> int: ...
