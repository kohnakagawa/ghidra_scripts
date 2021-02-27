import ghidra.framework.cmd
import ghidra.framework.model
import ghidra.util.task
import java.lang


class CaptureFunctionDataTypesCmd(ghidra.framework.cmd.BackgroundCommand):
    """
    Capture all selected function signature data types from the current program and put them
     in the data type manager.
    """





    def __init__(self, dtm: ghidra.program.model.data.DataTypeManager, set: ghidra.program.model.address.AddressSetView, listener: ghidra.app.cmd.function.CaptureFunctionDataTypesListener):
        """
        Constructs a new command to create function definition data types
         in the given data type manager from the function's whose entry points are in the
         address set.
        @param dtm data type manager containing the function signature data types
        @param set set of addresses containing the entry points of the functions whose signatures
         are to be turned into data types.
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

    def taskCompleted(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...