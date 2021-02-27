import java.lang


class Lock(object):
    """
    Ghidra synchronization lock. This class allows creation of named locks for
     synchroniing modification of multiple tables in the Ghidra database.
    """





    def __init__(self, name: unicode):
        """
        Creates an instance of a lock for synchronization within Ghidra.
        @param name the name of this lock
        """
        ...



    def acquire(self) -> None:
        """
        Acquire this synchronization lock. (i.e. begin synchronizing on this named
         lock.)
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getOwner(self) -> java.lang.Thread:
        """
        Gets the thread that currently owns the lock.
        @return the thread that owns the lock or null.
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def release(self) -> None:
        """
        Releases this lock, since you are through with the code that needed
         synchronization.
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
    def owner(self) -> java.lang.Thread: ...
