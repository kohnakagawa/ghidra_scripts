from typing import List
import ghidra.framework.options
import ghidra.program.model.address
import ghidra.program.model.listing
import ghidra.program.util
import java.lang


class ProgramLocation(object, java.lang.Comparable):
    """
    ProgramLocation provides information about a location in a program in the most
     generic way.


     ProgramLocations refer to a specific location in a program and can be specified down to an
     address, a field at that address, and within that field, a row, col, and character offset. The
     field is not recorded directly, but by the subclass of the ProgramLocation. The "cursor position"
     within a field is specified by three variables: row, col, and character offset. The row is
     literally the row (line #) the cursor is on within the field, the column represents the display
     item on that row (For example, in the bytes field the column will represent which "byte" the
     cursor is on. Most fields only have one column item per row.) And finally, the character offset
     is the character position within the display item specified by the row and column. Simple fields
     like the address field and Mnemonic field will always have a row and column of 0.
    """





    @overload
    def __init__(self):
        """
        Default constructor required for restoring a program location from XML.
        """
        ...

    @overload
    def __init__(self, program: ghidra.program.model.listing.Program, addr: ghidra.program.model.address.Address):
        """
        Construct a new ProgramLocation for the given address. The address will be adjusted to the
         beginning of the {@link CodeUnit code unit} containing that address (if it exists). The
         original address can be retrieved using the {@link #getByteAddress()} method.
        @param program the program associated with this program location (also used to obtain a
                    code-unit-aligned address)
        @param addr address for the location
        @throws NullPointerException if {@code addr} or {@code program} is null
        """
        ...

    @overload
    def __init__(self, program: ghidra.program.model.listing.Program, addr: ghidra.program.model.address.Address, refAddr: ghidra.program.model.address.Address):
        """
        Construct a new ProgramLocation for the given address. The address will be adjusted to the
         beginning of the {@link CodeUnit code unit} containing that address (if it exists). The
         original address can be retrieved using the {@link #getByteAddress()} method.
        @param program the program associated with this program location (also used to obtain a
                    code-unit-aligned address)
        @param addr address for the location
        @param refAddr the "referred to" address if the location is over a reference
        @throws NullPointerException if {@code addr} or {@code program} is null
        """
        ...

    @overload
    def __init__(self, program: ghidra.program.model.listing.Program, addr: ghidra.program.model.address.Address, row: int, col: int, charOffset: int):
        """
        Construct a new ProgramLocation for the given address. The address will be adjusted to the
         beginning of the {@link CodeUnit code unit} containing that address (if it exists). The
         original address can be retrieved using the {@link #getByteAddress()} method.
        @param program the program associated with this program location (also used to obtain a
                    code-unit-aligned address)
        @param addr address for the location
        @param row the row within the field.
        @param col the display item index on the given row. (Note most fields only have one display
                    item per row)
        @param charOffset the character offset within the display item.
        @throws NullPointerException if {@code addr} or {@code program} is null
        """
        ...

    @overload
    def __init__(self, program: ghidra.program.model.listing.Program, addr: ghidra.program.model.address.Address, componentPath: List[int], refAddr: ghidra.program.model.address.Address, row: int, col: int, charOffset: int):
        """
        Construct a new ProgramLocation for the given address. The address will be adjusted to the
         beginning of the {@link CodeUnit code unit} containing that address (if it exists). The
         original address can be retrieved using the {@link #getByteAddress()}" method.
        @param program the program associated with this program location (also used to obtain a
                    code-unit-aligned address)
        @param addr address of the location; cannot be null
        @param componentPath array of indexes for each nested data component; the index is the data
                    component's index within its parent; may be null
        @param refAddr the "referred to" address if the location is over a reference; may be null
        @param row the row within the field.
        @param col the display item index on the given row. (Note most fields only have one display
                    item per row)
        @param charOffset the character offset within the display item.
        @throws NullPointerException if {@code addr} or {@code program} is null
        """
        ...

    @overload
    def __init__(self, program: ghidra.program.model.listing.Program, addr: ghidra.program.model.address.Address, byteAddr: ghidra.program.model.address.Address, componentPath: List[int], refAddr: ghidra.program.model.address.Address, row: int, col: int, charOffset: int):
        """
        Construct a new ProgramLocation.
        @param program the program of the location
        @param addr address of the location; cannot be null; This could be a code unit minimum
                    address where the byteAddr is within the code unit.
        @param byteAddr address of the location; cannot be null
        @param componentPath array of indexes for each nested data component; the data index is the
                    data component's index within its parent; may be null
        @param refAddr the "referred to" address if the location is over a reference; may be null
        @param row the row within the field.
        @param col the display item index on the given row. (Note most fields only have one display
                    item per row)
        @param charOffset the character offset within the display item.
        @throws NullPointerException if {@code addr} or {@code program} is null
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

    def isValid(self, testProgram: ghidra.program.model.listing.Program) -> bool:
        """
        Returns true if this location represents a valid location in the given program
        @param testProgram the program to test if this location is valid.
        @return true if this location represents a valid location in the given program
        """
        ...

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
    def address(self) -> ghidra.program.model.address.Address: ...

    @property
    def byteAddress(self) -> ghidra.program.model.address.Address: ...

    @property
    def charOffset(self) -> int: ...

    @property
    def column(self) -> int: ...

    @property
    def componentPath(self) -> List[int]: ...

    @property
    def program(self) -> ghidra.program.model.listing.Program: ...

    @property
    def refAddress(self) -> ghidra.program.model.address.Address: ...

    @property
    def row(self) -> int: ...
