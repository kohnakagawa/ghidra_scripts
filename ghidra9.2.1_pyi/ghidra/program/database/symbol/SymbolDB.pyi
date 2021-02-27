from typing import List
import db
import ghidra.program.database
import ghidra.program.model.address
import ghidra.program.model.listing
import ghidra.program.model.symbol
import ghidra.program.util
import ghidra.util
import ghidra.util.task
import java.lang


class SymbolDB(ghidra.program.database.DatabaseObject, ghidra.program.model.symbol.Symbol):
    """
    Base class for symbols
    """









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

    def delete(self) -> bool: ...

    def equals(self, obj: object) -> bool: ...

    def getAddress(self) -> ghidra.program.model.address.Address: ...

    def getClass(self) -> java.lang.Class: ...

    def getID(self) -> long: ...

    def getKey(self) -> long:
        """
        Get the database key for this object.
        """
        ...

    @overload
    def getName(self) -> unicode: ...

    @overload
    def getName(self, includeNamespace: bool) -> unicode: ...

    def getObject(self) -> object: ...

    def getParentNamespace(self) -> ghidra.program.model.symbol.Namespace: ...

    def getParentSymbol(self) -> ghidra.program.model.symbol.Symbol: ...

    def getPath(self) -> List[unicode]: ...

    def getProgram(self) -> ghidra.program.model.listing.Program: ...

    def getProgramLocation(self) -> ghidra.program.util.ProgramLocation: ...

    def getReferenceCount(self) -> int: ...

    @overload
    def getReferences(self) -> List[ghidra.program.model.symbol.Reference]: ...

    @overload
    def getReferences(self, monitor: ghidra.util.task.TaskMonitor) -> List[ghidra.program.model.symbol.Reference]: ...

    def getSource(self) -> ghidra.program.model.symbol.SourceType: ...

    def getSymbolData1(self) -> long: ...

    def getSymbolData2(self) -> int:
        """
        gets the generic symbol data 2 data.
        @return the symbol data
        """
        ...

    def getSymbolData3(self) -> unicode: ...

    def getSymbolType(self) -> ghidra.program.model.symbol.SymbolType: ...

    def hasMultipleReferences(self) -> bool: ...

    def hasReferences(self) -> bool: ...

    def hashCode(self) -> int: ...

    def isDeleted(self) -> bool:
        """
        Returns true if this object has been deleted. Note: once an object has been deleted, it will
         never be "refreshed". For example, if an object is ever deleted and is resurrected via an
         "undo", you will have get a fresh instance of the object.
        @return true if this object has been deleted.
        """
        ...

    def isDeleting(self) -> bool: ...

    def isDescendant(self, namespace: ghidra.program.model.symbol.Namespace) -> bool: ...

    def isDynamic(self) -> bool: ...

    def isExternal(self) -> bool: ...

    def isExternalEntryPoint(self) -> bool: ...

    def isGlobal(self) -> bool: ...

    def isInvalid(self) -> bool:
        """
        Returns true if object is currently invalid. Calling checkIsValid may successfully refresh
         object making it valid.
        @see #checkIsValid()
        """
        ...

    def isPinned(self) -> bool: ...

    def isPrimary(self) -> bool: ...

    def isValidParent(self, parent: ghidra.program.model.symbol.Namespace) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setInvalid(self) -> None:
        """
        Invalidate this object. This does not necessarily mean that this object can never be used
         again. If the object can refresh itself, it may still be useable.
        """
        ...

    def setName(self, newName: unicode, source: ghidra.program.model.symbol.SourceType) -> None: ...

    def setNameAndNamespace(self, newName: unicode, newNamespace: ghidra.program.model.symbol.Namespace, source: ghidra.program.model.symbol.SourceType) -> None: ...

    def setNamespace(self, newNamespace: ghidra.program.model.symbol.Namespace) -> None: ...

    def setPinned(self, pinned: bool) -> None: ...

    def setPrimary(self) -> bool:
        """
        @see ghidra.program.model.symbol.Symbol#setPrimary()
        """
        ...

    def setSource(self, newSource: ghidra.program.model.symbol.SourceType) -> None:
        """
        Sets this symbol's source as specified.
        @param newSource the new source type (IMPORTED, ANALYSIS, USER_DEFINED)
        @throws IllegalArgumentException if you try to change the source from default or to default
        """
        ...

    def setSymbolData1(self, value: long) -> None:
        """
        Sets the generic symbol data 1.
        @param value the value to set as symbol data 1.
        """
        ...

    def setSymbolData2(self, value: int) -> None:
        """
        Sets the generic symbol data 2 data
        @param value the value to set as the symbols data 2 value.
        """
        ...

    def setSymbolData3(self, data3: unicode) -> None: ...

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
    def ID(self) -> long: ...

    @property
    def address(self) -> ghidra.program.model.address.Address: ...

    @property
    def deleting(self) -> bool: ...

    @property
    def dynamic(self) -> bool: ...

    @property
    def externalEntryPoint(self) -> bool: ...

    @property
    def global(self) -> bool: ...

    @property
    def name(self) -> unicode: ...

    @property
    def namespace(self) -> None: ...  # No getter available.

    @namespace.setter
    def namespace(self, value: ghidra.program.model.symbol.Namespace) -> None: ...

    @property
    def parentNamespace(self) -> ghidra.program.model.symbol.Namespace: ...

    @property
    def parentSymbol(self) -> ghidra.program.model.symbol.Symbol: ...

    @property
    def path(self) -> List[unicode]: ...

    @property
    def pinned(self) -> bool: ...

    @pinned.setter
    def pinned(self, value: bool) -> None: ...

    @property
    def primary(self) -> bool: ...

    @property
    def program(self) -> ghidra.program.model.listing.Program: ...

    @property
    def referenceCount(self) -> int: ...

    @property
    def references(self) -> List[ghidra.program.model.symbol.Reference]: ...

    @property
    def source(self) -> ghidra.program.model.symbol.SourceType: ...

    @source.setter
    def source(self, value: ghidra.program.model.symbol.SourceType) -> None: ...

    @property
    def symbolData1(self) -> long: ...

    @symbolData1.setter
    def symbolData1(self, value: long) -> None: ...

    @property
    def symbolData2(self) -> int: ...

    @symbolData2.setter
    def symbolData2(self, value: int) -> None: ...

    @property
    def symbolData3(self) -> unicode: ...

    @symbolData3.setter
    def symbolData3(self, value: unicode) -> None: ...
