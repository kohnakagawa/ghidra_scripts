import ghidra.framework.cmd
import ghidra.framework.model
import ghidra.program.model.address
import ghidra.program.model.listing
import ghidra.util.task
import java.lang


class CreateMultipleFunctionsCmd(ghidra.framework.cmd.BackgroundCommand):
    """
    Command for Creating multiple functions from a selection.
     This tries to create functions by working from the minimum address to the maximum address in
     the selection. Any addresses in the selection that are already in existing functions are
     discarded. Every time a function is created, all the other addresses for that function are
     also discarded.
    """





    def __init__(self, selection: ghidra.program.model.address.AddressSetView, source: ghidra.program.model.symbol.SourceType): ...



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

    def createFunction(self, entryPoint: ghidra.program.model.address.Address, currentProgram: ghidra.program.model.listing.Program, monitor: ghidra.util.task.TaskMonitor) -> ghidra.program.model.listing.Function:
        """
        Creates a function at entry point in the specified program.
        @param entryPoint the entry point of the function
        @param currentProgram the program where the function should be created
        @param monitor the task monitor that allows the user to cancel
        @return the new function or null if the function was not created
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

    def getStatusMsg(self) -> unicode: ...

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
