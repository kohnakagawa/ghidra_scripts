import db
import ghidra.program.database
import ghidra.program.model.data
import ghidra.util
import java.lang


class SourceArchiveDB(ghidra.program.database.DatabaseObject, ghidra.program.model.data.SourceArchive):




    def __init__(self, dtMgr: ghidra.program.database.data.DataTypeManagerDB, cache: ghidra.program.database.DBObjectCache, adapter: ghidra.program.database.data.SourceArchiveAdapter, record: db.Record): ...



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

    def equals(self, __a0: object) -> bool: ...

    def getArchiveType(self) -> ghidra.program.model.data.ArchiveType:
        """
        Gets an indicator for the type of data type archive.
         (PROGRAM_TYPE, PROJECT_TYPE, FILE_TYPE)
        @return the type
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getDomainFileID(self) -> unicode:
        """
        Gets the ID used to uniquely identify the domain file for the data type archive.
        @return the domain file identifier
        """
        ...

    def getKey(self) -> long:
        """
        Get the database key for this object.
        """
        ...

    def getLastSyncTime(self) -> long: ...

    def getName(self) -> unicode: ...

    def getSourceArchiveID(self) -> ghidra.util.UniversalID:
        """
        Gets the ID that the program has associated with the data type archive.
        @return the data type archive ID
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

    def isDirty(self) -> bool: ...

    def isInvalid(self) -> bool:
        """
        Returns true if object is currently invalid. Calling checkIsValid may successfully refresh
         object making it valid.
        @see #checkIsValid()
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setDirtyFlag(self, isDirty: bool) -> None: ...

    def setInvalid(self) -> None:
        """
        Invalidate this object. This does not necessarily mean that this object can never be used
         again. If the object can refresh itself, it may still be useable.
        """
        ...

    def setLastSyncTime(self, syncTime: long) -> None: ...

    def setName(self, newName: unicode) -> None: ...

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

    @property
    def archiveType(self) -> ghidra.program.model.data.ArchiveType: ...

    @property
    def dirty(self) -> bool: ...

    @property
    def dirtyFlag(self) -> None: ...  # No getter available.

    @dirtyFlag.setter
    def dirtyFlag(self, value: bool) -> None: ...

    @property
    def domainFileID(self) -> unicode: ...

    @property
    def lastSyncTime(self) -> long: ...

    @lastSyncTime.setter
    def lastSyncTime(self, value: long) -> None: ...

    @property
    def name(self) -> unicode: ...

    @name.setter
    def name(self, value: unicode) -> None: ...

    @property
    def sourceArchiveID(self) -> ghidra.util.UniversalID: ...
