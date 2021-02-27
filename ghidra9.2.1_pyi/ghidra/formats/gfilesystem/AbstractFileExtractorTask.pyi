import ghidra.util.task
import java.lang


class AbstractFileExtractorTask(ghidra.util.task.Task):
    """
    Common base class for tasks that need to extract files from a GFileSystem location.

    """





    def __init__(self, title: unicode, canCancel: bool, hasProgress: bool, isModal: bool, rootOutputDir: java.io.File):
        """
        See {@link Task#Task(String, boolean, boolean, boolean)}.
        @param title See {@link Task#Task(String, boolean, boolean, boolean)}
        @param canCancel See {@link Task#Task(String, boolean, boolean, boolean)}
        @param hasProgress See {@link Task#Task(String, boolean, boolean, boolean)}
        @param isModal See {@link Task#Task(String, boolean, boolean, boolean)}
        @param rootOutputDir base directory where files will be extracted to
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

    def getTotalBytesExportedCount(self) -> long:
        """
        Return the number of bytes that were exported.
         <p>
        @return the number of bytes that were exported
        """
        ...

    def getTotalDirsExportedCount(self) -> int:
        """
        Return the number of directories that were exported.
         <p>
        @return the number of directories that were exported
        """
        ...

    def getTotalFilesExportedCount(self) -> int:
        """
        Return the number of files that were exported.
         <p>
        @return the number of files that were exported
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
        This is the method that will be called to do the work

         <P>Note: The run(TaskMonitor) method should not make any calls directly
         on Swing components, as these calls are not thread safe. Place Swing
         calls in a Runnable, then call {@link Swing#runLater(Runnable)} or
         {@link Swing#runNow(Runnable)}to schedule the Runnable inside of
         the AWT Event Thread.
        @param monitor The TaskMonitor that will monitor the executing Task
        @throws CancelledException if the task is cancelled.  Subclasses can trigger this exception
                                    by calling {@link TaskMonitor#checkCanceled()}.  This allows
                                    them to break out of the current work stack.
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

    @property
    def totalBytesExportedCount(self) -> long: ...

    @property
    def totalDirsExportedCount(self) -> int: ...

    @property
    def totalFilesExportedCount(self) -> int: ...
