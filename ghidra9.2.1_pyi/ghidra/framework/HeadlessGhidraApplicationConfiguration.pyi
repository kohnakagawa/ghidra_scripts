import ghidra.framework
import ghidra.util
import ghidra.util.task
import java.io
import java.lang


class HeadlessGhidraApplicationConfiguration(ghidra.framework.ApplicationConfiguration):




    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getApplicationLogFile(self) -> java.io.File:
        """
        Returns the <b>user-defined</b> log file.
        @return The <b>user-defined</b> log file. This is null by default and will only return a
         non-null value if it has been set by the user.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getErrorDisplay(self) -> ghidra.util.ErrorDisplay: ...

    def getScriptLogFile(self) -> java.io.File:
        """
        Returns the <b>user-defined</b> script log file.
        @return Returns the <b>user-defined</b> script log file.  This is null by default and will
         only return a non-null value if it has been set by the user.
        """
        ...

    def getTaskMonitor(self) -> ghidra.util.task.TaskMonitor:
        """
        Returns the currently set task monitor.
        @return The currently set task monitor, which is by default a dummy monitor.
        """
        ...

    def hashCode(self) -> int: ...

    def installStaticFactories(self) -> None: ...

    def isHeadless(self) -> bool:
        """
        Returns whether or not the application is headless.
        @return true if the application is headless; otherwise, false.
        """
        ...

    def isInitializeLogging(self) -> bool:
        """
        Returns whether or not logging is to be initialized.
        @return True if logging is to be initialized; otherwise, false.  This is true by default,
         but may be set to false by the user.
        @see #setInitializeLogging
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setApplicationLogFile(self, logFile: java.io.File) -> None: ...

    def setInitializeLogging(self, initializeLogging: bool) -> None: ...

    def setScriptLogFile(self, scriptLogFile: java.io.File) -> None: ...

    def setTaskMonitor(self, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Sets a task monitor that will be called back with messages that report the status of the
         initialization process.
        @param monitor The monitor to set.
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
