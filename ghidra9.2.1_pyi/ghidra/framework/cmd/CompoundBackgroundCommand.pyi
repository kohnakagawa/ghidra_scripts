import ghidra.framework.cmd
import ghidra.framework.model
import ghidra.util.task
import java.lang


class CompoundBackgroundCommand(ghidra.framework.cmd.BackgroundCommand):
    """
    Compound command to handle multiple background commands.
    """





    def __init__(self, name: unicode, modal: bool, canCancel: bool):
        """
        Constructor
        @param name name of the command
        @param modal true means the monitor dialog is modal and the command has to
                complete or be canceled before any other action can occur
        @param canCancel true means the command can be canceled
        """
        ...



    @overload
    def add(self, cmd: ghidra.framework.cmd.BackgroundCommand) -> None:
        """
        Add a background command to this compound background command.
        """
        ...

    @overload
    def add(self, cmd: ghidra.framework.cmd.Command) -> None:
        """
        Add a command to this compound background command.
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

    def isEmpty(self) -> bool:
        """
        @return true if no sub-commands have been added
        """
        ...

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

    def size(self) -> int:
        """
        Get the number of background commands in this compound background
         command.
        """
        ...

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
    def empty(self) -> bool: ...
