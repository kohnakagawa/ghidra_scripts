import ghidra.framework.cmd
import ghidra.framework.model
import ghidra.util.task
import java.lang


class AddMemRefsCmd(ghidra.framework.cmd.BackgroundCommand):
    """
    AddMemRefsCmd adds a set of memory references from a
     specified address and opIndex to all code units identified by a
     set of addresses.
    """





    def __init__(self, fromAddr: ghidra.program.model.address.Address, toSet: ghidra.program.model.address.AddressSetView, refType: ghidra.program.model.symbol.RefType, source: ghidra.program.model.symbol.SourceType, opIndex: int):
        """
        Add memory references.
        @param fromAddr reference source
        @param toSet set of addresses which make up reference destinations.
         Only those addresses on code where a code unit exists will be considered.
        @param refType reference type to be applied.
        @param source the source of the reference
        @param opIndex source operand index
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
