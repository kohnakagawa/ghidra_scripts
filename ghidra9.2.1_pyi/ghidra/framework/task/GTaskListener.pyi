import ghidra.framework.task
import java.lang


class GTaskListener(object):
    """
    Interface used to track the state of a GTaskManager
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def initialize(self) -> None:
        """
        Called when a task listener is added so that the listener can get all the initial state of
         the taskManger while the taskManager is in a locked state where nothing will change.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def suspendedStateChanged(self, suspended: bool) -> None:
        """
        Notification that the GTaskManager has been suspended or resumed.
        @param suspended true if the GTaskManger has been suspended, or false if it has been resumed.
        """
        ...

    def taskCompleted(self, task: ghidra.framework.task.GScheduledTask, result: ghidra.framework.task.GTaskResult) -> None:
        """
        Notification that a task is no longer running regardless of whether it completed normally,
         was cancelled, or threw an unhandled exception.
        @param task the ScheduledTask that was running.
        @param result the result state for the task.
        """
        ...

    def taskGroupCompleted(self, taskGroup: ghidra.framework.task.GTaskGroup) -> None:
        """
        Notification that the GTaskGroup has completed running.
        @param taskGroup the GTaskGroup that has completed running.
        """
        ...

    def taskGroupScheduled(self, group: ghidra.framework.task.GTaskGroup) -> None:
        """
        Notification that a GTaskGroup has been scheduled.
        @param group the GTaskGroup that has been scheduled to run.
        """
        ...

    def taskGroupStarted(self, taskGroup: ghidra.framework.task.GTaskGroup) -> None:
        """
        Notification that a new GTaskGroup has started to run.
        @param taskGroup the new GTaskGroup that is running.
        """
        ...

    def taskScheduled(self, scheduledTask: ghidra.framework.task.GScheduledTask) -> None:
        """
        Notification that a new GTask has been scheduled to run.
        @param scheduledTask the GScheduledTask that wraps the GTask with scheduling information.
        """
        ...

    def taskStarted(self, task: ghidra.framework.task.GScheduledTask) -> None:
        """
        Notification that a task is starting to run
        @param task the GTask that is starting to run
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
