import ghidra.util.task
import java.lang


class ImportBatchTask(ghidra.util.task.Task):
    """
    Performs a batch import using the data provided in the BatchInfo object which
     specifies what files and the import language that should be used.

     If there are just a few files to import, they will be opened using the ProgramManager,
     otherwise the programManager parameter will be unused.
    """

    MAX_PROGRAMS_TO_OPEN: int = 50



    def __init__(self, batchInfo: ghidra.plugins.importer.batch.BatchInfo, destFolder: ghidra.framework.model.DomainFolder, programManager: ghidra.app.services.ProgramManager, stripLeading: bool, stripAllContainerPath: bool):
        """
        Start a Batch Import session with an already populated {@link BatchInfo}
         instance.
         <p>
        @param batchInfo {@link BatchInfo} state object
        @param destFolder {@link DomainFolder} where to place imported files
        @param programManager {@link ProgramManager} to use when opening newly imported files, null ok
        @param stripLeading boolean true if each import source's leading path should be omitted
         when creating the destination project folder path.
        @param stripAllContainerPath boolean true if each imported file's parent container
         source path should be completely omitted when creating the destination project folder path.
         (the imported file's path within its container is still used)
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

    def run(self, monitor: ghidra.util.task.TaskMonitor) -> None: ...

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
