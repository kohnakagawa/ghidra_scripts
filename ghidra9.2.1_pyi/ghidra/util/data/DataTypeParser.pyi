from typing import List
import ghidra.program.model.data
import ghidra.util.data
import ghidra.util.data.DataTypeParser
import java.lang


class DataTypeParser(object):





    class AllowedDataTypes(java.lang.Enum):
        ALL: ghidra.util.data.DataTypeParser.AllowedDataTypes = ALL
        BITFIELD_BASE_TYPE: ghidra.util.data.DataTypeParser.AllowedDataTypes = BITFIELD_BASE_TYPE
        DYNAMIC: ghidra.util.data.DataTypeParser.AllowedDataTypes = DYNAMIC
        FIXED_LENGTH: ghidra.util.data.DataTypeParser.AllowedDataTypes = FIXED_LENGTH
        SIZABLE_DYNAMIC: ghidra.util.data.DataTypeParser.AllowedDataTypes = SIZABLE_DYNAMIC
        SIZABLE_DYNAMIC_AND_BITFIELD: ghidra.util.data.DataTypeParser.AllowedDataTypes = SIZABLE_DYNAMIC_AND_BITFIELD
        STRINGS_AND_FIXED_LENGTH: ghidra.util.data.DataTypeParser.AllowedDataTypes = STRINGS_AND_FIXED_LENGTH







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
        def valueOf(__a0: unicode) -> ghidra.util.data.DataTypeParser.AllowedDataTypes: ...

        @overload
        @staticmethod
        def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

        @staticmethod
        def values() -> List[ghidra.util.data.DataTypeParser.AllowedDataTypes]: ...

        @overload
        def wait(self) -> None: ...

        @overload
        def wait(self, __a0: long) -> None: ...

        @overload
        def wait(self, __a0: long, __a1: int) -> None: ...



    @overload
    def __init__(self, dataTypeManagerService: ghidra.app.services.DataTypeQueryService, allowedTypes: ghidra.util.data.DataTypeParser.AllowedDataTypes):
        """
        A constructor that does not use the source or destination data type managers.  In terms of
         the source data type manager, this means that all data type managers will be used when
         resolving data types.
        @param dataTypeManagerService
        @param allowedTypes
        """
        ...

    @overload
    def __init__(self, sourceDataTypeManager: ghidra.program.model.data.DataTypeManager, destinationDataTypeManager: ghidra.program.model.data.DataTypeManager, dataTypeManagerService: ghidra.app.services.DataTypeQueryService, allowedTypes: ghidra.util.data.DataTypeParser.AllowedDataTypes):
        """
        Constructor
        @param sourceDataTypeManager preferred source data-type manager, or null
        @param destinationDataTypeManager target data-type manager, or null
        @param dataTypeManagerService data-type manager tool service, or null
        @param allowedTypes constrains which data-types may be parsed
        @see #DataTypeParser(DataTypeQueryService, AllowedDataTypes)
        """
        ...



    @staticmethod
    def ensureIsAllowableType(dt: ghidra.program.model.data.DataType, allowedTypes: ghidra.util.data.DataTypeParser.AllowedDataTypes) -> None:
        """
        Throws exception if the data type does not match the specified {@link AllowedDataTypes}.
        @param dt {@link DataType} to check
        @param allowedTypes {@link AllowedDataTypes enum} specifying what category of data types are ok
        @throws InvalidDataTypeException if dt violates the specified allowedTypes
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @overload
    def parse(self, dataTypeString: unicode) -> ghidra.program.model.data.DataType:
        """
        Parse a data-type string specification
        @param dataTypeString a known data-type name followed by zero or more pointer/array decorations.
        @return parsed data-type or null if not found
        @throws InvalidDataTypeException if data-type string is invalid or length exceeds specified maxSize
        @throws CancelledException parse cancelled through user interaction
        """
        ...

    @overload
    def parse(self, dataTypeString: unicode, category: ghidra.program.model.data.CategoryPath) -> ghidra.program.model.data.DataType:
        """
        Parse a data-type string specification with category path.  If category is not null,
         the dataTypeManagerService will not be queried.
        @param dataTypeString a known data-type name followed by zero or more pointer/array decorations.
        @param category known path of data-type or null if unknown
        @return parsed data-type or null if not found
        @throws InvalidDataTypeException if data-type string is invalid or length exceeds specified maxSize
        @throws CancelledException parse cancelled through user interaction (only if parser contructed with service)
        """
        ...

    @overload
    def parse(self, dataTypeString: unicode, suggestedBaseDataType: ghidra.program.model.data.DataType) -> ghidra.program.model.data.DataType:
        """
        Parse a data-type string specification using the specified baseDatatype.
        @param suggestedBaseDataType base data-type (may be null), this will be used as the base data-type if
         its name matches the base name in the specified dataTypeString.
        @param dataTypeString a base data-type followed by a sequence of zero or more pointer/array decorations to be applied.
         The string may start with the baseDataType's name.
        @return parsed data-type or null if not found
        @throws InvalidDataTypeException if data-type string is invalid or length exceeds specified maxSize
        @throws CancelledException parse cancelled through user interaction (only if parser contructed with service)
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
