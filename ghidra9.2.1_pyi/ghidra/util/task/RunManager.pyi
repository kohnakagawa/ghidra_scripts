import ghidra.util.task
import java.lang
import javax.swing


class RunManager(object):
    """
    Helper class to execute a Runnable in a separate thread and provides a
     progress monitor component that is shown as needed. This class can support several
     different scheduling models described below.

     1) Only allow one runnable at any given time.  In this model, a new runnable will cause any running
     runnable to be cancelled and the new runnable will begin running. Because of this, there will
     never be any runnables waiting in the queue. Use the #runNow(MonitoredRunnable, String)
     method to get this behavior.

     2) Allow one running runnable and one pending runnable.  In this mode, any running runnable will be
     allowed to complete, but any currently pending runnable will be replaced by the new runnable. Use
     the #runNext(MonitoredRunnable, String) method to get this behavior.

     3) Run all scheduled runnables in the order they are scheduled.  Use the
     #runLater(MonitoredRunnable, String, int) for this behavior.

     If the given runnable has Swing work to perform after the main Runnable.run() method completes
     (e.g., updating Swing components),
     the runnable should implement the SwingRunnable interface and perform this work in
     SwingRunnable#swingRun(boolean).

     The progress monitor component, retrieved via #getMonitorComponent(), can be placed
     into a Swing widget.  This RunManager will show and hide this progress component as necessary
     when runnables are being run.
    """





    @overload
    def __init__(self): ...

    @overload
    def __init__(self, listener: ghidra.util.task.TaskListener): ...

    @overload
    def __init__(self, name: unicode, defaultComponent: java.awt.Component): ...

    @overload
    def __init__(self, name: unicode, defaultComponent: java.awt.Component, listener: ghidra.util.task.TaskListener): ...



    def cancelAllRunnables(self) -> None:
        """
        A convenience method to cancel the any currently running job and any scheduled jobs.  Note:
         this method does not block or wait for the currently running job to finish.
        """
        ...

    def dispose(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getMonitorComponent(self) -> javax.swing.JComponent: ...

    def hashCode(self) -> int: ...

    def isInProgress(self) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def runLater(self, runnable: ghidra.util.task.MonitoredRunnable, taskName: unicode, showProgressDelay: int) -> None:
        """
        Schedules this runnable to be run after all runnables currently queued.
         <P>
         This method differs from the {@link #runNow(MonitoredRunnable, String, int)} methods in that it will
         not cancel any currently running jobs.  This allows you to add new jobs to this run
         manager, which lets them queue up. See header docs for details.
        @param runnable The runnable to run
        @param taskName The name of the task to run
        @param showProgressDelay The amount of time to wait before showing a progress monitor.
        """
        ...

    @overload
    def runNext(self, runnable: ghidra.util.task.MonitoredRunnable, taskName: unicode) -> None:
        """
        Allows any currently running runnable to finish, clears any queued runnables,
         and then queues the given runnable to be run after the current runnable finishes.
         <p>
         This call will use the default {@link #SHOW_PROGRESS_DELAY delay} of
         {@value #SHOW_PROGRESS_DELAY}.
         <p>
         See the class header for more info.
        @param runnable Runnable to execute
        @param taskName name of runnable; may be null (this will appear in the progress panel)
        """
        ...

    @overload
    def runNext(self, runnable: ghidra.util.task.MonitoredRunnable, taskName: unicode, showProgressDelay: int) -> None:
        """
        Allows any currently running runnable to finish, clears any queued runnables,
         and then queues the given runnable to be run after the current runnable finishes.
         <p>
         See the class header for more info.
        @param runnable Runnable to execute
        @param taskName name of runnable; may be null (this will appear in the progress panel)
        @param showProgressDelay the amount of time (in milliseconds) before showing the progress
                panel
        """
        ...

    @overload
    def runNow(self, runnable: ghidra.util.task.MonitoredRunnable, taskName: unicode) -> None:
        """
        Cancels any currently running runnable, clears any queued runnables, and then runs the given
         runnable.
         <p>
         See the class header for more info.
        @param runnable Runnable to execute
        @param taskName name of runnable; may be null (this will appear in the progress panel)
        """
        ...

    @overload
    def runNow(self, runnable: ghidra.util.task.MonitoredRunnable, taskName: unicode, showProgressDelay: int) -> None:
        """
        Cancels any currently running runnable, clears any queued runnables, and then runs the given
         runnable.
         <p>
         See the class header for more info.
        @param runnable Runnable to execute
        @param taskName name of runnable; may be null (this will appear in the progress panel)
        @param showProgressDelay the amount of time (in milliseconds) before showing the progress
                panel
        """
        ...

    def showCancelButton(self, showCancel: bool) -> None:
        """
        Show the cancel button according to the showCancel parameter.
        @param showCancel true means to show the cancel button
        """
        ...

    def showProgressBar(self, showProgress: bool) -> None:
        """
        Show the progress bar according to the showProgress parameter.
        @param showProgress true means to show the progress bar
        """
        ...

    def showProgressIcon(self, showIcon: bool) -> None:
        """
        Show the progress icon according to the showIcon parameter.
        @param showIcon true means to show the progress icon
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    def waitForNotBusy(self, maxWaitMillis: int) -> None: ...

    @property
    def inProgress(self) -> bool: ...

    @property
    def monitorComponent(self) -> javax.swing.JComponent: ...
