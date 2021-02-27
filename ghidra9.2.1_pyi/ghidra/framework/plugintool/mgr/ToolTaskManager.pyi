import ghidra.framework.cmd
import ghidra.framework.model
import ghidra.framework.plugintool.mgr
import ghidra.util.task
import java.lang
import javax.swing


class ToolTaskManager(object, java.lang.Runnable):
    """
    Manages a queue of background tasks that execute commands.
    """





    def __init__(self, tool: ghidra.framework.plugintool.PluginTool):
        """
        Construct a new ToolTaskManager.
        @param tool tool associated with this ToolTaskManager
        """
        ...



    def cancelCurrentTask(self) -> None:
        """
        Cancel the current task.
        """
        ...

    def clearQueuedCommands(self, obj: ghidra.framework.model.UndoableDomainObject) -> None:
        """
        Clear the queue of scheduled commands.
        """
        ...

    @overload
    def clearTasks(self) -> None:
        """
        Clear the list of tasks.
        """
        ...

    @overload
    def clearTasks(self, obj: ghidra.framework.model.UndoableDomainObject) -> None:
        """
        Clear all tasks associated with specified domain object.
        @param obj domain object
        """
        ...

    def dispose(self) -> None:
        """
        Clear list of tasks and queue of scheduled commands.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def execute(self, cmd: ghidra.framework.cmd.Command, obj: ghidra.framework.model.DomainObject) -> bool:
        """
        Execute the given command in the foreground
        @param cmd command to execute
        @param obj domain object to which the command will be applied
        @return the completion status of the command
        @see Command#applyTo(DomainObject)
        """
        ...

    def executeCommand(self, cmd: ghidra.framework.cmd.BackgroundCommand, obj: ghidra.framework.model.UndoableDomainObject) -> None:
        """
        Execute the given command in the background
        @param cmd background command
        @param obj domain object that supports undo/redo
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getMonitorComponent(self) -> javax.swing.JComponent:
        """
        Get the monitor component that shows progress and has a cancel button.
        @return the monitor component
        """
        ...

    def getTaskThreadGroup(self) -> java.lang.ThreadGroup:
        """
        Returns the thread group associated with all background tasks run by this
         manager and their instantiated threads.
        @return task thread group
        """
        ...

    def hasTasksForDomainObject(self, domainObject: ghidra.framework.model.DomainObject) -> bool: ...

    def hashCode(self) -> int: ...

    def isBusy(self) -> bool:
        """
        Return true if a task is executing
        @return true if a task is executing
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def run(self) -> None:
        """
        @see java.lang.Runnable#run()
        """
        ...

    def scheduleFollowOnCommand(self, cmd: ghidra.framework.cmd.BackgroundCommand, obj: ghidra.framework.model.UndoableDomainObject) -> None:
        """
        Schedule the given background command when the current command completes.
        @param cmd background command to be scheduled
        @param obj domain object that supports undo/redo
        """
        ...

    def stop(self, wait: bool) -> None:
        """
        Cancel the currently running task and clear all commands that are
         scheduled to run. Block until the currently running task ends.
        @param wait if true wait for current task to cancel cleanly
        """
        ...

    def taskCompleted(self, obj: ghidra.framework.model.UndoableDomainObject, task: ghidra.framework.plugintool.mgr.BackgroundCommandTask, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Notification from the BackgroundCommandTask that it has completed; queued
         or scheduled commands are executed.
        @param obj domain object that supports undo/redo
        @param task background command task that has completed
        @param monitor task monitor
        """
        ...

    def taskFailed(self, obj: ghidra.framework.model.UndoableDomainObject, taskCmd: ghidra.framework.cmd.BackgroundCommand, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Notification from the BackgroundCommandTask that the given command
         failed. Any scheduled commands are cleared from the queue.
        @param obj domain object that supports undo/redo
        @param taskCmd background command that failed
        @param monitor task monitor for the background task
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
    def busy(self) -> bool: ...

    @property
    def monitorComponent(self) -> javax.swing.JComponent: ...

    @property
    def taskThreadGroup(self) -> java.lang.ThreadGroup: ...
