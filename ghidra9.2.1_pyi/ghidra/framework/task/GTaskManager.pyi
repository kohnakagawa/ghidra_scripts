from typing import List
import ghidra.framework.task
import java.lang


class GTaskManager(object):
    """
    Class for managing a queue of tasks to be executed, one at a time, in priority order.  All the
     tasks pertain to an UndoableDomainObject and transactions are created on the UndoableDomainObject
     so that tasks can operate on them.

     Tasks are organized into groups such that all tasks in a group will be completed before the
     tasks in the next group, regardless of priority.  Within a group, task are ordered first by
     priority and then by the order in which they were added to the group. Groups are executed
     in the order that they are scheduled.

     All tasks within the same group are executed within the same transaction on the
     UndoableDomainObject.  When all the tasks within a group are completed, the transaction is closed
     unless there is another group scheduled and that group does not specify that it should run in its
     own transaction.

     Suspending:
     The GTaskManager can be suspended.  When suspended, any currently running task will continue to
     run, but no new or currently scheduled tasks will be executed until the GTaskManager is resumed.
     There is a special method, #runNextTaskEvenWhenSuspended(), that will run the next scheduled task
     even if the GTaskManager is suspended.

     Yielding to Other Tasks:
     While running, a GTask can call the method #waitForHigherPriorityTasks() on the GTaskManager,
     which will cause the the GTaskManager to run scheduled tasks (within the same group) that are
     a higher priority than the running task, effectively allowing the running task to yield until all
     higher priority tasks are executed.
    """





    def __init__(self, undoableDomainObject: ghidra.framework.model.UndoableDomainObject, threadPool: generic.concurrent.GThreadPool):
        """
        Creates a new GTaskManager for an UndoableDomainObject
        @param undoableDomainObject the domainObject that tasks scheduled in this GTaskManager will
         operate upon.
        @param threadPool the GThreadPool that will provide the threads that will be used to run
         tasks in this GTaskManager.
        """
        ...



    def addTaskListener(self, listener: ghidra.framework.task.GTaskListener) -> None:
        """
        Adds a GTaskListener to be notified as tasks are completed.
        @param listener the listener to add
        """
        ...

    def cancelAll(self) -> None:
        """
        Cancels all scheduled groups and tasks. The TaskMonitor for
         the currently running task will be cancelled, but the task will continue to run until it
         checks the monitor.
        """
        ...

    def cancelRunningGroup(self, group: ghidra.framework.task.GTaskGroup) -> None:
        """
        Cancels all tasks in the currently running group.  Tasks in the group that have not yet started
         will never run and will immediately be put into the TaskResults list.  The TaskMonitor for
         the currently running task will be cancelled, but the task will continue to run until it
         checks the monitor.
        @param group the group to be cancelled.  It must match the currently running group or nothing
         will happen.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getCurrentGroup(self) -> ghidra.framework.task.GTaskGroup:
        """
        Returns the currently running group, or null if no group is running.
        @return the currently running group, or null if no group is running.
        """
        ...

    def getDelayedTasks(self) -> List[ghidra.framework.task.GScheduledTask]:
        """
        Returns a list of Tasks that are currently waiting for higher priority tasks.
        @return a list of Tasks that are currently waiting for higher priority tasks.
        """
        ...

    def getRunningTask(self) -> ghidra.framework.task.GScheduledTask:
        """
        Returns the currently running task, or null if no task is running.
        @return the currently running task;
        """
        ...

    def getScheduledGroups(self) -> List[ghidra.framework.task.GTaskGroup]:
        """
        Returns a list of Groups that are waiting to run.
        @return a list of Groups that are waiting to run.
        """
        ...

    def getScheduledTasks(self) -> List[ghidra.framework.task.GScheduledTask]:
        """
        Returns a list of scheduled tasks for the currently running group.
        @return a list of scheduled tasks for the currently running group.
        """
        ...

    def getTaskResults(self) -> List[ghidra.framework.task.GTaskResult]:
        """
        Returns a list of the most recent GTaskResults.  The TaskManager only keeps the most recent
         N GTaskResults.
        @return the list of the most recent GTaskResults.
        """
        ...

    def hashCode(self) -> int: ...

    def isBusy(self) -> bool:
        """
        Returns true if this manager is running a task, or if suspended has additional tasks queued.
        @return true if this manager is running a task, or if suspended has additional tasks queued.
        """
        ...

    def isRunning(self) -> bool:
        """
        Returns true if this manager is currently running a task. If not suspended, a GTaskManager
         will always be executing a task as long as there are tasks to execute.  If suspended, a
         GTaskManager may have tasks scheduled, but may not be currently executing one.
        @return true if this manager is currently running a task.
        """
        ...

    def isSuspended(self) -> bool:
        """
        Returns true if this GTaskManager is currently suspended.
        @return true if this GTaskManager is currently suspended.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def removeTaskListener(self, listener: ghidra.framework.task.GTaskListener) -> None:
        """
        Removes the given GTaskListener from this queue.
        @param listener the listener to remove.
        """
        ...

    def runNextTaskEvenWhenSuspended(self) -> None:
        """
        This method will cause the next scheduled task to run even though the task manager is
         suspended.  Calling this method while the queue is not suspended has no effect because
         if not suspended, it will be busy (or have nothing to do)
        """
        ...

    @overload
    def scheduleTask(self, task: ghidra.framework.task.GTask, priority: int, useCurrentGroup: bool) -> ghidra.framework.task.GScheduledTask:
        """
        Schedules a task to be run by this TaskManager. Tasks are run one at a time.
        @param task the task to be run.
        @param priority the priority of the task.  Lower numbers are run before higher numbers.
        @param useCurrentGroup . If true, this task will be rolled into the current transaction group
         							if one exists.  If false, any open transaction
         							will be closed and a new transaction will be opened before
         							this task is run.
        """
        ...

    @overload
    def scheduleTask(self, task: ghidra.framework.task.GTask, priority: int, groupName: unicode) -> None:
        """
        Schedules a task to be run by this TaskManager within the group with the given group name.
         If a group already exists with the given name(either currently running or waiting), the task
         will be added to that group. Otherwise, a new group will be created with the given group name
         and the task will be placed in that group.
        @param task the task to be run.
        @param priority the priority of the task.  Lower numbers are run before higher numbers.
        @param groupName . The name of the group that the task will be added to.
        """
        ...

    def scheduleTaskGroup(self, group: ghidra.framework.task.GTaskGroup) -> None:
        """
        Schedules a task group to run.  Task groups are run in the order they are scheduled. They
         have the option of being executed in the current transaction (if it exists) or starting
         a new transaction.
        @param group the TaskGroup to be scheduled.
        """
        ...

    def setSuspended(self, b: bool) -> None:
        """
        Sets the suspended state of this task queue.  While suspended, this task manager will not
         start any new tasks in its queue.  Any currently running task will continue to run.
        @param b true to suspend this manager, false to resume executing new tasks.
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    def waitForHigherPriorityTasks(self) -> None:
        """
        This methods is for currently running tasks to suspend and allow higher priority tasks
         (within the same task group) to complete before continuing.  If called by any thread other
         than the thread that is currently executing a task for this queue, an exception will be
         thrown.
        @throws IllegalStateException if this method is called from any thread not currently
         executing the current task for this queue.
        """
        ...

    def waitUntilBusy(self, timeoutMillis: long) -> bool: ...

    def waitWhileBusy(self, timeoutMillis: long) -> bool: ...

    @property
    def busy(self) -> bool: ...

    @property
    def currentGroup(self) -> ghidra.framework.task.GTaskGroup: ...

    @property
    def delayedTasks(self) -> List[object]: ...

    @property
    def running(self) -> bool: ...

    @property
    def runningTask(self) -> ghidra.framework.task.GScheduledTask: ...

    @property
    def scheduledGroups(self) -> List[object]: ...

    @property
    def scheduledTasks(self) -> List[object]: ...

    @property
    def suspended(self) -> bool: ...

    @suspended.setter
    def suspended(self, value: bool) -> None: ...

    @property
    def taskResults(self) -> List[object]: ...
