from typing import List
import ghidra.docking.settings
import ghidra.program.model.data
import ghidra.program.model.mem
import ghidra.util
import java.lang
import java.net


class Array(ghidra.program.model.data.DataType, object):
    """
    Array interface
    """

    ARRAY_LABEL_PREFIX: unicode = u'ARRAY'
    CONFLICT_SUFFIX: unicode = u'.conflict'
    DEFAULT: ghidra.program.model.data.DataType = undefined
    NO_LAST_CHANGE_TIME: long = 0x0L
    NO_SOURCE_SYNC_TIME: long = 0x0L
    VOID: ghidra.program.model.data.DataType = void







    def addParent(self, __a0: ghidra.program.model.data.DataType) -> None: ...

    def clone(self, __a0: ghidra.program.model.data.DataTypeManager) -> ghidra.program.model.data.DataType: ...

    def copy(self, __a0: ghidra.program.model.data.DataTypeManager) -> ghidra.program.model.data.DataType: ...

    def dataTypeDeleted(self, __a0: ghidra.program.model.data.DataType) -> None: ...

    def dataTypeNameChanged(self, __a0: ghidra.program.model.data.DataType, __a1: unicode) -> None: ...

    def dataTypeReplaced(self, __a0: ghidra.program.model.data.DataType, __a1: ghidra.program.model.data.DataType) -> None: ...

    def dataTypeSizeChanged(self, __a0: ghidra.program.model.data.DataType) -> None: ...

    def dependsOn(self, __a0: ghidra.program.model.data.DataType) -> bool: ...

    def equals(self, __a0: object) -> bool: ...

    def getAlignment(self) -> int: ...

    def getArrayDefaultLabelPrefix(self, buf: ghidra.program.model.mem.MemBuffer, settings: ghidra.docking.settings.Settings, len: int, options: ghidra.program.model.data.DataTypeDisplayOptions) -> unicode:
        """
        Get the appropriate string to use as the label prefix
         for an array, taking into account the actual data at the memory location.
         <p>
         See also {@link #getDefaultLabelPrefix()}
        @param buf memory buffer containing the bytes.
        @param settings the Settings object
        @param len the length of the data.
        @param options options for how to format the default label prefix.
        @return the label prefix or null if not applicable
        """
        ...

    def getArrayDefaultOffcutLabelPrefix(self, buf: ghidra.program.model.mem.MemBuffer, settings: ghidra.docking.settings.Settings, len: int, options: ghidra.program.model.data.DataTypeDisplayOptions, offcutLength: int) -> unicode:
        """
        Get the appropriate string to use as the offcut label prefix for an array, taking into
         account the actual data at the memory location.
         <p>
         See also {@link #getDefaultLabelPrefix()}
        @param buf memory buffer containing the bytes.
        @param settings the Settings object
        @param len the length of the data.
        @param options options for how to format the default label prefix.
        @param offcutLength offcut offset from start of buf
        @return the offcut label prefix or null if not applicable
        """
        ...

    def getArrayRepresentation(self, buf: ghidra.program.model.mem.MemBuffer, settings: ghidra.docking.settings.Settings, length: int) -> unicode:
        """
        Get the representation which corresponds to an array in memory.  This will either be a
         String for the ArrayStringable case, "??" for uninitialized data,
         or the empty string if it is not.
        @param buf data buffer
        @param settings data settings
        @param length length of array
        @return a String if it is an array of chars; otherwise empty string, never null.
        """
        ...

    def getArrayValue(self, buf: ghidra.program.model.mem.MemBuffer, settings: ghidra.docking.settings.Settings, length: int) -> object:
        """
        Get the value object which corresponds to an array in memory.  This will either be a
         String for the ArrayStringable case or null.
        @param buf data buffer
        @param settings data settings
        @param length length of array
        @return a String if it is an array of chars; otherwise null.
        """
        ...

    def getArrayValueClass(self, settings: ghidra.docking.settings.Settings) -> java.lang.Class:
        """
        Get the value Class of a specific arrayDt with settings
         ( see {@link #getArrayValueClass(Settings)} ).
        @param settings the relevant settings to use or null for default.
        @return Class of the value to be returned by the array or null if it can vary
         or is unspecified (String or Array class will be returned).
        """
        ...

    def getCategoryPath(self) -> ghidra.program.model.data.CategoryPath: ...

    def getClass(self) -> java.lang.Class: ...

    def getDataOrganization(self) -> ghidra.program.model.data.DataOrganization: ...

    def getDataType(self) -> ghidra.program.model.data.DataType:
        """
        Returns the dataType of the elements in the array.
        @return the dataType of the elements in the array
        """
        ...

    def getDataTypeManager(self) -> ghidra.program.model.data.DataTypeManager: ...

    def getDataTypePath(self) -> ghidra.program.model.data.DataTypePath: ...

    def getDefaultAbbreviatedLabelPrefix(self) -> unicode: ...

    @overload
    def getDefaultLabelPrefix(self) -> unicode: ...

    @overload
    def getDefaultLabelPrefix(self, __a0: ghidra.program.model.mem.MemBuffer, __a1: ghidra.docking.settings.Settings, __a2: int, __a3: ghidra.program.model.data.DataTypeDisplayOptions) -> unicode: ...

    def getDefaultOffcutLabelPrefix(self, __a0: ghidra.program.model.mem.MemBuffer, __a1: ghidra.docking.settings.Settings, __a2: int, __a3: ghidra.program.model.data.DataTypeDisplayOptions, __a4: int) -> unicode: ...

    def getDefaultSettings(self) -> ghidra.docking.settings.Settings: ...

    def getDescription(self) -> unicode: ...

    def getDisplayName(self) -> unicode: ...

    def getDocs(self) -> java.net.URL: ...

    def getElementLength(self) -> int:
        """
        Returns the length of an element in the array
        @return the length of one element in the array.
        """
        ...

    def getLastChangeTime(self) -> long: ...

    def getLastChangeTimeInSourceArchive(self) -> long: ...

    def getLength(self) -> int: ...

    def getMnemonic(self, __a0: ghidra.docking.settings.Settings) -> unicode: ...

    def getName(self) -> unicode: ...

    def getNumElements(self) -> int:
        """
        Returns the number of elements in the array
        @return the number of elements in the array
        """
        ...

    def getParents(self) -> List[ghidra.program.model.data.DataType]: ...

    def getPathName(self) -> unicode: ...

    def getRepresentation(self, __a0: ghidra.program.model.mem.MemBuffer, __a1: ghidra.docking.settings.Settings, __a2: int) -> unicode: ...

    def getSettingsDefinitions(self) -> List[ghidra.docking.settings.SettingsDefinition]: ...

    def getSourceArchive(self) -> ghidra.program.model.data.SourceArchive: ...

    def getUniversalID(self) -> ghidra.util.UniversalID: ...

    def getValue(self, __a0: ghidra.program.model.mem.MemBuffer, __a1: ghidra.docking.settings.Settings, __a2: int) -> object: ...

    def getValueClass(self, __a0: ghidra.docking.settings.Settings) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def isDeleted(self) -> bool: ...

    def isDynamicallySized(self) -> bool: ...

    def isEquivalent(self, __a0: ghidra.program.model.data.DataType) -> bool: ...

    def isNotYetDefined(self) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def removeParent(self, __a0: ghidra.program.model.data.DataType) -> None: ...

    def replaceWith(self, __a0: ghidra.program.model.data.DataType) -> None: ...

    def setCategoryPath(self, __a0: ghidra.program.model.data.CategoryPath) -> None: ...

    def setDefaultSettings(self, __a0: ghidra.docking.settings.Settings) -> None: ...

    def setDescription(self, __a0: unicode) -> None: ...

    def setLastChangeTime(self, __a0: long) -> None: ...

    def setLastChangeTimeInSourceArchive(self, __a0: long) -> None: ...

    def setName(self, __a0: unicode) -> None: ...

    def setNameAndCategory(self, __a0: ghidra.program.model.data.CategoryPath, __a1: unicode) -> None: ...

    def setSourceArchive(self, __a0: ghidra.program.model.data.SourceArchive) -> None: ...

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
    def categoryPath(self) -> ghidra.program.model.data.CategoryPath: ...

    @categoryPath.setter
    def categoryPath(self, value: ghidra.program.model.data.CategoryPath) -> None: ...

    @property
    def dataOrganization(self) -> ghidra.program.model.data.DataOrganization: ...

    @property
    def dataType(self) -> ghidra.program.model.data.DataType: ...

    @property
    def dataTypeManager(self) -> ghidra.program.model.data.DataTypeManager: ...

    @property
    def dataTypePath(self) -> ghidra.program.model.data.DataTypePath: ...

    @property
    def defaultAbbreviatedLabelPrefix(self) -> unicode: ...

    @property
    def defaultLabelPrefix(self) -> unicode: ...

    @property
    def defaultSettings(self) -> ghidra.docking.settings.Settings: ...

    @defaultSettings.setter
    def defaultSettings(self, value: ghidra.docking.settings.Settings) -> None: ...

    @property
    def deleted(self) -> bool: ...

    @property
    def description(self) -> unicode: ...

    @description.setter
    def description(self, value: unicode) -> None: ...

    @property
    def displayName(self) -> unicode: ...

    @property
    def docs(self) -> java.net.URL: ...

    @property
    def dynamicallySized(self) -> bool: ...

    @property
    def elementLength(self) -> int: ...

    @property
    def lastChangeTime(self) -> long: ...

    @lastChangeTime.setter
    def lastChangeTime(self, value: long) -> None: ...

    @property
    def lastChangeTimeInSourceArchive(self) -> long: ...

    @lastChangeTimeInSourceArchive.setter
    def lastChangeTimeInSourceArchive(self, value: long) -> None: ...

    @property
    def length(self) -> int: ...

    @property
    def name(self) -> unicode: ...

    @name.setter
    def name(self, value: unicode) -> None: ...

    @property
    def notYetDefined(self) -> bool: ...

    @property
    def numElements(self) -> int: ...

    @property
    def parents(self) -> List[ghidra.program.model.data.DataType]: ...

    @property
    def pathName(self) -> unicode: ...

    @property
    def settingsDefinitions(self) -> List[ghidra.docking.settings.SettingsDefinition]: ...

    @property
    def sourceArchive(self) -> ghidra.program.model.data.SourceArchive: ...

    @sourceArchive.setter
    def sourceArchive(self, value: ghidra.program.model.data.SourceArchive) -> None: ...

    @property
    def universalID(self) -> ghidra.util.UniversalID: ...
