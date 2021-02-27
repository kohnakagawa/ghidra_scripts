import java.lang


class GTimerMonitor(object):
    """
    Monitor object returned from a GTimer.schedule() call
    """

    DUMMY: ghidra.util.timer.GTimerMonitor = ghidra.util.timer.GTimerMonitor$1@68b4c065







    def cancel(self) -> bool:
        """
        Cancels the scheduled runnable associated with this GTimerMonitor if it has not already run.
        @return true if the scheduled runnable was cancelled before it had a chance to execute.
        """
        ...

    def didRun(self) -> bool:
        """
        Return true if the scheduled runnable has completed.
        @return true if the scheduled runnable has completed.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

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

    def wasCancelled(self) -> bool:
        """
        Return true if the scheduled runnable was cancelled before it had a chance to run.
        @return true if the scheduled runnable was cancelled before it had a chance to run.
        """
        ...
