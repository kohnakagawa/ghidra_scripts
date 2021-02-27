from typing import List
import ghidra.framework.options
import ghidra.program.model.address
import ghidra.program.model.listing
import ghidra.program.util
import java.lang


class ArrayElementFieldLocation(ghidra.program.util.OperandFieldLocation):




    @overload
    def __init__(self):
        """
        Default constructor needed for restoring from XML.
        """
        ...

    @overload
    def __init__(self, program: ghidra.program.model.listing.Program, address: ghidra.program.model.address.Address, componentPath: List[int], displayValue: unicode, elementIndex: int, charOffset: int):
        """
        Creates an ArrayElementFieldLocation
        @param program the program
        @param address the address of the location
        @param componentPath the data component path
        @param displayValue the text being displayed in the text.
        @param elementIndex the element of the array on the line.
        @param charOffset the character position within the text.
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

    def getElementIndexOnLine(self, firstDataOnLine: ghidra.program.model.listing.Data) -> int: ...

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
