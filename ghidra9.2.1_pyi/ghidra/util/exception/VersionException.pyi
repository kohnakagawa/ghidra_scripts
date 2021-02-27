from typing import List
import ghidra.util.exception
import java.io
import java.lang


class VersionException(ghidra.util.exception.UsrException):
    """
    Exception thrown when an object's version does not match its expected version.
    """

    NEWER_VERSION: int = 2
    OLDER_VERSION: int = 1
    UNKNOWN_VERSION: int = 0



    @overload
    def __init__(self):
        """
        Constructor - not upgradeable
        """
        ...

    @overload
    def __init__(self, upgradable: bool):
        """
        Constructor.
        @param upgradable true indicates that an upgrade is possible.
         If true the version indicator value is set to OLDER_VERSION, if false
         it is set to UNKNOWN_VERSION.
        """
        ...

    @overload
    def __init__(self, msg: unicode):
        """
        Constructor - not upgradeable
        @param msg detailed message
        """
        ...

    @overload
    def __init__(self, versionIndicator: int, upgradable: bool):
        """
        Constructor.
        @param versionIndicator OLDER_VERSION, NEWER_VERSION or UNKNOWN_VERSION
        @param upgradable true indicates that an upgrade is possible.
        """
        ...

    @overload
    def __init__(self, msg: unicode, versionIndicator: int, upgradable: bool):
        """
        Constructor.
        @param msg detailed message
        @param versionIndicator OLDER_VERSION, NEWER_VERSION or UNKNOWN_VERSION
        @param upgradable true indicates that an upgrade is possible.
        """
        ...



    def addSuppressed(self, __a0: java.lang.Throwable) -> None: ...

    def combine(self, ve: ghidra.util.exception.VersionException) -> ghidra.util.exception.VersionException:
        """
        Combine another VersionException with this one.
        @param ve another version exception
        @return this combined version exception
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def fillInStackTrace(self) -> java.lang.Throwable: ...

    def getCause(self) -> java.lang.Throwable: ...

    def getClass(self) -> java.lang.Class: ...

    def getDetailMessage(self) -> unicode: ...

    def getLocalizedMessage(self) -> unicode: ...

    def getMessage(self) -> unicode: ...

    def getStackTrace(self) -> List[java.lang.StackTraceElement]: ...

    def getSuppressed(self) -> List[java.lang.Throwable]: ...

    def getVersionIndicator(self) -> int:
        """
        Return a version indicator (OLDER_VERSION, NEWER_VERSION or UNKNOWN_VERSION).
         Only an OLDER_VERSION has the possibility of being upgradeable.
        """
        ...

    def hashCode(self) -> int: ...

    def initCause(self, __a0: java.lang.Throwable) -> java.lang.Throwable: ...

    def isUpgradable(self) -> bool:
        """
        Return true if the file can be upgraded to the current version.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @overload
    def printStackTrace(self) -> None: ...

    @overload
    def printStackTrace(self, __a0: java.io.PrintStream) -> None: ...

    @overload
    def printStackTrace(self, __a0: java.io.PrintWriter) -> None: ...

    def setDetailMessage(self, message: unicode) -> None: ...

    def setStackTrace(self, __a0: List[java.lang.StackTraceElement]) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def detailMessage(self) -> unicode: ...

    @detailMessage.setter
    def detailMessage(self, value: unicode) -> None: ...

    @property
    def upgradable(self) -> bool: ...

    @property
    def versionIndicator(self) -> int: ...
