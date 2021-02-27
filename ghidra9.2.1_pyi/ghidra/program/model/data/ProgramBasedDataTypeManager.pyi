from typing import List
import ghidra.framework.model
import ghidra.program.model.data
import ghidra.program.model.listing
import ghidra.util
import ghidra.util.task
import java.lang
import java.util


class ProgramBasedDataTypeManager(ghidra.program.model.data.DomainFileBasedDataTypeManager, object):
    """
    Extends DataTypeManager to include methods specific to a data type manager for
     a program.
    """

    BAD_DATATYPE_ID: long = -0x2L
    BUILT_IN_ARCHIVE_KEY: long = 0x1L
    BUILT_IN_ARCHIVE_UNIVERSAL_ID: ghidra.util.UniversalID = 1
    BUILT_IN_DATA_TYPES_NAME: unicode = u'BuiltInTypes'
    DEFAULT_DATATYPE_ID: long = 0x0L
    LOCAL_ARCHIVE_KEY: long = 0x0L
    LOCAL_ARCHIVE_UNIVERSAL_ID: ghidra.util.UniversalID = 0
    NULL_DATATYPE_ID: long = -0x1L







    def addDataType(self, __a0: ghidra.program.model.data.DataType, __a1: ghidra.program.model.data.DataTypeConflictHandler) -> ghidra.program.model.data.DataType: ...

    def addDataTypeManagerListener(self, __a0: ghidra.program.model.data.DataTypeManagerChangeListener) -> None: ...

    def addDataTypes(self, __a0: java.util.Collection, __a1: ghidra.program.model.data.DataTypeConflictHandler, __a2: ghidra.util.task.TaskMonitor) -> None: ...

    def addInvalidatedListener(self, __a0: ghidra.program.model.data.InvalidatedListener) -> None: ...

    def associateDataTypeWithArchive(self, __a0: ghidra.program.model.data.DataType, __a1: ghidra.program.model.data.SourceArchive) -> None: ...

    def close(self) -> None: ...

    def contains(self, __a0: ghidra.program.model.data.DataType) -> bool: ...

    def containsCategory(self, __a0: ghidra.program.model.data.CategoryPath) -> bool: ...

    def createCategory(self, __a0: ghidra.program.model.data.CategoryPath) -> ghidra.program.model.data.Category: ...

    def dataTypeChanged(self, __a0: ghidra.program.model.data.DataType) -> None: ...

    def disassociate(self, __a0: ghidra.program.model.data.DataType) -> None: ...

    def endTransaction(self, __a0: int, __a1: bool) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def findDataType(self, __a0: unicode) -> ghidra.program.model.data.DataType: ...

    def findDataTypeForID(self, __a0: ghidra.util.UniversalID) -> ghidra.program.model.data.DataType: ...

    @overload
    def findDataTypes(self, __a0: unicode, __a1: List[object]) -> None: ...

    @overload
    def findDataTypes(self, __a0: unicode, __a1: List[object], __a2: bool, __a3: ghidra.util.task.TaskMonitor) -> None: ...

    def findEnumValueNames(self, __a0: long, __a1: java.util.Set) -> None: ...

    def flushEvents(self) -> None: ...

    def getAllComposites(self) -> java.util.Iterator: ...

    @overload
    def getAllDataTypes(self) -> java.util.Iterator: ...

    @overload
    def getAllDataTypes(self, __a0: List[object]) -> None: ...

    def getAllStructures(self) -> java.util.Iterator: ...

    @overload
    def getCategory(self, __a0: long) -> ghidra.program.model.data.Category: ...

    @overload
    def getCategory(self, __a0: ghidra.program.model.data.CategoryPath) -> ghidra.program.model.data.Category: ...

    def getCategoryCount(self) -> int: ...

    def getClass(self) -> java.lang.Class: ...

    def getDataOrganization(self) -> ghidra.program.model.data.DataOrganization: ...

    @overload
    def getDataType(self, __a0: long) -> ghidra.program.model.data.DataType: ...

    @overload
    def getDataType(self, __a0: unicode) -> ghidra.program.model.data.DataType: ...

    @overload
    def getDataType(self, __a0: ghidra.program.model.data.DataTypePath) -> ghidra.program.model.data.DataType: ...

    @overload
    def getDataType(self, __a0: ghidra.program.model.data.CategoryPath, __a1: unicode) -> ghidra.program.model.data.DataType: ...

    @overload
    def getDataType(self, __a0: ghidra.program.model.data.SourceArchive, __a1: ghidra.util.UniversalID) -> ghidra.program.model.data.DataType: ...

    def getDataTypeCount(self, __a0: bool) -> int: ...

    def getDataTypes(self, __a0: ghidra.program.model.data.SourceArchive) -> List[object]: ...

    def getDataTypesContaining(self, __a0: ghidra.program.model.data.DataType) -> java.util.Set: ...

    def getDomainFile(self) -> ghidra.framework.model.DomainFile: ...

    def getFavorites(self) -> List[object]: ...

    def getID(self, __a0: ghidra.program.model.data.DataType) -> long: ...

    def getLastChangeTimeForMyManager(self) -> long: ...

    def getLocalSourceArchive(self) -> ghidra.program.model.data.SourceArchive: ...

    def getName(self) -> unicode: ...

    def getPath(self) -> unicode: ...

    @overload
    def getPointer(self, __a0: ghidra.program.model.data.DataType) -> ghidra.program.model.data.Pointer: ...

    @overload
    def getPointer(self, __a0: ghidra.program.model.data.DataType, __a1: int) -> ghidra.program.model.data.Pointer: ...

    def getProgram(self) -> ghidra.program.model.listing.Program: ...

    def getResolvedID(self, __a0: ghidra.program.model.data.DataType) -> long: ...

    def getRootCategory(self) -> ghidra.program.model.data.Category: ...

    def getSourceArchive(self, __a0: ghidra.util.UniversalID) -> ghidra.program.model.data.SourceArchive: ...

    def getSourceArchives(self) -> List[object]: ...

    def getType(self) -> ghidra.program.model.data.ArchiveType: ...

    def getUniqueName(self, __a0: ghidra.program.model.data.CategoryPath, __a1: unicode) -> unicode: ...

    def getUniversalID(self) -> ghidra.util.UniversalID: ...

    def hashCode(self) -> int: ...

    def isFavorite(self, __a0: ghidra.program.model.data.DataType) -> bool: ...

    def isUpdatable(self) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def remove(self, __a0: ghidra.program.model.data.DataType, __a1: ghidra.util.task.TaskMonitor) -> bool: ...

    def removeDataTypeManagerListener(self, __a0: ghidra.program.model.data.DataTypeManagerChangeListener) -> None: ...

    def removeInvalidatedListener(self, __a0: ghidra.program.model.data.InvalidatedListener) -> None: ...

    def removeSourceArchive(self, __a0: ghidra.program.model.data.SourceArchive) -> None: ...

    def replaceDataType(self, __a0: ghidra.program.model.data.DataType, __a1: ghidra.program.model.data.DataType, __a2: bool) -> ghidra.program.model.data.DataType: ...

    def resolve(self, __a0: ghidra.program.model.data.DataType, __a1: ghidra.program.model.data.DataTypeConflictHandler) -> ghidra.program.model.data.DataType: ...

    def resolveSourceArchive(self, __a0: ghidra.program.model.data.SourceArchive) -> ghidra.program.model.data.SourceArchive: ...

    def setFavorite(self, __a0: ghidra.program.model.data.DataType, __a1: bool) -> None: ...

    def setName(self, __a0: unicode) -> None: ...

    def startTransaction(self, __a0: unicode) -> int: ...

    def toString(self) -> unicode: ...

    @overload
    def updateSourceArchiveName(self, __a0: unicode, __a1: unicode) -> bool: ...

    @overload
    def updateSourceArchiveName(self, __a0: ghidra.util.UniversalID, __a1: unicode) -> bool: ...

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
    def dataOrganization(self) -> ghidra.program.model.data.DataOrganization: ...

    @property
    def domainFile(self) -> ghidra.framework.model.DomainFile: ...

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
    def path(self) -> unicode: ...

    @property
    def program(self) -> ghidra.program.model.listing.Program: ...

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
