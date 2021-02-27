import ghidra.framework.cmd
import ghidra.framework.model
import ghidra.program.model.address
import ghidra.program.model.listing
import ghidra.util.task
import java.lang


class CreateFunctionCmd(ghidra.framework.cmd.BackgroundCommand):
    """
    Command for Creating a function at an address.  It will copy off the
     parameters used to create the function (Selection or just an address) and
     create the function on redo and clear on undo.
    """





    @overload
    def __init__(self, entry: ghidra.program.model.address.Address):
        """
        Constructs a new command for creating a function that automatically computes
         the body of the function.
        @param entry the entry point at which to create a function.
        """
        ...

    @overload
    def __init__(self, entries: ghidra.program.model.address.AddressSetView):
        """
        Constructs a new command for creating functions that automatically computes
         the body of each function.
        @param entries the entry points at which to create functions.
        """
        ...

    @overload
    def __init__(self, entry: ghidra.program.model.address.Address, findEntryPoint: bool): ...

    @overload
    def __init__(self, entries: ghidra.program.model.address.AddressSetView, findEntryPoint: bool):
        """
        Constructs a new command for creating functions that automatically computes
         the body of each function.
        @param entries the entry points at which to create functions.
        """
        ...

    @overload
    def __init__(self, entries: ghidra.program.model.address.AddressSetView, source: ghidra.program.model.symbol.SourceType):
        """
        Constructs a new command for creating functions that automatically computes
         the body of each function.
        @param entries the entry points at which to create functions.
        """
        ...

    @overload
    def __init__(self, name: unicode, entry: ghidra.program.model.address.Address, body: ghidra.program.model.address.AddressSetView, source: ghidra.program.model.symbol.SourceType): ...

    @overload
    def __init__(self, name: unicode, entry: ghidra.program.model.address.Address, body: ghidra.program.model.address.AddressSetView, source: ghidra.program.model.symbol.SourceType, findEntryPoint: bool, recreateFunction: bool):
        """
        Constructs a new command for creating a function.  The default name
         for a function is the name associated with the current primary symbol which
         will be removed.
        @param name function name or null for default name.
        @param entry entry point address for the function to be created.
        @param body set of addresses to associated with the function to be created.
         The addresses must not already be included in the body of any existing function.
        @param source the source of this function
        @param findEntryPoint true if the entry point should be computed (entry could be in the middle of a function)
        @param recreateFunction true if the function body should be recreated even if the function exists.
        """
        ...

    @overload
    def __init__(self, name: unicode, entries: ghidra.program.model.address.AddressSetView, body: ghidra.program.model.address.AddressSetView, source: ghidra.program.model.symbol.SourceType, findEntryPoint: bool, recreateFunction: bool):
        """
        Constructs a new command for creating a function.  The default name
         for a function is the name associated with the current primary symbol which
         will be removed.
        @param name function name or null for default name.
        @param entries the entry points at which to create functions.
        @param body set of addresses to associated with the function to be created.
         The addresses must not already be included in the body of any existing function.
        @param source the source of this function
        @param findEntryPoint true if the entry point should be computed (entry could be in the middle of a function)
        @param recreateFunction true if the function body should be recreated even if the function exists.
        """
        ...



    @overload
    def applyTo(self, obj: ghidra.framework.model.DomainObject) -> bool: ...

    @overload
    def applyTo(self, obj: ghidra.framework.model.DomainObject, monitor: ghidra.util.task.TaskMonitor) -> bool:
        """
        @see ghidra.framework.cmd.BackgroundCommand#applyTo(ghidra.framework.model.DomainObject, ghidra.util.task.TaskMonitor)
        """
        ...

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

    @overload
    @staticmethod
    def fixupFunctionBody(program: ghidra.program.model.listing.Program, func: ghidra.program.model.listing.Function, monitor: ghidra.util.task.TaskMonitor) -> bool:
        """
        Recompute function body.  An open transaction must already exist.
        @param program the program the function is in.
        @param func the function to be fixed up.  A null function will return false.
        @param monitor task monitor
        @return true if successful, false if unable to fixup function or
         no function found containing the start address of the indicated instruction
        @throws CancelledException if the function fixup is cancelled.
        """
        ...

    @overload
    @staticmethod
    def fixupFunctionBody(program: ghidra.program.model.listing.Program, start_inst: ghidra.program.model.listing.Instruction, monitor: ghidra.util.task.TaskMonitor) -> bool:
        """
        Recompute function body.  An open transaction must already exist.
        @param program the program the function is in.
        @param start_inst instruction that is within the function to be fixed up.
        @param monitor task monitor
        @return true if successful, false if cancelled or unable to fixup function or
         no function found containing the start address of the indicated instruction
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getFunction(self) -> ghidra.program.model.listing.Function:
        """
        Returns function if create command was successful
        """
        ...

    @overload
    @staticmethod
    def getFunctionBody(program: ghidra.program.model.listing.Program, entry: ghidra.program.model.address.Address) -> ghidra.program.model.address.AddressSetView:
        """
        Find the function body by following all flows other than a call from the
         entry point.
        @param program the program where the function is being created.
        @param entry entry point to start tracing flow
        @return AddressSetView address set representing the body of the function
        """
        ...

    @overload
    @staticmethod
    def getFunctionBody(program: ghidra.program.model.listing.Program, entry: ghidra.program.model.address.Address, monitor: ghidra.util.task.TaskMonitor) -> ghidra.program.model.address.AddressSetView: ...

    @overload
    @staticmethod
    def getFunctionBody(monitor: ghidra.util.task.TaskMonitor, program: ghidra.program.model.listing.Program, entry: ghidra.program.model.address.Address) -> ghidra.program.model.address.AddressSetView:
        """
        Find the function body by following all flows other than a call from the
         entry point.
        @param program the program where the function is being created.
        @param entry entry point to start tracing flow
        @return AddressSetView address set representing the body of the function
        """
        ...

    @overload
    @staticmethod
    def getFunctionBody(program: ghidra.program.model.listing.Program, entry: ghidra.program.model.address.Address, includeOtherFunctions: bool, monitor: ghidra.util.task.TaskMonitor) -> ghidra.program.model.address.AddressSetView: ...

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

    @property
    def function(self) -> ghidra.program.model.listing.Function: ...
