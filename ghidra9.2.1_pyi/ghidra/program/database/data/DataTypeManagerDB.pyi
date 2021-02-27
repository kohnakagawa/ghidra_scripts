from typing import Iterator
from typing import List
import ghidra.program.model.address
import ghidra.program.model.data
import ghidra.util
import ghidra.util.task
import java.io
import java.lang
import java.util


class DataTypeManagerDB(object, ghidra.program.model.data.DataTypeManager):
    """
    Base class for DB-backed data type managers.
     Important Notes:

     When invoking DataType#isEquivalent(DataType) involving
     DataTypeDB objects it is important to invoke the method on DataTypeDB. This
     will ensure that the internal optimization mechanisms are used.
     It is important that the use of DataType#clone(DataTypeManager)
     and DataType#copy(DataTypeManager) be avoided when possible to ensure
     full benefit of the #equivalenceCache and #resolveCache.

    """

    BAD_DATATYPE_ID: long = -0x2L
    BUILT_IN_ARCHIVE_KEY: long = 0x1L
    BUILT_IN_ARCHIVE_UNIVERSAL_ID: ghidra.util.UniversalID = 1
    BUILT_IN_DATA_TYPES_NAME: unicode = u'BuiltInTypes'
    DEFAULT_DATATYPE_ID: long = 0x0L
    LOCAL_ARCHIVE_KEY: long = 0x0L
    LOCAL_ARCHIVE_UNIVERSAL_ID: ghidra.util.UniversalID = 0
    NULL_DATATYPE_ID: long = -0x1L







    def addDataType(self, originalDataType: ghidra.program.model.data.DataType, handler: ghidra.program.model.data.DataTypeConflictHandler) -> ghidra.program.model.data.DataType: ...

    def addDataTypeManagerListener(self, l: ghidra.program.model.data.DataTypeManagerChangeListener) -> None: ...

    def addDataTypes(self, dataTypes: java.util.Collection, handler: ghidra.program.model.data.DataTypeConflictHandler, monitor: ghidra.util.task.TaskMonitor) -> None: ...

    def addInvalidatedListener(self, listener: ghidra.program.model.data.InvalidatedListener) -> None: ...

    def associateDataTypeWithArchive(self, datatype: ghidra.program.model.data.DataType, archive: ghidra.program.model.data.SourceArchive) -> None: ...

    def clearAllSettings(self, dataAddr: ghidra.program.model.address.Address) -> None:
        """
        Clear all settings at the given address.
        @param dataAddr the address for this settings.
        """
        ...

    def clearSetting(self, dataAddr: ghidra.program.model.address.Address, name: unicode) -> bool:
        """
        Clear the setting
        @param dataAddr min address of data
        @param name settings name
        @return true if the settings were cleared
        """
        ...

    def clearSettings(self, start: ghidra.program.model.address.Address, end: ghidra.program.model.address.Address, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Clears all settings in the given address range.
        @param start the first address of the range to clear
        @param end the last address of the range to clear.
        @param monitor the progress monitor for this operation.
        @throws CancelledException if the user cancels the operation.
        """
        ...

    def close(self) -> None: ...

    def contains(self, dataType: ghidra.program.model.data.DataType) -> bool: ...

    def containsCategory(self, path: ghidra.program.model.data.CategoryPath) -> bool: ...

    def createCategory(self, path: ghidra.program.model.data.CategoryPath) -> ghidra.program.model.data.Category: ...

    def dataTypeChanged(self, dt: ghidra.program.model.data.DataType) -> None: ...

    def dbError(self, e: java.io.IOException) -> None:
        """
        Handles IOExceptions
        @param e the exception to handle
        """
        ...

    def deleteAddressRange(self, startAddr: ghidra.program.model.address.Address, endAddr: ghidra.program.model.address.Address, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Removes all settings in the range
        @param startAddr the first address in the range.
        @param endAddr the last address in the range.
        @param monitor the progress monitor
        @throws CancelledException if the user cancelled the operation.
        """
        ...

    def disassociate(self, dataType: ghidra.program.model.data.DataType) -> None: ...

    def endTransaction(self, __a0: int, __a1: bool) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def findDataType(self, dataTypePath: unicode) -> ghidra.program.model.data.DataType: ...

    def findDataTypeForID(self, datatypeID: ghidra.util.UniversalID) -> ghidra.program.model.data.DataType: ...

    @overload
    def findDataTypes(self, __a0: unicode, __a1: List[object]) -> None: ...

    @overload
    def findDataTypes(self, __a0: unicode, __a1: List[object], __a2: bool, __a3: ghidra.util.task.TaskMonitor) -> None: ...

    def findEnumValueNames(self, value: long, enumValueNames: java.util.Set) -> None: ...

    def fixupComposites(self, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Fixup all composites and thier components which may be affected by a data organization
         change include primitive type size changes and alignment changes.  It is highly recommended
         that this program be open with exclusive access before invoking this method to avoid
         excessive merge conflicts with other users.
        @param monitor task monitor
        @throws CancelledException if operation is cancelled
        """
        ...

    def flushEvents(self) -> None: ...

    def getAllComposites(self) -> Iterator[ghidra.program.model.data.Composite]: ...

    @overload
    def getAllDataTypes(self) -> Iterator[ghidra.program.model.data.DataType]: ...

    @overload
    def getAllDataTypes(self, __a0: List[object]) -> None: ...

    def getAllStructures(self) -> Iterator[ghidra.program.model.data.Structure]: ...

    def getByteSettingsValue(self, dataAddr: ghidra.program.model.address.Address, name: unicode) -> List[int]:
        """
        Get the byte array value for an instance setting.
        @param dataAddr min address of data
        @param name settings name
        @return null if the named setting was not found
        """
        ...

    @overload
    def getCategory(self, id: long) -> ghidra.program.model.data.Category:
        """
        Get the category for the given ID.
        @return null if no category exists with the given ID.
        """
        ...

    @overload
    def getCategory(self, path: ghidra.program.model.data.CategoryPath) -> ghidra.program.model.data.Category: ...

    def getCategoryCount(self) -> int: ...

    def getClass(self) -> java.lang.Class: ...

    def getDataOrganization(self) -> ghidra.program.model.data.DataOrganization: ...

    @overload
    def getDataType(self, dataTypeID: long) -> ghidra.program.model.data.DataType: ...

    @overload
    def getDataType(self, dataTypePath: unicode) -> ghidra.program.model.data.DataType: ...

    @overload
    def getDataType(self, dataTypePath: ghidra.program.model.data.DataTypePath) -> ghidra.program.model.data.DataType: ...

    @overload
    def getDataType(self, path: ghidra.program.model.data.CategoryPath, name: unicode) -> ghidra.program.model.data.DataType: ...

    @overload
    def getDataType(self, sourceArchive: ghidra.program.model.data.SourceArchive, datatypeID: ghidra.util.UniversalID) -> ghidra.program.model.data.DataType: ...

    def getDataTypeCount(self, includePointersAndArrays: bool) -> int: ...

    @overload
    def getDataTypes(self, path: ghidra.program.model.data.CategoryPath) -> List[ghidra.program.model.data.DataType]:
        """
        Gets the datatypes in the given category path
        @param path the category path in which to look for datatypes
        @return array of datatypes contained with specified category
        """
        ...

    @overload
    def getDataTypes(self, sourceArchive: ghidra.program.model.data.SourceArchive) -> List[ghidra.program.model.data.DataType]: ...

    def getDataTypesContaining(self, dataType: ghidra.program.model.data.DataType) -> java.util.Set: ...

    def getFavorites(self) -> List[ghidra.program.model.data.DataType]: ...

    def getID(self, dt: ghidra.program.model.data.DataType) -> long: ...

    def getLastChangeTimeForMyManager(self) -> long: ...

    def getLocalSourceArchive(self) -> ghidra.program.model.data.SourceArchive: ...

    def getLongSettingsValue(self, dataAddr: ghidra.program.model.address.Address, name: unicode) -> long:
        """
        Get the long value for an instance setting.
        @param dataAddr min address of data
        @param name settings name
        @return null if the named setting was not found
        """
        ...

    def getName(self) -> unicode: ...

    def getNames(self, dataAddr: ghidra.program.model.address.Address) -> List[unicode]:
        """
        Returns all the Settings names for the given address
        @param dataAddr the address
        @return the names
        """
        ...

    @overload
    def getPointer(self, dt: ghidra.program.model.data.DataType) -> ghidra.program.model.data.Pointer: ...

    @overload
    def getPointer(self, dt: ghidra.program.model.data.DataType, size: int) -> ghidra.program.model.data.Pointer: ...

    def getResolvedID(self, dt: ghidra.program.model.data.DataType) -> long: ...

    def getRootCategory(self) -> ghidra.program.model.data.Category: ...

    def getSettings(self, dataAddr: ghidra.program.model.address.Address, name: unicode) -> object:
        """
        Gets the value of a settings as an object (either String, byte[], or Long).
        @param dataAddr the address of the data for this settings
        @param name the name of settings.
        @return the settings object
        """
        ...

    @overload
    def getSourceArchive(self, fileID: unicode) -> ghidra.program.model.data.SourceArchive: ...

    @overload
    def getSourceArchive(self, sourceID: ghidra.util.UniversalID) -> ghidra.program.model.data.SourceArchive: ...

    def getSourceArchives(self) -> List[ghidra.program.model.data.SourceArchive]: ...

    def getStringSettingsValue(self, dataAddr: ghidra.program.model.address.Address, name: unicode) -> unicode:
        """
        Get the String value for an instance setting.
        @param dataAddr min address of data
        @param name settings name
        @return null if the named setting was not found
        """
        ...

    def getType(self) -> ghidra.program.model.data.ArchiveType: ...

    @overload
    def getUniqueName(self, path: ghidra.program.model.data.CategoryPath, baseName: unicode) -> unicode: ...

    @overload
    def getUniqueName(self, path1: ghidra.program.model.data.CategoryPath, path2: ghidra.program.model.data.CategoryPath, baseName: unicode) -> unicode: ...

    def getUniversalID(self) -> ghidra.util.UniversalID: ...

    def getUnusedConflictName(self, path: ghidra.program.model.data.CategoryPath, name: unicode) -> unicode:
        """
        This method gets a ".conflict" name that is not currently used by any data
         types in the indicated category of the data type manager.
        @param path the category path of the category where the new data type live in
                     the data type manager.
        @param name The name of the data type. This name may or may not contain
                     ".conflict" as part of it. If the name contains ".conflict", only
                     the part of the name that comes prior to the ".conflict" will be
                     used to determine a new unused conflict name.
        @return the unused conflict name
        """
        ...

    def hashCode(self) -> int: ...

    def invalidateCache(self) -> None:
        """
        Invalidates the cache.
        """
        ...

    def isChanged(self) -> bool: ...

    def isEmptySetting(self, dataAddr: ghidra.program.model.address.Address) -> bool:
        """
        Returns true if no settings are set for the given address
        @param dataAddr the address to test
        @return true if not settings
        """
        ...

    def isFavorite(self, dataType: ghidra.program.model.data.DataType) -> bool: ...

    def isUpdatable(self) -> bool: ...

    def moveAddressRange(self, fromAddr: ghidra.program.model.address.Address, toAddr: ghidra.program.model.address.Address, length: long, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Move the settings in the range to the new start address
        @param fromAddr start address from where to move
        @param toAddr new Address to move to
        @param length number of addresses to move
        @param monitor progress monitor
        @throws CancelledException if the operation was cancelled
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def remove(self, dataType: ghidra.program.model.data.DataType, monitor: ghidra.util.task.TaskMonitor) -> bool: ...

    def removeDataTypeManagerListener(self, l: ghidra.program.model.data.DataTypeManagerChangeListener) -> None: ...

    def removeInvalidatedListener(self, listener: ghidra.program.model.data.InvalidatedListener) -> None: ...

    def removeSourceArchive(self, sourceArchive: ghidra.program.model.data.SourceArchive) -> None: ...

    def replaceDataType(self, existingDt: ghidra.program.model.data.DataType, replacementDt: ghidra.program.model.data.DataType, updateCategoryPath: bool) -> ghidra.program.model.data.DataType: ...

    def replaceSourceArchive(self, oldSourceArchive: ghidra.program.model.data.SourceArchive, newSourceArchive: ghidra.program.model.data.SourceArchive) -> None:
        """
        Replace one source archive (oldDTM) with another (newDTM). Any data types
         whose source was the oldDTM will be changed to have a source that is the
         newDTM. The oldDTM will no longer be referenced as a source by this data type
         manager.
        @param oldSourceArchive data type manager for the old source archive
        @param newSourceArchive data type manager for the new source archive
        @throws IllegalArgumentException if the oldDTM isn't currently a source
                                          archive for this data type manager or if the
                                          old and new source archives already have the
                                          same unique ID.
        """
        ...

    def resolve(self, dataType: ghidra.program.model.data.DataType, handler: ghidra.program.model.data.DataTypeConflictHandler) -> ghidra.program.model.data.DataType: ...

    def resolveSourceArchive(self, sourceArchive: ghidra.program.model.data.SourceArchive) -> ghidra.program.model.data.SourceArchive: ...

    def setByteSettingsValue(self, dataAddr: ghidra.program.model.address.Address, name: unicode, byteValue: List[int]) -> bool:
        """
        Set the byte array value for instance settings.
        @param dataAddr min address of data ata
        @param name settings name
        @param byteValue byte array value of setting
        @return true if the settings actually changed
        """
        ...

    def setFavorite(self, dataType: ghidra.program.model.data.DataType, isFavorite: bool) -> None: ...

    def setLongSettingsValue(self, dataAddr: ghidra.program.model.address.Address, name: unicode, value: long) -> bool:
        """
        Set the long value for instance settings.
        @param dataAddr min address of data
        @param name settings name
        @param value value of setting
        @return true if the settings actually changed
        """
        ...

    def setName(self, __a0: unicode) -> None: ...

    def setSettings(self, dataAddr: ghidra.program.model.address.Address, name: unicode, value: object) -> bool:
        """
        Set the Object settings.
        @param dataAddr min address of data
        @param name the name of the settings
        @param value the value for the settings, must be either a String, byte[]
                         or Long
        @return true if the settings were updated
        """
        ...

    def setStringSettingsValue(self, dataAddr: ghidra.program.model.address.Address, name: unicode, value: unicode) -> bool:
        """
        Set the string value for instance settings.
        @param dataAddr min address of data
        @param name settings name
        @param value value of setting
        @return true if the settings actually changed
        """
        ...

    def sourceArchiveChanged(self, sourceArchiveID: ghidra.util.UniversalID) -> None: ...

    def startTransaction(self, __a0: unicode) -> int: ...

    def toString(self) -> unicode: ...

    def updateID(self) -> None: ...

    @overload
    def updateSourceArchiveName(self, archiveFileID: unicode, name: unicode) -> bool: ...

    @overload
    def updateSourceArchiveName(self, sourceID: ghidra.util.UniversalID, name: unicode) -> bool: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def allComposites(self) -> java.util.Iterator: ...

    @property
    def allDataTypes(self) -> java.util.Iterator: ...

    @property
    def allStructures(self) -> java.util.Iterator: ...

    @property
    def categoryCount(self) -> int: ...

    @property
    def changed(self) -> bool: ...

    @property
    def dataOrganization(self) -> ghidra.program.model.data.DataOrganization: ...

    @property
    def favorites(self) -> List[object]: ...

    @property
    def lastChangeTimeForMyManager(self) -> long: ...

    @property
    def localSourceArchive(self) -> ghidra.program.model.data.SourceArchive: ...

    @property
    def name(self) -> unicode: ...

    @name.setter
    def name(self, value: unicode) -> None: ...

    @property
    def rootCategory(self) -> ghidra.program.model.data.Category: ...

    @property
    def sourceArchives(self) -> List[object]: ...

    @property
    def type(self) -> ghidra.program.model.data.ArchiveType: ...

    @property
    def universalID(self) -> ghidra.util.UniversalID: ...

    @property
    def updatable(self) -> bool: ...
