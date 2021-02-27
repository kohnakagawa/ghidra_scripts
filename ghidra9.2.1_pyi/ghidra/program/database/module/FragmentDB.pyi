from typing import Iterator
from typing import List
import db
import ghidra.program.database
import ghidra.program.model.address
import ghidra.program.model.listing
import ghidra.util
import java.lang
import java.util
import java.util.function


class FragmentDB(ghidra.program.database.DatabaseObject, ghidra.program.model.listing.ProgramFragment):
    """
    Database implementation for Fragment.
    """





    def __init__(self, cache: ghidra.program.database.DBObjectCache, key: long):
        """
        Constructs a new DatabaseObject and adds it to the specified cache.
        @param cache to be used for this object or null if object will not be cached
        @param key database key to uniquely identify this object
        """
        ...

    def __iter__(self): ...

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

    @overload
    def contains(self, addr: ghidra.program.model.address.Address) -> bool:
        """
        @see ghidra.program.model.address.AddressSetView#contains(ghidra.program.model.address.Address)
        """
        ...

    @overload
    def contains(self, rangeSet: ghidra.program.model.address.AddressSetView) -> bool:
        """
        @see ghidra.program.model.address.AddressSetView#contains(ghidra.program.model.address.AddressSetView)
        """
        ...

    @overload
    def contains(self, codeUnit: ghidra.program.model.listing.CodeUnit) -> bool:
        """
        @see ghidra.program.model.listing.Group#contains(ghidra.program.model.listing.CodeUnit)
        """
        ...

    @overload
    def contains(self, start: ghidra.program.model.address.Address, end: ghidra.program.model.address.Address) -> bool:
        """
        @see ghidra.program.model.address.AddressSetView#contains(ghidra.program.model.address.Address, ghidra.program.model.address.Address)
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def findFirstAddressInCommon(self, set: ghidra.program.model.address.AddressSetView) -> ghidra.program.model.address.Address: ...

    def forEach(self, __a0: java.util.function.Consumer) -> None: ...

    @overload
    def getAddressRanges(self) -> ghidra.program.model.address.AddressRangeIterator:
        """
        @see ghidra.program.model.address.AddressSetView#getAddressRanges()
        """
        ...

    @overload
    def getAddressRanges(self, atStart: bool) -> ghidra.program.model.address.AddressRangeIterator:
        """
        @see ghidra.program.model.address.AddressSetView#getAddressRanges(boolean)
        """
        ...

    @overload
    def getAddressRanges(self, start: ghidra.program.model.address.Address, forward: bool) -> ghidra.program.model.address.AddressRangeIterator: ...

    @overload
    def getAddresses(self, forward: bool) -> ghidra.program.model.address.AddressIterator: ...

    @overload
    def getAddresses(self, start: ghidra.program.model.address.Address, forward: bool) -> ghidra.program.model.address.AddressIterator: ...

    def getClass(self) -> java.lang.Class: ...

    def getCodeUnits(self) -> ghidra.program.model.listing.CodeUnitIterator:
        """
        @see ghidra.program.model.listing.ProgramFragment#getCodeUnits()
        """
        ...

    def getComment(self) -> unicode:
        """
        @see ghidra.program.model.listing.Group#getComment()
        """
        ...

    def getFirstRange(self) -> ghidra.program.model.address.AddressRange: ...

    def getKey(self) -> long:
        """
        Get the database key for this object.
        """
        ...

    def getLastRange(self) -> ghidra.program.model.address.AddressRange: ...

    def getMaxAddress(self) -> ghidra.program.model.address.Address:
        """
        @see ghidra.program.model.address.AddressSetView#getMaxAddress()
        """
        ...

    def getMinAddress(self) -> ghidra.program.model.address.Address:
        """
        @see ghidra.program.model.address.AddressSetView#getMinAddress()
        """
        ...

    def getName(self) -> unicode:
        """
        @see ghidra.program.model.listing.Group#getName()
        """
        ...

    def getNumAddressRanges(self) -> int:
        """
        @see ghidra.program.model.address.AddressSetView#getNumAddressRanges()
        """
        ...

    def getNumAddresses(self) -> long:
        """
        @see ghidra.program.model.address.AddressSetView#getNumAddresses()
        """
        ...

    def getNumParents(self) -> int:
        """
        @see ghidra.program.model.listing.Group#getNumParents()
        """
        ...

    def getParentNames(self) -> List[unicode]:
        """
        @see ghidra.program.model.listing.Group#getParentNames()
        """
        ...

    def getParents(self) -> List[ghidra.program.model.listing.ProgramModule]:
        """
        @see ghidra.program.model.listing.Group#getParents()
        """
        ...

    def getRangeContaining(self, address: ghidra.program.model.address.Address) -> ghidra.program.model.address.AddressRange: ...

    def getTreeName(self) -> unicode:
        """
        @see ghidra.program.model.listing.Group#getTreeName()
        """
        ...

    def hasSameAddresses(self, view: ghidra.program.model.address.AddressSetView) -> bool:
        """
        @see ghidra.program.model.address.AddressSetView#equals(ghidra.program.model.address.AddressSetView)
        """
        ...

    def hashCode(self) -> int: ...

    def intersect(self, view: ghidra.program.model.address.AddressSetView) -> ghidra.program.model.address.AddressSet:
        """
        @see ghidra.program.model.address.AddressSetView#intersect(ghidra.program.model.address.AddressSetView)
        """
        ...

    def intersectRange(self, start: ghidra.program.model.address.Address, end: ghidra.program.model.address.Address) -> ghidra.program.model.address.AddressSet:
        """
        @see ghidra.program.model.address.AddressSetView#intersectRange(ghidra.program.model.address.Address, ghidra.program.model.address.Address)
        """
        ...

    @overload
    def intersects(self, set: ghidra.program.model.address.AddressSetView) -> bool:
        """
        @see ghidra.program.model.address.AddressSetView#intersects(ghidra.program.model.address.AddressSetView)
        """
        ...

    @overload
    def intersects(self, start: ghidra.program.model.address.Address, end: ghidra.program.model.address.Address) -> bool:
        """
        @see ghidra.program.model.address.AddressSetView#intersects(ghidra.program.model.address.Address, ghidra.program.model.address.Address)
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

    def isEmpty(self) -> bool:
        """
        @see ghidra.program.model.address.AddressSetView#isEmpty()
        """
        ...

    def isInvalid(self) -> bool:
        """
        Returns true if object is currently invalid. Calling checkIsValid may successfully refresh
         object making it valid.
        @see #checkIsValid()
        """
        ...

    @overload
    def iterator(self) -> Iterator[ghidra.program.model.address.AddressRange]: ...

    @overload
    def iterator(self, forward: bool) -> Iterator[ghidra.program.model.address.AddressRange]: ...

    @overload
    def iterator(self, start: ghidra.program.model.address.Address, forward: bool) -> Iterator[ghidra.program.model.address.AddressRange]: ...

    def move(self, min: ghidra.program.model.address.Address, max: ghidra.program.model.address.Address) -> None:
        """
        @see ghidra.program.model.listing.ProgramFragment#move(ghidra.program.model.address.Address, ghidra.program.model.address.Address)
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setComment(self, comment: unicode) -> None:
        """
        @see ghidra.program.model.listing.Group#setComment(java.lang.String)
        """
        ...

    def setInvalid(self) -> None:
        """
        Invalidate this object. This does not necessarily mean that this object can never be used
         again. If the object can refresh itself, it may still be useable.
        """
        ...

    def setName(self, name: unicode) -> None:
        """
        @see ghidra.program.model.listing.Group#setName(java.lang.String)
        """
        ...

    def spliterator(self) -> java.util.Spliterator: ...

    def subtract(self, set: ghidra.program.model.address.AddressSetView) -> ghidra.program.model.address.AddressSet:
        """
        @see ghidra.program.model.address.AddressSetView#subtract(ghidra.program.model.address.AddressSetView)
        """
        ...

    def toString(self) -> unicode: ...

    @staticmethod
    def trimEnd(__a0: ghidra.program.model.address.AddressSetView, __a1: ghidra.program.model.address.Address) -> ghidra.program.model.address.AddressSetView: ...

    @staticmethod
    def trimStart(__a0: ghidra.program.model.address.AddressSetView, __a1: ghidra.program.model.address.Address) -> ghidra.program.model.address.AddressSetView: ...

    def union(self, set: ghidra.program.model.address.AddressSetView) -> ghidra.program.model.address.AddressSet:
        """
        @see ghidra.program.model.address.AddressSetView#union(ghidra.program.model.address.AddressSetView)
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

    def xor(self, set: ghidra.program.model.address.AddressSetView) -> ghidra.program.model.address.AddressSet:
        """
        @see ghidra.program.model.address.AddressSetView#xor(ghidra.program.model.address.AddressSetView)
        """
        ...
