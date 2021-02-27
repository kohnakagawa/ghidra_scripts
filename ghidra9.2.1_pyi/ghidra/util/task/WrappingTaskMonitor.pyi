import ghidra.util.task
import java.lang


class WrappingTaskMonitor(object, ghidra.util.task.TaskMonitor):
    """
    An implementation of the TaskMonitor interface that simply wraps a delegate task
     monitor.   This is useful for classes that wish to wrap a task monitor, changing behavior
     as needed by overriding a subset of methods.

     Synchronization Policy:
     We wish for this class to be performant.    Thus, we do not synchronize the methods of this
     class. The #setDelegate(TaskMonitor) is synchronized to ensure thread visibility
     for the state of the delegate monitor.

     When calling #setDelegate(TaskMonitor) there is the potential for the values being
     transferred to become inconsistent with any new values being set.  We have decided that this
     does not much matter for the overall progress or the messages on the monitor.  However, most
     of the other setter methods could lead to bad behavior if they are inconsistent.
    """

    DUMMY: ghidra.util.task.TaskMonitor = ghidra.util.task.StubTaskMonitor@167dbce
    NO_PROGRESS_VALUE: int = -1



    def __init__(self, delegate: ghidra.util.task.TaskMonitor):
        """
        Constructor
        @param delegate the delegate task monitor
        """
        ...



    def addCancelledListener(self, listener: ghidra.util.task.CancelledListener) -> None: ...

    def cancel(self) -> None: ...

    def checkCanceled(self) -> None: ...

    def clearCanceled(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

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

    def setDelegate(self, newDelegate: ghidra.util.task.TaskMonitor) -> None:
        """
        Sets the delegate of this wrapper to be the new value.  The new delegate will be
         initialized with the current values of the existing delegate.
        @param newDelegate the new delegate
        """
        ...

    def setIndeterminate(self, indeterminate: bool) -> None: ...

    def setMaximum(self, max: long) -> None: ...

    def setMessage(self, message: unicode) -> None: ...

    def setProgress(self, value: long) -> None: ...

    def setShowProgressValue(self, showProgressValue: bool) -> None: ...

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
    def delegate(self) -> None: ...  # No getter available.

    @delegate.setter
    def delegate(self, value: ghidra.util.task.TaskMonitor) -> None: ...

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
