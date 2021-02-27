import ghidra.framework.model
import ghidra.util.task
import java.lang


class GTask(object):
    """
    Interface for tasks to be run by GTaskManager.
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getName(self) -> unicode:
        """
        Returns the name of this task.
        @return the name of this task.
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def run(self, domainObject: ghidra.framework.model.UndoableDomainObject, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        the run method where work can be performed on the given domain object.
        @param domainObject the object to affect.
        @param monitor the taskMonitor to be used to cancel and report progress.
        @throws CancelledException if the user cancelled the task.
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
    def name(self) -> unicode: ...
