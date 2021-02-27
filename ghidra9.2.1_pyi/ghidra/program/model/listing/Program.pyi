from typing import List
import ghidra.framework.model
import ghidra.framework.options
import ghidra.program.database
import ghidra.program.database.map
import ghidra.program.model.address
import ghidra.program.model.data
import ghidra.program.model.lang
import ghidra.program.model.listing
import ghidra.program.model.mem
import ghidra.program.model.pcode
import ghidra.program.model.reloc
import ghidra.program.model.symbol
import ghidra.program.model.util
import ghidra.util.task
import java.io
import java.lang
import java.util


class Program(ghidra.program.model.data.DataTypeManagerDomainObject, object):
    """
    This interface represents the main entry point into an object which
     stores all information relating to a single program.  This program
     model divides a program into four major parts: the memory, the symbol table,
     the equate table, and the listing.  Each of these parts has an extensive
     interface and can be retrieved via this program interface.  Although the
     components are divided into separate objects, they are not independent.  Any
     changes to one component may and probably will affect the other components.
     Also, the state of one component will restrict the actions of another
     component.
     For example, the createCodeUnit() method of listing will fail if memory is
     undefined at the address where the codeUnit is to be created.
    """

    ANALYSIS_PROPERTIES: unicode = u'Analyzers'
    ANALYSIS_START_DATE: unicode = u'2007-Jan-01'
    ANALYSIS_START_DATE_FORMAT: unicode = u'yyyy-MMM-dd'
    ANALYZED: unicode = u'Analyzed'
    CREATED_WITH_GHIDRA_VERSION: unicode = u'Created With Ghidra Version'
    DATE_CREATED: unicode = u'Date Created'
    DISASSEMBLER_PROPERTIES: unicode = u'Disassembler'
    DO_DOMAIN_FILE_CHANGED: int = 2
    DO_OBJECT_CLOSED: int = 6
    DO_OBJECT_ERROR: int = 8
    DO_OBJECT_RENAMED: int = 3
    DO_OBJECT_RESTORED: int = 4
    DO_OBJECT_SAVED: int = 1
    DO_PROPERTY_CHANGED: int = 5
    JANUARY_1_1970: java.util.Date = Thu Jan 01 09:00:00 JST 1970
    MAX_OPERANDS: int = 16
    PROGRAM_INFO: unicode = u'Program Information'
    PROGRAM_SETTINGS: unicode = u'Program Settings'
    undoLock: object = java.lang.Object@471b5ac7







    def addCloseListener(self, __a0: ghidra.framework.model.DomainObjectClosedListener) -> None: ...

    def addConsumer(self, __a0: object) -> bool: ...

    def addListener(self, __a0: ghidra.framework.model.DomainObjectListener) -> None: ...

    def addSynchronizedDomainObject(self, __a0: ghidra.framework.model.DomainObject) -> None: ...

    def addTransactionListener(self, __a0: ghidra.framework.model.TransactionListener) -> None: ...

    def canLock(self) -> bool: ...

    def canRedo(self) -> bool: ...

    def canSave(self) -> bool: ...

    def canUndo(self) -> bool: ...

    def clearUndo(self) -> None: ...

    def createAddressSetPropertyMap(self, name: unicode) -> ghidra.program.model.util.AddressSetPropertyMap:
        """
        Create a new AddressSetPropertyMap with the specified name.
        @param name name of the property map.
        @return the newly created property map.
        @throws DuplicateNameException if a property map already exists with the given name.
        """
        ...

    def createIntRangeMap(self, name: unicode) -> ghidra.program.database.IntRangeMap:
        """
        Create a new IntRangeMap with the specified name.
        @param name name of the property map.
        @return the newly created property map.
        @throws DuplicateNameException if a property map already exists with the given name.
        """
        ...

    def createPrivateEventQueue(self, __a0: ghidra.framework.model.DomainObjectListener, __a1: int) -> ghidra.framework.model.EventQueueID: ...

    def deleteAddressSetPropertyMap(self, name: unicode) -> None:
        """
        Remove the property map from the program.
        @param name name of the property map to remove
        """
        ...

    def deleteIntRangeMap(self, name: unicode) -> None:
        """
        Remove the property map from the program.
        @param name name of the property map to remove
        """
        ...

    def endTransaction(self, __a0: int, __a1: bool) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def flushEvents(self) -> None: ...

    def flushPrivateEventQueue(self, __a0: ghidra.framework.model.EventQueueID) -> None: ...

    def forceLock(self, __a0: bool, __a1: unicode) -> None: ...

    def getAddressFactory(self) -> ghidra.program.model.address.AddressFactory:
        """
        Returns the AddressFactory for this program.
        """
        ...

    def getAddressMap(self) -> ghidra.program.database.map.AddressMap: ...

    def getAddressSetPropertyMap(self, name: unicode) -> ghidra.program.model.util.AddressSetPropertyMap:
        """
        Get the property map with the given name.
        @param name name of the property map
        @return null if no property map exist with the given name
        """
        ...

    def getBookmarkManager(self) -> ghidra.program.model.listing.BookmarkManager:
        """
        Get the bookmark manager.
        """
        ...

    def getChanges(self) -> ghidra.program.model.listing.ProgramChangeSet:
        """
        Get the program changes since the last save as a set of addresses.
        @return set of changed addresses within program.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getCompiler(self) -> unicode:
        """
        Gets the name of the compiler believed to have been used to create this program.
         If the compiler hasn't been determined then "unknown" is returned.
        @return name of the compiler or "unknown".
        """
        ...

    def getCompilerSpec(self) -> ghidra.program.model.lang.CompilerSpec:
        """
        Returns the CompilerSpec currently used by this program.
        @return the compilerSpec currently used by this program.
        """
        ...

    def getConsumerList(self) -> java.util.ArrayList: ...

    def getCreationDate(self) -> java.util.Date:
        """
        Returns the creation date of this program.
         If the program was created before this property
         existed, then Jan 1, 1970 is returned.
        @return the creation date of this program
        """
        ...

    def getCurrentTransaction(self) -> ghidra.framework.model.Transaction: ...

    def getDataTypeManager(self) -> ghidra.program.model.data.ProgramBasedDataTypeManager:
        """
        Returns the program's datatype manager.
        """
        ...

    def getDefaultPointerSize(self) -> int:
        """
        Gets the default pointer size in bytes as it may be stored within the program listing.
        @return default pointer size.
        @see DataOrganization#getPointerSize()
        """
        ...

    def getDescription(self) -> unicode: ...

    def getDomainFile(self) -> ghidra.framework.model.DomainFile: ...

    def getEquateTable(self) -> ghidra.program.model.symbol.EquateTable:
        """
        Get the equate table object.
        @return the equate table.
        """
        ...

    def getExecutableFormat(self) -> unicode:
        """
        Returns a value corresponding to the original file format.
        """
        ...

    def getExecutableMD5(self) -> unicode:
        """
        Returns a value corresponding to the original binary file MD5 hash.
         May be null if program source did not correspond to a binary file.
        """
        ...

    def getExecutablePath(self) -> unicode:
        """
        Gets the path to the program's executable file.
         For example, <code>C:\Temp\test.exe</code>.
         This will allow plugins to execute the program.
        @return String  path to program's exe file
        """
        ...

    def getExecutableSHA256(self) -> unicode:
        """
        Returns a value corresponding to the original binary file SHA256 hash.
         May be null if program source did not correspond to a binary file.
        """
        ...

    def getExternalManager(self) -> ghidra.program.model.symbol.ExternalManager:
        """
        Returns the external manager.
        """
        ...

    def getFunctionManager(self) -> ghidra.program.model.listing.FunctionManager:
        """
        Returns the programs function manager.
        """
        ...

    def getGlobalNamespace(self) -> ghidra.program.model.symbol.Namespace:
        """
        Returns the global namespace for this program
        """
        ...

    def getImageBase(self) -> ghidra.program.model.address.Address:
        """
        Returns the current program image base address;
        """
        ...

    def getIntRangeMap(self, name: unicode) -> ghidra.program.database.IntRangeMap:
        """
        Get the property map with the given name.
        @param name name of the property map
        @return null if no property map exist with the given name
        """
        ...

    def getLanguage(self) -> ghidra.program.model.lang.Language:
        """
        Returns the language used by this program.
        @return the language used by this program.
        """
        ...

    def getLanguageID(self) -> ghidra.program.model.lang.LanguageID:
        """
        Return the name of the language used by this program.
        @return the name of the language
        """
        ...

    def getListing(self) -> ghidra.program.model.listing.Listing:
        """
        Get the listing object.
        @return the Listing interface to the listing object.
        """
        ...

    def getMaxAddress(self) -> ghidra.program.model.address.Address:
        """
        Get the programs maximum address.
        @return the program's maximum address or null if no memory blocks
         have been defined in the program.
        """
        ...

    def getMemory(self) -> ghidra.program.model.mem.Memory:
        """
        Get the memory object.
        @return the memory object.
        """
        ...

    def getMetadata(self) -> java.util.Map: ...

    def getMinAddress(self) -> ghidra.program.model.address.Address:
        """
        get the program's minimum address.
        @return the program's minimum address or null if no memory blocks
         have been defined in the program.
        """
        ...

    def getModificationNumber(self) -> long: ...

    def getName(self) -> unicode: ...

    def getOptions(self, __a0: unicode) -> ghidra.framework.options.Options: ...

    def getOptionsNames(self) -> List[object]: ...

    def getProgramContext(self) -> ghidra.program.model.listing.ProgramContext:
        """
        Returns the program context.
        """
        ...

    def getProgramUserData(self) -> ghidra.program.model.listing.ProgramUserData:
        """
        Returns the user-specific data manager for
         this program.
        """
        ...

    def getRedoName(self) -> unicode: ...

    def getReferenceManager(self) -> ghidra.program.model.symbol.ReferenceManager:
        """
        Get the reference manager.
        """
        ...

    @overload
    def getRegister(self, name: unicode) -> ghidra.program.model.lang.Register:
        """
        Returns the register with the given name;
        @param name the name of the register to retrieve
        @return register or null
        """
        ...

    @overload
    def getRegister(self, addr: ghidra.program.model.address.Address) -> ghidra.program.model.lang.Register:
        """
        Returns the largest register located at the specified address
        @param addr
        @return largest register or null
        """
        ...

    @overload
    def getRegister(self, varnode: ghidra.program.model.pcode.Varnode) -> ghidra.program.model.lang.Register:
        """
        Returns the register which corresponds to the specified varnode
        @param varnode the varnode
        @return register or null
        """
        ...

    @overload
    def getRegister(self, addr: ghidra.program.model.address.Address, size: int) -> ghidra.program.model.lang.Register:
        """
        Returns a specific register based upon its address and size
        @param addr register address
        @param size the size of the register (in bytes);
        @return register or null
        """
        ...

    def getRegisters(self, addr: ghidra.program.model.address.Address) -> List[ghidra.program.model.lang.Register]:
        """
        Returns all registers located at the specified address
        @param addr
        @return largest register
        """
        ...

    def getRelocationTable(self) -> ghidra.program.model.reloc.RelocationTable:
        """
        Gets the relocation table.
        """
        ...

    def getSymbolTable(self) -> ghidra.program.model.symbol.SymbolTable:
        """
        Get the symbol table object.
        @return the symbol table object.
        """
        ...

    def getSynchronizedDomainObjects(self) -> List[ghidra.framework.model.DomainObject]: ...

    def getUndoName(self) -> unicode: ...

    def getUniqueProgramID(self) -> long:
        """
        Returns an ID that is unique for this program.  This provides an easy way to store
         references to a program across client persistence.
        """
        ...

    def getUsrPropertyManager(self) -> ghidra.program.model.util.PropertyMapManager:
        """
        Get the user propertyMangager stored with this program. The user property
         manager is used to store arbitrary address indexed information associated
         with the program.
        @return the user property manager.
        """
        ...

    def hasExclusiveAccess(self) -> bool: ...

    def hasTerminatedTransaction(self) -> bool: ...

    def hashCode(self) -> int: ...

    def invalidate(self) -> None:
        """
        Invalidates any caching in a program.
         NOTE: Over-using this method can adversely affect system performance.
        """
        ...

    def isChangeable(self) -> bool: ...

    def isChanged(self) -> bool: ...

    def isClosed(self) -> bool: ...

    def isLocked(self) -> bool: ...

    def isSendingEvents(self) -> bool: ...

    def isTemporary(self) -> bool: ...

    def isUsedBy(self, __a0: object) -> bool: ...

    def lock(self, __a0: unicode) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @overload
    def parseAddress(self, addrStr: unicode) -> List[ghidra.program.model.address.Address]:
        """
        Return an array of Addresses that could represent the given
         string.
        @param addrStr the string to parse.
        @return zero length array if addrStr is properly formatted but
         no matching addresses were found or if the address is improperly formatted.
        """
        ...

    @overload
    def parseAddress(self, addrStr: unicode, caseSensitive: bool) -> List[ghidra.program.model.address.Address]:
        """
        Return an array of Addresses that could represent the given
         string.
        @param addrStr the string to parse.
        @param caseSensitive whether or not to process any addressSpace names as case sensitive.
        @return zero length array if addrStr is properly formatted but
         no matching addresses were found or if the address is improperly formatted.
        """
        ...

    def redo(self) -> None: ...

    def release(self, __a0: object) -> None: ...

    def releaseSynchronizedDomainObject(self) -> None: ...

    def removeCloseListener(self, __a0: ghidra.framework.model.DomainObjectClosedListener) -> None: ...

    def removeListener(self, __a0: ghidra.framework.model.DomainObjectListener) -> None: ...

    def removePrivateEventQueue(self, __a0: ghidra.framework.model.EventQueueID) -> bool: ...

    def removeTransactionListener(self, __a0: ghidra.framework.model.TransactionListener) -> None: ...

    def restoreImageBase(self) -> None:
        """
        Restores the last committed image base.
        """
        ...

    def save(self, __a0: unicode, __a1: ghidra.util.task.TaskMonitor) -> None: ...

    def saveToPackedFile(self, __a0: java.io.File, __a1: ghidra.util.task.TaskMonitor) -> None: ...

    def setCompiler(self, compiler: unicode) -> None:
        """
        Sets the name of the compiler which created this program.
        @param compiler the name
        """
        ...

    def setEventsEnabled(self, __a0: bool) -> None: ...

    def setExecutableFormat(self, format: unicode) -> None:
        """
        Sets the value corresponding to the original file format.
        @param format the format string to set.
        """
        ...

    def setExecutableMD5(self, md5: unicode) -> None:
        """
        Sets the value corresponding to the original binary file MD5 hash.
        @param md5 MD5 binary file hash
        """
        ...

    def setExecutablePath(self, path: unicode) -> None:
        """
        Sets the path to the program's executable file.
         For example, <code>C:\Temp\test.exe</code>.
        @param path the path to the program's exe
        """
        ...

    def setExecutableSHA256(self, sha256: unicode) -> None:
        """
        Sets the value corresponding to the original binary file SHA256 hash.
        @param sha256 SHA256 binary file hash
        """
        ...

    def setImageBase(self, base: ghidra.program.model.address.Address, commit: bool) -> None:
        """
        Sets the program's image base address.
        @param base the new image base address;
        @param commit if false, then the image base change is temporary and does not really change
         the program and will be lost once the program is closed.  If true, the change is permanent
         and marks the program as "changed" (needs saving).
        @throws AddressOverflowException if the new image would cause a memory block to end past the
         the address space.
        @throws LockException if the program is shared and the user does not have an exclusive checkout.
         This will never be thrown if commit is false.
        @throws IllegalStateException if the program state is not suitable for setting the image base.
        """
        ...

    def setLanguage(self, language: ghidra.program.model.lang.Language, compilerSpecID: ghidra.program.model.lang.CompilerSpecID, forceRedisassembly: bool, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Sets the language for the program. If the new language is "compatible" with the old language,
         the addressMap is adjusted then the program is "re-disassembled".
        @param language the new language to use.
        @param forceRedisassembly if true a redisassembly will be forced.  This should always be false.
        @param monitor the task monitor
        @throws IllegalStateException thrown if any error occurs, including a cancelled monitor, which leaves this
         program object in an unusable state.  The current transaction should be aborted and the program instance
         discarded.
        @throws IncompatibleLanguageException thrown if the new language is too different from the
         existing language.
        @throws LockException if the program is shared and not checked out exclusively.
        """
        ...

    def setName(self, __a0: unicode) -> None: ...

    def setTemporary(self, __a0: bool) -> None: ...

    @overload
    def startTransaction(self, __a0: unicode) -> int: ...

    @overload
    def startTransaction(self, __a0: unicode, __a1: ghidra.framework.model.AbortedTransactionListener) -> int: ...

    def toString(self) -> unicode: ...

    def undo(self) -> None: ...

    def unlock(self) -> None: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def addressFactory(self) -> ghidra.program.model.address.AddressFactory: ...

    @property
    def addressMap(self) -> ghidra.program.database.map.AddressMap: ...

    @property
    def bookmarkManager(self) -> ghidra.program.model.listing.BookmarkManager: ...

    @property
    def changeable(self) -> bool: ...

    @property
    def changed(self) -> bool: ...

    @property
    def changes(self) -> ghidra.program.model.listing.ProgramChangeSet: ...

    @property
    def closed(self) -> bool: ...

    @property
    def compiler(self) -> unicode: ...

    @compiler.setter
    def compiler(self, value: unicode) -> None: ...

    @property
    def compilerSpec(self) -> ghidra.program.model.lang.CompilerSpec: ...

    @property
    def consumerList(self) -> java.util.ArrayList: ...

    @property
    def creationDate(self) -> java.util.Date: ...

    @property
    def currentTransaction(self) -> ghidra.framework.model.Transaction: ...

    @property
    def dataTypeManager(self) -> ghidra.program.model.data.ProgramBasedDataTypeManager: ...

    @property
    def defaultPointerSize(self) -> int: ...

    @property
    def description(self) -> unicode: ...

    @property
    def domainFile(self) -> ghidra.framework.model.DomainFile: ...

    @property
    def equateTable(self) -> ghidra.program.model.symbol.EquateTable: ...

    @property
    def eventsEnabled(self) -> None: ...  # No getter available.

    @eventsEnabled.setter
    def eventsEnabled(self, value: bool) -> None: ...

    @property
    def executableFormat(self) -> unicode: ...

    @executableFormat.setter
    def executableFormat(self, value: unicode) -> None: ...

    @property
    def executableMD5(self) -> unicode: ...

    @executableMD5.setter
    def executableMD5(self, value: unicode) -> None: ...

    @property
    def executablePath(self) -> unicode: ...

    @executablePath.setter
    def executablePath(self, value: unicode) -> None: ...

    @property
    def executableSHA256(self) -> unicode: ...

    @executableSHA256.setter
    def executableSHA256(self, value: unicode) -> None: ...

    @property
    def externalManager(self) -> ghidra.program.model.symbol.ExternalManager: ...

    @property
    def functionManager(self) -> ghidra.program.model.listing.FunctionManager: ...

    @property
    def globalNamespace(self) -> ghidra.program.model.symbol.Namespace: ...

    @property
    def imageBase(self) -> ghidra.program.model.address.Address: ...

    @property
    def language(self) -> ghidra.program.model.lang.Language: ...

    @property
    def languageID(self) -> ghidra.program.model.lang.LanguageID: ...

    @property
    def listing(self) -> ghidra.program.model.listing.Listing: ...

    @property
    def locked(self) -> bool: ...

    @property
    def maxAddress(self) -> ghidra.program.model.address.Address: ...

    @property
    def memory(self) -> ghidra.program.model.mem.Memory: ...

    @property
    def metadata(self) -> java.util.Map: ...

    @property
    def minAddress(self) -> ghidra.program.model.address.Address: ...

    @property
    def modificationNumber(self) -> long: ...

    @property
    def name(self) -> unicode: ...

    @name.setter
    def name(self, value: unicode) -> None: ...

    @property
    def optionsNames(self) -> List[object]: ...

    @property
    def programContext(self) -> ghidra.program.model.listing.ProgramContext: ...

    @property
    def programUserData(self) -> ghidra.program.model.listing.ProgramUserData: ...

    @property
    def redoName(self) -> unicode: ...

    @property
    def referenceManager(self) -> ghidra.program.model.symbol.ReferenceManager: ...

    @property
    def relocationTable(self) -> ghidra.program.model.reloc.RelocationTable: ...

    @property
    def sendingEvents(self) -> bool: ...

    @property
    def symbolTable(self) -> ghidra.program.model.symbol.SymbolTable: ...

    @property
    def synchronizedDomainObjects(self) -> List[ghidra.framework.model.DomainObject]: ...

    @property
    def temporary(self) -> bool: ...

    @temporary.setter
    def temporary(self, value: bool) -> None: ...

    @property
    def undoName(self) -> unicode: ...

    @property
    def uniqueProgramID(self) -> long: ...

    @property
    def usrPropertyManager(self) -> ghidra.program.model.util.PropertyMapManager: ...
