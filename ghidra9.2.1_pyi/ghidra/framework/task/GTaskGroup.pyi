from typing import List
import ghidra.framework.task
import java.lang


class GTaskGroup(object):
    """
    Class for grouping several GTasks that all should be
     executed before any new group of tasks are
     executed, regardless of priority.
    """





    def __init__(self, description: unicode, startNewTransaction: bool):
        """
        Creates a new named GTaskGroup.
        @param description the display name for the group.
        @param startNewTransaction if true, any existing transaction (if there is one) will be closed
         and a new transaction will be created.  Otherwise, the tasks in this group will be executed
         in the same transaction as the previous group. Note that this can only happen if there was
         a previous group executing at the time this group is scheduled.
        """
        ...



    def addTask(self, task: ghidra.framework.task.GTask, priority: int) -> ghidra.framework.task.GScheduledTask:
        """
        Add a task to this group with the given priority.  Tasks can only be added to this group
         before the group is added to the GTaskManager.  After that, an IllegalStateException will
         be thrown.
        @param task the task being added to this group.
        @param priority the priority for the task within the group.
        @return the GScheduledTask created to schedule this task within the group.
        @throws IllegalStateException if this method is called after the group has been added to
         the GTaskManager.
        """
        ...

    def compareTo(self, group: ghidra.framework.task.GTaskGroup) -> int: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDescription(self) -> unicode:
        """
        Returns a description for the group.
        @return a description for this group.
        """
        ...

    def getTaskMonitor(self) -> ghidra.framework.task.GTaskMonitor:
        """
        Returns the TaskMonitor that will be used to track the overall progress of tasks within this
         group.
        @return the TaskMonitor that will be used to track the overall progress of tasks within this
         group.
        """
        ...

    def getTasks(self) -> List[ghidra.framework.task.GScheduledTask]:
        """
        Returns a list scheduled tasks in the group.
        @return a list scheduled tasks in the group.
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setCancelled(self) -> None:
        """
        Cancels the group.  Any tasks that haven't yet started will never run.
        """
        ...

    def setScheduled(self) -> None: ...

    def taskCompleted(self) -> None:
        """
        Notification that a task in the group has been completed.  The group keeps track of the overall
         progress of the tasks completed in this group.  This call is used to notify the group that
         another one of its tasks was completed.
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    def wantsNewTransaction(self) -> bool:
        """
        Returns true if this group wants to start a new transaction when it runs.  Otherwise, the
         group will add-on to any existing transaction from the previous group.
        @return true if a new transaction should be started for this group.
        """
        ...

    def wasCancelled(self) -> bool:
        """
        Returns true if this group was cancelled.
        @return true if this group was cancelled.
        """
        ...

    @property
    def description(self) -> unicode: ...

    @property
    def taskMonitor(self) -> ghidra.framework.task.GTaskMonitor: ...

    @property
    def tasks(self) -> List[object]: ...
