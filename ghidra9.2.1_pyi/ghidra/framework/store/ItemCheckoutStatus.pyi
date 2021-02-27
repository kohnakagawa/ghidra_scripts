import ghidra.framework.store
import java.io
import java.lang
import java.util


class ItemCheckoutStatus(object, java.io.Serializable):
    """
    ItemCheckoutStatus provides immutable status information for a
     checked-out item.  This class is serializable so that it may be passed
     to a remote client.
    """

    serialVersionUID: long = 0x1L



    def __init__(self, checkoutId: long, checkoutType: ghidra.framework.store.CheckoutType, user: unicode, version: int, time: long, projectPath: unicode):
        """
        Constructor.
        @param checkoutId unique checkout ID
        @param checkoutType type of checkout
        @param user user name
        @param version version of file which was checked-out
        @param time time when checkout was completed.
        """
        ...



    def equals(self, obj: object) -> bool: ...

    def getCheckoutDate(self) -> java.util.Date:
        """
        Returns the time at which the checkout was completed.
        @return
        """
        ...

    def getCheckoutId(self) -> long:
        """
        Returns the unique ID for the associated checkout.
        """
        ...

    def getCheckoutTime(self) -> long:
        """
        Returns the time at which the checkout was completed.
        """
        ...

    def getCheckoutType(self) -> ghidra.framework.store.CheckoutType:
        """
        Returns the checkout type
        @return checkout type
        """
        ...

    def getCheckoutVersion(self) -> int:
        """
        Returns the file version which was checked-out.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getProjectLocation(self) -> unicode:
        """
        Return a Project location which corresponds to the projectPath
         or null if one can not be constructed.
        @return project location
        """
        ...

    def getProjectName(self) -> unicode:
        """
        Return a Project location which corresponds to the projectPath
         or null if one can not be constructed.
        @return project location
        """
        ...

    @overload
    def getProjectPath(self) -> unicode:
        """
        Returns user's local project path if known.
        """
        ...

    @overload
    @staticmethod
    def getProjectPath(projectPath: unicode, isTransient: bool) -> unicode:
        """
        Get project path string suitable for checkout requests
        @param projectPath
        @param isTransient true if project is transient
        @return project location path
        """
        ...

    def getUser(self) -> unicode:
        """
        Returns the user name for the associated checkout.
        """
        ...

    def getUserHostName(self) -> unicode:
        """
        Returns the user's hostname associated with the original checkout
        @return host name or null
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
    def checkoutDate(self) -> java.util.Date: ...

    @property
    def checkoutId(self) -> long: ...

    @property
    def checkoutTime(self) -> long: ...

    @property
    def checkoutType(self) -> ghidra.framework.store.CheckoutType: ...

    @property
    def checkoutVersion(self) -> int: ...

    @property
    def projectLocation(self) -> unicode: ...

    @property
    def projectName(self) -> unicode: ...

    @property
    def projectPath(self) -> unicode: ...

    @property
    def user(self) -> unicode: ...

    @property
    def userHostName(self) -> unicode: ...
