from typing import List
import ghidra.program.model.address
import ghidra.program.model.data
import ghidra.program.model.listing
import ghidra.program.model.mem
import java.lang


class MSDataTypeUtils(object):
    """
    An abstract class containing static utility methods for creating structure data types.
    """









    def equals(self, __a0: object) -> bool: ...

    @staticmethod
    def getAbsoluteAddress(program: ghidra.program.model.listing.Program, address: ghidra.program.model.address.Address) -> ghidra.program.model.address.Address:
        """
        Extracts an absolute address from the bytes in memory at the indicated address in memory.
        @param program the program containing the bytes
        @param address the address in memory where the address bytes should be obtained.
        @return the absolute address or null if the address isn't in the program's memory.
        """
        ...

    @staticmethod
    def getAlignedPack4Structure(dataTypeManager: ghidra.program.model.data.DataTypeManager, categoryPath: ghidra.program.model.data.CategoryPath, structureName: unicode) -> ghidra.program.model.data.StructureDataType:
        """
        Gets an empty aligned structure with a packing value of 4 that can be use to create the
         model's data type.
        @param dataTypeManager the data type manager to associate with the structure.
        @param categoryPath the structure's category path.
        @param structureName the structure's name.
        @return the aligned pack(4) structure.
        """
        ...

    @staticmethod
    def getAlignedPack8Structure(dataTypeManager: ghidra.program.model.data.DataTypeManager, categoryPath: ghidra.program.model.data.CategoryPath, structureName: unicode) -> ghidra.program.model.data.StructureDataType:
        """
        Gets an empty aligned structure with a packing value of 8 that can be use to create the
         model's data type.
        @param dataTypeManager the data type manager to associate with the structure.
        @param categoryPath the structure's category path.
        @param structureName the structure's name.
        @return the aligned pack(8) structure.
        """
        ...

    @staticmethod
    def getBytes(memory: ghidra.program.model.mem.Memory, startAddress: ghidra.program.model.address.Address, length: int) -> List[int]:
        """
        Gets bytes from <code>memory</code> at the indicated <code>startAddress</code>.
         The <code>length</code> indicates the number of bytes that must be read
         from memory.
        @param memory the program memory for obtaining the bytes
        @param startAddress the address to begin reading bytes
        @param length the number of bytes to read
        @return the bytes
        @throws InvalidDataTypeException if the <code>length</code> number of bytes couldn't
         be read starting at the <code>startAddress</code> in <code>memory</code>.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getEHStateDataType(program: ghidra.program.model.listing.Program) -> ghidra.program.model.data.DataType:
        """
        Gets an exception handling state data type.
        @param program the program for the data type.
        @return the exception handling state data type.
        """
        ...

    @staticmethod
    def getMatchingDataType(program: ghidra.program.model.listing.Program, comparisonDt: ghidra.program.model.data.DataType) -> ghidra.program.model.data.DataType:
        """
        Gets the named data type from the program or the windows data type archive. If neither
         the program or data type archive has an equivalent data type then the original data type
         is returned.
        @param program the program for the data type.
        @param comparisonDt the data type it should match
        @return the matching data type
        """
        ...

    @staticmethod
    def getPMDDataType(program: ghidra.program.model.listing.Program) -> ghidra.program.model.data.Structure:
        """
        Gets a PMD displacement structure data type.
        @param program the program for the data type.
        @return the PMD data type or null.
        """
        ...

    @staticmethod
    def getPointerDisplacementDataType(program: ghidra.program.model.listing.Program) -> ghidra.program.model.data.DataType:
        """
        Gets a pointer displacement data type.
        @param program the program for the data type.
        @return the pointer displacement data type.
        """
        ...

    @staticmethod
    def getReferenceDataType(program: ghidra.program.model.listing.Program, referredToDataType: ghidra.program.model.data.DataType) -> ghidra.program.model.data.DataType:
        """
        Gets the appropriate reference data type. If program is 64 bit, then a 32-bit image
         base offset data type will be returned. Otherwise, a default pointer to the
         referredToDataType will be returned.
        @param program the program that will contain the returned data type
        @param referredToDataType the data type that is at the address being referred to by the
         pointer or image base offset. Otherwise, null.
        @return the image base offset or pointer reference data type
        """
        ...

    @staticmethod
    def getReferencedAddress(program: ghidra.program.model.listing.Program, address: ghidra.program.model.address.Address) -> ghidra.program.model.address.Address:
        """
        Gets the referred to address from the bytes in the program at the indicated address.
         If the program has 64 bit pointers, then a 32 bit image base offset value is expected to
         be found at the indicated address.
         If the program has 32 bit pointers, then a 32 bit absolute pointer value is expected at the
         indicated address.
        @param program the program whose memory is to be read.
        @param address the address to start reading the bytes for the referenced address.
        @return the referred to address or null.
        """
        ...

    def hashCode(self) -> int: ...

    @staticmethod
    def is64Bit(program: ghidra.program.model.listing.Program) -> bool:
        """
        Determines if the indicated program appears to be 64 bit (has 64 bit pointers).
        @param program the program
        @return true if 64 bit.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
