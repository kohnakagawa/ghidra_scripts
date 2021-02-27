from typing import List
import ghidra.framework.options
import ghidra.program.model.address
import ghidra.program.model.listing
import ghidra.program.util
import java.lang


class MnemonicFieldLocation(ghidra.program.util.CodeUnitLocation):
    """
    The MnemonicFieldLocation class contains specific location
     information within the MNEMONIC field of a CodeUnitLocation object.
    """





    @overload
    def __init__(self):
        """
        Default constructor needed for restoring a mnemonic field location from
         XML.
        """
        ...

    @overload
    def __init__(self, program: ghidra.program.model.listing.Program, address: ghidra.program.model.address.Address):
        """
        @see ProgramLocation#ProgramLocation(Program, Address)
        """
        ...

    @overload
    def __init__(self, program: ghidra.program.model.listing.Program, addr: ghidra.program.model.address.Address, componentPath: List[int], mnemonicString: unicode, charOffset: int):
        """
        Construct a new MnemonicFieldLocation.
        @param program the program of the location
        @param addr address of the location; should not be null
        @param componentPath array of indexes for each nested data component; the
                    index is the data component's index within its parent; may be
                    null
        @param mnemonicString the mnemonic string
        @param charOffset the character position within the mnemonic string for
                    this location.
        """
        ...

    @overload
    def __init__(self, program: ghidra.program.model.listing.Program, addr: ghidra.program.model.address.Address, refAddr: ghidra.program.model.address.Address, componentPath: List[int], mnemonicString: unicode, charOffset: int):
        """
        Construct a new MnemonicFieldLocation.
        @param program the program of the location
        @param addr address of the location; should not be null
        @param refAddr the "referred to" address if the location is over a
                    reference; may be null
        @param componentPath array of indexes for each nested data component; the
                    index is the data component's index within its parent; may be
                    null
        @param mnemonicString the mnemonic string
        @param charOffset the character position within the mnemonic string for
                    this location.
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

    def getMnemonic(self) -> unicode:
        """
        Returns the mnemonic string at this location.
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
    def mnemonic(self) -> unicode: ...
