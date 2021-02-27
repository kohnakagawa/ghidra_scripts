import ghidra.framework.cmd
import ghidra.framework.model
import ghidra.util.task
import java.lang


class SharedReturnAnalysisCmd(ghidra.framework.cmd.BackgroundCommand):
    """
    Identifies functions to which Jump references exist and converts
     the associated branching instruction flow to a CALL-RETURN
    """





    def __init__(self, set: ghidra.program.model.address.AddressSetView, assumeContiguousFunctions: bool, considerConditionalBranches: bool):
        """
        Constructor
        @param set set of addresses over which destination functions will be
         examined for Jump reference to those functions.
        @param assumeContiguousFunctions if true it will be assumed that any unconditional
         jump over another function will trigger a call-return override and the creation of
        @param considerConditionalBranches if true conditional jumps can also be considered for jumping
         to another function as a shared return.
         a function at the destination.
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
