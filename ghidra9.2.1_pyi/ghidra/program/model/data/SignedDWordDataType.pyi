from typing import List
import ghidra.docking.settings
import ghidra.program.model.data
import ghidra.program.model.lang
import ghidra.program.model.mem
import ghidra.util
import java.lang
import java.net
import javax.swing.event


class SignedDWordDataType(ghidra.program.model.data.AbstractIntegerDataType):
    """
    Provides a definition of a Signed Double Word within a program.
    """

    dataType: ghidra.program.model.data.SignedDWordDataType = sdword



    @overload
    def __init__(self): ...

    @overload
    def __init__(self, dtm: ghidra.program.model.data.DataTypeManager): ...



    def addParent(self, dt: ghidra.program.model.data.DataType) -> None: ...

    def clone(self, dtm: ghidra.program.model.data.DataTypeManager) -> ghidra.program.model.data.SignedDWordDataType: ...

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

    def getArrayDefaultLabelPrefix(self, buf: ghidra.program.model.mem.MemBuffer, settings: ghidra.docking.settings.Settings, len: int, options: ghidra.program.model.data.DataTypeDisplayOptions) -> unicode: ...

    def getArrayDefaultOffcutLabelPrefix(self, buf: ghidra.program.model.mem.MemBuffer, settings: ghidra.docking.settings.Settings, len: int, options: ghidra.program.model.data.DataTypeDisplayOptions, offcutOffset: int) -> unicode: ...

    def getArrayString(self, __a0: ghidra.program.model.mem.MemBuffer, __a1: ghidra.docking.settings.Settings, __a2: int) -> unicode: ...

    @staticmethod
    def getArrayStringable(__a0: ghidra.program.model.data.DataType) -> ghidra.program.model.data.ArrayStringable: ...

    def getAssemblyMnemonic(self) -> unicode: ...

    def getCDeclaration(self) -> unicode:
        """
        @return the C style data-type declaration
         for this data-type.  Null is returned if
         no appropriate declaration exists.
        """
        ...

    def getCMnemonic(self) -> unicode:
        """
        @return the C style data-type mnemonic
         for this data-type.
         NOTE: currently the same as getCDeclaration().
        """
        ...

    def getCTypeDeclaration(self, dataOrganization: ghidra.program.model.data.DataOrganization) -> unicode: ...

    def getCategoryPath(self) -> ghidra.program.model.data.CategoryPath: ...

    def getClass(self) -> java.lang.Class: ...

    def getDataOrganization(self) -> ghidra.program.model.data.DataOrganization: ...

    def getDataTypeManager(self) -> ghidra.program.model.data.DataTypeManager:
        """
        @see ghidra.program.model.data.DataType#getDataTypeManager()
        """
        ...

    def getDataTypePath(self) -> ghidra.program.model.data.DataTypePath: ...

    def getDecompilerDisplayName(self, language: ghidra.program.model.lang.DecompilerLanguage) -> unicode:
        """
        Return token used to represent this type in decompiler/source-code output
        @param language is the language being displayed
        @return the name string
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

    def getLastChangeTime(self) -> long: ...

    def getLastChangeTimeInSourceArchive(self) -> long: ...

    def getLength(self) -> int: ...

    def getMnemonic(self, settings: ghidra.docking.settings.Settings) -> unicode: ...

    def getName(self) -> unicode: ...

    def getOppositeSignednessDataType(self) -> ghidra.program.model.data.DWordDataType: ...

    def getParents(self) -> List[ghidra.program.model.data.DataType]: ...

    def getPathName(self) -> unicode: ...

    def getRepresentation(self, buf: ghidra.program.model.mem.MemBuffer, settings: ghidra.docking.settings.Settings, length: int) -> unicode: ...

    def getSettingsDefinitions(self) -> List[ghidra.docking.settings.SettingsDefinition]:
        """
        Gets a list of all the settingsDefinitions used by this datatype.
        @return a list of the settingsDefinitions used by this datatype.
        """
        ...

    @staticmethod
    def getSignedDataType(size: int, dtm: ghidra.program.model.data.DataTypeManager) -> ghidra.program.model.data.DataType:
        """
        Get a Signed Integer data-type instance of the requested size
        @param size data type size, sizes greater than 8 (and other than 16)
         will cause an SignedByteDataType[size] (i.e., Array) to be returned.
        @param dtm optional program data-type manager, if specified
         a generic data-type will be returned if possible.
        @return signed integer data type
        """
        ...

    @staticmethod
    def getSignedDataTypes(dtm: ghidra.program.model.data.DataTypeManager) -> List[ghidra.program.model.data.AbstractIntegerDataType]:
        """
        Returns all built-in signed integer data-types.
        @param dtm optional program data-type manager, if specified
         generic data-types will be returned in place of fixed-sized data-types.
        @return array of all signed integer types (char and bool types excluded)
        """
        ...

    def getSourceArchive(self) -> ghidra.program.model.data.SourceArchive: ...

    def getUniversalID(self) -> ghidra.util.UniversalID: ...

    @staticmethod
    def getUnsignedDataType(size: int, dtm: ghidra.program.model.data.DataTypeManager) -> ghidra.program.model.data.DataType:
        """
        Get a Unsigned Integer data-type instance of the requested size
        @param size data type size, sizes greater than 8 (and other than 16)
         will cause an undefined type to be returned.
        @param dtm optional program data-type manager, if specified
         a generic data-type will be returned if possible.
        @return unsigned integer data type
        """
        ...

    @staticmethod
    def getUnsignedDataTypes(dtm: ghidra.program.model.data.DataTypeManager) -> List[ghidra.program.model.data.AbstractIntegerDataType]:
        """
        Returns all built-in unsigned integer data-types
        @param dtm optional program data-type manager, if specified
         generic data-types will be returned in place of fixed-sized data-types.
        @return array of all unsigned integer types (char and bool types excluded)
        """
        ...

    def getValue(self, buf: ghidra.program.model.mem.MemBuffer, settings: ghidra.docking.settings.Settings, length: int) -> object: ...

    def getValueClass(self, settings: ghidra.docking.settings.Settings) -> java.lang.Class: ...

    def hasStringValue(self, settings: ghidra.docking.settings.Settings) -> bool: ...

    def hashCode(self) -> int: ...

    def isDeleted(self) -> bool: ...

    def isDynamicallySized(self) -> bool:
        """
        @see ghidra.program.model.data.DataType#isDynamicallySized()
        """
        ...

    def isEquivalent(self, dt: ghidra.program.model.data.DataType) -> bool: ...

    def isNotYetDefined(self) -> bool: ...

    def isSigned(self) -> bool:
        """
        @return true if this is a signed integer data-type
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def removeParent(self, dt: ghidra.program.model.data.DataType) -> None: ...

    def replaceWith(self, dataType: ghidra.program.model.data.DataType) -> None: ...

    def setCategoryPath(self, path: ghidra.program.model.data.CategoryPath) -> None: ...

    def setDefaultSettings(self, settings: ghidra.docking.settings.Settings) -> None: ...

    def setDescription(self, description: unicode) -> None:
        """
        Sets a String briefly describing this DataType.
         <br>If a data type that extends this class wants to allow the description to be changed,
         then it must override this method.
        @param description a one-liner describing this DataType.
        @throws UnsupportedOperationException if the description is not allowed to be set for this data type.
        """
        ...

    def setLastChangeTime(self, lastChangeTime: long) -> None: ...

    def setLastChangeTimeInSourceArchive(self, lastChangeTimeInSourceArchive: long) -> None: ...

    def setName(self, name: unicode) -> None: ...

    def setNameAndCategory(self, path: ghidra.program.model.data.CategoryPath, name: unicode) -> None: ...

    def setSourceArchive(self, archive: ghidra.program.model.data.SourceArchive) -> None: ...

    def stateChanged(self, e: javax.swing.event.ChangeEvent) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def assemblyMnemonic(self) -> unicode: ...

    @property
    def description(self) -> unicode: ...

    @description.setter
    def description(self, value: unicode) -> None: ...

    @property
    def length(self) -> int: ...

    @property
    def oppositeSignednessDataType(self) -> ghidra.program.model.data.DWordDataType: ...
