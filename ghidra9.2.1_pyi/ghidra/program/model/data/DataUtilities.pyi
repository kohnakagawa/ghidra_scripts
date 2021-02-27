from typing import List
import ghidra.program.model.address
import ghidra.program.model.data
import ghidra.program.model.data.DataUtilities
import ghidra.program.model.listing
import ghidra.program.util
import java.lang


class DataUtilities(object):





    class ClearDataMode(java.lang.Enum):
        CHECK_FOR_SPACE: ghidra.program.model.data.DataUtilities.ClearDataMode = CHECK_FOR_SPACE
        CLEAR_ALL_CONFLICT_DATA: ghidra.program.model.data.DataUtilities.ClearDataMode = CLEAR_ALL_CONFLICT_DATA
        CLEAR_ALL_UNDEFINED_CONFLICT_DATA: ghidra.program.model.data.DataUtilities.ClearDataMode = CLEAR_ALL_UNDEFINED_CONFLICT_DATA
        CLEAR_SINGLE_DATA: ghidra.program.model.data.DataUtilities.ClearDataMode = CLEAR_SINGLE_DATA







        @overload
        def compareTo(self, __a0: java.lang.Enum) -> int: ...

        @overload
        def compareTo(self, __a0: object) -> int: ...

        def equals(self, __a0: object) -> bool: ...

        def getClass(self) -> java.lang.Class: ...

        def getDeclaringClass(self) -> java.lang.Class: ...

        def hashCode(self) -> int: ...

        def name(self) -> unicode: ...

        def notify(self) -> None: ...

        def notifyAll(self) -> None: ...

        def ordinal(self) -> int: ...

        def toString(self) -> unicode: ...

        @overload
        @staticmethod
        def valueOf(__a0: unicode) -> ghidra.program.model.data.DataUtilities.ClearDataMode: ...

        @overload
        @staticmethod
        def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

        @staticmethod
        def values() -> List[ghidra.program.model.data.DataUtilities.ClearDataMode]: ...

        @overload
        def wait(self) -> None: ...

        @overload
        def wait(self, __a0: long) -> None: ...

        @overload
        def wait(self, __a0: long, __a1: int) -> None: ...







    @staticmethod
    def createData(program: ghidra.program.model.listing.Program, addr: ghidra.program.model.address.Address, newDataType: ghidra.program.model.data.DataType, length: int, stackPointers: bool, clearMode: ghidra.program.model.data.DataUtilities.ClearDataMode) -> ghidra.program.model.listing.Data:
        """
        Create data where existing data may already exist.
        @param program
        @param addr data address (offcut data address only allowed if clearMode == ClearDataMode.CLEAR_ALL_CONFLICT_DATA)
        @param newDataType new data-type being applied
        @param length data length (used only for Dynamic newDataType which has canSpecifyLength()==true)
        @param stackPointers see {@link #reconcileAppliedDataType(DataType, DataType, boolean)}
        @param clearMode see CreateDataMode
        @return new data created
        @throws CodeUnitInsertionException if data creation failed
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    @staticmethod
    def findFirstConflictingAddress(program: ghidra.program.model.listing.Program, addr: ghidra.program.model.address.Address, length: int, ignoreUndefinedData: bool) -> ghidra.program.model.address.Address:
        """
        Finds the first conflicting address in the given address range.
        @param program The program.
        @param addr The starting address of the range.
        @param length The length of the range.
        @param ignoreUndefinedData True if the search should ignore {@link Undefined} data as a
           potential conflict, or false if {@link Undefined} data should trigger conflicts.
        @return The address of the first conflict in the range, or null if there were no conflicts.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getDataAtAddress(program: ghidra.program.model.listing.Program, address: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Data:
        """
        Get the data for the given address.
         <P>
         This will return a Data if and only if there is data that starts at the given address.
        @return the Data that starts at the given address or null if the address is code or offcut.
        """
        ...

    @staticmethod
    def getDataAtLocation(loc: ghidra.program.util.ProgramLocation) -> ghidra.program.model.listing.Data:
        """
        Get the data for the given address; if the code unit at the address is
         an instruction, return null.
        @param loc the location. This provides the address and subcomponent
         within the data at the address.
        @return the data or null if the code unit at the address is an instruction.
        """
        ...

    @staticmethod
    def getMaxAddressOfUndefinedRange(program: ghidra.program.model.listing.Program, addr: ghidra.program.model.address.Address) -> ghidra.program.model.address.Address:
        """
        Get the maximum address of an undefined data range starting at addr.
         Both undefined code units and defined data which have an Undefined
         data type are included in the range.
        @param program the program which will have its code units checked.
        @param addr the address where this will start checking for Undefined data. This address can
         be offcut into an Undefined Data.
        @return end of undefined range or null if addr does not correspond
         to an undefined location.
        """
        ...

    @staticmethod
    def getNextNonUndefinedDataAfter(program: ghidra.program.model.listing.Program, addr: ghidra.program.model.address.Address, maxAddr: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Data:
        """
        Get the next defined data that comes after the address indicated by addr and that is
         no more than the specified maxAddr and that is not a sized undefined data type.
        @param program the program whose code units are to be checked to find the next
         non-undefined data.
        @param addr start looking for data after this address.
        @param maxAddr do not look any further than this address.
        @return the next defined data that isn't a sized undefined data type, or return null if
         there isn't one.
        """
        ...

    def hashCode(self) -> int: ...

    @staticmethod
    def isUndefinedData(program: ghidra.program.model.listing.Program, addr: ghidra.program.model.address.Address) -> bool:
        """
        Determine if the specified addr corresponds to an undefined data location
         where both undefined code units and defined data which has an Undefined
         data type is considered to be undefined.
        @param program
        @param addr
        @return
        """
        ...

    @staticmethod
    def isUndefinedRange(program: ghidra.program.model.listing.Program, startAddress: ghidra.program.model.address.Address, endAddress: ghidra.program.model.address.Address) -> bool:
        """
        Determine if there is only undefined data from the specified startAddress to the specified
         endAddress. The start and end addresses must both be in the same defined block of memory.
        @param program the program whose code units are to be checked.
        @param startAddress start looking for undefined data at this address in a defined memory block.
        @param endAddress do not look any further than this address.
         This must be greater than or equal to the startAddress and must be in the same memory block
         as the start address or false is returned.
        @return true if the range of addresses in a memory block is where only undefined data exists.
        """
        ...

    @staticmethod
    def isValidDataTypeName(name: unicode) -> bool:
        """
        Determine if the specified name is a valid data-type name
        @param name candidate data-type name
        @return true if name is valid, else false
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def reconcileAppliedDataType(originalDataType: ghidra.program.model.data.DataType, newDataType: ghidra.program.model.data.DataType, stackPointers: bool) -> ghidra.program.model.data.DataType:
        """
        Determine the final data-type which should be applied based upon a
         user applied type of newDataType on an existing originalDataType.
         Pointer conversion is performed when appropriate, otherwise the
         newDataType is returned unchanged.
         If newDataType is a FunctionDefinition, or Typedef to a FunctionDefinition, it will either be stacked
         with the existing pointer if enabled/applicable, or will be converted to a pointer since
         FunctionDefinitions may only been used in the form of a pointer.
         Note that originalDataType and newDataType should be actual applied types.
         (i.e., do not strip typedefs, pointers, arrays, etc.).
        @param originalDataType existing data type onto which newDataTye is applied
        @param newDataType new data-type being applied
        @param stackPointers If true the following data type transformation will be performed:
         <ul>
         <li>If newDataType is a default pointer and the originalDataType
         is a pointer the new pointer will wrap
         the existing pointer thus increasing is 'depth'
         (e.g., int * would become int ** when default pointer applied).
         If the originalDataType is not a pointer the newDataType will be returned unchanged.
         </li>
         <li>If the originalDataType is any type of pointer the supplied newDatatype
         will replace the pointer's base type (e.g., int * would become db * when
         newDataType is {@link ByteDataType}).
         </ul>
         <P>If false, only required transformations will be applied, Example:
         if newDataType is a FunctionDefinitionDataType it will be transformed
         to a pointer before being applied.
        @return either a combined pointer data-type or the newDataType specified with any
         required transformation
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
