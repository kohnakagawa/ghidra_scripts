import ghidra.util.task
import java.awt
import java.lang


class TaskBuilder(object):
    """
    A builder object that allows clients to launch tasks in the background, with a progress
     dialog representing the task.

     Using this class obviates the need for clients to create full class objects to implement
     the Task interface, which means less boiler-plate code.

     An example of usage:


     Or,



      Or,


    	    TaskBuilder.withTask(new AwesomeTask(awesomeStuff)).launchModal();


     Or,


    	    TaskLauncher#launch(Task)(new AwesomeTask(awesomeStuff));



     Note: this class will check to see if it is in a headless environment before launching
     its task.  This makes it safe to use this class in headed or headless environments.
    """





    def __init__(self, title: unicode, runnable: ghidra.util.task.MonitoredRunnable):
        """
        Constructor
        @param title the required title for your task.  This will appear as the title of the
                task dialog
        @param runnable the runnable that will be called when the task is run
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def launchInBackground(self, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Runs the task in a background thread with the given monitor that cannot be null.  This
         is a special case for clients that already have a task monitor widget in their UI and
         they wish to let it show the progress of the given task while not blocking the Swing
         thread.
        @param monitor the task monitor; may not be null
        """
        ...

    def launchModal(self) -> None:
        """
        Launches the task built by this builder, using a blocking modal dialog.  The task will
         be run in the current thread if in a headless environment.
        """
        ...

    def launchNonModal(self) -> None:
        """
        Launches the task built by this builder, using a non-blocking dialog.  The task will
         be run in the current thread if in a headless environment.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setCanCancel(self, canCancel: bool) -> ghidra.util.task.TaskBuilder:
        """
        Sets whether the task can be cancelled.  The default is <code>true</code>.
        @param canCancel true if the task can be cancelled.
        @return this builder
        """
        ...

    def setDialogWidth(self, width: int) -> ghidra.util.task.TaskBuilder:
        """
        The desired width of the dialog.  The default is {@link TaskDialog#DEFAULT_WIDTH}.
        @param width the width
        @return this builder
        """
        ...

    def setHasProgress(self, hasProgress: bool) -> ghidra.util.task.TaskBuilder:
        """
        Sets whether this task reports progress.   The default is <code>true</code>.
        @param hasProgress true if the task reports progress
        @return this builder
        """
        ...

    def setLaunchDelay(self, delay: int) -> ghidra.util.task.TaskBuilder:
        """
        Sets the amount of time that will pass before showing the dialog.  The default is
         {@link TaskLauncher#INITIAL_DELAY_MS} for non-modal tasks and
         {@link TaskLauncher#INITIAL_MODAL_DELAY_MS} for modal tasks.
        @param delay the delay time
        @return this builder
        """
        ...

    def setParent(self, parent: java.awt.Component) -> ghidra.util.task.TaskBuilder:
        """
        Sets the component over which the task dialog will be shown.  The default is <code>null</code>,
         which shows the dialog over the active window.
        @param parent the parent
        @return this builder
        """
        ...

    def setStatusTextAlignment(self, alignment: int) -> ghidra.util.task.TaskBuilder:
        """
        Sets the horizontal text alignment of messages shown in the task dialog.  The
         default is {@link SwingConstants#CENTER}.  Valid values are {@link SwingConstants}
         LEADING, CENTER and TRAILING.
        @param alignment the alignment
        @return this builder
        """
        ...

    def setTitle(self, title: unicode) -> ghidra.util.task.TaskBuilder:
        """
        Sets the title of this task.  The title must be set before calling any of the
         <code>launch</code> methods.
        @param title the title
        @return this builder
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @staticmethod
    def withRunnable(r: ghidra.util.task.MonitoredRunnable) -> ghidra.util.task.TaskBuilder:
        """
        A convenience method to start a builder using the given runnable.  After calling this
         method you are still required to call {@link #setTitle(String)}.

         <p>This method allows for a more attractive fluent API usage than does the constructor
         (see the javadoc header).
        @param r the runnable
        @return this builder
        """
        ...

    @staticmethod
    def withTask(t: ghidra.util.task.Task) -> ghidra.util.task.TaskBuilder:
        """
        A convenience method to start a builder using the given task.  The
         {@link #setTitle(String) title} of the task will be the value of
         {@link Task#getTaskTitle()}.

         <p>This method allows for a more attractive fluent API usage than does the constructor
         (see the javadoc header).
        @param t the task
        @return this builder
        """
        ...

    @property
    def canCancel(self) -> None: ...  # No getter available.

    @canCancel.setter
    def canCancel(self, value: bool) -> None: ...

    @property
    def dialogWidth(self) -> None: ...  # No getter available.

    @dialogWidth.setter
    def dialogWidth(self, value: int) -> None: ...

    @property
    def hasProgress(self) -> None: ...  # No getter available.

    @hasProgress.setter
    def hasProgress(self, value: bool) -> None: ...

    @property
    def launchDelay(self) -> None: ...  # No getter available.

    @launchDelay.setter
    def launchDelay(self, value: int) -> None: ...

    @property
    def parent(self) -> None: ...  # No getter available.

    @parent.setter
    def parent(self, value: java.awt.Component) -> None: ...

    @property
    def statusTextAlignment(self) -> None: ...  # No getter available.

    @statusTextAlignment.setter
    def statusTextAlignment(self, value: int) -> None: ...

    @property
    def title(self) -> None: ...  # No getter available.

    @title.setter
    def title(self, value: unicode) -> None: ...
