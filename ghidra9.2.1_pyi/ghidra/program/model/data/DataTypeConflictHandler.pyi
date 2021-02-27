from typing import List
import ghidra.program.model.data
import ghidra.program.model.data.DataTypeConflictHandler
import java.lang


class DataTypeConflictHandler(object):
    DEFAULT_HANDLER: ghidra.program.model.data.DataTypeConflictHandler = ghidra.program.model.data.DataTypeConflictHandler$1@703e3d75
    KEEP_HANDLER: ghidra.program.model.data.DataTypeConflictHandler = ghidra.program.model.data.DataTypeConflictHandler$5@258d25b4
    REPLACE_EMPTY_STRUCTS_OR_RENAME_AND_ADD_HANDLER: ghidra.program.model.data.DataTypeConflictHandler = ghidra.program.model.data.DataTypeConflictHandler$6@557d74f
    REPLACE_HANDLER: ghidra.program.model.data.DataTypeConflictHandler




    class ConflictResult(java.lang.Enum):
        RENAME_AND_ADD: ghidra.program.model.data.DataTypeConflictHandler.ConflictResult = RENAME_AND_ADD
        REPLACE_EXISTING: ghidra.program.model.data.DataTypeConflictHandler.ConflictResult = REPLACE_EXISTING
        USE_EXISTING: ghidra.program.model.data.DataTypeConflictHandler.ConflictResult = USE_EXISTING







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
        def valueOf(__a0: unicode) -> ghidra.program.model.data.DataTypeConflictHandler.ConflictResult: ...

        @overload
        @staticmethod
        def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

        @staticmethod
        def values() -> List[ghidra.program.model.data.DataTypeConflictHandler.ConflictResult]: ...

        @overload
        def wait(self) -> None: ...

        @overload
        def wait(self, __a0: long) -> None: ...

        @overload
        def wait(self, __a0: long, __a1: int) -> None: ...






    class ConflictResolutionPolicy(java.lang.Enum):
        RENAME_AND_ADD: ghidra.program.model.data.DataTypeConflictHandler.ConflictResolutionPolicy = RENAME_AND_ADD
        REPLACE_EMPTY_STRUCTS_OR_RENAME_AND_ADD: ghidra.program.model.data.DataTypeConflictHandler.ConflictResolutionPolicy = REPLACE_EMPTY_STRUCTS_OR_RENAME_AND_ADD
        REPLACE_EXISTING: ghidra.program.model.data.DataTypeConflictHandler.ConflictResolutionPolicy = REPLACE_EXISTING
        USE_EXISTING: ghidra.program.model.data.DataTypeConflictHandler.ConflictResolutionPolicy = USE_EXISTING







        @overload
        def compareTo(self, __a0: java.lang.Enum) -> int: ...

        @overload
        def compareTo(self, __a0: object) -> int: ...

        def equals(self, __a0: object) -> bool: ...

        def getClass(self) -> java.lang.Class: ...

        def getDeclaringClass(self) -> java.lang.Class: ...

        def getHandler(self) -> ghidra.program.model.data.DataTypeConflictHandler: ...

        def hashCode(self) -> int: ...

        def name(self) -> unicode: ...

        def notify(self) -> None: ...

        def notifyAll(self) -> None: ...

        def ordinal(self) -> int: ...

        def toString(self) -> unicode: ...

        @overload
        @staticmethod
        def valueOf(__a0: unicode) -> ghidra.program.model.data.DataTypeConflictHandler.ConflictResolutionPolicy: ...

        @overload
        @staticmethod
        def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

        @staticmethod
        def values() -> List[ghidra.program.model.data.DataTypeConflictHandler.ConflictResolutionPolicy]: ...

        @overload
        def wait(self) -> None: ...

        @overload
        def wait(self, __a0: long) -> None: ...

        @overload
        def wait(self, __a0: long, __a1: int) -> None: ...

        @property
        def handler(self) -> ghidra.program.model.data.DataTypeConflictHandler: ...

    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getSubsequentHandler(self) -> ghidra.program.model.data.DataTypeConflictHandler:
        """
        Returns the appropriate handler for recursive resolve calls.
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def resolveConflict(self, addedDataType: ghidra.program.model.data.DataType, existingDataType: ghidra.program.model.data.DataType) -> ghidra.program.model.data.DataTypeConflictHandler.ConflictResult:
        """
        Callback to handle conflicts in a datatype manager when new datatypes are added that
         have the same name as an existing datatype. The implementer of this interface should do
         one of the following:
         		return the addedDataType - which means to replace the existingDataType with the addedDataType
         							(may throw exception if the datatypes are not compatible)
         		return the existingDataType the addedDataType will be ignored and the existing dataType will
         							be used.
         		return a new DataType with a new name/category
        @param addedDataType the datatype being added.
        @param existingDataType the datatype that exists with the same name/category as the one added
        @return an enum specify how to handle the conflict
        """
        ...

    def shouldUpdate(self, sourceDataType: ghidra.program.model.data.DataType, localDataType: ghidra.program.model.data.DataType) -> bool:
        """
        Callback invoked when an associated dataType is being resolved and its local version of the
         dataType is different from the source archive's dataType.  This method returns true if the
         local version should be updated to the archive's version of the dataType.  Otherwise, the
         local dataType will be used (without updating) in the resolve operation.
        @param sourceDataType
        @param localDataType
        @return true if the localDataType should be updated to be equivalent to the sourceDataType.
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
    def subsequentHandler(self) -> ghidra.program.model.data.DataTypeConflictHandler: ...
