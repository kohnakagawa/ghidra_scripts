from typing import List
import ghidra.docking.settings
import ghidra.program.model.data
import ghidra.program.model.lang
import ghidra.program.model.mem
import ghidra.util
import java.lang
import java.net
import javax.swing.event


class Undefined5DataType(ghidra.program.model.data.Undefined):
    """
    Provides an implementation of a byte that has not been defined yet as a
     particular type of data in the program.
    """

    dataType: ghidra.program.model.data.Undefined5DataType = undefined5



    @overload
    def __init__(self):
        """
        Constructs a new Undefined1 dataType
        """
        ...

    @overload
    def __init__(self, dtm: ghidra.program.model.data.DataTypeManager): ...



    def addParent(self, dt: ghidra.program.model.data.DataType) -> None: ...

    def clone(self, dtm: ghidra.program.model.data.DataTypeManager) -> ghidra.program.model.data.DataType: ...

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

    def getCTypeDeclaration(self, dataOrganization: ghidra.program.model.data.DataOrganization) -> unicode:
        """
        Returns null for FactoryDataType (which should never be used) and Dynamic types which should
         generally be replaced by a primitive array (e.g., char[5]) or, a primitive pointer (e.g., char *).
         For other types an appropriately sized unsigned integer typedef is returned.
        @see ghidra.program.model.data.BuiltInDataType#getCTypeDeclaration(ghidra.program.model.data.DataOrganization)
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

    def getDescription(self) -> unicode:
        """
        @see ghidra.program.model.data.DataType#getDescription()
        """
        ...

    def getDisplayName(self) -> unicode: ...

    def getDocs(self) -> java.net.URL: ...

    def getLastChangeTime(self) -> long: ...

    def getLastChangeTimeInSourceArchive(self) -> long: ...

    def getLength(self) -> int:
        """
        @see ghidra.program.model.data.DataType#getLength()
        """
        ...

    def getMnemonic(self, settings: ghidra.docking.settings.Settings) -> unicode:
        """
        @see ghidra.program.model.data.DataType#getMnemonic(Settings)
        """
        ...

    def getName(self) -> unicode: ...

    def getParents(self) -> List[ghidra.program.model.data.DataType]: ...

    def getPathName(self) -> unicode: ...

    def getRepresentation(self, buf: ghidra.program.model.mem.MemBuffer, settings: ghidra.docking.settings.Settings, length: int) -> unicode:
        """
        @see ghidra.program.model.data.DataType#getRepresentation(MemBuffer, Settings, int)
        """
        ...

    def getSettingsDefinitions(self) -> List[ghidra.docking.settings.SettingsDefinition]:
        """
        Gets a list of all the settingsDefinitions used by this datatype.
        @return a list of the settingsDefinitions used by this datatype.
        """
        ...

    def getSourceArchive(self) -> ghidra.program.model.data.SourceArchive: ...

    @staticmethod
    def getUndefinedDataType(size: int) -> ghidra.program.model.data.DataType:
        """
        Get an Undefined data-type instance of the requested size
        @param size data type size, sizes greater than 8 will cause an Undefined1[size] (i.e., Array) to be returned.
        @return Undefined data type
        """
        ...

    @staticmethod
    def getUndefinedDataTypes() -> List[ghidra.program.model.data.Undefined]: ...

    def getUniversalID(self) -> ghidra.util.UniversalID: ...

    def getValue(self, buf: ghidra.program.model.mem.MemBuffer, settings: ghidra.docking.settings.Settings, length: int) -> object:
        """
        @see ghidra.program.model.data.DataType#getValue(ghidra.program.model.mem.MemBuffer, ghidra.docking.settings.Settings, int)
        """
        ...

    def getValueClass(self, settings: ghidra.docking.settings.Settings) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def isDeleted(self) -> bool: ...

    def isDynamicallySized(self) -> bool:
        """
        @see ghidra.program.model.data.DataType#isDynamicallySized()
        """
        ...

    def isEquivalent(self, dt: ghidra.program.model.data.DataType) -> bool: ...

    def isNotYetDefined(self) -> bool: ...

    @staticmethod
    def isUndefined(dataType: ghidra.program.model.data.DataType) -> bool:
        """
        Determine if the specified dataType is either a DefaultDataType,
         an Undefined data-type, or an Array of Undefined data-types.
        @param dataType
        @return true if dataType represents an undefined data-type in
         its various forms, else false.
        """
        ...

    @staticmethod
    def isUndefinedArray(dataType: ghidra.program.model.data.DataType) -> bool:
        """
        Determine if the specified dataType is an undefined array
         used to represent large undefined data.
        @param dataType
        @return true if the specified dataType is an undefined array
         used to represent large undefined data, otherwise false.
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
    def description(self) -> unicode: ...

    @description.setter
    def description(self, value: unicode) -> None: ...

    @property
    def length(self) -> int: ...
