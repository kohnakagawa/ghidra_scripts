from typing import List
import ghidra.docking.settings
import ghidra.program.model.data
import ghidra.program.model.mem
import ghidra.util
import java.lang
import java.net


class BitFieldDataType(ghidra.program.model.data.AbstractDataType):
    """
    BitFieldDataType provides a means of defining a minimally sized bit-field
     for use within data structures.  The length (i.e., storage size) of this bitfield datatype is
     the minimum number of bytes required to contain the bitfield at its specified offset.
     The effective bit-size of a bitfield will be limited by the size of the base
     datatype whose size may be controlled by its associated datatype manager and data organization
     (e.g., IntegerDataType).

     NOTE: Instantiation of this datatype implementation is intended for internal use only.
     Creating and manipulating bitfields should be accomplished directly via Structure or Union
     bitfield methods.
    """









    def addParent(self, dt: ghidra.program.model.data.DataType) -> None: ...

    @staticmethod
    def checkBaseDataType(baseDataType: ghidra.program.model.data.DataType) -> None:
        """
        Check a bitfield base datatype
        @param baseDataType bitfield base data type (Enum, AbstractIntegerDataType and derived TypeDefs permitted)
        @throws InvalidDataTypeException if baseDataType is invalid as a bitfield base type.
        """
        ...

    def clone(self, dtm: ghidra.program.model.data.DataTypeManager) -> ghidra.program.model.data.BitFieldDataType:
        """
        Clone this bitfield to a new datatype manager.  This may change the effective bit
         size and storage size of the resulting datatype based upon the data organization
         of the specified dtm.
        @param dtm target datatype manager
        @return new instance or same instance of dtm is unchanged.
        """
        ...

    def copy(self, dtm: ghidra.program.model.data.DataTypeManager) -> ghidra.program.model.data.DataType:
        """
        Returns a clone of this built-in DataType
        @see ghidra.program.model.data.DataType#copy(ghidra.program.model.data.DataTypeManager)
        """
        ...

    def dataTypeDeleted(self, dt: ghidra.program.model.data.DataType) -> None: ...

    def dataTypeNameChanged(self, dt: ghidra.program.model.data.DataType, oldName: unicode) -> None: ...

    def dataTypeReplaced(self, oldDt: ghidra.program.model.data.DataType, newDt: ghidra.program.model.data.DataType) -> None: ...

    def dataTypeSizeChanged(self, dt: ghidra.program.model.data.DataType) -> None: ...

    def dependsOn(self, dt: ghidra.program.model.data.DataType) -> bool: ...

    def equals(self, obj: object) -> bool: ...

    def getAlignment(self) -> int: ...

    def getBaseDataType(self) -> ghidra.program.model.data.DataType:
        """
        Get the base datatype associated with this bit-field
         (e.g., int, long, etc., or TypeDef to supported base type)
        @return base data type
        """
        ...

    def getBaseTypeSize(self) -> int:
        """
        Get the size of the base data type based upon the associated data organization.
        @return base type size
        """
        ...

    def getBitOffset(self) -> int:
        """
        Get the bit offset of the least-significant bit relative to bit-0 of the
         base datatype (i.e., least significant bit).  This corresponds to the
         right-shift amount within the base data type when viewed as a big-endian value.
        @return bit offset
        """
        ...

    def getBitSize(self) -> int:
        """
        Get the effective bit size of this bit-field which may not exceed the size of the
         base datatype.
        @return bit size
        """
        ...

    def getCategoryPath(self) -> ghidra.program.model.data.CategoryPath: ...

    def getClass(self) -> java.lang.Class: ...

    def getDataOrganization(self) -> ghidra.program.model.data.DataOrganization: ...

    def getDataTypeManager(self) -> ghidra.program.model.data.DataTypeManager:
        """
        @see ghidra.program.model.data.DataType#getDataTypeManager()
        """
        ...

    def getDataTypePath(self) -> ghidra.program.model.data.DataTypePath: ...

    def getDeclaredBitSize(self) -> int:
        """
        Get the declared bit size of this bit-field which may be larger than the effective
         size which could be truncated.
        @return bit size as defined by the field construction/declaration.
        """
        ...

    def getDefaultAbbreviatedLabelPrefix(self) -> unicode: ...

    @overload
    def getDefaultLabelPrefix(self) -> unicode: ...

    @overload
    def getDefaultLabelPrefix(self, buf: ghidra.program.model.mem.MemBuffer, settings: ghidra.docking.settings.Settings, len: int, options: ghidra.program.model.data.DataTypeDisplayOptions) -> unicode: ...

    def getDefaultOffcutLabelPrefix(self, buf: ghidra.program.model.mem.MemBuffer, settings: ghidra.docking.settings.Settings, len: int, options: ghidra.program.model.data.DataTypeDisplayOptions, offcutLength: int) -> unicode: ...

    def getDefaultSettings(self) -> ghidra.docking.settings.Settings: ...

    def getDescription(self) -> unicode: ...

    def getDisplayName(self) -> unicode: ...

    def getDocs(self) -> java.net.URL: ...

    @staticmethod
    def getEffectiveBitSize(declaredBitSize: int, baseTypeByteSize: int) -> int:
        """
        Get the effective bit-size based upon the specified base type size.  A bit size
         larger than the base type size will truncated to the base type size.
        @param declaredBitSize
        @param baseTypeByteSize
        @return effective bit-size
        """
        ...

    def getLastChangeTime(self) -> long: ...

    def getLastChangeTimeInSourceArchive(self) -> long: ...

    def getLength(self) -> int: ...

    @overload
    @staticmethod
    def getMinimumStorageSize(bitSize: int) -> int:
        """
        Get the minimum storage size in bytes for a given size in bits.
         This does not consider the bit offset which may increase the required
         storage.
        @param bitSize number of bits within bitfield
        @return minimum storage size in bytes
        """
        ...

    @overload
    @staticmethod
    def getMinimumStorageSize(bitSize: int, bitOffset: int) -> int:
        """
        Get the minimum storage size in bytes for a given size in bits with
         the specified bitOffset (lsb position within big endian storage)
        @param bitSize number of bits within bitfield
        @param bitOffset normalized bitfield offset within storage (lsb)
        @return minimum storage size in bytes
        """
        ...

    def getMnemonic(self, settings: ghidra.docking.settings.Settings) -> unicode: ...

    def getName(self) -> unicode: ...

    def getParents(self) -> List[ghidra.program.model.data.DataType]: ...

    def getPathName(self) -> unicode: ...

    def getPrimitiveBaseDataType(self) -> ghidra.program.model.data.AbstractIntegerDataType:
        """
        Get the base datatype associated with this bit-field
         (e.g., int, long, etc., or TypeDef to supported base type)
        @return base data type
        """
        ...

    def getRepresentation(self, buf: ghidra.program.model.mem.MemBuffer, settings: ghidra.docking.settings.Settings, length: int) -> unicode: ...

    def getSettingsDefinitions(self) -> List[ghidra.docking.settings.SettingsDefinition]:
        """
        Gets a list of all the settingsDefinitions used by this datatype.
        @return a list of the settingsDefinitions used by this datatype.
        """
        ...

    def getSourceArchive(self) -> ghidra.program.model.data.SourceArchive: ...

    def getStorageSize(self) -> int:
        """
        Get the packing storage size in bytes associated with this bit-field which may be
         larger than the base type associated with the fields original definition.
         Returned value is the same as {@link #getLength()}.
        @return packing storage size in bytes
        """
        ...

    def getUniversalID(self) -> ghidra.util.UniversalID: ...

    def getValue(self, buf: ghidra.program.model.mem.MemBuffer, settings: ghidra.docking.settings.Settings, length: int) -> object: ...

    def getValueClass(self, settings: ghidra.docking.settings.Settings) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def isDeleted(self) -> bool: ...

    def isDynamicallySized(self) -> bool: ...

    def isEquivalent(self, dt: ghidra.program.model.data.DataType) -> bool: ...

    def isNotYetDefined(self) -> bool: ...

    @staticmethod
    def isValidBaseDataType(baseDataType: ghidra.program.model.data.DataType) -> bool:
        """
        Check if a specified baseDataType is valid for use with a bitfield
        @param baseDataType bitfield base data type (Enum, AbstractIntegerDataType and derived TypeDefs permitted)
        @return true if baseDataType is valid else false
        """
        ...

    def isZeroLengthField(self) -> bool:
        """
        Determine if this bit-field has a zero length (i.e., alignment field)
        @return true if this bit-field has a zero length
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def removeParent(self, dt: ghidra.program.model.data.DataType) -> None: ...

    def replaceWith(self, dataType: ghidra.program.model.data.DataType) -> None: ...

    def setCategoryPath(self, path: ghidra.program.model.data.CategoryPath) -> None: ...

    def setDefaultSettings(self, settings: ghidra.docking.settings.Settings) -> None: ...

    def setDescription(self, description: unicode) -> None: ...

    def setLastChangeTime(self, lastChangeTime: long) -> None: ...

    def setLastChangeTimeInSourceArchive(self, lastChangeTimeInSourceArchive: long) -> None: ...

    def setName(self, name: unicode) -> None: ...

    def setNameAndCategory(self, path: ghidra.program.model.data.CategoryPath, name: unicode) -> None: ...

    def setSourceArchive(self, archive: ghidra.program.model.data.SourceArchive) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def alignment(self) -> int: ...

    @property
    def baseDataType(self) -> ghidra.program.model.data.DataType: ...

    @property
    def baseTypeSize(self) -> int: ...

    @property
    def bitOffset(self) -> int: ...

    @property
    def bitSize(self) -> int: ...

    @property
    def declaredBitSize(self) -> int: ...

    @property
    def defaultSettings(self) -> ghidra.docking.settings.Settings: ...

    @defaultSettings.setter
    def defaultSettings(self, value: ghidra.docking.settings.Settings) -> None: ...

    @property
    def description(self) -> unicode: ...

    @description.setter
    def description(self, value: unicode) -> None: ...

    @property
    def length(self) -> int: ...

    @property
    def primitiveBaseDataType(self) -> ghidra.program.model.data.AbstractIntegerDataType: ...

    @property
    def settingsDefinitions(self) -> List[ghidra.docking.settings.SettingsDefinition]: ...

    @property
    def storageSize(self) -> int: ...

    @property
    def zeroLengthField(self) -> bool: ...
