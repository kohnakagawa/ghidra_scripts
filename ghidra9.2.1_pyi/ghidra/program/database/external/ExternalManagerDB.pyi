from typing import List
import ghidra.program.database
import ghidra.program.database.symbol
import ghidra.program.model.address
import ghidra.program.model.listing
import ghidra.program.model.symbol
import ghidra.program.util
import ghidra.util.task
import java.lang


class ExternalManagerDB(object, ghidra.program.database.ManagerDB, ghidra.program.model.symbol.ExternalManager):
    """
    Manages the database for external references.
    """





    def __init__(self, handle: db.DBHandle, addrMap: ghidra.program.database.map.AddressMap, openMode: int, lock: ghidra.util.Lock, monitor: ghidra.util.task.TaskMonitor):
        """
        Constructs a new ExternalManagerDB
        @param handle the open database handle
        @param addrMap the address map
        @param openMode the program open mode.
        @param lock the program synchronization lock
        @param monitor the progress monitor used when upgrading
        @throws CancelledException if the user cancelled while an upgrade was occurring
        @throws IOException if a database io error occurs.
        @throws VersionException if the database version does not match the expected version
        """
        ...



    @overload
    def addExtFunction(self, extLibraryName: unicode, extLabel: unicode, extAddr: ghidra.program.model.address.Address, sourceType: ghidra.program.model.symbol.SourceType) -> ghidra.program.model.symbol.ExternalLocation: ...

    @overload
    def addExtFunction(self, extParentNamespace: ghidra.program.model.symbol.Namespace, extLabel: unicode, extAddr: ghidra.program.model.address.Address, sourceType: ghidra.program.model.symbol.SourceType) -> ghidra.program.model.symbol.ExternalLocation: ...

    @overload
    def addExtFunction(self, extNamespace: ghidra.program.model.symbol.Namespace, extLabel: unicode, extAddr: ghidra.program.model.address.Address, sourceType: ghidra.program.model.symbol.SourceType, reuseExisting: bool) -> ghidra.program.model.symbol.ExternalLocation: ...

    @overload
    def addExtLocation(self, extLibraryName: unicode, extLabel: unicode, extAddr: ghidra.program.model.address.Address, sourceType: ghidra.program.model.symbol.SourceType) -> ghidra.program.model.symbol.ExternalLocation: ...

    @overload
    def addExtLocation(self, extParentNamespace: ghidra.program.model.symbol.Namespace, extLabel: unicode, extAddr: ghidra.program.model.address.Address, sourceType: ghidra.program.model.symbol.SourceType) -> ghidra.program.model.symbol.ExternalLocation: ...

    @overload
    def addExtLocation(self, extParentNamespace: ghidra.program.model.symbol.Namespace, extLabel: unicode, extAddr: ghidra.program.model.address.Address, sourceType: ghidra.program.model.symbol.SourceType, reuseExisting: bool) -> ghidra.program.model.symbol.ExternalLocation: ...

    def addExternalLibraryName(self, name: unicode, source: ghidra.program.model.symbol.SourceType) -> ghidra.program.model.listing.Library: ...

    def contains(self, libraryName: unicode) -> bool:
        """
        @see ghidra.program.model.symbol.ExternalManager#contains(java.lang.String)
        """
        ...

    def deleteAddressRange(self, startAddr: ghidra.program.model.address.Address, endAddr: ghidra.program.model.address.Address, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        @see ghidra.program.database.ManagerDB#deleteAddressRange(ghidra.program.model.address.Address, ghidra.program.model.address.Address, ghidra.util.task.TaskMonitor)
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getDefaultExternalName(sym: ghidra.program.database.symbol.SymbolDB) -> unicode:
        """
        Get the default name for an external function or code symbol
        @param sym
        @return default name
        """
        ...

    def getExtLocation(self, externalAddr: ghidra.program.model.address.Address) -> ghidra.program.model.symbol.ExternalLocation:
        """
        Returns the external location associated with the given external address
        @param externalAddr the external address.
        """
        ...

    def getExternalLibrary(self, name: unicode) -> ghidra.program.model.listing.Library: ...

    def getExternalLibraryNames(self) -> List[unicode]:
        """
        @see ghidra.program.model.symbol.ExternalManager#getExternalLibraryNames()
        """
        ...

    def getExternalLibraryPath(self, externalName: unicode) -> unicode:
        """
        @see ghidra.program.model.symbol.ExternalManager#getExternalLibraryPath(java.lang.String)
        """
        ...

    @overload
    def getExternalLocation(self, symbol: ghidra.program.model.symbol.Symbol) -> ghidra.program.model.symbol.ExternalLocation: ...

    @overload
    def getExternalLocation(self, extName: unicode, extLabel: unicode) -> ghidra.program.model.symbol.ExternalLocation: ...

    @overload
    def getExternalLocation(self, extNamespace: ghidra.program.model.symbol.Namespace, extLabel: unicode) -> ghidra.program.model.symbol.ExternalLocation: ...

    @overload
    def getExternalLocations(self, externalName: unicode) -> ghidra.program.model.symbol.ExternalLocationIterator:
        """
        @see ghidra.program.model.symbol.ExternalManager#getExternalLocations(java.lang.String)
        """
        ...

    @overload
    def getExternalLocations(self, memoryAddress: ghidra.program.model.address.Address) -> ghidra.program.model.symbol.ExternalLocationIterator: ...

    @overload
    def getExternalLocations(self, libraryName: unicode, label: unicode) -> List[ghidra.program.model.symbol.ExternalLocation]: ...

    @overload
    def getExternalLocations(self, libScope: ghidra.program.model.symbol.Namespace, extLabel: unicode) -> List[ghidra.program.model.symbol.ExternalLocation]: ...

    @overload
    def getUniqueExternalLocation(self, libraryName: unicode, label: unicode) -> ghidra.program.model.symbol.ExternalLocation: ...

    @overload
    def getUniqueExternalLocation(self, namespace: ghidra.program.model.symbol.Namespace, label: unicode) -> ghidra.program.model.symbol.ExternalLocation: ...

    def hashCode(self) -> int: ...

    def invalidateCache(self, all: bool) -> None:
        """
        @see ghidra.program.database.ManagerDB#invalidateCache(boolean)
        """
        ...

    def moveAddressRange(self, fromAddr: ghidra.program.model.address.Address, toAddr: ghidra.program.model.address.Address, length: long, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        @see ghidra.program.database.ManagerDB#moveAddressRange(ghidra.program.model.address.Address, ghidra.program.model.address.Address, long, ghidra.util.task.TaskMonitor)
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def programReady(self, openMode: int, currentRevision: int, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        @see ghidra.program.database.ManagerDB#programReady(int, int, ghidra.util.task.TaskMonitor)
        """
        ...

    def removeExternalLibrary(self, name: unicode) -> bool:
        """
        @see ghidra.program.model.symbol.ExternalManager#removeExternalLibrary(java.lang.String)
        """
        ...

    def removeExternalLocation(self, externalAddr: ghidra.program.model.address.Address) -> bool:
        """
        Removes the external location at the given external address
        @param externalAddr the address at which to remove the external location.
        """
        ...

    def setExternalPath(self, externalName: unicode, externalPath: unicode, userDefined: bool) -> None: ...

    def setLanguage(self, translator: ghidra.program.util.LanguageTranslator, monitor: ghidra.util.task.TaskMonitor) -> None: ...

    def setProgram(self, program: ghidra.program.database.ProgramDB) -> None:
        """
        @see ghidra.program.database.ManagerDB#setProgram(ghidra.program.database.ProgramDB)
        """
        ...

    def toString(self) -> unicode: ...

    def updateExternalLibraryName(self, oldName: unicode, newName: unicode, source: ghidra.program.model.symbol.SourceType) -> None:
        """
        Update the external program for all references.
        @param oldName old external program name
        @param newName new external program name
        @param source the source of this external library:
         Symbol.DEFAULT, Symbol.ANALYSIS, Symbol.IMPORTED, or Symbol.USER_DEFINED
        @throws DuplicateNameException
        @throws InvalidInputException
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def externalLibraryNames(self) -> List[unicode]: ...

    @property
    def program(self) -> None: ...  # No getter available.

    @program.setter
    def program(self, value: ghidra.program.database.ProgramDB) -> None: ...
