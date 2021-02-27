import ghidra.framework.store
import java.lang


class FileSystemListenerList(object, ghidra.framework.store.FileSystemListener):
    """
    FileSystemListenerList maintains a list of FileSystemListener's.
     This class, acting as a FileSystemListener, simply relays each callback to
     all FileSystemListener's within its list.  Employs either a synchronous
     and asynchronous notification mechanism.
    """





    def __init__(self, enableAsynchronousDispatching: bool):
        """
        Construct FileSystemListenerList
        @param enableAsynchronousDispatching if true a separate dispatch thread will be used
         to notify listeners.  If false, blocking notification will be performed.
        """
        ...



    def add(self, listener: ghidra.framework.store.FileSystemListener) -> None:
        """
        Add a listener to this list.
        @param listener
        """
        ...

    def clear(self) -> None:
        """
        Remove all listeners from this list.
        """
        ...

    def dispose(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def folderCreated(self, parentPath: unicode, folderName: unicode) -> None:
        """
        Forwards folderCreated callback to all listeners within this list.
        @see ghidra.framework.store.FileSystemListener#folderCreated(String, String)
        """
        ...

    def folderDeleted(self, parentPath: unicode, folderName: unicode) -> None:
        """
        Forwards folderDeleted callback to all listeners within this list.
        @see ghidra.framework.store.FileSystemListener#folderDeleted(String, String)
        """
        ...

    def folderMoved(self, parentPath: unicode, folderName: unicode, newParentPath: unicode) -> None:
        """
        Forwards folderMoved callback to all listeners within this list.
        @see ghidra.framework.store.FileSystemListener#folderMoved(String, String, String)
        """
        ...

    def folderRenamed(self, parentPath: unicode, folderName: unicode, newFolderName: unicode) -> None:
        """
        Forwards folderRenamed callback to all listeners within this list.
        @see ghidra.framework.store.FileSystemListener#folderRenamed(String, String, String)
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def isProcessingEvents(self) -> bool:
        """
        Returns true if this class is processing events <b>or</b> needs to process events that are
         in its event queue.
        @return true if this class is processing events <b>or</b> needs to process events that are
         in its event queue.
        """
        ...

    def itemChanged(self, parentPath: unicode, itemName: unicode) -> None:
        """
        Forwards itemChanged callback to all listeners within this list.
        @see ghidra.framework.store.FileSystemListener#itemChanged(String, String)
        """
        ...

    def itemCreated(self, parentPath: unicode, itemName: unicode) -> None:
        """
        Forwards itemCreated callback to all listeners within this list.
        @see ghidra.framework.store.FileSystemListener#itemCreated(String, String)
        """
        ...

    def itemDeleted(self, parentPath: unicode, itemName: unicode) -> None:
        """
        Forwards itemDeleted callback to all listeners within this list.
        @see ghidra.framework.store.FileSystemListener#itemDeleted(String, String)
        """
        ...

    def itemMoved(self, parentPath: unicode, name: unicode, newParentPath: unicode, newName: unicode) -> None:
        """
        Forwards itemMoved callback to all listeners within this list.
        @see ghidra.framework.store.FileSystemListener#itemMoved(String, String, String, String)
        """
        ...

    def itemRenamed(self, parentPath: unicode, itemName: unicode, newName: unicode) -> None:
        """
        Forwards itemRenamed callback to all listeners within this list.
        @see ghidra.framework.store.FileSystemListener#itemRenamed(String, String, String)
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def remove(self, listener: ghidra.framework.store.FileSystemListener) -> None:
        """
        Remove a listener from this list.
        @param listener
        """
        ...

    def syncronize(self) -> None:
        """
        Forwards syncronize callback to all listeners within this list.
        @see ghidra.framework.store.FileSystemListener#syncronize()
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
    def processingEvents(self) -> bool: ...
