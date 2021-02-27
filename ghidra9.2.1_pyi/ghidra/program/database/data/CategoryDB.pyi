from typing import List
import db
import ghidra.program.database
import ghidra.program.database.data
import ghidra.program.model.data
import ghidra.util
import ghidra.util.task
import java.lang


class CategoryDB(ghidra.program.database.DatabaseObject, ghidra.program.model.data.Category):
    """
    Database implementation for Category.
    """





    def __init__(self, cache: ghidra.program.database.DBObjectCache, key: long):
        """
        Constructs a new DatabaseObject and adds it to the specified cache.
        @param cache to be used for this object or null if object will not be cached
        @param key database key to uniquely identify this object
        """
        ...



    def addDataType(self, dt: ghidra.program.model.data.DataType, handler: ghidra.program.model.data.DataTypeConflictHandler) -> ghidra.program.model.data.DataType:
        """
        @see ghidra.program.model.data.Category#addDataType(ghidra.program.model.data.DataType, ghidra.program.model.data.DataTypeConflictHandler)
        """
        ...

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

    def compareTo(self, __a0: object) -> int: ...

    def copyCategory(self, category: ghidra.program.model.data.Category, handler: ghidra.program.model.data.DataTypeConflictHandler, monitor: ghidra.util.task.TaskMonitor) -> ghidra.program.model.data.Category:
        """
        @see ghidra.program.model.data.Category#copyCategory(ghidra.program.model.data.Category, ghidra.program.model.data.DataTypeConflictHandler, ghidra.util.task.TaskMonitor)
        """
        ...

    def createCategory(self, categoryName: unicode) -> ghidra.program.model.data.Category:
        """
        @see ghidra.program.model.data.Category#createCategory(java.lang.String)
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getCategories(self) -> List[ghidra.program.model.data.Category]:
        """
        @see ghidra.program.model.data.Category#getCategories()
        """
        ...

    def getCategory(self, subcategoryName: unicode) -> ghidra.program.database.data.CategoryDB:
        """
        @see ghidra.program.model.data.Category#getCategory(java.lang.String)
        """
        ...

    def getCategoryPath(self) -> ghidra.program.model.data.CategoryPath:
        """
        @see ghidra.program.model.data.Category#getCategoryPath()
        """
        ...

    def getCategoryPathName(self) -> unicode:
        """
        Get the fully qualified name for this category.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getDataType(self, dataTypeName: unicode) -> ghidra.program.model.data.DataType:
        """
        @see ghidra.program.model.data.Category#getDataType(java.lang.String)
        """
        ...

    def getDataTypeManager(self) -> ghidra.program.model.data.DataTypeManager:
        """
        Get the data type manager associated with this category.
        """
        ...

    def getDataTypes(self) -> List[ghidra.program.model.data.DataType]:
        """
        @see ghidra.program.model.data.Category#getDataTypes()
        """
        ...

    def getDataTypesByBaseName(self, dataTypeName: unicode) -> List[ghidra.program.model.data.DataType]: ...

    def getID(self) -> long:
        """
        @see ghidra.program.model.data.Category#getID()
        """
        ...

    def getKey(self) -> long:
        """
        Get the database key for this object.
        """
        ...

    def getName(self) -> unicode:
        """
        @see ghidra.program.model.data.Category#getName()
        """
        ...

    def getParent(self) -> ghidra.program.model.data.Category:
        """
        @see ghidra.program.model.data.Category#getParent()
        """
        ...

    def getRoot(self) -> ghidra.program.model.data.Category:
        """
        Get the root category.
        """
        ...

    def hashCode(self) -> int: ...

    def isDeleted(self) -> bool:
        """
        Returns true if this object has been deleted. Note: once an object has been deleted, it will
         never be "refreshed". For example, if an object is ever deleted and is resurrected via an
         "undo", you will have get a fresh instance of the object.
        @return true if this object has been deleted.
        """
        ...

    def isInvalid(self) -> bool:
        """
        Returns true if object is currently invalid. Calling checkIsValid may successfully refresh
         object making it valid.
        @see #checkIsValid()
        """
        ...

    def isRoot(self) -> bool:
        """
        @see ghidra.program.model.data.Category#isRoot()
        """
        ...

    def moveCategory(self, category: ghidra.program.model.data.Category, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        @see ghidra.program.model.data.Category#moveCategory(ghidra.program.model.data.Category, ghidra.util.task.TaskMonitor)
        """
        ...

    def moveDataType(self, movedDataType: ghidra.program.model.data.DataType, handler: ghidra.program.model.data.DataTypeConflictHandler) -> None:
        """
        @see ghidra.program.model.data.Category#moveDataType(ghidra.program.model.data.DataType, ghidra.program.model.data.DataTypeConflictHandler)
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def remove(self, type: ghidra.program.model.data.DataType, monitor: ghidra.util.task.TaskMonitor) -> bool:
        """
        @see ghidra.program.model.data.Category#remove(ghidra.program.model.data.DataType, ghidra.util.task.TaskMonitor)
        """
        ...

    def removeCategory(self, categoryName: unicode, monitor: ghidra.util.task.TaskMonitor) -> bool:
        """
        @see ghidra.program.model.data.Category#removeCategory(java.lang.String, ghidra.util.task.TaskMonitor)
        """
        ...

    def removeEmptyCategory(self, categoryName: unicode, monitor: ghidra.util.task.TaskMonitor) -> bool: ...

    def setInvalid(self) -> None:
        """
        Invalidate this object. This does not necessarily mean that this object can never be used
         again. If the object can refresh itself, it may still be useable.
        """
        ...

    def setName(self, newName: unicode) -> None:
        """
        @see ghidra.program.model.data.Category#setName(java.lang.String)
        """
        ...

    def toString(self) -> unicode:
        """
        @see java.lang.Object#toString()
        """
        ...

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
