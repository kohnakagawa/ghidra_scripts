import ghidra.util.task
import java.lang


class ServerConnectTask(ghidra.util.task.Task):
    """
    Task for connecting to server with Swing thread.
    """





    @overload
    def __init__(self, title: unicode):
        """
        Creates new Task.
        @param title the title associated with the task
        """
        ...

    @overload
    def __init__(self, title: unicode, canCancel: bool, hasProgress: bool, isModal: bool):
        """
        Construct a new Task.
        @param title title the title associated with the task
        @param canCancel true means that the user can cancel the task
        @param hasProgress true means that the dialog should show a
         progress indicator
        @param isModal true means that the dialog is modal and the task has to
         complete or be canceled before any other action can occur
        """
        ...

    @overload
    def __init__(self, title: unicode, canCancel: bool, hasProgress: bool, isModal: bool, waitForTaskCompleted: bool):
        """
        Construct a new Task.
        @param title title the title associated with the task
        @param canCancel true means that the user can cancel the task
        @param hasProgress true means that the dialog should show a
         progress indicator
        @param isModal true means that the dialog is modal and the task has to
         complete or be canceled before any other action can occur
        @param waitForTaskCompleted true causes the running thread to block until the finish or
          	  cancelled callback has completed on the swing thread.  Note: passing true
          	  only makes sense if the task is modal.
        """
        ...



    def addTaskListener(self, listener: ghidra.util.task.TaskListener) -> None:
        """
        Sets the task listener on this task.  It is a programming error to call this method more
         than once or to call this method if a listener was passed into the constructor of this class.
        @param listener the listener
        """
        ...

    def canCancel(self) -> bool:
        """
        Returns true if the task can be canceled.
        @return boolean true if the user can cancel the task
        """
        ...

    def cancel(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getStatusTextAlignment(self) -> int:
        """
        Returns the alignment of the text displayed in the modal dialog.  The default is
         {@link SwingConstants#CENTER}.   For status updates where the initial portion of the
         text does not change, {@link SwingConstants#LEADING} is recommended.  To change the
         default value, simply override this method and return one of {@link SwingConstants}
         CENTER, LEADING or TRAILING.
        @return the alignment of the text displayed
        """
        ...

    def getTaskTitle(self) -> unicode:
        """
        Get the title associated with the task
        @return String title shown in the dialog
        """
        ...

    def hasProgress(self) -> bool:
        """
        Return true if the task has a progress indicator.
        @return boolean true if the task shows progress
        """
        ...

    def hashCode(self) -> int: ...

    def isModal(self) -> bool:
        """
        Returns true if the dialog associated with the task is modal.
        @return boolean true if the associated dialog is modal
        """
        ...

    def monitoredRun(self, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        When an object implementing interface <code>Runnable</code> is used to create a thread,
         starting the thread causes the object's <code>run</code> method to be called in that
         separately executing thread.
        @param monitor the task monitor
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def run(self, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Completes and necessary authentication and obtains a repository handle.
         If a connection error occurs, an exception will be stored ({@link #getException()}.
        @see ghidra.util.task.Task#run(ghidra.util.task.TaskMonitor)
        """
        ...

    def setHasProgress(self, b: bool) -> None:
        """
        Sets this task to have progress or not.  Note: changing this value after launching the
         task will have no effect.
        @param b true to show progress, false otherwise.
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
