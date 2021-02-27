import java.io
import java.lang


class PyDevUtils(object):
    PYDEV_REMOTE_DEBUGGER_PORT: int = 5678







    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getPyDevSrcDir() -> java.io.File:
        """
        Gets The PyDev source directory.
        @return The PyDev source directory, or null if it not known.
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
