from typing import List
import ghidra.framework.options
import ghidra.program.model.address
import ghidra.program.model.listing
import ghidra.program.model.symbol
import ghidra.program.util
import java.lang


class EquateOperandFieldLocation(ghidra.program.util.OperandFieldLocation):
    """
    A simple version of OperandFieldLocation that allows us to store equate information.
    """





    @overload
    def __init__(self):
        """
        Default constructor needed for restoring
         an operand field location from XML.
        """
        ...

    @overload
    def __init__(self, program: ghidra.program.model.listing.Program, addr: ghidra.program.model.address.Address, refAddr: ghidra.program.model.address.Address, rep: unicode, equate: ghidra.program.model.symbol.Equate, opIndex: int, subOpIndex: int, charOffset: int):
        """
        @param program The program
        @param addr the address of the location
        @param refAddr the reference address.
        @param rep the representation of the equate location
        @param equate the equate object.
        @param opIndex the operand index
        @param subOpIndex the operand subOpIndex
        @param charOffset the character offset in to subOpPiece.
        """
        ...



    @overload
    def compareTo(self, other: ghidra.program.util.ProgramLocation) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def equals(self, obj: object) -> bool:
        """
        @see java.lang.Object#equals(java.lang.Object)
        """
        ...

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

    def getEquate(self) -> ghidra.program.model.symbol.Equate:
        """
        Returns the equate at this operand field location.
        @return equate
        """
        ...

    def getEquateValue(self) -> long: ...

    @staticmethod
    def getLocation(program: ghidra.program.model.listing.Program, saveState: ghidra.framework.options.SaveState) -> ghidra.program.util.ProgramLocation:
        """
        Get the program location for the given program and save state object.
        @param program the program for the location
        @param saveState the state to restore
        @return the restored program location
        """
        ...

    def getOperandIndex(self) -> int:
        """
        Returns the index of the operand at this location.
        """
        ...

    def getOperandRepresentation(self) -> unicode:
        """
        Returns a string representation of the opernand at this location.
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

    def getReferences(self) -> List[ghidra.program.model.symbol.EquateReference]: ...

    def getRow(self) -> int:
        """
        Returns the row within the program location.
        @return the row within the program location.
        """
        ...

    def getSubOperandIndex(self) -> int:
        """
        Returns the sub operand index at this location.
         This index can be used on the instruction.getOpObjects()
         to find the actual object (Address, Register, Scalar) the
         cursor is over.
        @return 0-n if over a valid OpObject, -1 otherwise
        """
        ...

    def getVariableOffset(self) -> ghidra.program.model.listing.VariableOffset:
        """
        Returns VariableOffset object if applicable or null
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
    def equate(self) -> ghidra.program.model.symbol.Equate: ...

    @property
    def equateValue(self) -> long: ...

    @property
    def references(self) -> List[ghidra.program.model.symbol.EquateReference]: ...
