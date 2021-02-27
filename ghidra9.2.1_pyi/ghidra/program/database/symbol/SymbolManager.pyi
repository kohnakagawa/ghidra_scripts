from typing import Iterator
from typing import List
import db
import ghidra.program.database
import ghidra.program.database.symbol
import ghidra.program.model.address
import ghidra.program.model.listing
import ghidra.program.model.symbol
import ghidra.program.util
import ghidra.util.task
import java.lang


class SymbolManager(object, ghidra.program.model.symbol.SymbolTable, ghidra.program.database.ManagerDB):




    def __init__(self, handle: db.DBHandle, addrMap: ghidra.program.database.map.AddressMap, openMode: int, lock: ghidra.util.Lock, monitor: ghidra.util.task.TaskMonitor):
        """
        Creates a new Symbol manager.
        @param handle the database handler
        @param addrMap the address map.
        @param openMode the open mode.
        @param lock the program synchronization lock
        @param monitor the progress monitor used when upgrading.
        @throws CancelledException if the user cancels the upgrade.
        @throws IOException if a database io error occurs.
        @throws VersionException if the database version doesn't match the current version.
        """
        ...



    def addExternalEntryPoint(self, addr: ghidra.program.model.address.Address) -> None: ...

    def createClass(self, parent: ghidra.program.model.symbol.Namespace, name: unicode, source: ghidra.program.model.symbol.SourceType) -> ghidra.program.model.listing.GhidraClass: ...

    def createCodeSymbol(self, addr: ghidra.program.model.address.Address, name: unicode, namespace: ghidra.program.model.symbol.Namespace, source: ghidra.program.model.symbol.SourceType, data3: unicode) -> ghidra.program.model.symbol.Symbol:
        """
        Internal method for creating label symbols.
        @param addr the address for the new symbol
        @param name the name of the new symbol
        @param namespace the namespace for the new symbol
        @param source the SourceType of the new symbol
        @param data3 special use depending on the symbol type and whether or not it is external
        @return the new symbol
        @throws InvalidInputException if the name contains illegal characters (i.e. space)
        """
        ...

    def createExternalLibrary(self, name: unicode, source: ghidra.program.model.symbol.SourceType) -> ghidra.program.model.listing.Library: ...

    def createFunctionSymbol(self, addr: ghidra.program.model.address.Address, name: unicode, namespace: ghidra.program.model.symbol.Namespace, source: ghidra.program.model.symbol.SourceType, data3: unicode) -> ghidra.program.model.symbol.Symbol:
        """
        Internal method for creating funcions symbols.
        @param addr the address for the new symbol
        @param name the name of the new symbol
        @param namespace the namespace for the new symbol
        @param source the SourceType of the new symbol
        @param data3 special use depending on the symbol type and whether or not it is external.
        @return the new symbol
        @throws InvalidInputException if the name contains illegal characters (i.e. space)
        """
        ...

    @overload
    def createLabel(self, addr: ghidra.program.model.address.Address, name: unicode, source: ghidra.program.model.symbol.SourceType) -> ghidra.program.model.symbol.Symbol: ...

    @overload
    def createLabel(self, addr: ghidra.program.model.address.Address, name: unicode, namespace: ghidra.program.model.symbol.Namespace, source: ghidra.program.model.symbol.SourceType) -> ghidra.program.model.symbol.Symbol: ...

    def createNameSpace(self, parent: ghidra.program.model.symbol.Namespace, name: unicode, source: ghidra.program.model.symbol.SourceType) -> ghidra.program.model.symbol.Namespace: ...

    def createSpecialSymbol(self, addr: ghidra.program.model.address.Address, name: unicode, parent: ghidra.program.model.symbol.Namespace, symbolType: ghidra.program.model.symbol.SymbolType, data1: long, data2: int, data3: unicode, source: ghidra.program.model.symbol.SourceType) -> ghidra.program.database.symbol.SymbolDB:
        """
        Creates a symbol, specifying all information for the record.  This method is not on the
         public interface and is only intended for program API internal use.  The user of this
         method must carefully provided exactly the information needed depending on the type of symbol
         being created.
        @param addr the address for the symbol
        @param name the name of the symbol
        @param parent the namespace for the symbol
        @param symbolType the type of the symbol
        @param data1 long value whose meaning depends on the symbol type.
        @param data2 int value whose meaning depends on the symbol type.
        @param data3 string value whose meaning depends on the symbol type.
        @param source the SourceType for the new symbol
        @return the newly created symbol
        @throws DuplicateNameException if the symbol type must be unique and another already has that name
         	       in the given namespace.
        @throws InvalidInputException if the name contains any illegal characters (i.e. space)
        """
        ...

    @overload
    def createSymbol(self, addr: ghidra.program.model.address.Address, name: unicode, source: ghidra.program.model.symbol.SourceType) -> ghidra.program.model.symbol.Symbol: ...

    @overload
    def createSymbol(self, addr: ghidra.program.model.address.Address, name: unicode, namespace: ghidra.program.model.symbol.Namespace, source: ghidra.program.model.symbol.SourceType) -> ghidra.program.model.symbol.Symbol: ...

    def createSymbolPlaceholder(self, address: ghidra.program.model.address.Address, id: long) -> ghidra.program.model.symbol.Symbol: ...

    def createVariableSymbol(self, name: unicode, namespace: ghidra.program.model.symbol.Namespace, type: ghidra.program.model.symbol.SymbolType, firstUseOffsetOrOrdinal: int, storage: ghidra.program.model.listing.VariableStorage, source: ghidra.program.model.symbol.SourceType) -> ghidra.program.database.symbol.VariableSymbolDB:
        """
        Creates variable symbols. Note this is not a method defined in the Symbol Table interface.
         It is intended to be used by Ghidra program internals.
        @param name the name of the variable
        @param namespace the function that contains the variable.
        @param type the type of the variable (can only be PARAMETER or LOCAL_VAR)
        @param firstUseOffsetOrOrdinal the offset in the function where the variable is first used.
        @param storage the VariableStorage (stack, registers, etc.)
        @param source the symbol source type (user defined, analysis, etc.)
        @return the new VariableSymbol that was created.
        @throws DuplicateNameException if there is another variable in this function with that name.
        @throws InvalidInputException if the name contains illegal characters (space for example)
        """
        ...

    def deleteAddressRange(self, startAddr: ghidra.program.model.address.Address, endAddr: ghidra.program.model.address.Address, monitor: ghidra.util.task.TaskMonitor) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def findVariableStorageAddress(self, storage: ghidra.program.model.listing.VariableStorage) -> ghidra.program.model.address.Address:
        """
        Find previously defined variable storage address
        @param storage variable storage
        @return previously defined variable storage address or null if not found
        @throws IOException
        """
        ...

    def getAllSymbols(self, includeDynamicSymbols: bool) -> ghidra.program.model.symbol.SymbolIterator: ...

    def getChildren(self, parentSymbol: ghidra.program.model.symbol.Symbol) -> ghidra.program.model.symbol.SymbolIterator: ...

    def getClass(self) -> java.lang.Class: ...

    def getClassNamespaces(self) -> Iterator[ghidra.program.model.listing.GhidraClass]: ...

    def getClassSymbol(self, name: unicode, namespace: ghidra.program.model.symbol.Namespace) -> ghidra.program.model.symbol.Symbol: ...

    def getDefinedSymbols(self) -> ghidra.program.model.symbol.SymbolIterator: ...

    def getDynamicSymbolID(self, addr: ghidra.program.model.address.Address) -> long: ...

    def getExternalEntryPointIterator(self) -> ghidra.program.model.address.AddressIterator: ...

    def getExternalSymbol(self, name: unicode) -> ghidra.program.model.symbol.Symbol: ...

    @overload
    def getExternalSymbols(self) -> ghidra.program.model.symbol.SymbolIterator: ...

    @overload
    def getExternalSymbols(self, name: unicode) -> ghidra.program.model.symbol.SymbolIterator: ...

    def getGlobalSymbol(self, name: unicode, addr: ghidra.program.model.address.Address) -> ghidra.program.model.symbol.Symbol: ...

    def getGlobalSymbols(self, name: unicode) -> List[ghidra.program.model.symbol.Symbol]: ...

    @overload
    def getLabelHistory(self) -> Iterator[ghidra.program.model.symbol.LabelHistory]: ...

    @overload
    def getLabelHistory(self, addr: ghidra.program.model.address.Address) -> List[ghidra.program.model.symbol.LabelHistory]: ...

    def getLabelOrFunctionSymbols(self, name: unicode, namespace: ghidra.program.model.symbol.Namespace) -> List[ghidra.program.model.symbol.Symbol]: ...

    def getLibrarySymbol(self, name: unicode) -> ghidra.program.model.symbol.Symbol: ...

    def getLocalVariableSymbol(self, name: unicode, namespace: ghidra.program.model.symbol.Namespace) -> ghidra.program.model.symbol.Symbol: ...

    def getMaxSymbolAddress(self, space: ghidra.program.model.address.AddressSpace) -> ghidra.program.model.address.Address:
        """
        Returns the maximum symbol address within the specified address space.
        @param space address space
        @return maximum symbol address within space or null if none are found.
        """
        ...

    @overload
    def getNamespace(self, addr: ghidra.program.model.address.Address) -> ghidra.program.model.symbol.Namespace: ...

    @overload
    def getNamespace(self, name: unicode, namespace: ghidra.program.model.symbol.Namespace) -> ghidra.program.model.symbol.Namespace: ...

    def getNamespaceSymbol(self, name: unicode, namespace: ghidra.program.model.symbol.Namespace) -> ghidra.program.model.symbol.Symbol: ...

    def getNextExternalSymbolAddress(self) -> ghidra.program.model.address.Address:
        """
        Returns the next available external symbol address
        @return
        """
        ...

    def getNumSymbols(self) -> int: ...

    def getParameterSymbol(self, name: unicode, namespace: ghidra.program.model.symbol.Namespace) -> ghidra.program.model.symbol.Symbol: ...

    def getPrimarySymbol(self, addr: ghidra.program.model.address.Address) -> ghidra.program.model.symbol.Symbol: ...

    @overload
    def getPrimarySymbolIterator(self, forward: bool) -> ghidra.program.model.symbol.SymbolIterator: ...

    @overload
    def getPrimarySymbolIterator(self, startAddr: ghidra.program.model.address.Address, forward: bool) -> ghidra.program.model.symbol.SymbolIterator: ...

    @overload
    def getPrimarySymbolIterator(self, set: ghidra.program.model.address.AddressSetView, forward: bool) -> ghidra.program.model.symbol.SymbolIterator: ...

    @overload
    def getSymbol(self, symbolID: long) -> ghidra.program.model.symbol.Symbol: ...

    @overload
    def getSymbol(self, name: unicode) -> ghidra.program.model.symbol.Symbol: ...

    @overload
    def getSymbol(self, ref: ghidra.program.model.symbol.Reference) -> ghidra.program.model.symbol.Symbol: ...

    @overload
    def getSymbol(self, name: unicode, namespace: ghidra.program.model.symbol.Namespace) -> ghidra.program.model.symbol.Symbol: ...

    @overload
    def getSymbol(self, name: unicode, addr: ghidra.program.model.address.Address, namespace: ghidra.program.model.symbol.Namespace) -> ghidra.program.model.symbol.Symbol: ...

    @overload
    def getSymbolIterator(self) -> ghidra.program.model.symbol.SymbolIterator: ...

    @overload
    def getSymbolIterator(self, forward: bool) -> ghidra.program.model.symbol.SymbolIterator: ...

    @overload
    def getSymbolIterator(self, searchStr: unicode, caseSensitive: bool) -> ghidra.program.model.symbol.SymbolIterator: ...

    @overload
    def getSymbolIterator(self, startAddr: ghidra.program.model.address.Address, forward: bool) -> ghidra.program.model.symbol.SymbolIterator: ...

    @overload
    def getSymbols(self, namespaceID: long) -> ghidra.program.model.symbol.SymbolIterator: ...

    @overload
    def getSymbols(self, name: unicode) -> ghidra.program.model.symbol.SymbolIterator: ...

    @overload
    def getSymbols(self, addr: ghidra.program.model.address.Address) -> List[ghidra.program.model.symbol.Symbol]: ...

    @overload
    def getSymbols(self, namespace: ghidra.program.model.symbol.Namespace) -> ghidra.program.model.symbol.SymbolIterator: ...

    @overload
    def getSymbols(self, name: unicode, namespace: ghidra.program.model.symbol.Namespace) -> List[ghidra.program.model.symbol.Symbol]: ...

    @overload
    def getSymbols(self, set: ghidra.program.model.address.AddressSetView, type: ghidra.program.model.symbol.SymbolType, forward: bool) -> ghidra.program.model.symbol.SymbolIterator: ...

    def getUserSymbols(self, addr: ghidra.program.model.address.Address) -> List[ghidra.program.model.symbol.Symbol]: ...

    def getVariableSymbol(self, name: unicode, function: ghidra.program.model.listing.Function) -> ghidra.program.model.symbol.Symbol: ...

    def hasLabelHistory(self, addr: ghidra.program.model.address.Address) -> bool: ...

    def hasSymbol(self, addr: ghidra.program.model.address.Address) -> bool: ...

    def hashCode(self) -> int: ...

    def imageBaseChanged(self, oldBase: ghidra.program.model.address.Address, base: ghidra.program.model.address.Address) -> None: ...

    def invalidateCache(self, all: bool) -> None: ...

    def isExternalEntryPoint(self, addr: ghidra.program.model.address.Address) -> bool: ...

    def migrateFromOldVariableStorageManager(self, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        No more sharing the same variable address for multiple variable symbols.
         Must split these up.  Only reference to variable addresses should be the
         symbol address - reference refer to physical/stack addresses, and symbolIDs.
        @param monitor
        @throws CancelledException
        """
        ...

    def moveAddressRange(self, fromAddr: ghidra.program.model.address.Address, toAddr: ghidra.program.model.address.Address, length: long, monitor: ghidra.util.task.TaskMonitor) -> None: ...

    def moveSymbolsAt(self, oldAddr: ghidra.program.model.address.Address, newAddr: ghidra.program.model.address.Address) -> None:
        """
        Move symbol.  Only symbol address is changed.
         References must be moved separately.
        @param oldAddr the old symbol address
        @param newAddr the new symbol address
        """
        ...

    def namespaceRemoved(self, namespaceID: long) -> None:
        """
        Called by the NamespaceManager when a namespace is removed; remove all symbols that have the
         given namespace ID.
        @param namespaceID ID of namespace being removed
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def programReady(self, openMode: int, currentRevision: int, monitor: ghidra.util.task.TaskMonitor) -> None: ...

    def removeExternalEntryPoint(self, addr: ghidra.program.model.address.Address) -> None: ...

    def removeSymbolSpecial(self, sym: ghidra.program.model.symbol.Symbol) -> bool: ...

    def replaceDataTypes(self, oldDataTypeID: long, newDataTypeID: long) -> None: ...

    @staticmethod
    def saveLocalSymbol(tmpHandle: db.DBHandle, symbolID: long, oldAddr: long, name: unicode, isPrimary: bool) -> None:
        """
        Save off old local symbols whose upgrade needs to be deferred until after function manager
         upgrade has been completed.
        @param tmpHandle scratch pad database handle
        @param symbolID local symbol ID
        @param oldAddr old address value from symbol table
        @param name symbol name
        @param isPrimary true if symbol is primary at oldAddr
        """
        ...

    def setLanguage(self, translator: ghidra.program.util.LanguageTranslator, monitor: ghidra.util.task.TaskMonitor) -> None: ...

    def setProgram(self, program: ghidra.program.database.ProgramDB) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def classNamespaces(self) -> java.util.Iterator: ...

    @property
    def definedSymbols(self) -> ghidra.program.model.symbol.SymbolIterator: ...

    @property
    def externalEntryPointIterator(self) -> ghidra.program.model.address.AddressIterator: ...

    @property
    def externalSymbols(self) -> ghidra.program.model.symbol.SymbolIterator: ...

    @property
    def labelHistory(self) -> java.util.Iterator: ...

    @property
    def nextExternalSymbolAddress(self) -> ghidra.program.model.address.Address: ...

    @property
    def numSymbols(self) -> int: ...

    @property
    def program(self) -> None: ...  # No getter available.

    @program.setter
    def program(self, value: ghidra.program.database.ProgramDB) -> None: ...

    @property
    def symbolIterator(self) -> ghidra.program.model.symbol.SymbolIterator: ...
