import java.io
import java.lang


class LockFile(object):
    """
    Provides for the creation and management of a named lock file. Keep in mind
     that if a lock expires it may be removed without notice.  Care should be
     taken to renew a lock file in a timely manner.
    """

    nextInstanceId: int



    @overload
    def __init__(self, file: java.io.File):
        """
        Constructor.
        @param file file whose lock state will be controlled with this lock file.
        """
        ...

    @overload
    def __init__(self, dir: java.io.File, name: unicode):
        """
        Constructor.
        @param dir directory containing lock file
        @param name unmangled name of entity which this lock is associated with.
        """
        ...

    @overload
    def __init__(self, dir: java.io.File, name: unicode, lockType: unicode):
        """
        Constructor.
        @param dir directory containing lock file
        @param name unmangled name of entity which this lock is associated with.
        @param lockType unique lock identifier (may not contain a '.')
        """
        ...



    @staticmethod
    def containsLock(dir: java.io.File) -> bool: ...

    @overload
    def createLock(self) -> bool:
        """
        Create the lock file using the default timeout.
         Lock is guaranteed for MAX_LOCK_LEASE_PERIOD seconds.
        @return true if lock creation was successful.
        """
        ...

    @overload
    def createLock(self, timeout: int, hold: bool) -> bool:
        """
        Create the lock file.
         If another lock file already exists, wait for it to expire
         within the specified timeout period.  Method will block
         until either the lock is obtained or the timeout period lapses.
        @param timeout maximum time in milliseconds to wait for lock.
        @param hold if true the lock will be held and maintained until
         removed, otherwise it is only guaranteed for MAX_LOCK_LEASE_PERIOD seconds.
        @return true if lock creation was successful.
        """
        ...

    def dispose(self) -> None:
        """
        Cleanup lock resources and tasks.
         Invoking this method could prevent stale locks from being removed
         if createLock was invoked with a very short timeout.
         Use of dispose is optional - the associated wait task should
         stop by it self allowing the LockFile object to be finalized.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getLockOwner(self) -> unicode:
        """
        Return the name of the current lock owner
         or {@code "<Unknown>"} if not locked or could not be determined.
        """
        ...

    def hashCode(self) -> int: ...

    @overload
    def haveLock(self) -> bool:
        """
        Determine if lock file was successfully created by this instance.
         This does not quarentee that the lock is still present if more
         than MAX_LOCK_LEASE_PERIOD has lapsed since lock was created.
        @return true if lock has been created, otherwise false.
        """
        ...

    @overload
    def haveLock(self, verify: bool) -> bool:
        """
        Determine if lock is still in place.
         Verifying the lock may be necessary when slow processes are holding
         the lock without timely renewals.
        @return true if lock is still in place, otherwise false.
        """
        ...

    @overload
    @staticmethod
    def isLocked(file: java.io.File) -> bool:
        """
        @param file file whose lock state is controlled with this lock file.
        @return true if any lock exists within dir for the given entity name.
        """
        ...

    @overload
    @staticmethod
    def isLocked(dir: java.io.File, name: unicode) -> bool:
        """
        @param dir directory containing lock file
        @param name of entity which this lock is associated with.
        @return true if any lock exists within dir for the given entity name.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def removeLock(self) -> None:
        """
        Remove the lock file.
         This method should be invoked when the corresponding transaction is complete.
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
    def lockOwner(self) -> unicode: ...
