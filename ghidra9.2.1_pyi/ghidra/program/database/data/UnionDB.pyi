from typing import List
import db
import ghidra.docking.settings
import ghidra.program.database.data
import ghidra.program.model.data
import ghidra.program.model.mem
import ghidra.util
import java.lang
import java.net
import javax.swing.event


class UnionDB(ghidra.program.database.data.CompositeDB, ghidra.program.model.data.Union):
    """
    Database implementation for the Union data type.
    """





    def __init__(self, cache: ghidra.program.database.DBObjectCache, key: long):
        """
        Constructs a new DatabaseObject and adds it to the specified cache.
        @param cache to be used for this object or null if object will not be cached
        @param key database key to uniquely identify this object
        """
        ...



    @overload
    def add(self, dataType: ghidra.program.model.data.DataType) -> ghidra.program.model.data.DataTypeComponent: ...

    @overload
    def add(self, dataType: ghidra.program.model.data.DataType, length: int) -> ghidra.program.model.data.DataTypeComponent: ...

    @overload
    def add(self, dataType: ghidra.program.model.data.DataType, fieldName: unicode, comment: unicode) -> ghidra.program.model.data.DataTypeComponent: ...

    @overload
    def add(self, dataType: ghidra.program.model.data.DataType, length: int, componentName: unicode, comment: unicode) -> ghidra.program.model.data.DataTypeComponent: ...

    def addBitField(self, baseDataType: ghidra.program.model.data.DataType, bitSize: int, componentName: unicode, comment: unicode) -> ghidra.program.model.data.DataTypeComponent: ...

    def addParent(self, dt: ghidra.program.model.data.DataType) -> None: ...

    def checkDeleted(self) -> None:
        """
        Checks if this object has been deleted, in which case any use of the object is not allowed.
        @throws ConcurrentModificationException if the object has been deleted from the database.
        """
        ...

    @overload
    def checkIsValid(self) -> bool:
        """
        Check whether this object is still valid. If the object is invalid, the object will attempt
         to refresh itself. If the refresh fails, the object will be marked as deleted.
        @return true if the object is valid.
        """
        ...

    @overload
    def checkIsValid(self, record: db.Record) -> bool:
        """
        Check whether this object is still valid. If the object is invalid, the object will attempt
         to refresh itself using the specified record. If the refresh fails, the object will be marked
         as deleted and removed from cache. If this object is already marked as deleted, the record
         can not be used to refresh the object.
        @param record optional record which may be used to refresh invalid object
        @return true if the object is valid.
        """
        ...

    def clone(self, dtm: ghidra.program.model.data.DataTypeManager) -> ghidra.program.model.data.DataType: ...

    def copy(self, dtm: ghidra.program.model.data.DataTypeManager) -> ghidra.program.model.data.DataType: ...

    def dataTypeAlignmentChanged(self, dt: ghidra.program.model.data.DataType) -> None: ...

    def dataTypeDeleted(self, dt: ghidra.program.model.data.DataType) -> None: ...

    def dataTypeNameChanged(self, dt: ghidra.program.model.data.DataType, oldName: unicode) -> None: ...

    def dataTypeReplaced(self, oldDt: ghidra.program.model.data.DataType, newDt: ghidra.program.model.data.DataType) -> None: ...

    def dataTypeSizeChanged(self, dt: ghidra.program.model.data.DataType) -> None: ...

    @overload
    def delete(self, ordinal: int) -> None: ...

    @overload
    def delete(self, ordinals: List[int]) -> None: ...

    def dependsOn(self, dt: ghidra.program.model.data.DataType) -> bool: ...

    def equals(self, obj: object) -> bool: ...

    def getAlignment(self) -> int: ...

    def getBitFieldPacking(self) -> ghidra.program.model.data.BitFieldPacking: ...

    def getCategoryPath(self) -> ghidra.program.model.data.CategoryPath: ...

    def getClass(self) -> java.lang.Class: ...

    def getComponent(self, ordinal: int) -> ghidra.program.model.data.DataTypeComponent: ...

    def getComponents(self) -> List[ghidra.program.database.data.DataTypeComponentDB]: ...

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

    def getDefaultSettings(self) -> ghidra.docking.settings.Settings:
        """
        @see ghidra.program.model.data.DataType#getDefaultSettings()
        """
        ...

    def getDefinedComponents(self) -> List[ghidra.program.database.data.DataTypeComponentDB]: ...

    def getDescription(self) -> unicode: ...

    def getDisplayName(self) -> unicode:
        """
        @see ghidra.program.model.data.DataType#getDisplayName()
        """
        ...

    def getDocs(self) -> java.net.URL:
        """
        @see ghidra.program.model.data.DataType#getDocs()
        """
        ...

    def getKey(self) -> long:
        """
        Get the database key for this object.
        """
        ...

    def getLastChangeTime(self) -> long: ...

    def getLastChangeTimeInSourceArchive(self) -> long: ...

    def getLength(self) -> int: ...

    def getMinimumAlignment(self) -> int: ...

    def getMnemonic(self, settings: ghidra.docking.settings.Settings) -> unicode: ...

    def getName(self) -> unicode: ...

    def getNumComponents(self) -> int: ...

    def getNumDefinedComponents(self) -> int: ...

    def getPackingValue(self) -> int: ...

    def getParents(self) -> List[ghidra.program.model.data.DataType]: ...

    def getPathName(self) -> unicode:
        """
        @see ghidra.program.model.data.DataType#getPathName()
        """
        ...

    def getRepresentation(self, buf: ghidra.program.model.mem.MemBuffer, settings: ghidra.docking.settings.Settings, length: int) -> unicode: ...

    def getSettingsDefinitions(self) -> List[ghidra.docking.settings.SettingsDefinition]:
        """
        @see ghidra.program.model.data.DataType#getSettingsDefinitions()
        """
        ...

    def getSourceArchive(self) -> ghidra.program.model.data.SourceArchive: ...

    def getUniversalID(self) -> ghidra.util.UniversalID: ...

    def getValue(self, buf: ghidra.program.model.mem.MemBuffer, settings: ghidra.docking.settings.Settings, length: int) -> object: ...

    def getValueClass(self, settings: ghidra.docking.settings.Settings) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    @overload
    def insert(self, ordinal: int, dataType: ghidra.program.model.data.DataType) -> ghidra.program.model.data.DataTypeComponent: ...

    @overload
    def insert(self, ordinal: int, dataType: ghidra.program.model.data.DataType, length: int) -> ghidra.program.model.data.DataTypeComponent: ...

    @overload
    def insert(self, ordinal: int, dataType: ghidra.program.model.data.DataType, length: int, name: unicode, comment: unicode) -> ghidra.program.model.data.DataTypeComponent: ...

    def insertBitField(self, ordinal: int, baseDataType: ghidra.program.model.data.DataType, bitSize: int, componentName: unicode, comment: unicode) -> ghidra.program.model.data.DataTypeComponent: ...

    def isDefaultAligned(self) -> bool: ...

    def isDeleted(self) -> bool:
        """
        @see ghidra.program.model.data.DataType#isDeleted()
        """
        ...

    def isDynamicallySized(self) -> bool: ...

    def isEquivalent(self, dataType: ghidra.program.model.data.DataType) -> bool: ...

    def isInternallyAligned(self) -> bool: ...

    def isInvalid(self) -> bool:
        """
        Returns true if object is currently invalid. Calling checkIsValid may successfully refresh
         object making it valid.
        @see #checkIsValid()
        """
        ...

    def isMachineAligned(self) -> bool: ...

    def isNotYetDefined(self) -> bool: ...

    def isPartOf(self, dataType: ghidra.program.model.data.DataType) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def realign(self) -> None: ...

    def removeParent(self, dt: ghidra.program.model.data.DataType) -> None: ...

    def replaceWith(self, dataType: ghidra.program.model.data.DataType) -> None: ...

    def setCategoryPath(self, path: ghidra.program.model.data.CategoryPath) -> None:
        """
        @see ghidra.program.model.data.DataType#setCategoryPath(ghidra.program.model.data.CategoryPath)
        """
        ...

    def setDefaultSettings(self, settings: ghidra.docking.settings.Settings) -> None:
        """
        @see ghidra.program.model.data.DataType#setDefaultSettings(ghidra.docking.settings.Settings)
        """
        ...

    def setDescription(self, desc: unicode) -> None: ...

    def setInternallyAligned(self, aligned: bool) -> None: ...

    def setInvalid(self) -> None:
        """
        Invalidate this object. This does not necessarily mean that this object can never be used
         again. If the object can refresh itself, it may still be useable.
        """
        ...

    def setLastChangeTime(self, lastChangeTime: long) -> None: ...

    def setLastChangeTimeInSourceArchive(self, lastChangeTime: long) -> None: ...

    def setMinimumAlignment(self, externalAlignment: int) -> None: ...

    def setName(self, name: unicode) -> None:
        """
        @see ghidra.program.model.data.DataType#setName(java.lang.String)
        """
        ...

    def setNameAndCategory(self, path: ghidra.program.model.data.CategoryPath, name: unicode) -> None: ...

    def setPackingValue(self, packingValue: int) -> None: ...

    def setSourceArchive(self, archive: ghidra.program.model.data.SourceArchive) -> None: ...

    def setToDefaultAlignment(self) -> None: ...

    def setToMachineAlignment(self) -> None: ...

    def stateChanged(self, e: javax.swing.event.ChangeEvent) -> None:
        """
        @see javax.swing.event.ChangeListener#stateChanged(javax.swing.event.ChangeEvent)
        """
        ...

    def toString(self) -> unicode: ...

    def validate(self, lock: ghidra.util.Lock) -> bool:
        """
        This method provides a cheap (lock free) way to test if an object is valid. If this object is
         invalid, then the lock will be used to refresh as needed.
        @param lock the lock that will be used if the object needs to be refreshed.
        @return true if object is valid, else false
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
