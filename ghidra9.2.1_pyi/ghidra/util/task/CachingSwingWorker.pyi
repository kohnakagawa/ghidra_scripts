import ghidra.util.task
import java.lang


class CachingSwingWorker(object, ghidra.util.task.CachingLoader):
    """
    Class for managing the creation of some slow loading object that may be used by multiple threads,
     including the Swing thread.  Further, repeated calls to this object will used the
     cached value.

     The basic uses cases are:


     		Call #get(TaskMonitor) from the Swing thread - this will block the Swing thread,
          showing a modal dialog, as needed.


      	Call #get(TaskMonitor) from a non-Swing thread - this will block the calling
          thread, with no effect on the UI.

      Call #startLoading() - this will trigger this worker to load in the background
          without blocking the calling thread.


      	Call #getCachedValue() - this is a way to see if the value has been loaded
          without blocking the current thread.


      	Override #done() - this method will be called when the initial loading
          is finished.


    """





    def __init__(self, name: unicode, hasProgress: bool):
        """
        Create a new CachingSwingWorker
        @param name the name of worker. (Displayed in the progress dialog)
        @param hasProgress true if the dialog should show progress or be indeterminate.
        """
        ...



    def clear(self) -> None:
        """
        Clears the cached value for the object causing it to be recreated on the next call to get()
        """
        ...

    def done(self) -> None:
        """
        A method for clients to use as a callback for completion.  This method will be called in
         the Swing thread, after the value has been set.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def get(self, monitor: ghidra.util.task.TaskMonitor) -> object:
        """
        Returns the object that this class is managing/caching.  It will return the object if it is
         already created or it will block until the object can be created.  If called from the Swing
         thread, it will also launch a modal progress dialog while waiting for the object to be
         created.
        @param monitor the monitor (may be null)
        @return the object that this class is managing/caching
        @see #getCachedValue()
        """
        ...

    def getCachedValue(self) -> object:
        """
        Returns the value only if it is cached, otherwise return null.
        @return the value only if it is cached, otherwise return null.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setTaskDialogDelay(self, delay: int) -> None:
        """
        Sets the initial delay before showing a progress dialog.  The default is 100ms.
        @param delay the delay to wait before displaying a progress dialog.
        """
        ...

    def startLoading(self) -> None:
        """
        Allows clients to start this worker loading without blocking.
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
    def cachedValue(self) -> object: ...

    @property
    def taskDialogDelay(self) -> None: ...  # No getter available.

    @taskDialogDelay.setter
    def taskDialogDelay(self, value: int) -> None: ...
