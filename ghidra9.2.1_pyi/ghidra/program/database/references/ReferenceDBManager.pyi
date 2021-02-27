from typing import List
import db.util
import ghidra.program.database
import ghidra.program.model.address
import ghidra.program.model.lang
import ghidra.program.model.listing
import ghidra.program.model.symbol
import ghidra.util.task
import java.io
import java.lang


class ReferenceDBManager(object, ghidra.program.model.symbol.ReferenceManager, ghidra.program.database.ManagerDB, db.util.ErrorHandler):
    """
    Reference manager implementation for the database.
    """

    MNEMONIC: int = -1



    def __init__(self, dbHandle: db.DBHandle, addrMap: ghidra.program.database.map.AddressMap, openMode: int, lock: ghidra.util.Lock, monitor: ghidra.util.task.TaskMonitor):
        """
        Construct a new reference manager.
        @param dbHandle handle to the database
        @param addrMap map to convert addresses to longs and longs to addresses
        @param openMode one of ProgramDB.CREATE, UPDATE, UPGRADE, or READ_ONLY
        @param lock the program synchronization lock
        @param monitor Task monitor for upgrading
        @throws IOException if a database io error occurs.
        @throws VersionException if the database version is different from the expected version
        """
        ...



    def addExternalEntryPointRef(self, toAddr: ghidra.program.model.address.Address) -> None:
        """
        Create a memory reference to the given address to mark it as
         an external entry point.
        @param toAddr the address at which to make an external entry point
        """
        ...

    @overload
    def addExternalReference(self, fromAddr: ghidra.program.model.address.Address, opIndex: int, location: ghidra.program.model.symbol.ExternalLocation, sourceType: ghidra.program.model.symbol.SourceType, type: ghidra.program.model.symbol.RefType) -> ghidra.program.model.symbol.Reference: ...

    @overload
    def addExternalReference(self, fromAddr: ghidra.program.model.address.Address, libraryName: unicode, extLabel: unicode, extAddr: ghidra.program.model.address.Address, sourceType: ghidra.program.model.symbol.SourceType, opIndex: int, type: ghidra.program.model.symbol.RefType) -> ghidra.program.model.symbol.Reference: ...

    @overload
    def addExternalReference(self, fromAddr: ghidra.program.model.address.Address, extNamespace: ghidra.program.model.symbol.Namespace, extLabel: unicode, extAddr: ghidra.program.model.address.Address, sourceType: ghidra.program.model.symbol.SourceType, opIndex: int, type: ghidra.program.model.symbol.RefType) -> ghidra.program.model.symbol.Reference: ...

    def addMemoryReference(self, fromAddr: ghidra.program.model.address.Address, toAddr: ghidra.program.model.address.Address, type: ghidra.program.model.symbol.RefType, sourceType: ghidra.program.model.symbol.SourceType, opIndex: int) -> ghidra.program.model.symbol.Reference: ...

    def addOffsetMemReference(self, fromAddr: ghidra.program.model.address.Address, toAddr: ghidra.program.model.address.Address, offset: long, type: ghidra.program.model.symbol.RefType, sourceType: ghidra.program.model.symbol.SourceType, opIndex: int) -> ghidra.program.model.symbol.Reference: ...

    def addReference(self, ref: ghidra.program.model.symbol.Reference) -> ghidra.program.model.symbol.Reference: ...

    def addRegisterReference(self, fromAddr: ghidra.program.model.address.Address, opIndex: int, register: ghidra.program.model.lang.Register, type: ghidra.program.model.symbol.RefType, sourceType: ghidra.program.model.symbol.SourceType) -> ghidra.program.model.symbol.Reference: ...

    def addShiftedMemReference(self, fromAddr: ghidra.program.model.address.Address, toAddr: ghidra.program.model.address.Address, shiftValue: int, type: ghidra.program.model.symbol.RefType, sourceType: ghidra.program.model.symbol.SourceType, opIndex: int) -> ghidra.program.model.symbol.Reference: ...

    def addStackReference(self, fromAddr: ghidra.program.model.address.Address, opIndex: int, stackOffset: int, type: ghidra.program.model.symbol.RefType, sourceType: ghidra.program.model.symbol.SourceType) -> ghidra.program.model.symbol.Reference: ...

    def dbError(self, e: java.io.IOException) -> None: ...

    def delete(self, ref: ghidra.program.model.symbol.Reference) -> None: ...

    def deleteAddressRange(self, startAddr: ghidra.program.model.address.Address, endAddr: ghidra.program.model.address.Address, monitor: ghidra.util.task.TaskMonitor) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getExternalEntryIterator(self) -> ghidra.program.model.address.AddressIterator:
        """
        Get address iterator over references that are external entry
         mem references.
        """
        ...

    def getExternalReferences(self) -> ghidra.program.model.symbol.ReferenceIterator: ...

    def getFlowReferencesFrom(self, addr: ghidra.program.model.address.Address) -> List[ghidra.program.model.symbol.Reference]: ...

    def getPrimaryReferenceFrom(self, addr: ghidra.program.model.address.Address, opIndex: int) -> ghidra.program.model.symbol.Reference: ...

    def getReference(self, fromAddr: ghidra.program.model.address.Address, toAddr: ghidra.program.model.address.Address, opIndex: int) -> ghidra.program.model.symbol.Reference: ...

    def getReferenceCountFrom(self, fromAddr: ghidra.program.model.address.Address) -> int: ...

    def getReferenceCountTo(self, toAddr: ghidra.program.model.address.Address) -> int: ...

    def getReferenceDestinationCount(self) -> int: ...

    @overload
    def getReferenceDestinationIterator(self, startAddr: ghidra.program.model.address.Address, forward: bool) -> ghidra.program.model.address.AddressIterator: ...

    @overload
    def getReferenceDestinationIterator(self, addrSet: ghidra.program.model.address.AddressSetView, forward: bool) -> ghidra.program.model.address.AddressIterator: ...

    def getReferenceIterator(self, startAddr: ghidra.program.model.address.Address) -> ghidra.program.model.symbol.ReferenceIterator: ...

    def getReferenceLevel(self, toAddr: ghidra.program.model.address.Address) -> int:
        """
        Returns the reference level for the references to the given address
        @param toAddr the address at which to find the highest reference level
        """
        ...

    def getReferenceSourceCount(self) -> int: ...

    @overload
    def getReferenceSourceIterator(self, startAddr: ghidra.program.model.address.Address, forward: bool) -> ghidra.program.model.address.AddressIterator: ...

    @overload
    def getReferenceSourceIterator(self, addrSet: ghidra.program.model.address.AddressSetView, forward: bool) -> ghidra.program.model.address.AddressIterator: ...

    def getReferencedVariable(self, reference: ghidra.program.model.symbol.Reference) -> ghidra.program.model.listing.Variable:
        """
        Attempts to determine which if any of the local functions variables are referenced by the specified
         reference.  In utilizing the firstUseOffset scoping model, negative offsets (relative to the functions
         entry) are shifted beyond the maximum positive offset within the function.  While this does not account for the
         actual instruction flow, it is hopefully accurate enough for most situations.
        @see ghidra.program.model.symbol.ReferenceManager#getReferencedVariable(ghidra.program.model.symbol.Reference)
        """
        ...

    def getReferences(self, fromAddr: ghidra.program.model.address.Address, opIndex: int) -> List[ghidra.program.model.symbol.Reference]:
        """
        Get all memory references with the given from address at opIndex.
        """
        ...

    @overload
    def getReferencesFrom(self, addr: ghidra.program.model.address.Address) -> List[ghidra.program.model.symbol.Reference]: ...

    @overload
    def getReferencesFrom(self, fromAddr: ghidra.program.model.address.Address, opIndex: int) -> List[ghidra.program.model.symbol.Reference]: ...

    @overload
    def getReferencesTo(self, addr: ghidra.program.model.address.Address) -> ghidra.program.model.symbol.ReferenceIterator: ...

    @overload
    def getReferencesTo(self, var: ghidra.program.model.listing.Variable) -> List[ghidra.program.model.symbol.Reference]:
        """
        Attempts to determine the set of references which refer to the specified variable.
         In utilizing the firstUseOffset scoping model, negative offsets (relative to the functions
         entry) are shifted beyond the maximum positive offset within the function.  While this does not account for the
         actual instruction flow, it is hopefully accurate enough for most situations.
        @see ghidra.program.model.symbol.ReferenceManager#getReferencesTo(ghidra.program.model.listing.Variable)
        """
        ...

    def hasFlowReferencesFrom(self, addr: ghidra.program.model.address.Address) -> bool: ...

    @overload
    def hasReferencesFrom(self, fromAddr: ghidra.program.model.address.Address) -> bool: ...

    @overload
    def hasReferencesFrom(self, fromAddr: ghidra.program.model.address.Address, opIndex: int) -> bool: ...

    def hasReferencesTo(self, toAddr: ghidra.program.model.address.Address) -> bool: ...

    def hashCode(self) -> int: ...

    def invalidateCache(self, all: bool) -> None: ...

    def isExternalEntryPoint(self, toAddr: ghidra.program.model.address.Address) -> bool:
        """
        Return whether the address is an external entry point.
        @param toAddr the address to test for external entry point
        """
        ...

    def moveAddressRange(self, fromAddr: ghidra.program.model.address.Address, toAddr: ghidra.program.model.address.Address, length: long, monitor: ghidra.util.task.TaskMonitor) -> None: ...

    def moveReferencesTo(self, oldToAddr: ghidra.program.model.address.Address, newToAddr: ghidra.program.model.address.Address, monitor: ghidra.util.task.TaskMonitor) -> int:
        """
        Move all references to the specified oldAddr.  Any symbol binding will be discarded since
         these are intended for memory label references only.
         This method is intended specifically to support upgrading of certain references
         (i.e., Stack, Register and External addresses).
         NOTE! After ProgramDB version 12, this method will no longer be useful for
         upgrading stack and register references since they will not exist
         within the ReferenceTo-list.
        @param oldToAddr old reference to address
        @param newToAddr new reference to address
        @return number of references updated
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def programReady(self, openMode: int, currentRevision: int, monitor: ghidra.util.task.TaskMonitor) -> None: ...

    @overload
    def removeAllReferencesFrom(self, fromAddr: ghidra.program.model.address.Address) -> None: ...

    @overload
    def removeAllReferencesFrom(self, beginAddr: ghidra.program.model.address.Address, endAddr: ghidra.program.model.address.Address) -> None: ...

    def removeAssociation(self, ref: ghidra.program.model.symbol.Reference) -> None: ...

    def removeExternalEntryPoint(self, addr: ghidra.program.model.address.Address) -> None:
        """
        Removes the external entry point at the given address
        @param addr that address at which to remove the external entry point attribute.
        """
        ...

    def setAssociation(self, s: ghidra.program.model.symbol.Symbol, ref: ghidra.program.model.symbol.Reference) -> None: ...

    def setPrimary(self, ref: ghidra.program.model.symbol.Reference, isPrimary: bool) -> None: ...

    def setProgram(self, program: ghidra.program.database.ProgramDB) -> None: ...

    def symbolAdded(self, sym: ghidra.program.model.symbol.Symbol) -> None:
        """
        Symbol has been added
        @param sym new symbol
        """
        ...

    def symbolRemoved(self, symbol: ghidra.program.model.symbol.Symbol) -> None:
        """
        Symbol is about to be removed.
         symbol becomes unusable.
        @param symbol
        """
        ...

    def toString(self) -> unicode: ...

    def updateRefType(self, ref: ghidra.program.model.symbol.Reference, refType: ghidra.program.model.symbol.RefType) -> ghidra.program.model.symbol.Reference: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def externalEntryIterator(self) -> ghidra.program.model.address.AddressIterator: ...

    @property
    def externalReferences(self) -> ghidra.program.model.symbol.ReferenceIterator: ...

    @property
    def program(self) -> None: ...  # No getter available.

    @program.setter
    def program(self, value: ghidra.program.database.ProgramDB) -> None: ...

    @property
    def referenceDestinationCount(self) -> int: ...

    @property
    def referenceSourceCount(self) -> int: ...
