from typing import List
import db
import ghidra.program.database
import ghidra.program.model.address
import ghidra.program.model.listing
import ghidra.util
import java.lang


class ModuleDB(ghidra.program.database.DatabaseObject, ghidra.program.model.listing.ProgramModule):
    """
    Database implementation for Module.
    """





    def __init__(self, cache: ghidra.program.database.DBObjectCache, key: long):
        """
        Constructs a new DatabaseObject and adds it to the specified cache.
        @param cache to be used for this object or null if object will not be cached
        @param key database key to uniquely identify this object
        """
        ...



    @overload
    def add(self, fragment: ghidra.program.model.listing.ProgramFragment) -> None:
        """
        @see ghidra.program.model.listing.ProgramModule#add(ghidra.program.model.listing.ProgramFragment)
        """
        ...

    @overload
    def add(self, module: ghidra.program.model.listing.ProgramModule) -> None:
        """
        @see ghidra.program.model.listing.ProgramModule#add(ghidra.program.model.listing.ProgramModule)
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

    @overload
    def contains(self, codeUnit: ghidra.program.model.listing.CodeUnit) -> bool:
        """
        @see ghidra.program.model.listing.Group#contains(ghidra.program.model.listing.CodeUnit)
        """
        ...

    @overload
    def contains(self, fragment: ghidra.program.model.listing.ProgramFragment) -> bool:
        """
        @see ghidra.program.model.listing.ProgramModule#contains(ghidra.program.model.listing.ProgramFragment)
        """
        ...

    @overload
    def contains(self, module: ghidra.program.model.listing.ProgramModule) -> bool:
        """
        @see ghidra.program.model.listing.ProgramModule#contains(ghidra.program.model.listing.ProgramModule)
        """
        ...

    def createFragment(self, fragmentName: unicode) -> ghidra.program.model.listing.ProgramFragment:
        """
        @see ghidra.program.model.listing.ProgramModule#createFragment(java.lang.String)
        """
        ...

    def createModule(self, moduleName: unicode) -> ghidra.program.model.listing.ProgramModule:
        """
        @see ghidra.program.model.listing.ProgramModule#createModule(java.lang.String)
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getAddressSet(self) -> ghidra.program.model.address.AddressSetView:
        """
        @see ghidra.program.model.listing.ProgramModule#getAddressSet()
        """
        ...

    def getChildren(self) -> List[ghidra.program.model.listing.Group]:
        """
        @see ghidra.program.model.listing.ProgramModule#getChildren()
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getComment(self) -> unicode:
        """
        @see ghidra.program.model.listing.Group#getComment()
        """
        ...

    def getFirstAddress(self) -> ghidra.program.model.address.Address:
        """
        @see ghidra.program.model.listing.ProgramModule#getFirstAddress()
        """
        ...

    def getIndex(self, name: unicode) -> int:
        """
        @see ghidra.program.model.listing.ProgramModule#getIndex(java.lang.String)
        """
        ...

    def getKey(self) -> long:
        """
        Get the database key for this object.
        """
        ...

    def getLastAddress(self) -> ghidra.program.model.address.Address:
        """
        @see ghidra.program.model.listing.ProgramModule#getLastAddress()
        """
        ...

    def getMaxAddress(self) -> ghidra.program.model.address.Address:
        """
        @see ghidra.program.model.listing.ProgramModule#getMaxAddress()
        """
        ...

    def getMinAddress(self) -> ghidra.program.model.address.Address:
        """
        @see ghidra.program.model.listing.ProgramModule#getMinAddress()
        """
        ...

    def getModificationNumber(self) -> long: ...

    def getName(self) -> unicode:
        """
        @see ghidra.program.model.listing.Group#getName()
        """
        ...

    def getNumChildren(self) -> int:
        """
        @see ghidra.program.model.listing.ProgramModule#getNumChildren()
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

    def getTreeID(self) -> long: ...

    def getTreeName(self) -> unicode:
        """
        @see ghidra.program.model.listing.Group#getTreeName()
        """
        ...

    def getVersionTag(self) -> object:
        """
        @see ghidra.program.model.listing.ProgramModule#getVersionTag()
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

    @overload
    def isDescendant(self, fragment: ghidra.program.model.listing.ProgramFragment) -> bool:
        """
        @see ghidra.program.model.listing.ProgramModule#isDescendant(ghidra.program.model.listing.ProgramFragment)
        """
        ...

    @overload
    def isDescendant(self, module: ghidra.program.model.listing.ProgramModule) -> bool:
        """
        @see ghidra.program.model.listing.ProgramModule#isDescendant(ghidra.program.model.listing.ProgramModule)
        """
        ...

    def isInvalid(self) -> bool:
        """
        Returns true if object is currently invalid. Calling checkIsValid may successfully refresh
         object making it valid.
        @see #checkIsValid()
        """
        ...

    def moveChild(self, name: unicode, index: int) -> None:
        """
        @see ghidra.program.model.listing.ProgramModule#moveChild(java.lang.String, int)
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def removeChild(self, name: unicode) -> bool:
        """
        @see ghidra.program.model.listing.ProgramModule#removeChild(java.lang.String)
        """
        ...

    def reparent(self, name: unicode, oldParent: ghidra.program.model.listing.ProgramModule) -> None:
        """
        @see ghidra.program.model.listing.ProgramModule#reparent(java.lang.String, ghidra.program.model.listing.ProgramModule)
        """
        ...

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
