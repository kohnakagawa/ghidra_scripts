import ghidra.framework.cmd
import ghidra.framework.model
import ghidra.util.task
import java.lang


class FunctionResultStateStackAnalysisCmd(ghidra.framework.cmd.BackgroundCommand):
    """
    Command for analyzing the Stack; the command is run in the background.
    """





    @overload
    def __init__(self, entry: ghidra.program.model.address.Address, forceProcessing: bool):
        """
        Constructs a new command for analyzing the Stack.
        @param entry the entry point of the function that contains the stack to
                   be analyzed.
        @param forceProcessing flag to force processing of stack references even if the stack
                   has already been defined.
        """
        ...

    @overload
    def __init__(self, entries: ghidra.program.model.address.AddressSetView, forceProcessing: bool):
        """
        Constructs a new command for analyzing the Stack.
        @param entries and address set indicating the entry points of functions that have
         stacks to be analyzed.
        @param forceProcessing flag to force processing of stack references even if the stack
                   has already been defined.
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
