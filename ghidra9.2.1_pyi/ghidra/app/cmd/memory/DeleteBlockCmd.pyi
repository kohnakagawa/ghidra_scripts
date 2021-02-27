import ghidra.framework.cmd
import ghidra.framework.model
import ghidra.util.task
import java.lang


class DeleteBlockCmd(ghidra.framework.cmd.BackgroundCommand):
    """
    Command that runs in the background to delete a memory block, as
     the delete may be a time consuming operation.
    """





    def __init__(self, blockAddresses: List[ghidra.program.model.address.Address], listener: ghidra.app.cmd.memory.DeleteBlockListener):
        """
        Creates a background command for deleting memory blocks. Each address in
         the array of block addresses indicates that the block containing that
         address should be removed.
         After the command has completed, getStatus() can be called to check the success.
         If unsuccessful, getStatusMsg() can be called to get a message
         indicating why the command failed.
        @param blockAddresses addresses indicating each block to be removed.
        @param listener listener that will be notified when the delete block has completed.
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

    def getStatus(self) -> bool:
        """
        Return whether the delete block was successful.
        @return true if the block was deleted
        """
        ...

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
        @see ghidra.framework.cmd.BackgroundCommand#taskCompleted()
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
    def status(self) -> bool: ...
