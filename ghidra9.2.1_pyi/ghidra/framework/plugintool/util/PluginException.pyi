from typing import List
import ghidra.framework.plugintool.util
import ghidra.util.exception
import java.io
import java.lang


class PluginException(ghidra.util.exception.UsrException):
    """
    Exception thrown if plugin was not found.
    """





    @overload
    def __init__(self, message: unicode):
        """
        Construct a PluginException with the given message.
        @param message message that is returned in the getMessage() method
        """
        ...

    @overload
    def __init__(self, className: unicode, details: unicode):
        """
        Construct PluginException with a detail message.
        @param className class name of the plugin
        @param details the reason the addPlugin failed.
        """
        ...

    @overload
    def __init__(self, message: unicode, cause: java.lang.Throwable):
        """
        Construct a PluginException with the given message and cause.
        @param message the exception message
        @param cause the exception cause
        """
        ...



    def addSuppressed(self, __a0: java.lang.Throwable) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def fillInStackTrace(self) -> java.lang.Throwable: ...

    def getCause(self) -> java.lang.Throwable: ...

    def getClass(self) -> java.lang.Class: ...

    def getLocalizedMessage(self) -> unicode: ...

    def getMessage(self) -> unicode: ...

    def getPluginException(self, e: ghidra.framework.plugintool.util.PluginException) -> ghidra.framework.plugintool.util.PluginException:
        """
        Creates a new PluginException by appending the message from
         this exception to the message of the given exception if it
         is not null. If e is null, returns this exception.
        @param e exception whose message will be appended to this
         exceptions message if e is not null
        @return this exception if e is null, or a new exception
        """
        ...

    def getStackTrace(self) -> List[java.lang.StackTraceElement]: ...

    def getSuppressed(self) -> List[java.lang.Throwable]: ...

    def hashCode(self) -> int: ...

    def initCause(self, __a0: java.lang.Throwable) -> java.lang.Throwable: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @overload
    def printStackTrace(self) -> None: ...

    @overload
    def printStackTrace(self, __a0: java.io.PrintStream) -> None: ...

    @overload
    def printStackTrace(self, __a0: java.io.PrintWriter) -> None: ...

    def setStackTrace(self, __a0: List[java.lang.StackTraceElement]) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
