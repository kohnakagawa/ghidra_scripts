import ghidra.framework.cmd
import ghidra.framework.model
import ghidra.util.task
import java.lang


class BackgroundCommand(object, ghidra.framework.cmd.Command):
    """
    Abstract command that will be run in a thread (in the background)
     other than the AWT(GUI) thread.  Use this to apply a long running
     command that is interruptable.

     The monitor allows the command to display status information as it
     executes.

     This allows commands to make changes in the background so that the
     GUI is not frozen and the user can still interact with the GUI.
    """





    @overload
    def __init__(self): ...

    @overload
    def __init__(self, name: unicode, hasProgress: bool, canCancel: bool, isModal: bool): ...



    @overload
    def applyTo(self, obj: ghidra.framework.model.DomainObject) -> bool: ...

    @overload
    def applyTo(self, obj: ghidra.framework.model.DomainObject, monitor: ghidra.util.task.TaskMonitor) -> bool:
        """
        Method called when this command is to apply changes to the
         given domain object.  A monitor is provided to display status
         information about the command as it executes in the background.
        @param obj domain object that will be affected by the command
        @param monitor monitor to show progress of the command
        @return true if the command applied successfully
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

    @property
    def modal(self) -> bool: ...

    @property
    def name(self) -> unicode: ...

    @property
    def statusMsg(self) -> unicode: ...
