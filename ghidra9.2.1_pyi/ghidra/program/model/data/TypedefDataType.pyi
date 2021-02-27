from typing import List
import ghidra.docking.settings
import ghidra.program.model.data
import ghidra.program.model.mem
import ghidra.util
import java.lang
import java.net
import javax.swing.event


class TypedefDataType(ghidra.program.model.data.GenericDataType, ghidra.program.model.data.TypeDef):
    """
    Basic implementation for the typedef dataType
    """





    @overload
    def __init__(self, name: unicode, dt: ghidra.program.model.data.DataType): ...

    @overload
    def __init__(self, path: ghidra.program.model.data.CategoryPath, name: unicode, dt: ghidra.program.model.data.DataType):
        """
        Construct a new typedef.
        @param name name to use as the alias
        @param dt data type that is being typedef'ed
        """
        ...

    @overload
    def __init__(self, path: ghidra.program.model.data.CategoryPath, name: unicode, dt: ghidra.program.model.data.DataType, dtm: ghidra.program.model.data.DataTypeManager):
        """
        Construct a new typedef.
        @param name name to use as the alias
        @param dt data type that is being typedef'ed
        """
        ...

    @overload
    def __init__(self, path: ghidra.program.model.data.CategoryPath, name: unicode, dt: ghidra.program.model.data.DataType, universalID: ghidra.util.UniversalID, sourceArchive: ghidra.program.model.data.SourceArchive, lastChangeTime: long, lastChangeTimeInSourceArchive: long, dtm: ghidra.program.model.data.DataTypeManager):
        """
        Construct a new typedef.
        @param path the category path indicating where this data type is located.
        @param name the name of the new structure
        @param universalID the id for the data type
        @param sourceArchive the source archive for this data type
        @param lastChangeTime the last time this data type was changed
        @param lastChangeTimeInSourceArchive the last time this data type was changed in
         its source archive.
        @param dtm the data type manager associated with this data type. This can be null.
         Also, the data type manager may not contain this actual data type.
        """
        ...



    def addParent(self, dt: ghidra.program.model.data.DataType) -> None: ...

    def clone(self, dtm: ghidra.program.model.data.DataTypeManager) -> ghidra.program.model.data.DataType: ...

    def copy(self, dtm: ghidra.program.model.data.DataTypeManager) -> ghidra.program.model.data.DataType: ...

    def dataTypeDeleted(self, dt: ghidra.program.model.data.DataType) -> None: ...

    def dataTypeNameChanged(self, dt: ghidra.program.model.data.DataType, oldName: unicode) -> None: ...

    def dataTypeReplaced(self, oldDt: ghidra.program.model.data.DataType, newDt: ghidra.program.model.data.DataType) -> None: ...

    def dataTypeSizeChanged(self, dt: ghidra.program.model.data.DataType) -> None: ...

    def dependsOn(self, dt: ghidra.program.model.data.DataType) -> bool: ...

    def equals(self, obj: object) -> bool: ...

    def getAlignment(self) -> int: ...

    def getBaseDataType(self) -> ghidra.program.model.data.DataType: ...

    def getCategoryPath(self) -> ghidra.program.model.data.CategoryPath: ...

    def getClass(self) -> java.lang.Class: ...

    def getDataOrganization(self) -> ghidra.program.model.data.DataOrganization: ...

    def getDataType(self) -> ghidra.program.model.data.DataType: ...

    def getDataTypeManager(self) -> ghidra.program.model.data.DataTypeManager:
        """
        @see ghidra.program.model.data.DataType#getDataTypeManager()
        """
        ...

    def getDataTypePath(self) -> ghidra.program.model.data.DataTypePath: ...

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

    def getParents(self) -> List[ghidra.program.model.data.DataType]: ...

    def getPathName(self) -> unicode: ...

    def getRepresentation(self, buf: ghidra.program.model.mem.MemBuffer, settings: ghidra.docking.settings.Settings, length: int) -> unicode: ...

    def getSettingsDefinitions(self) -> List[ghidra.docking.settings.SettingsDefinition]: ...

    def getSourceArchive(self) -> ghidra.program.model.data.SourceArchive: ...

    def getUniversalID(self) -> ghidra.util.UniversalID: ...

    def getValue(self, buf: ghidra.program.model.mem.MemBuffer, settings: ghidra.docking.settings.Settings, length: int) -> object: ...

    def getValueClass(self, settings: ghidra.docking.settings.Settings) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def isDeleted(self) -> bool: ...

    def isDynamicallySized(self) -> bool: ...

    def isEquivalent(self, obj: ghidra.program.model.data.DataType) -> bool: ...

    def isNotYetDefined(self) -> bool: ...

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
    def baseDataType(self) -> ghidra.program.model.data.DataType: ...

    @property
    def dataType(self) -> ghidra.program.model.data.DataType: ...

    @property
    def defaultLabelPrefix(self) -> unicode: ...

    @property
    def deleted(self) -> bool: ...

    @property
    def description(self) -> unicode: ...

    @description.setter
    def description(self, value: unicode) -> None: ...

    @property
    def dynamicallySized(self) -> bool: ...

    @property
    def length(self) -> int: ...

    @property
    def notYetDefined(self) -> bool: ...

    @property
    def settingsDefinitions(self) -> List[ghidra.docking.settings.SettingsDefinition]: ...
