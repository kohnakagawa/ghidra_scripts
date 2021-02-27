import ghidra.util.task
import java.lang
import java.util.concurrent
import utility.function


class TimeoutTaskMonitor(object, ghidra.util.task.TaskMonitor):
    """
    A task monitor that allows clients the ability to specify a timeout after which this monitor
     will be cancelled.

     This monitor can wrap an existing monitor.

     You can call #setTimeoutListener(Callback) to get a notification that the monitor
     timed-out.  In order to prevent this from firing after your work is finished normally, call
     #finished().
    """

    DUMMY: ghidra.util.task.TaskMonitor = ghidra.util.task.StubTaskMonitor@167dbce
    NO_PROGRESS_VALUE: int = -1







    def addCancelledListener(self, listener: ghidra.util.task.CancelledListener) -> None: ...

    def cancel(self) -> None: ...

    def checkCanceled(self) -> None: ...

    def clearCanceled(self) -> None: ...

    def didTimeout(self) -> bool:
        """
        Returns true if this monitor has timed-out
        @return true if this monitor has timed-out
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def finished(self) -> None: ...

    def getClass(self) -> java.lang.Class: ...

    def getMaximum(self) -> long: ...

    def getMessage(self) -> unicode: ...

    def getProgress(self) -> long: ...

    def hashCode(self) -> int: ...

    def incrementProgress(self, incrementAmount: long) -> None: ...

    def initialize(self, max: long) -> None: ...

    def isCancelEnabled(self) -> bool: ...

    def isCancelled(self) -> bool: ...

    def isIndeterminate(self) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def removeCancelledListener(self, listener: ghidra.util.task.CancelledListener) -> None: ...

    def setCancelEnabled(self, enable: bool) -> None: ...

    def setIndeterminate(self, indeterminate: bool) -> None: ...

    def setMaximum(self, max: long) -> None: ...

    def setMessage(self, message: unicode) -> None: ...

    def setProgress(self, value: long) -> None: ...

    def setShowProgressValue(self, showProgressValue: bool) -> None: ...

    def setTimeoutListener(self, timeoutCallback: utility.function.Callback) -> None:
        """
        Sets a callback function that will be called if the timeout is reached.
        @param timeoutCallback the callback to call
        """
        ...

    @overload
    @staticmethod
    def timeoutIn(timeout: long, timeUnit: java.util.concurrent.TimeUnit) -> ghidra.util.task.TimeoutTaskMonitor:
        """
        Creates a timeout task monitor that will be cancelled after the specified timeout.
        @param timeout the timeout value
        @param timeUnit the timeout time unit
        @return the newly created monitor
        """
        ...

    @overload
    @staticmethod
    def timeoutIn(timeout: long, timeUnit: java.util.concurrent.TimeUnit, monitor: ghidra.util.task.TaskMonitor) -> ghidra.util.task.TimeoutTaskMonitor:
        """
        Creates a timeout task monitor that will be cancelled after the specified timeout.  The
         created monitor wraps the given monitor, calling cancel on the given monitor when the
         timeout is reached.  This method allows you to use an existing monitor while adding
         the timeout feature.
        @param timeout the timeout value
        @param timeUnit the timeout time unit
        @param monitor the monitor to wrap
        @return the newly created monitor
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
    def cancelEnabled(self) -> bool: ...

    @cancelEnabled.setter
    def cancelEnabled(self, value: bool) -> None: ...

    @property
    def cancelled(self) -> bool: ...

    @property
    def indeterminate(self) -> bool: ...

    @indeterminate.setter
    def indeterminate(self, value: bool) -> None: ...

    @property
    def maximum(self) -> long: ...

    @maximum.setter
    def maximum(self, value: long) -> None: ...

    @property
    def message(self) -> unicode: ...

    @message.setter
    def message(self, value: unicode) -> None: ...

    @property
    def progress(self) -> long: ...

    @progress.setter
    def progress(self, value: long) -> None: ...

    @property
    def showProgressValue(self) -> None: ...  # No getter available.

    @showProgressValue.setter
    def showProgressValue(self, value: bool) -> None: ...

    @property
    def timeoutListener(self) -> None: ...  # No getter available.

    @timeoutListener.setter
    def timeoutListener(self, value: utility.function.Callback) -> None: ...
