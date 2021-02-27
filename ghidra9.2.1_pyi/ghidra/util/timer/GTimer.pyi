import ghidra.util.timer
import java.lang


class GTimer(object):




    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def scheduleRepeatingRunnable(delay: long, period: long, callback: java.lang.Runnable) -> ghidra.util.timer.GTimerMonitor:
        """
        Schedules a runnable for <b>repeated</b> execution after the specified delay.
        @param delay the time (in milliseconds) to wait before executing the runnable.
        @param period time in milliseconds between successive runnable executions.
        @param callback the runnable to be executed.
        @return a GTimerMonitor which allows the caller to cancel the timer and check its status.
        """
        ...

    @staticmethod
    def scheduleRunnable(delay: long, callback: java.lang.Runnable) -> ghidra.util.timer.GTimerMonitor:
        """
        Schedules a runnable for execution after the specified delay.
        @param delay the time (in milliseconds) to wait before executing the runnable.
        @param callback the runnable to be executed.
        @return a GTimerMonitor which allows the caller to cancel the timer and check its status.
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
