import ghidra.app.util.demangler
import ghidra.framework.cmd
import ghidra.framework.model
import ghidra.util.task
import java.lang


class DemanglerCmd(ghidra.framework.cmd.BackgroundCommand):




    @overload
    def __init__(self, addr: ghidra.program.model.address.Address, mangled: unicode): ...

    @overload
    def __init__(self, addr: ghidra.program.model.address.Address, mangled: unicode, options: ghidra.app.util.demangler.DemanglerOptions): ...



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

    def getDemangledObject(self) -> ghidra.app.util.demangler.DemangledObject: ...

    def getName(self) -> unicode: ...

    def getResult(self) -> unicode: ...

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
    def demangledObject(self) -> ghidra.app.util.demangler.DemangledObject: ...

    @property
    def result(self) -> unicode: ...