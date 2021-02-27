import java.io
import java.lang


class RepositoryChangeEvent(object, java.io.Serializable):
    """
    Repository change event (used by server only).
    """

    REP_FOLDER_CREATED: int = 0
    REP_FOLDER_DELETED: int = 2
    REP_FOLDER_MOVED: int = 3
    REP_FOLDER_RENAMED: int = 4
    REP_ITEM_CHANGED: int = 8
    REP_ITEM_CREATED: int = 1
    REP_ITEM_DELETED: int = 5
    REP_ITEM_MOVED: int = 7
    REP_ITEM_RENAMED: int = 6
    REP_NULL_EVENT: int = -1
    REP_OPEN_HANDLE_COUNT: int = 9
    name: unicode
    newName: unicode
    newParentPath: unicode
    parentPath: unicode
    serialVersionUID: long = 0x1L
    type: int



    def __init__(self, type: int, parentPath: unicode, name: unicode, newParentPath: unicode, newName: unicode):
        """
        Constructor.
         Parameters not applicable to the specified type may be null.
        @param type event type
        @param parentPath parent folder path for repository item or folder
        @param name repository item or folder name
        @param newParentPath new parent folder path for repository item or folder
        @param newName new repository item or folder name
        """
        ...



    def equals(self, __a0: object) -> bool: ...

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
