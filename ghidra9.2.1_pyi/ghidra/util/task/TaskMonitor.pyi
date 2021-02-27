import ghidra.util.task
import java.lang


class TaskMonitor(object):
    """
    TaskMonitor provides an interface by means of which a
     potentially long running task can show its progress and also check if the user
     has cancelled the operation.

     Operations that support a task monitor should periodically
     check to see if the operation has been cancelled and abort. If possible, the
     operation should also provide periodic progress information. If it can estimate a
     percentage done, then it should use the setProgress(int) method,
     otherwise it should just call the setMessage(String) method.
    """

    DUMMY: ghidra.util.task.TaskMonitor = ghidra.util.task.StubTaskMonitor@167dbce
    NO_PROGRESS_VALUE: int = -1







    def addCancelledListener(self, listener: ghidra.util.task.CancelledListener) -> None:
        """
        Add cancelled listener
        @param listener the cancel listener
        """
        ...

    def cancel(self) -> None:
        """
        Cancel the task
        """
        ...

    def checkCanceled(self) -> None:
        """
        Check to see if this monitor has been canceled
        @throws CancelledException if monitor has been cancelled
        """
        ...

    def clearCanceled(self) -> None:
        """
        Clear the cancellation so that this TaskMonitor may be reused
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getMaximum(self) -> long:
        """
        Returns the current maximum value for progress
        @return the maximum progress value
        """
        ...

    def getMessage(self) -> unicode:
        """
        Gets the last set message of this monitor
        @return the message
        """
        ...

    def getProgress(self) -> long:
        """
        Returns the current progress value or {@link #NO_PROGRESS_VALUE} if there is no value
         set
        @return the current progress value or {@link #NO_PROGRESS_VALUE} if there is no value
         set
        """
        ...

    def hashCode(self) -> int: ...

    def incrementProgress(self, incrementAmount: long) -> None:
        """
        A convenience method to increment the current progress by the given value
        @param incrementAmount The amount by which to increment the progress
        """
        ...

    def initialize(self, max: long) -> None:
        """
        Initialized this TaskMonitor to the given max values.  The current value of this monitor
         will be set to zero.
        @param max maximum value for progress
        """
        ...

    def isCancelEnabled(self) -> bool:
        """
        Returns true if cancel ability is enabled
        @return true if cancel ability is enabled
        """
        ...

    def isCancelled(self) -> bool:
        """
        Returns true if the user has cancelled the operation
        @return true if the user has cancelled the operation
        """
        ...

    def isIndeterminate(self) -> bool:
        """
        Returns true if this monitor shows no progress
        @return true if this monitor shows no progress
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def removeCancelledListener(self, listener: ghidra.util.task.CancelledListener) -> None:
        """
        Remove cancelled listener
        @param listener the cancel listener
        """
        ...

    def setCancelEnabled(self, enable: bool) -> None:
        """
        Set the enablement of the Cancel button
        @param enable true means to enable the cancel button
        """
        ...

    def setIndeterminate(self, indeterminate: bool) -> None:
        """
        An indeterminate task monitor may choose to show an animation instead of updating progress
        @param indeterminate true if indeterminate
        """
        ...

    def setMaximum(self, max: long) -> None:
        """
        Set the progress maximum value
         <p><b>
         Note: setting this value will reset the progress to be the max if the progress is currently
         greater than the new new max value.</b>
        @param max maximum value for progress
        """
        ...

    def setMessage(self, message: unicode) -> None:
        """
        Sets the message displayed on the task monitor
        @param message the message to display
        """
        ...

    def setProgress(self, value: long) -> None:
        """
        Sets the current progress value
        @param value progress value
        """
        ...

    def setShowProgressValue(self, showProgressValue: bool) -> None:
        """
        True (the default) signals to paint the progress information inside of the progress bar
        @param showProgressValue true to paint the progress value; false to not
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
