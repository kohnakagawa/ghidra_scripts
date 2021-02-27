from typing import Iterator
from typing import List
import ghidra.program.database
import ghidra.program.model.address
import ghidra.program.model.lang
import ghidra.program.model.listing
import ghidra.program.model.symbol
import ghidra.program.util
import ghidra.util.task
import java.lang


class FunctionManagerDB(object, ghidra.program.database.ManagerDB, ghidra.program.model.listing.FunctionManager):
    """
    Class that manages all functions within the program; there are some
     convenience methods on Listing to create and access functions, but
     all function related calls are routed to this class.
    """





    def __init__(self, dbHandle: db.DBHandle, addrMap: ghidra.program.database.map.AddressMap, openMode: int, lock: ghidra.util.Lock, monitor: ghidra.util.task.TaskMonitor):
        """
        Construct a new FunctionManager
        @param dbHandle data base handle
        @param addrMap address map for the program
        @param openMode CREATE, UPDATE, READ_ONLY, or UPGRADE defined in
         db.DBConstants
        @param lock the program synchronization lock
        @param monitor
        @throws VersionException if function manager's version does not match
         its expected version
        @throws CancelledException if the function table is being upgraded
         and the user canceled the upgrade process
        @throws IOException if there was a problem accessing the database
        """
        ...



    def createExternalFunction(self, extSpaceAddr: ghidra.program.model.address.Address, name: unicode, nameSpace: ghidra.program.model.symbol.Namespace, extData3: unicode, source: ghidra.program.model.symbol.SourceType) -> ghidra.program.model.listing.Function:
        """
        Transform an existing external symbol into an external function.
         This method should only be invoked by an ExternalSymbol
        @param extSpaceAddr the external space address to use when creating this external.
        @param name
        @param nameSpace
        @param extData3 internal symbol-data-3 string (see {@link ExternalLocationDB})
        @param source the source of this external.
        @return external function
        @throws InvalidInputException
        @throws DuplicateNameException
        """
        ...

    @overload
    def createFunction(self, name: unicode, entryPoint: ghidra.program.model.address.Address, body: ghidra.program.model.address.AddressSetView, source: ghidra.program.model.symbol.SourceType) -> ghidra.program.model.listing.Function: ...

    @overload
    def createFunction(self, name: unicode, nameSpace: ghidra.program.model.symbol.Namespace, entryPoint: ghidra.program.model.address.Address, body: ghidra.program.model.address.AddressSetView, source: ghidra.program.model.symbol.SourceType) -> ghidra.program.model.listing.Function: ...

    def createThunkFunction(self, name: unicode, nameSpace: ghidra.program.model.symbol.Namespace, entryPoint: ghidra.program.model.address.Address, body: ghidra.program.model.address.AddressSetView, thunkedFunction: ghidra.program.model.listing.Function, source: ghidra.program.model.symbol.SourceType) -> ghidra.program.model.listing.Function: ...

    def deleteAddressRange(self, startAddr: ghidra.program.model.address.Address, endAddr: ghidra.program.model.address.Address, monitor: ghidra.util.task.TaskMonitor) -> None: ...

    def doRemoveFunction(self, key: long) -> bool: ...

    def equals(self, __a0: object) -> bool: ...

    def functionNamespaceChanged(self, key: long) -> None: ...

    def functionTagsChanged(self) -> None: ...

    def getCallingConvention(self, name: unicode) -> ghidra.program.model.lang.PrototypeModel: ...

    def getCallingConventionNames(self) -> List[unicode]: ...

    def getCallingConventions(self) -> List[ghidra.program.model.lang.PrototypeModel]: ...

    def getClass(self) -> java.lang.Class: ...

    def getDefaultCallingConvention(self) -> ghidra.program.model.lang.PrototypeModel: ...

    def getExternalFunctions(self) -> ghidra.program.model.listing.FunctionIterator: ...

    def getFunction(self, key: long) -> ghidra.program.model.listing.Function:
        """
        Get the function with the given key.
        @param key ID of the function; ID is obtained by calling
         Function.getID()
        @return null if there is no function with the given key
        """
        ...

    def getFunctionAt(self, entryPoint: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Function: ...

    def getFunctionContaining(self, addr: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Function: ...

    def getFunctionCount(self) -> int: ...

    def getFunctionTagManager(self) -> ghidra.program.model.listing.FunctionTagManager: ...

    @overload
    def getFunctions(self, forward: bool) -> ghidra.program.model.listing.FunctionIterator: ...

    @overload
    def getFunctions(self, start: ghidra.program.model.address.Address, foward: bool) -> ghidra.program.model.listing.FunctionIterator: ...

    @overload
    def getFunctions(self, asv: ghidra.program.model.address.AddressSetView, forward: bool) -> ghidra.program.model.listing.FunctionIterator: ...

    @overload
    def getFunctionsNoStubs(self, forward: bool) -> ghidra.program.model.listing.FunctionIterator: ...

    @overload
    def getFunctionsNoStubs(self, start: ghidra.program.model.address.Address, foward: bool) -> ghidra.program.model.listing.FunctionIterator: ...

    @overload
    def getFunctionsNoStubs(self, asv: ghidra.program.model.address.AddressSetView, forward: bool) -> ghidra.program.model.listing.FunctionIterator: ...

    def getFunctionsOverlapping(self, set: ghidra.program.model.address.AddressSetView) -> Iterator[ghidra.program.model.listing.Function]: ...

    def getProgram(self) -> ghidra.program.database.ProgramDB: ...

    def getReferencedFunction(self, address: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Function: ...

    def getReferencedVariable(self, instrAddr: ghidra.program.model.address.Address, storageAddr: ghidra.program.model.address.Address, size: int, isRead: bool) -> ghidra.program.model.listing.Variable: ...

    def getThunkFunctionIds(self, referencedFunctionId: long) -> List[long]:
        """
        Returns list of thunk function keys which reference the specified referencedFunctionKey
        @param referencedFunctionId
        @return list of thunk function IDs or null
        """
        ...

    def getThunkedFunctionId(self, functionId: long) -> long: ...

    def hashCode(self) -> int: ...

    def initSignatureSource(self, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Initialize function signature source when it was first introduced and attempt to
         disable custom storage if possible.
         NOTE: This method intended to be called by ProgramDB only during appropriate upgrade.
        @param monitor
        @throws CancelledException
        @throws IOException
        """
        ...

    def invalidateCache(self, all: bool) -> None: ...

    def isInFunction(self, addr: ghidra.program.model.address.Address) -> bool: ...

    def isThunk(self, key: long) -> bool: ...

    def moveAddressRange(self, fromAddr: ghidra.program.model.address.Address, toAddr: ghidra.program.model.address.Address, length: long, monitor: ghidra.util.task.TaskMonitor) -> None: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def programReady(self, openMode: int, currentRevision: int, monitor: ghidra.util.task.TaskMonitor) -> None: ...

    def removeExplicitThisParameters(self, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Remove parameter symbols which correspond to the 'this' parameter for all
         __thiscall functions using dynamic storage.
         NOTE: This method intended to be called by ProgramDB only during appropriate upgrade.
        @param monitor
        @throws CancelledException
        @throws IOException
        """
        ...

    def removeFunction(self, entryPoint: ghidra.program.model.address.Address) -> bool: ...

    def replaceDataTypes(self, oldDataTypeID: long, newDataTypeID: long) -> None: ...

    def setLanguage(self, translator: ghidra.program.util.LanguageTranslator, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Perform language translation.
         Update function return storage specifications to reflect address space and register mappings
        @param translator
        @param monitor
        @throws CancelledException
        """
        ...

    def setProgram(self, program: ghidra.program.database.ProgramDB) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def callingConventionNames(self) -> List[object]: ...

    @property
    def callingConventions(self) -> List[ghidra.program.model.lang.PrototypeModel]: ...

    @property
    def defaultCallingConvention(self) -> ghidra.program.model.lang.PrototypeModel: ...

    @property
    def externalFunctions(self) -> ghidra.program.model.listing.FunctionIterator: ...

    @property
    def functionCount(self) -> int: ...

    @property
    def functionTagManager(self) -> ghidra.program.model.listing.FunctionTagManager: ...

    @property
    def program(self) -> ghidra.program.database.ProgramDB: ...

    @program.setter
    def program(self, value: ghidra.program.database.ProgramDB) -> None: ...
