from typing import Iterator
from typing import List
import ghidra.program.database
import ghidra.program.model.address
import ghidra.program.model.lang
import ghidra.program.model.listing
import ghidra.program.model.symbol
import ghidra.util.task
import java.lang


class FunctionManager(object):








    @overload
    def createFunction(self, name: unicode, entryPoint: ghidra.program.model.address.Address, body: ghidra.program.model.address.AddressSetView, source: ghidra.program.model.symbol.SourceType) -> ghidra.program.model.listing.Function:
        """
        Create a function with the given body at entry point within the global namespace.
        @param name the name of the new function or null for default name
        @param entryPoint entry point of function
        @param body addresses contained in the function body
        @param source the source of this function
        @return new function or null if one or more functions overlap the specified body address set.
        @throws InvalidInputException if the name has invalid characters
        @throws OverlappingFunctionException if the address set of the body overlaps an existing
                     function
        """
        ...

    @overload
    def createFunction(self, name: unicode, nameSpace: ghidra.program.model.symbol.Namespace, entryPoint: ghidra.program.model.address.Address, body: ghidra.program.model.address.AddressSetView, source: ghidra.program.model.symbol.SourceType) -> ghidra.program.model.listing.Function:
        """
        Create a function with the given body at entry point.
        @param name the name of the new function or null for default name
        @param nameSpace the nameSpace in which to create the function
        @param entryPoint entry point of function
        @param body addresses contained in the function body
        @param source the source of this function
        @return new function or null if one or more functions overlap the specified body address set.
        @throws InvalidInputException if the name has invalid characters
        @throws OverlappingFunctionException if the address set of the body overlaps an existing
                     function
        """
        ...

    def createThunkFunction(self, name: unicode, nameSpace: ghidra.program.model.symbol.Namespace, entryPoint: ghidra.program.model.address.Address, body: ghidra.program.model.address.AddressSetView, thunkedFunction: ghidra.program.model.listing.Function, source: ghidra.program.model.symbol.SourceType) -> ghidra.program.model.listing.Function:
        """
        Create a thunk function with the given body at entry point.
        @param name the name of the new function or null for default name
        @param nameSpace the nameSpace in which to create the function
        @param entryPoint entry point of function
        @param body addresses contained in the function body
        @param thunkedFunction referenced function (required is creating a thunk function)
        @param source the source of this function
        @return new function or null if one or more functions overlap the specified body address set.
        @throws OverlappingFunctionException if the address set of the body overlaps an existing
                     function
        """
        ...

    def deleteAddressRange(self, startAddr: ghidra.program.model.address.Address, endAddr: ghidra.program.model.address.Address, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        @see ghidra.program.database.ManagerDB#deleteAddressRange(ghidra.program.model.address.Address,
              ghidra.program.model.address.Address, ghidra.util.task.TaskMonitor)
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getCallingConvention(self, name: unicode) -> ghidra.program.model.lang.PrototypeModel:
        """
        Gets the prototype model of the calling convention with the specified name in this program.
        @return the named function calling convention prototype model or null.
        """
        ...

    def getCallingConventionNames(self) -> List[unicode]:
        """
        Gets the names associated with each of the current calling conventions associated with this
         program. Within the exception of "unknown", all of these calling convention names should have
         a PrototypeModel.
        @return the calling convention names.
        """
        ...

    def getCallingConventions(self) -> List[ghidra.program.model.lang.PrototypeModel]:
        """
        Gets all the calling convention prototype models in this program that have names.
        @return the function calling convention prototype models.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getDefaultCallingConvention(self) -> ghidra.program.model.lang.PrototypeModel:
        """
        Gets the default calling convention's prototype model in this program.
        @return the default calling convention prototype model or null.
        """
        ...

    def getExternalFunctions(self) -> ghidra.program.model.listing.FunctionIterator:
        """
        Get an iterator over all external functions. Functions returned have no particular order.
        @return an iterator over external functions
        """
        ...

    def getFunction(self, key: long) -> ghidra.program.model.listing.Function:
        """
        Get a Function object by its key
        @param key function symbol key
        @return function object or null if not found
        """
        ...

    def getFunctionAt(self, entryPoint: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Function:
        """
        Get the function at entryPoint.
        @return null if there is no function at entryPoint.
        """
        ...

    def getFunctionContaining(self, addr: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Function:
        """
        Get a function containing an address.
        @param addr address within the function
        @return function containing this address, null otherwise
        """
        ...

    def getFunctionCount(self) -> int:
        """
        Returns the total number of functions in the program including external functions.
        """
        ...

    @overload
    def getFunctions(self, forward: bool) -> ghidra.program.model.listing.FunctionIterator:
        """
        Returns an iterator over all non-external functions in address (entry point) order.
        @param forward true means to iterate in ascending address order
        """
        ...

    @overload
    def getFunctions(self, start: ghidra.program.model.address.Address, forward: bool) -> ghidra.program.model.listing.FunctionIterator:
        """
        Get an iterator over non-external functions starting at an address and ordered by entry
         address.
        @param start starting address
        @param forward true means to iterate in ascending address order
        @return an iterator over functions.
        """
        ...

    @overload
    def getFunctions(self, asv: ghidra.program.model.address.AddressSetView, forward: bool) -> ghidra.program.model.listing.FunctionIterator:
        """
        Get an iterator over functions with entry points in the specified address set. Function are
         ordered based upon entry address.
        @param asv address set to iterate over
        @param forward true means to iterate in ascending address order
        @return an iterator over functions.
        """
        ...

    @overload
    def getFunctionsNoStubs(self, forward: bool) -> ghidra.program.model.listing.FunctionIterator:
        """
        Returns an iterator over all REAL functions in address (entry point) order (real functions
         have instructions, and aren't stubs).
        @param forward true means to iterate in ascending address order
        """
        ...

    @overload
    def getFunctionsNoStubs(self, start: ghidra.program.model.address.Address, forward: bool) -> ghidra.program.model.listing.FunctionIterator:
        """
        Get an iterator over REAL functions starting at an address and ordered by entry address (real
         functions have instructions, and aren't stubs).
        @param start starting address
        @param forward true means to iterate in ascending address order
        @return an iterator over functions.
        """
        ...

    @overload
    def getFunctionsNoStubs(self, asv: ghidra.program.model.address.AddressSetView, forward: bool) -> ghidra.program.model.listing.FunctionIterator:
        """
        Get an iterator over REAL functions with entry points in the specified address set (real
         functions have instructions, and aren't stubs). Functions are ordered based upon entry
         address.
        @param asv address set to iterate over
        @param forward true means to iterate in ascending address order
        @return an iterator over functions.
        """
        ...

    def getFunctionsOverlapping(self, set: ghidra.program.model.address.AddressSetView) -> Iterator[ghidra.program.model.listing.Function]:
        """
        Return an iterator over functions that overlap the given address set.
        @param set address set of interest
        @return iterator over Functions
        """
        ...

    def getProgram(self) -> ghidra.program.model.listing.Program: ...

    def getReferencedFunction(self, address: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Function:
        """
        Get the function which resides at the specified address or is referenced from the specified
         address.
        @param address function address or address of pointer to a function.
        @return referenced function or null
        """
        ...

    def getReferencedVariable(self, instrAddr: ghidra.program.model.address.Address, storageAddr: ghidra.program.model.address.Address, size: int, isRead: bool) -> ghidra.program.model.listing.Variable:
        """
        Attempts to determine which if any of the local functions variables are referenced by the
         specified reference. In utilizing the firstUseOffset scoping model, negative offsets
         (relative to the functions entry) are shifted beyond the maximum positive offset within the
         function. While this does not account for the actual instruction flow, it is hopefully
         accurate enough for most situations.
        @param instrAddr
        @param storageAddr
        @param size varnode size in bytes (1 is assumed if value &lt;= 0)
        @param isRead
        @return referenced variable or null if one not found
        """
        ...

    def hashCode(self) -> int: ...

    def invalidateCache(self, all: bool) -> None: ...

    def isInFunction(self, addr: ghidra.program.model.address.Address) -> bool:
        """
        Check if this address contains a function.
        @param addr address to check
        @return true if this address is contained in a function.
        """
        ...

    def moveAddressRange(self, fromAddr: ghidra.program.model.address.Address, toAddr: ghidra.program.model.address.Address, length: long, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        @see ghidra.program.database.ManagerDB#moveAddressRange(ghidra.program.model.address.Address,
              ghidra.program.model.address.Address, long, ghidra.util.task.TaskMonitor)
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def programReady(self, openMode: int, currentRevision: int, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        @param currentRevision TODO
        @see ghidra.program.database.ManagerDB#programReady(int, int, ghidra.util.task.TaskMonitor)
        """
        ...

    def removeFunction(self, entryPoint: ghidra.program.model.address.Address) -> bool:
        """
        Remove a function defined at entryPoint.
        """
        ...

    def setProgram(self, program: ghidra.program.database.ProgramDB) -> None:
        """
        @see ghidra.program.database.ManagerDB#setProgram(ghidra.program.database.ProgramDB)
        """
        ...

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
    def program(self) -> ghidra.program.model.listing.Program: ...
