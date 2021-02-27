import ghidra.framework.task
import java.lang


class GScheduledTask(object, java.lang.Comparable):
    """
    Class for tracking scheduled GTasks.  When tasks are scheduled, they are assigned to a GTaskGroup,
     given a priority, assigned a one-up ID, given a GTaskMonitor.  This class is used to keep all
     that information together.

    """





    def __init__(self, group: ghidra.framework.task.GTaskGroup, task: ghidra.framework.task.GTask, priority: int):
        """
        Create a new GScheduledTask when a task is scheduled with the GTaskManager.
        @param group the group that this task belongs to.
        @param task the task being scheduled.
        @param priority the priority at which this task is to be executed relative to other
         scheduled tasks.  Lower numbers are run before higher numbers.
        """
        ...



    @overload
    def compareTo(self, other: ghidra.framework.task.GScheduledTask) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDescription(self) -> unicode:
        """
        Returns the description for the scheduled GTask.
        @return the description for the scheduled GTask.
        """
        ...

    def getGroup(self) -> ghidra.framework.task.GTaskGroup:
        """
        Return GTaskGroup for this task.
        @return the GTaskGroup
        """
        ...

    def getPriority(self) -> int:
        """
        Returns the priority at which the task was scheduled. Lower numbers have higher priority.
        @return the priority at which the task was scheduled.
        """
        ...

    def getTask(self) -> ghidra.framework.task.GTask:
        """
        Returns the GTask that is scheduled.
        @return the GTask that is scheduled.
        """
        ...

    def getTaskMonitor(self) -> ghidra.framework.task.GTaskMonitor:
        """
        Returns the GTaskMonitor that will be used for this task.
        @return the GTaskMonitor that will be used for this task.
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def description(self) -> unicode: ...

    @property
    def group(self) -> ghidra.framework.task.GTaskGroup: ...

    @property
    def priority(self) -> int: ...

    @property
    def task(self) -> ghidra.framework.task.GTask: ...

    @property
    def taskMonitor(self) -> ghidra.framework.task.GTaskMonitor: ...
