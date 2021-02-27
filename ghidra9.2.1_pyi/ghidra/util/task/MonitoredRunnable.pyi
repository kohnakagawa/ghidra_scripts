import ghidra.util.task
import java.lang


class MonitoredRunnable(object):








    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def monitoredRun(self, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Similar to a runnable except that is given a monitor to report progress and check for
         cancellation.
        @param monitor the TaskMonitor to use.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
