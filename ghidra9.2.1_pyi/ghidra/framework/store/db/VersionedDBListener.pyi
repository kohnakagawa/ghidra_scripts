import ghidra.framework.store.db
import java.lang


class VersionedDBListener(object):
    """
    VersionedDBListener provides listeners the ability to be notified
     when changes occur to a versioned database.
    """









    def checkinCompleted(self, checkoutId: long) -> None:
        """
        Terminate the specified checkout.
         A new version may or may not have been created.
        @param checkoutId
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getCheckoutVersion(self, checkoutId: long) -> int:
        """
        Returns the checkout version associated with the specified
         checkoutId.  A returned version of -1 indicates that the
         checkoutId is not valid.
        @param checkoutId
        @return checkout version
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    def versionCreated(self, db: ghidra.framework.store.db.VersionedDatabase, version: int, time: long, comment: unicode, checkinId: long) -> bool:
        """
        A new database version has been created.
        @param db
        @param version
        @param time
        @param comment
        @param checkinId
        @return true if version is allowed, if false is returned
         the version will be removed.
        """
        ...

    def versionDeleted(self, version: int) -> None:
        """
        A version has been deleted.
        @param version
        """
        ...

    def versionsChanged(self, minVersion: int, currentVersion: int) -> None:
        """
        Available database versions have been modified.
         This method is not invoked when a new version is created.
        @param minVersion minimum available version
        @param currentVersion current/latest version
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
