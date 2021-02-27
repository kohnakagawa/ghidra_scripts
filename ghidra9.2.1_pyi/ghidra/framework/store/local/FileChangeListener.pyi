import java.io
import java.lang


class FileChangeListener(object):
    """
    Defines a file change listener interface.
    """









    def equals(self, __a0: object) -> bool: ...

    def fileModified(self, file: java.io.File) -> None:
        """
        Used to notify a listener that the specified file has been modified.
         If the file watcher was created with a lock file, the lock will be set
         on behalf of the caller.  This method should not attempt to alter the
         lock.
        @param file the modified file.
        """
        ...

    def fileRemoved(self, file: java.io.File) -> None:
        """
        Used to notify a listener that the specified file has been removed.
         If the file watcher was created with a lock file, the lock will be set
         on behalf of the caller.  This method should not attempt to alter the
         lock.
        @param file the removed file.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
