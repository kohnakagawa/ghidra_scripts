from typing import Iterator
from typing import List
import ghidra.program.model.data
import ghidra.util
import ghidra.util.task
import java.lang
import java.util


class DataTypeManager(object):
    """
    Interface for Managing data types.
    """

    BAD_DATATYPE_ID: long = -0x2L
    BUILT_IN_ARCHIVE_KEY: long = 0x1L
    BUILT_IN_ARCHIVE_UNIVERSAL_ID: ghidra.util.UniversalID = 1
    BUILT_IN_DATA_TYPES_NAME: unicode = u'BuiltInTypes'
    DEFAULT_DATATYPE_ID: long = 0x0L
    LOCAL_ARCHIVE_KEY: long = 0x0L
    LOCAL_ARCHIVE_UNIVERSAL_ID: ghidra.util.UniversalID = 0
    NULL_DATATYPE_ID: long = -0x1L







    def addDataType(self, dataType: ghidra.program.model.data.DataType, handler: ghidra.program.model.data.DataTypeConflictHandler) -> ghidra.program.model.data.DataType:
        """
        Returns a data type after adding it to this data manager.
         The returned dataType will be in a category in this dataTypeManager
         that is equivalent to the category of the passed in dataType.
        @param dataType the dataType to be resolved.
        @param handler used to resolve conflicts with existing dataTypes.
        @return an equivalent dataType that "belongs" to this dataTypeManager.
        """
        ...

    def addDataTypeManagerListener(self, l: ghidra.program.model.data.DataTypeManagerChangeListener) -> None:
        """
        Add a listener that is notified when the dataTypeManger changes.
        @param l the listener
        """
        ...

    def addDataTypes(self, dataTypes: java.util.Collection, handler: ghidra.program.model.data.DataTypeConflictHandler, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Sequentially adds a collection of datatypes to this data manager.
         This method provides the added benefit of equivalence caching
         for improved performance.
         <br>
         WARNING: This is an experimental method whoose use may cause the GUI and
         task monitor to become unresponsive due to extended hold times on the manager lock.
        @param dataTypes collection of datatypes
        @param handler conflict handler
        @param monitor task monitor
        @throws CancelledException if monitor is cancelled
        """
        ...

    def addInvalidatedListener(self, listener: ghidra.program.model.data.InvalidatedListener) -> None:
        """
        Adds a listener that will be notified when this manager's cache is invalidated.  This will
         happen when the system has changed and the manager cannot determine the exact change, like
         during an undo or a redo.
        @param listener The listener to add
        """
        ...

    def associateDataTypeWithArchive(self, datatype: ghidra.program.model.data.DataType, archive: ghidra.program.model.data.SourceArchive) -> None:
        """
        Change the given data type so that its source archive is the given archive
        @param datatype the type
        @param archive the archive
        """
        ...

    def close(self) -> None:
        """
        Closes this dataType manager
        """
        ...

    def contains(self, dataType: ghidra.program.model.data.DataType) -> bool:
        """
        Return true if the given dataType exists in this data type manager
        @param dataType the type
        @return true if the type is in this manager
        """
        ...

    def containsCategory(self, path: ghidra.program.model.data.CategoryPath) -> bool:
        """
        Returns true if the given category path exists in this datatype manager
        @param path the path
        @return true if the given category path exists in this datatype manager
        """
        ...

    def createCategory(self, path: ghidra.program.model.data.CategoryPath) -> ghidra.program.model.data.Category:
        """
        Create a category for the given path; returns the current category if it already exits
        @param path the path
        @return the category
        """
        ...

    def dataTypeChanged(self, dataType: ghidra.program.model.data.DataType) -> None:
        """
        Notification when data type is changed.
        @param dataType data type that is changed
        """
        ...

    def disassociate(self, datatype: ghidra.program.model.data.DataType) -> None:
        """
        If the indicated data type is associated with a source archive, this will remove the
         association and the data type will become local to this data type manager.
        @param datatype the data type to be disassociated from a source archive.
        """
        ...

    def endTransaction(self, transactionID: int, commit: bool) -> None:
        """
        Ends the current transaction
        @param transactionID id of the transaction to end
        @param commit true if changes are committed, false if changes in transaction are revoked
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def findDataType(self, dataTypePath: unicode) -> ghidra.program.model.data.DataType:
        """
        Gets the dataType for the given path. See {@link #getDataType(String)} for details.
        @param dataTypePath dataType path
        @return dataType at the given path
        @deprecated use {@link #getDataType(String)} or better yet {@link #getDataType(DataTypePath)}
        """
        ...

    def findDataTypeForID(self, datatypeID: ghidra.util.UniversalID) -> ghidra.program.model.data.DataType:
        """
        Get's the data type with the matching universal data type id.
        @param datatypeID The universal id of the data type to search for
        @return The data type with the matching UUID, or null if no such data type can be found.
        """
        ...

    @overload
    def findDataTypes(self, __a0: unicode, __a1: List[object]) -> None: ...

    @overload
    def findDataTypes(self, __a0: unicode, __a1: List[object], __a2: bool, __a3: ghidra.util.task.TaskMonitor) -> None: ...

    def findEnumValueNames(self, value: long, enumValueNames: java.util.Set) -> None:
        """
        Adds all enum value names that match the given value, to the given set.
        @param value the value to look for enum name matches
        @param enumValueNames the set to add matches to.
        """
        ...

    def flushEvents(self) -> None:
        """
        Force all pending notification events to be flushed
        @throws IllegalStateException if the client is holding this object's lock
        """
        ...

    def getAllComposites(self) -> Iterator[ghidra.program.model.data.Composite]:
        """
        Returns an iterator over all composite data types (structures and unions) in this manager
        @return the iterator
        """
        ...

    @overload
    def getAllDataTypes(self) -> Iterator[ghidra.program.model.data.DataType]:
        """
        Returns an iterator over all the dataTypes in this manager
        @return an iterator over all the dataTypes in this manager
        """
        ...

    @overload
    def getAllDataTypes(self, __a0: List[object]) -> None: ...

    def getAllStructures(self) -> Iterator[ghidra.program.model.data.Structure]:
        """
        Returns an iterator over all structures in this manager
        @return the iterator
        """
        ...

    @overload
    def getCategory(self, categoryID: long) -> ghidra.program.model.data.Category:
        """
        Returns the Category with the given id
        @param categoryID id of the desired category
        @return the category
        """
        ...

    @overload
    def getCategory(self, path: ghidra.program.model.data.CategoryPath) -> ghidra.program.model.data.Category:
        """
        Get the category that has the given path
        @param path the path
        @return the category
        """
        ...

    def getCategoryCount(self) -> int:
        """
        Returns the total number of data type categories
        @return the count
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getDataOrganization(self) -> ghidra.program.model.data.DataOrganization:
        """
        Get the data organization associated with this data type manager.  Note that the
         DataOrganization settings may not be changed dynamically.
        @return data organization (will never be null)
        """
        ...

    @overload
    def getDataType(self, dataTypeID: long) -> ghidra.program.model.data.DataType:
        """
        Returns the dataType associated with the given dataTypeId or null if the dataTypeId is
         not valid
        @param dataTypeID the ID
        @return the type
        """
        ...

    @overload
    def getDataType(self, dataTypePath: unicode) -> ghidra.program.model.data.DataType:
        """
        Retrieve the data type with the fully qualified path. So you can get the data named
         "bar" in the category "foo" by calling getDataType("/foo/bar").  This method can
         be problematic now that datatype names can contain slashes.  It will work provided
         that the part of the datatype name that precedes its internal slash is not also the
         name of a category in the same category as the datatype.  For example, if you call
         getDataType("/a/b/c"), and "b/c" is the name of your datatype, it will find it unless
         there is also a category "b" under category "a".  A better solution is to use
         the {@link #getDataType(DataTypePath)} method because the DataTypePath keeps the
         category and datatype name separate.
        @param dataTypePath path
        @return the dataType or null if it isn't found
        """
        ...

    @overload
    def getDataType(self, dataTypePath: ghidra.program.model.data.DataTypePath) -> ghidra.program.model.data.DataType:
        """
        Find the dataType for the given dataTypePath.
        @param dataTypePath the DataTypePath for the datatype
        @return the datatype for the given path.
        """
        ...

    @overload
    def getDataType(self, path: ghidra.program.model.data.CategoryPath, name: unicode) -> ghidra.program.model.data.DataType:
        """
        Gets the data type with the indicated name in the indicated category.
        @param path the path for the category
        @param name the data type's name
        @return the data type.
        """
        ...

    @overload
    def getDataType(self, sourceArchive: ghidra.program.model.data.SourceArchive, datatypeID: ghidra.util.UniversalID) -> ghidra.program.model.data.DataType: ...

    def getDataTypeCount(self, includePointersAndArrays: bool) -> int:
        """
        Returns the total number of defined data types.
        @param includePointersAndArrays if true all pointers and array data types will be included
        @return the count
        """
        ...

    def getDataTypes(self, sourceArchive: ghidra.program.model.data.SourceArchive) -> List[ghidra.program.model.data.DataType]:
        """
        Returns all data types within this manager that have as their source the given archive
        @param sourceArchive the archive
        @return the types
        """
        ...

    def getDataTypesContaining(self, dataType: ghidra.program.model.data.DataType) -> java.util.Set:
        """
        Returns the data types within this data type manager that contain the specified data type.
        @param dataType the data type
        @return a set of data types that contain the specified data type.
        """
        ...

    def getFavorites(self) -> List[ghidra.program.model.data.DataType]:
        """
        Returns a list of datatypes that have been designated as favorites.
        @return the list of favorite datatypes in this manager.
        """
        ...

    def getID(self, dt: ghidra.program.model.data.DataType) -> long:
        """
        Returns the dataTypeId for the given dataType.  If the dataType does not exist,
         a -1 will be returned
        @param dt the datatype to get an id for
        @return the ID of the type
        """
        ...

    def getLastChangeTimeForMyManager(self) -> long:
        """
        Returns the timestamp of the last time this manager was changed
        @return the timestamp
        """
        ...

    def getLocalSourceArchive(self) -> ghidra.program.model.data.SourceArchive:
        """
        Returns the source archive for this manager
        @return the archive; null if the ID is null; null if the archive does not exist
        """
        ...

    def getName(self) -> unicode:
        """
        Returns this data type manager's name
        @return the name
        """
        ...

    @overload
    def getPointer(self, datatype: ghidra.program.model.data.DataType) -> ghidra.program.model.data.Pointer:
        """
        Returns a default sized pointer to the given datatype.  The pointer size is established
         dynamically based upon the data organization established by the compiler specification.
        @param datatype the pointed to data type
        @return the pointer
        """
        ...

    @overload
    def getPointer(self, datatype: ghidra.program.model.data.DataType, size: int) -> ghidra.program.model.data.Pointer:
        """
        Returns a pointer of the given size to the given datatype.
         Note: It is preferred to use default sized pointers when possible (i.e., size=-1,
         see {@link #getPointer(DataType)}) instead of explicitly specifying the size value.
        @param datatype the pointed to data type
        @param size the size of the pointer to be created or -1 for a default sized pointer
        @return the pointer
        """
        ...

    def getResolvedID(self, dt: ghidra.program.model.data.DataType) -> long:
        """
        Returns the dataTypeId for the given dataType.  If the dataType is not
         currently in the dataTypeManger, it will be added
        @param dt the data type
        @return the ID of the resolved type
        """
        ...

    def getRootCategory(self) -> ghidra.program.model.data.Category:
        """
        Returns the root category Manager
        @return the category
        """
        ...

    def getSourceArchive(self, sourceID: ghidra.util.UniversalID) -> ghidra.program.model.data.SourceArchive:
        """
        Returns the source archive for the given ID
        @param sourceID the ID
        @return the archive; null if the ID is null; null if the archive does not exist
        """
        ...

    def getSourceArchives(self) -> List[ghidra.program.model.data.SourceArchive]:
        """
        Returns a list of source archives not including the builtin or the program's archive.
        @return a list of source archives not including the builtin or the program's archive.
        """
        ...

    def getType(self) -> ghidra.program.model.data.ArchiveType:
        """
        Returns this manager's archive type
        @return the type
        """
        ...

    def getUniqueName(self, path: ghidra.program.model.data.CategoryPath, baseName: unicode) -> unicode:
        """
        Returns a unique name not currently used by any other dataType or category
         with the same baseName
        @param path the path of the name
        @param baseName the base name to be made unique
        @return a unique name starting with baseName
        """
        ...

    def getUniversalID(self) -> ghidra.util.UniversalID:
        """
        Returns the universal ID for this dataType manager
        @return the universal ID for this dataType manager
        """
        ...

    def hashCode(self) -> int: ...

    def isFavorite(self, datatype: ghidra.program.model.data.DataType) -> bool:
        """
        Returns true if the given datatype has been designated as a favorite. If the datatype
         does not belong to this datatype manager, then false will be returned.
        @param datatype the datatype to check.
        @return true if the given datatype is a favorite in this manager.
        """
        ...

    def isUpdatable(self) -> bool:
        """
        Returns true if this DataTypeManager can be modified.
        @return true if this DataTypeMangaer can be modified.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def remove(self, dataType: ghidra.program.model.data.DataType, monitor: ghidra.util.task.TaskMonitor) -> bool:
        """
        Remove the given datatype from this manager
        @param dataType the dataType to be removed
        @param monitor the task monitor
        @return true if the data type existed and was removed
        """
        ...

    def removeDataTypeManagerListener(self, l: ghidra.program.model.data.DataTypeManagerChangeListener) -> None:
        """
        Remove the DataTypeManger change listener.
        @param l the listener
        """
        ...

    def removeInvalidatedListener(self, listener: ghidra.program.model.data.InvalidatedListener) -> None:
        """
        Removes a previously added InvalidatedListener
        @param listener the listener to remove.
        """
        ...

    def removeSourceArchive(self, sourceArchive: ghidra.program.model.data.SourceArchive) -> None:
        """
        Removes the source archive from this manager.  This will disassociate all data types in
         this manager from the given archive.
        @param sourceArchive the archive
        """
        ...

    def replaceDataType(self, existingDt: ghidra.program.model.data.DataType, replacementDt: ghidra.program.model.data.DataType, updateCategoryPath: bool) -> ghidra.program.model.data.DataType:
        """
        Replace an existing dataType with another.  All instances and references will be updated to
         use the replacement dataType.
        @param existingDt the dataType to be replaced.
        @param replacementDt the dataType to use as the replacement.
        @param updateCategoryPath if true, the replacementDt will have its categoryPath changed
         to the exitingDt's path.
        @return the resolved replacement dataType.
        @throws DataTypeDependencyException if the replacement datatype depends on
         the existing dataType;
        """
        ...

    def resolve(self, dataType: ghidra.program.model.data.DataType, handler: ghidra.program.model.data.DataTypeConflictHandler) -> ghidra.program.model.data.DataType:
        """
        Returns a dataType that is "in" (ie suitable implementation) this
         Manager, creating a new one if necessary.  Also the returned dataType
         will be in a category in this dataTypeManager that is equivalent to the
         category of the passed in dataType.
        @param dataType the dataType to be resolved.
        @param handler used to resolve conflicts with existing dataTypes.
        @return an equivalent dataType that "belongs" to this dataTypeManager.
        """
        ...

    def resolveSourceArchive(self, sourceArchive: ghidra.program.model.data.SourceArchive) -> ghidra.program.model.data.SourceArchive:
        """
        Returns or creates a persisted version of the given source archive
        @param sourceArchive the archive
        @return the archive
        """
        ...

    def setFavorite(self, datatype: ghidra.program.model.data.DataType, isFavorite: bool) -> None:
        """
        Sets the given dataType to be either a favorite or not a favorite.
        @param datatype the datatype for which to change its status as a favorite.
        @param isFavorite true if the datatype is to be a favorite or false otherwise.
        @throws IllegalArgumentException if the given datatype does not belong to this manager.
        """
        ...

    def setName(self, name: unicode) -> None:
        """
        Sets this data type manager's name
        @param name the new name
        @throws InvalidNameException if the given name is invalid (such as when null or empty)
        """
        ...

    def startTransaction(self, description: unicode) -> int:
        """
        Starts a transaction for making changes in this data type manager.
        @param description a short description of the changes to be made.
        @return the transaction ID
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def updateSourceArchiveName(self, archiveFileID: unicode, name: unicode) -> bool:
        """
        Updates the name associated with a source archive in this data type manager.
        @param archiveFileID Universal domain file ID of the source data type archive that has a new name.
        @param name the new name of the program or archive.
        @return true if the name associated with the source data type archive was changed.
         false if it wasn't changed.
        """
        ...

    @overload
    def updateSourceArchiveName(self, sourceID: ghidra.util.UniversalID, name: unicode) -> bool:
        """
        Updates the name associated with a source archive in this data type manager.
        @param sourceID Universal archive ID of the source data type archive that has a new name.
        @param name the new name of the program or archive.
        @return true if the name associated with the source data type archive was changed.
         false if it wasn't changed.
        """
        ...

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
