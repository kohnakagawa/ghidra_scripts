import ghidra.util
import ghidra.util.task
import java.lang


class TaskUtilities(object):




    def __init__(self): ...



    @staticmethod
    def addTrackedTask(task: ghidra.util.task.Task, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Adds a Task to the list of tasks that have not yet finished running.
         <P>
         Note: it is safe to add the same task more than once, as it will not be repeatedly
         tracked.
        @param task The task to watch
        @param monitor the task monitor for the given task
        """
        ...

    @staticmethod
    def addTrackedTaskListener(listener: ghidra.util.TrackedTaskListener) -> None:
        """
        Adds a listener that will be notified when tasks are tracked (when they are added and
         removed from tracking).
        @param listener The listener to add.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    @staticmethod
    def isExecutingTasks() -> bool:
        """
        Returns true if there are tasks that are running or need to be run.
        @return true if there are tasks that are running or need to be run.
        """
        ...

    @staticmethod
    def isTaskRunning(title: unicode) -> bool:
        """
        Returns true if the task with the indicated title is running.
        @param title the title of the desired task
        @return true if the task with the indicated title is running.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def removeTrackedTask(task: ghidra.util.task.Task) -> None:
        """
        Removes the Task to the list of tasks that have not yet finished running.
        @param task The task to stop watching.
        """
        ...

    @staticmethod
    def removeTrackedTaskListener(listener: ghidra.util.TrackedTaskListener) -> None:
        """
        Removes the given listener added via {@link #addTrackedTask(Task,TaskMonitor)}.
        @param listener The listener that needs to be removed.
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
