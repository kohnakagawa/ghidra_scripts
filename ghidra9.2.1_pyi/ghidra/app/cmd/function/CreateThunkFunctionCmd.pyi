import ghidra.framework.cmd
import ghidra.framework.model
import ghidra.program.model.address
import ghidra.program.model.listing
import ghidra.util.task
import java.lang


class CreateThunkFunctionCmd(ghidra.framework.cmd.BackgroundCommand):
    """
    Command for creating a thunk function at an address.
    """





    @overload
    def __init__(self, entry: ghidra.program.model.address.Address, checkForSideEffects: bool):
        """
        Constructs a new command for creating a thunk function that can compute the function this function is thunking to.
        @param entry entry point address for the function to be created.
        @param checkForSideEffects true to check for side-effects that indicate it is not a pure thunk.

         The body may be computed.  References to the thunked to function may be created.

         If no function exists at the location being thunked, it will be created based on the above rules.
        """
        ...

    @overload
    def __init__(self, entry: ghidra.program.model.address.Address, body: ghidra.program.model.address.AddressSetView, referencedFunctionAddr: ghidra.program.model.address.Address):
        """
        Constructs a new command for creating a thunk function.
        @param entry entry point address for the function to be created.
        @param body set of addresses to associated with the function to be created.
         The addresses must not already be included in the body of any existing function.
         If null, and entry corresponds to an existing function, that function will be
         converted to a thunk, otherwise an error will result.
        @param referencedFunctionAddr the function address to which this thunk refers.  If no function
         exists at that specified referencedFunctionAddr one will be created per the following scheme:
         <br><ul>
         <li>If referencedFunctionAddr is not contained within a memory block, an external function will<br>
         be created (a check will be done to look for an previously defined external location)</li>
         <li>If referencedFunctionAddr corresponds to an instruction, a new function will be<br>
         created at that address.</li>
         </ul>
        """
        ...

    @overload
    def __init__(self, entry: ghidra.program.model.address.Address, body: ghidra.program.model.address.AddressSetView, referencedSymbol: ghidra.program.model.symbol.Symbol):
        """
        Constructs a new command for creating a thunk function.
        @param entry entry point address for the function to be created.
        @param body set of addresses to associated with the function to be created.
         The addresses must not already be included in the body of any existing function.
         If null, and entry corresponds to an existing function, that function will be
         converted to a thunk, otherwise an error will result.
        @param referencedSymbol the symbol which identifies the intended function to which this thunk refers.
         If no function exists at that specified referencedSymbol location, one will be created per the following scheme:
         <br><ul>
         <li>If referencedFunctionAddr is not contained within a memory block, an external function will<br>
         be created (a check will be done to look for an previously defined external location)</li>
         <li>If referencedFunctionAddr corresponds to an instruction, a new function will be<br>
         created at that address.</li>
         <li>If referencedSymbol corresponds to an external CODE symbol, it will be converted to an<br>
         external FUNCTION</li>
         </ul>
        """
        ...

    @overload
    def __init__(self, __a0: ghidra.program.model.address.Address, __a1: ghidra.program.model.address.AddressSetView, __a2: ghidra.program.model.address.Address, __a3: List[object]): ...



    @overload
    def applyTo(self, obj: ghidra.framework.model.DomainObject) -> bool: ...

    @overload
    def applyTo(self, obj: ghidra.framework.model.DomainObject, monitor: ghidra.util.task.TaskMonitor) -> bool: ...

    def canCancel(self) -> bool:
        """
        Check if the command can be canceled.
        @return true if this command can be canceled
        """
        ...

    def dispose(self) -> None:
        """
        Called when this command is going to be removed/canceled without
         running it.  This gives the command the opportunity to free any
         temporary resources it has hold of.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getName(self) -> unicode: ...

    def getReferencedFunction(self) -> ghidra.program.model.listing.Function:
        """
        @return the function referenced by the newly created thunk function
         is command was successful
        """
        ...

    def getStatusMsg(self) -> unicode: ...

    def getThunkFunction(self) -> ghidra.program.model.listing.Function:
        """
        @return function if create command was successful
        """
        ...

    @overload
    @staticmethod
    def getThunkedAddr(program: ghidra.program.model.listing.Program, entry: ghidra.program.model.address.Address) -> ghidra.program.model.address.Address:
        """
        if the code starting at entry is a thunk, return the thunked addess if known.
        @param program code resides in
        @param entry start of the code
        @return the function address, Address.NO_ADDRESS if thunk but unknonw addr, null otherwise
        """
        ...

    @overload
    @staticmethod
    def getThunkedAddr(program: ghidra.program.model.listing.Program, entry: ghidra.program.model.address.Address, checkForSideEffects: bool) -> ghidra.program.model.address.Address:
        """
        Get the address that this function would thunk if it is a valid thunk
        @param program
        @param entry location to check for a thunk
        @param checkForSideEffects true if there should be no extra registers affected
        @return address that the thunk thunks,Address.NO_ADDRESS if thunk but unknown addr, null otherwise
        """
        ...

    def hasProgress(self) -> bool:
        """
        Check if the command provides progress information.
        @return true if the command shows progress information
        """
        ...

    def hashCode(self) -> int: ...

    def isModal(self) -> bool:
        """
        Check if the command requires the monitor to be modal.  No other
         command should be allowed, and the GUI will be locked.
        @return true if no other operation should be going on while this
         command is in progress.
        """
        ...

    @staticmethod
    def isThunk(program: ghidra.program.model.listing.Program, func: ghidra.program.model.listing.Function) -> bool:
        """
        Check if this is a Thunking function.
        @return true if this is a function thunking another.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def taskCompleted(self) -> None:
        """
        Called when the task monitor is completely done with indicating progress.
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
    def referencedFunction(self) -> ghidra.program.model.listing.Function: ...

    @property
    def thunkFunction(self) -> ghidra.program.model.listing.Function: ...
