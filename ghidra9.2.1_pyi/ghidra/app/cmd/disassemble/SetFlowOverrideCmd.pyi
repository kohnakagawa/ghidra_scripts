import ghidra.framework.cmd
import ghidra.framework.model
import ghidra.util.task
import java.lang


class SetFlowOverrideCmd(ghidra.framework.cmd.BackgroundCommand):
    """
    Command for setting the fallthrough property on an instruction.
    """





    @overload
    def __init__(self, instAddr: ghidra.program.model.address.Address, flowOverride: ghidra.program.model.listing.FlowOverride):
        """
        Constructs a new command for overriding the flow  semantics of an instruction.
        @param instAddr the address of the instruction whose flow override is
         to be set.
        @param flowOverride the type of flow override.
        """
        ...

    @overload
    def __init__(self, set: ghidra.program.model.address.AddressSetView, flowOverride: ghidra.program.model.listing.FlowOverride):
        """
        Constructs a new command for overriding the flow  semantics of all instructions
         within the address set.
        @param set the address set of the instructions whose flow override is
         to be set.
        @param flowOverride the type of flow override.
        """
        ...



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
