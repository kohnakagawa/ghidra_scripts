import ghidra.framework.cmd
import ghidra.framework.model
import ghidra.framework.plugintool
import ghidra.util.task
import java.lang


class SubroutineModelCmd(ghidra.framework.cmd.BackgroundCommand):
    """
    Command that organizes a Module or Fragment according to a specified block
     model. This organization produces a "flat" (single layer) partitioning.
    """





    def __init__(self, groupPath: ghidra.program.util.GroupPath, treeName: unicode, blockModelService: ghidra.app.services.BlockModelService, modelName: unicode):
        """
        Constructor
        @param groupPath group path of the affected Module or Fragment
        @param treeName name of the tree where group exists
        @param blockModelService service that has the known block models
        @param modelName name of the model to use
        """
        ...



    @overload
    def applyTo(self, obj: ghidra.framework.model.DomainObject) -> bool: ...

    @overload
    def applyTo(self, obj: ghidra.framework.model.DomainObject, monitor: ghidra.util.task.TaskMonitor) -> bool:
        """
        @see ghidra.framework.cmd.BackgroundCommand#applyTo(ghidra.framework.model.DomainObject,
              ghidra.util.task.TaskMonitor)
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

    def setPluginTool(self, tool: ghidra.framework.plugintool.PluginTool) -> None: ...

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
    def pluginTool(self) -> None: ...  # No getter available.

    @pluginTool.setter
    def pluginTool(self, value: ghidra.framework.plugintool.PluginTool) -> None: ...
