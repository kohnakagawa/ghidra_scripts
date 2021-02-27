import java.io
import java.lang


class Version(object, java.io.Serializable):
    """
    Version provides immutable information about a specific version of an item.
    """

    serialVersionUID: long = 0x1L



    def __init__(self, version: int, createTime: long, user: unicode, comment: unicode):
        """
        Constructor.
        @param version file version number
        @param createTime time version was created
        @param user name of user who created version
        @param comment version comment
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getComment(self) -> unicode:
        """
        Returns version comment.
        """
        ...

    def getCreateTime(self) -> long:
        """
        Returns time at which version was created.
        """
        ...

    def getUser(self) -> unicode:
        """
        Returns name of user who created version.
        """
        ...

    def getVersion(self) -> int:
        """
        Returns version number.
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
    def comment(self) -> unicode: ...

    @property
    def createTime(self) -> long: ...

    @property
    def user(self) -> unicode: ...

    @property
    def version(self) -> int: ...
