import ghidra.util.task
import java.lang


class SwingRunnable(ghidra.util.task.MonitoredRunnable, object):
    """
    Runnable that has a method that may need to be run in the Swing AWT thread.
     Pass a SwingRunnable to the RunManager if follow on work needs to be done
     after the run() method completes.
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def monitoredRun(self, __a0: ghidra.util.task.TaskMonitor) -> None: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def swingRun(self, isCancelled: bool) -> None:
        """
        Callback on the swing thread.
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
