import ghidra.util.task
import java.lang


class TaskLauncher(object):
    """
    Class to initiate a Task in a new Thread, and to show a progress dialog that indicates
     activity if the task takes too long.  The progress dialog will show an
     animation in the event that the task of this class cannot show progress.

     For complete control of how this class functions, use
     #TaskLauncher(Task, Component, int, int).  Alternatively, for simpler uses,
     see one of the many static convenience methods.

     Modal Usage
     Most clients of this class should not be concerned with where
     the dialog used by this class will appear.  By default, it will be shown over
     the active window, which is the desired
     behavior for most uses.  If you should need a dialog to appear over a non-active window,
     then either specify that window, or a child component of that window, by calling a
     constructor that takes in a Component.  Further, if you task is modal, then the
     progress dialog should always be shown over the active window so that users understand that
     their UI is blocked.  In this case, there is no need to specify a component over which to
     show the dialog.

     An alternative to using this class is to use the TaskBuilder, which offers a
     more Fluent API approach for your tasking needs.
    """





    @overload
    def __init__(self, task: ghidra.util.task.Task):
        """
        Constructor for TaskLauncher

         <p>This constructor assumes that if a progress dialog is needed, then it should appear
         over the active window.  If you should need a dialog to appear over a non-active window,
         then either specify that window or a component within that window by calling a
         constructor that takes in a {@link Component}.
        @param task task to run in another thread (other than the Swing Thread)
        """
        ...

    @overload
    def __init__(self, task: ghidra.util.task.Task, parent: java.awt.Component):
        """
        Constructor for TaskLauncher

         <p>See <a href="#modal_usage">notes on modal usage</a>
        @param task task to run in another thread (other than the Swing Thread)
        @param parent component whose window to use to parent the dialog.
        """
        ...

    @overload
    def __init__(self, task: ghidra.util.task.Task, parent: java.awt.Component, delayMs: int):
        """
        Construct a new TaskLauncher

         <p>See <a href="#modal_usage">notes on modal usage</a>
        @param task task to run in another thread (other than the Swing Thread)
        @param parent component whose window to use to parent the dialog; null centers the task
                dialog over the current window
        @param delayMs number of milliseconds to delay until the task monitor is displayed
        """
        ...

    @overload
    def __init__(self, task: ghidra.util.task.Task, parent: java.awt.Component, delayMs: int, dialogWidth: int):
        """
        Construct a new TaskLauncher

         <p>See <a href="#modal_usage">notes on modal usage</a>
        @param task task to run in another thread (other than the Swing Thread)
        @param parent component whose window to use to parent the dialog; null centers the task
                dialog over the current window
        @param delayMs number of milliseconds to delay until the task monitor is displayed
        @param dialogWidth The preferred width of the dialog (this allows clients to make a wider
                dialog, which better shows long messages).
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    @staticmethod
    def launch(__a0: ghidra.util.task.Task) -> ghidra.util.task.Task: ...

    @overload
    @staticmethod
    def launchModal(title: unicode, runnable: ghidra.util.task.MonitoredRunnable) -> None:
        """
        A convenience method to directly run a {@link MonitoredRunnable} in a separate
         thread as a {@link Task}, displaying a <b>modal</b> progress dialog.
         <p>
         <code>
         TaskLauncher.launchModal( "My task", <br>
          &nbsp;&nbsp;null, // parent<br>
         	&nbsp;&nbsp;monitor -&gt; { while ( !monitor.isCanceled() ) { longRunningWork(); } }<br>
         );
         </code>

         <p>Note: the task created by this call will be both cancellable and have progress.  If
         you task cannot be cancelled or does not have progress, then do not use this
         convenience method, but rather call one of the constructors of this class or
         {@link #launchModal(String, MonitoredRunnable)}.
        @param title name of the task thread that will be executing this task.
        @param runnable {@link MonitoredRunnable} that takes a {@link TaskMonitor}.
        """
        ...

    @overload
    @staticmethod
    def launchModal(title: unicode, runnable: java.lang.Runnable) -> None:
        """
        A convenience method to directly run a {@link Runnable} in a separate
         thread as a {@link Task}, displaying a non-modal progress dialog.

         <p>This modal will be launched immediately, without delay.  Typically this launcher will
         delay showing the modal dialog in order to prevent the dialog from being show, just
         to have it immediately go away.  If you desire this default behavior, then do not use
         this convenience method.

         <p><code>
         TaskLauncher.launchModal( "My task", <br>
         	&nbsp;&nbsp;monitor -&gt; { { foo(); }<br>
         );
         </code>

         <p>Note: the task created by this call will not be cancellable nor have progress.  If
         you need either of these behaviors, the do not use this
         convenience method, but rather call one of the constructors of this class.
        @param title name of the task thread that will be executing this task.
        @param runnable {@link Runnable} to be called in a background thread
        """
        ...

    @staticmethod
    def launchNonModal(title: unicode, runnable: ghidra.util.task.MonitoredRunnable) -> None:
        """
        A convenience method to directly run a {@link MonitoredRunnable} in a separate
         thread as a {@link Task}, displaying a non-modal progress dialog.
         <p>
         <code>
         TaskLauncher.launchNonModal( "My task", <br>
          &nbsp;&nbsp;null, // parent<br>
         	&nbsp;&nbsp;monitor -&gt; { while ( !monitor.isCanceled() ) { longRunningWork(); } }<br>
         );
         </code>

         <p>Note: the task created by this call will be both cancellable and have progress.  If
         you task cannot be cancelled or does not have progress, then do not use this
         convenience method, but rather call one of the constructors of this class.

         <p>See <a href="#modal_usage">notes on non-modal usage</a>
        @param title name of the task thread that will be executing this task.
        @param runnable {@link MonitoredRunnable} that takes a {@link TaskMonitor}.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
