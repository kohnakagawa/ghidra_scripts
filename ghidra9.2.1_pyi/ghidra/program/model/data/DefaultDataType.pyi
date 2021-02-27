from typing import List
import ghidra.docking.settings
import ghidra.program.model.data
import ghidra.program.model.mem
import ghidra.util
import java.lang
import java.net
import javax.swing.event


class DefaultDataType(ghidra.program.model.data.DataTypeImpl):
    """
    Provides an implementation of a byte that has not been defined yet as a
     particular type of data in the program.
    """

    dataType: ghidra.program.model.data.DefaultDataType







    def addParent(self, dt: ghidra.program.model.data.DataType) -> None:
        """
        @see ghidra.program.model.data.DataType#addParent(ghidra.program.model.data.DataType)
        """
        ...

    def clone(self, dtm: ghidra.program.model.data.DataTypeManager) -> ghidra.program.model.data.DataType: ...

    def copy(self, dtm: ghidra.program.model.data.DataTypeManager) -> ghidra.program.model.data.DataType: ...

    def dataTypeDeleted(self, dt: ghidra.program.model.data.DataType) -> None:
        """
        @see ghidra.program.model.data.DataType#dataTypeDeleted(ghidra.program.model.data.DataType)
        """
        ...

    def dataTypeNameChanged(self, dt: ghidra.program.model.data.DataType, oldName: unicode) -> None:
        """
        @see ghidra.program.model.data.DataType#dataTypeNameChanged(ghidra.program.model.data.DataType, java.lang.String)
        """
        ...

    def dataTypeReplaced(self, oldDt: ghidra.program.model.data.DataType, newDt: ghidra.program.model.data.DataType) -> None:
        """
        @see ghidra.program.model.data.DataType#dataTypeReplaced(ghidra.program.model.data.DataType, ghidra.program.model.data.DataType)
        """
        ...

    def dataTypeSizeChanged(self, dt: ghidra.program.model.data.DataType) -> None:
        """
        @see ghidra.program.model.data.DataType#dataTypeSizeChanged(ghidra.program.model.data.DataType)
        """
        ...

    def dependsOn(self, dt: ghidra.program.model.data.DataType) -> bool:
        """
        @see ghidra.program.model.data.DataType#dependsOn(ghidra.program.model.data.DataType)
        """
        ...

    def equals(self, obj: object) -> bool: ...

    def getAlignment(self) -> int: ...

    def getCategoryPath(self) -> ghidra.program.model.data.CategoryPath: ...

    def getClass(self) -> java.lang.Class: ...

    def getDataOrganization(self) -> ghidra.program.model.data.DataOrganization: ...

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

    def getSettingsDefinitions(self) -> List[ghidra.docking.settings.SettingsDefinition]: ...

    def getSourceArchive(self) -> ghidra.program.model.data.SourceArchive: ...

    def getUniversalID(self) -> ghidra.util.UniversalID: ...

    def getValue(self, buf: ghidra.program.model.mem.MemBuffer, settings: ghidra.docking.settings.Settings, length: int) -> object:
        """
        Get the Undefined byte as a Scalar.
        @param buf the data buffer.
        @param settings the display settings to use.
        @param length the number of bytes to get the value from.
        @return the data Object.
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

    def isEquivalent(self, dt: ghidra.program.model.data.DataType) -> bool:
        """
        @see ghidra.program.model.data.DataType#isEquivalent(ghidra.program.model.data.DataType)
        """
        ...

    def isNotYetDefined(self) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def removeParent(self, dt: ghidra.program.model.data.DataType) -> None:
        """
        @see ghidra.program.model.data.DataType#removeParent(ghidra.program.model.data.DataType)
        """
        ...

    def replaceWith(self, dataType: ghidra.program.model.data.DataType) -> None: ...

    def setCategoryPath(self, path: ghidra.program.model.data.CategoryPath) -> None:
        """
        @see ghidra.program.model.data.DataType#setCategoryPath(ghidra.program.model.data.CategoryPath)
        """
        ...

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

    def setName(self, name: unicode) -> None:
        """
        @see ghidra.program.model.data.DataType#setName(java.lang.String)
        """
        ...

    def setNameAndCategory(self, path: ghidra.program.model.data.CategoryPath, name: unicode) -> None:
        """
        @see ghidra.program.model.data.DataType#setNameAndCategory(ghidra.program.model.data.CategoryPath, java.lang.String)
        """
        ...

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
    def categoryPath(self) -> ghidra.program.model.data.CategoryPath: ...

    @categoryPath.setter
    def categoryPath(self, value: ghidra.program.model.data.CategoryPath) -> None: ...

    @property
    def description(self) -> unicode: ...

    @description.setter
    def description(self, value: unicode) -> None: ...

    @property
    def dynamicallySized(self) -> bool: ...

    @property
    def lastChangeTime(self) -> long: ...

    @lastChangeTime.setter
    def lastChangeTime(self, value: long) -> None: ...

    @property
    def length(self) -> int: ...

    @property
    def name(self) -> unicode: ...

    @name.setter
    def name(self, value: unicode) -> None: ...
