import java.lang


class FileSystemListener(object):
    """
    FileSystemListener provides a listener the ability
     to be notified of folder and file changes within a FileSystem.
    """









    def equals(self, __a0: object) -> bool: ...

    def folderCreated(self, parentPath: unicode, name: unicode) -> None:
        """
        Notification that a new folder was created.
        @param parentPath the path of the folder that contains the new folder
        @param name the name of the new folder
        """
        ...

    def folderDeleted(self, parentPath: unicode, folderName: unicode) -> None:
        """
        Notification that a folder was deleted.
        @param parentPath the path of the folder that contained the deleted folder.
        @param folderName the name of the folder that was deleted.
        """
        ...

    def folderMoved(self, parentPath: unicode, folderName: unicode, newParentPath: unicode) -> None:
        """
        Notification that a folder was moved.
        @param parentPath the path of the folder that used to contain the moved folder.
        @param folderName the name of the folder that was moved.
        @param newParentPath the path of the folder that now contains the moved folder.
        """
        ...

    def folderRenamed(self, parentPath: unicode, oldFolderName: unicode, newFolderName: unicode) -> None:
        """
        Notification that a folder was renamed.
        @param parentPath the path of the folder containing the folder that was renamed.
        @param oldFolderName the old name of the folder.
        @param newFolderName the new name of the folder.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def itemChanged(self, parentPath: unicode, itemName: unicode) -> None:
        """
        Notfication that an item's state has changed.
        @param parentPath the path of the folder containing the item.
        @param itemName the name of the item that has changed.
        """
        ...

    def itemCreated(self, parentPath: unicode, name: unicode) -> None:
        """
        Notification that a new folder item was created.
        @param parentPath the path of the folder that contains the new item.
        @param name the name of the new item.
        """
        ...

    def itemDeleted(self, folderPath: unicode, itemName: unicode) -> None:
        """
        Notification that a folder item was deleted.
        @param folderPath the path of the folder that contained the deleted item.
        @param itemName the name of the item that was deleted.
        """
        ...

    def itemMoved(self, parentPath: unicode, name: unicode, newParentPath: unicode, newName: unicode) -> None:
        """
        Notification that an item was moved.
        @param parentPath the path of the folder that used to contain the item.
        @param name the name of the item that was moved.
        @param newParentPath the path of the folder that the item was moved to.
        @param newName the new name of the item.
        """
        ...

    def itemRenamed(self, folderPath: unicode, oldItemName: unicode, newItemName: unicode) -> None:
        """
        Notification that an item was renamed.
        @param folderPath the path of the folder that contains the renamed item
        @param oldItemName the old name of the item.
        @param newItemName the new name of the item.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def syncronize(self) -> None:
        """
        Perform a full refresh / synchronization
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
