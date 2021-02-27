from typing import List
import db
import ghidra.program.database
import ghidra.program.model.address
import ghidra.program.model.symbol
import ghidra.util
import java.lang


class EquateDB(ghidra.program.database.DatabaseObject, ghidra.program.model.symbol.Equate):
    """
    Database object for an Equate.
    """





    def __init__(self, equateMgr: ghidra.program.database.symbol.EquateManager, cache: ghidra.program.database.DBObjectCache, record: db.Record):
        """
        Constructor
        @param equateMgr the equate manager
        @param cache EquateDB cache
        @param record the record for this equate.
        """
        ...



    @overload
    def addReference(self, refAddr: ghidra.program.model.address.Address, opIndex: int) -> None:
        """
        @see ghidra.program.model.symbol.Equate#addReference(ghidra.program.model.address.Address, int)
        """
        ...

    @overload
    def addReference(self, dynamicHash: long, refAddr: ghidra.program.model.address.Address) -> None:
        """
        @see ghidra.program.model.symbol.Equate#addReference(long, ghidra.program.model.address.Address)
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

    def equals(self, obj: object) -> bool:
        """
        @see java.lang.Object#equals(Object)
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getDisplayName(self) -> unicode: ...

    def getDisplayValue(self) -> unicode:
        """
        @see ghidra.program.model.symbol.Equate#getDisplayValue()
        """
        ...

    def getEnumUUID(self) -> ghidra.util.UniversalID: ...

    def getKey(self) -> long:
        """
        Get the database key for this object.
        """
        ...

    def getName(self) -> unicode:
        """
        @see ghidra.program.model.symbol.Equate#getName()
        """
        ...

    def getReferenceCount(self) -> int:
        """
        @see ghidra.program.model.symbol.Equate#getReferenceCount()
        """
        ...

    def getReferences(self) -> List[ghidra.program.model.symbol.EquateReference]:
        """
        @see ghidra.program.model.symbol.Equate#getReferences()
        """
        ...

    def getValue(self) -> long:
        """
        @see ghidra.program.model.symbol.Equate#getValue()
        """
        ...

    def hashCode(self) -> int:
        """
        @see java.lang.Object#hashCode()
        """
        ...

    def isDeleted(self) -> bool:
        """
        Returns true if this object has been deleted. Note: once an object has been deleted, it will
         never be "refreshed". For example, if an object is ever deleted and is resurrected via an
         "undo", you will have get a fresh instance of the object.
        @return true if this object has been deleted.
        """
        ...

    def isEnumBased(self) -> bool: ...

    def isInvalid(self) -> bool:
        """
        Returns true if object is currently invalid. Calling checkIsValid may successfully refresh
         object making it valid.
        @see #checkIsValid()
        """
        ...

    def isValidUUID(self) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @overload
    def removeReference(self, refAddr: ghidra.program.model.address.Address, opIndex: int) -> None:
        """
        @see ghidra.program.model.symbol.Equate#removeReference(ghidra.program.model.address.Address, int)
        """
        ...

    @overload
    def removeReference(self, dynamicHash: long, refAddr: ghidra.program.model.address.Address) -> None:
        """
        @see ghidra.program.model.symbol.Equate#removeReference(long, ghidra.program.model.address.Address)
        """
        ...

    def renameEquate(self, newName: unicode) -> None:
        """
        @see ghidra.program.model.symbol.Equate#renameEquate(java.lang.String)
        """
        ...

    def setInvalid(self) -> None:
        """
        Invalidate this object. This does not necessarily mean that this object can never be used
         again. If the object can refresh itself, it may still be useable.
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

    @property
    def displayName(self) -> unicode: ...

    @property
    def displayValue(self) -> unicode: ...

    @property
    def enumBased(self) -> bool: ...

    @property
    def enumUUID(self) -> ghidra.util.UniversalID: ...

    @property
    def name(self) -> unicode: ...

    @property
    def referenceCount(self) -> int: ...

    @property
    def references(self) -> List[ghidra.program.model.symbol.EquateReference]: ...

    @property
    def validUUID(self) -> bool: ...

    @property
    def value(self) -> long: ...
