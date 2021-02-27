import java.io
import java.lang


class RepositoryItem(object, java.io.Serializable):
    """
    RepositoryItemStatus provides status information for a
     repository folder item.
    """

    DATABASE: int = 2
    FILE: int = 1
    serialVersionUID: long = 0x2L



    def __init__(self, folderPath: unicode, itemName: unicode, fileID: unicode, itemType: int, contentType: unicode, version: int, versionTime: long):
        """
        Constructor.
        @param folderPath path of folder containing item.
        @param itemName name of item
        @param itemType type of item (FILE or DATABASE)
        @param contentType content type associated with item
        @param version repository item version or -1 if versioning not supported
        @param versionTime version creation time
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getContentType(self) -> unicode:
        """
        Returns content class
        """
        ...

    def getFileID(self) -> unicode: ...

    def getItemType(self) -> int:
        """
        Returns type of item.
        """
        ...

    def getName(self) -> unicode:
        """
        Returns the item name.
        """
        ...

    def getParentPath(self) -> unicode:
        """
        Returns path of the parent folder containing this item.
        """
        ...

    def getPathName(self) -> unicode:
        """
        Returns the folder item path within the repository.
        """
        ...

    def getVersion(self) -> int:
        """
        Returns the current version of the item or
         -1 if versioning not supported.
        """
        ...

    def getVersionTime(self) -> long:
        """
        Returns the time (UTC milliseconds) when the current version was created.
        """
        ...

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

    @property
    def contentType(self) -> unicode: ...

    @property
    def fileID(self) -> unicode: ...

    @property
    def itemType(self) -> int: ...

    @property
    def name(self) -> unicode: ...

    @property
    def parentPath(self) -> unicode: ...

    @property
    def pathName(self) -> unicode: ...

    @property
    def version(self) -> int: ...

    @property
    def versionTime(self) -> long: ...
