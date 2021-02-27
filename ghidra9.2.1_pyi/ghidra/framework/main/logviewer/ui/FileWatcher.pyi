import java.lang


class FileWatcher(object):
    """
    The FileWatcher *watches* a single file and fires a change notification whenever the file
     is modified. A couple notes:

     1. To keep from processing change events every time the file is modified, which may be
        too frequent and cause processing issues, we use a simple polling mechanism.

     2. Changes in the file are identified by inspecting the File#lastModified()
        timestamp.

     3. The WatchService mechanism is not being used here since we cannot specify a
        polling rate.
    """





    def __init__(self, file: java.io.File, eventListener: ghidra.framework.main.logviewer.event.FVEventListener):
        """
        Constructor. Creates a new {@link Executor} that will inspect the file at regular
         intervals.  Users must call {@link #start()} to begin polling.
        @param file the file to be watched
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def start(self) -> None:
        """
        Starts polling, or resumes polling if previously stopped.
        """
        ...

    def stop(self) -> None:
        """
        Suspends the timer so it will no longer poll. This does not perform a shutdown, so the
         future may be scheduled again.
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
