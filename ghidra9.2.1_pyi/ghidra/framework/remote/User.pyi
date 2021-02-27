import ghidra.framework.remote
import java.io
import java.lang


class User(object, java.lang.Comparable, java.io.Serializable):
    """
    Container class for the user name and the permission type: READ_ONLY,
     WRITE, or ADMIN.
    """

    ADMIN: int = 2
    ANONYMOUS_USERNAME: unicode = u'-anonymous-'
    READ_ONLY: int = 0
    WRITE: int = 1
    serialVersionUID: long = 0x2L



    def __init__(self, name: unicode, permission: int):
        """
        Constructor.
        @param name user id/name
        @param permission permission value (READ_ONLY, WRITE or ADMIN)
        """
        ...



    @overload
    def compareTo(self, other: ghidra.framework.remote.User) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def equals(self, obj: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getName(self) -> unicode:
        """
        Returns user id/name
        """
        ...

    def getPermissionType(self) -> int:
        """
        Returns the permission value assigned this user.
        """
        ...

    def hasWritePermission(self) -> bool:
        """
        Return true if this user has permission of WRITE or ADMIN.
        """
        ...

    def hashCode(self) -> int: ...

    def isAdmin(self) -> bool:
        """
        Returns true if permission is ADMIN.
        """
        ...

    def isReadOnly(self) -> bool:
        """
        Returns true if permission is READ_ONLY.
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

    @property
    def admin(self) -> bool: ...

    @property
    def name(self) -> unicode: ...

    @property
    def permissionType(self) -> int: ...

    @property
    def readOnly(self) -> bool: ...
