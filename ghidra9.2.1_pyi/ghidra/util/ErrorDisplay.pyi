import ghidra.util
import java.awt
import java.lang


class ErrorDisplay(object):








    def displayErrorMessage(self, errorLogger: ghidra.util.ErrorLogger, originator: object, parent: java.awt.Component, title: unicode, message: object, throwable: java.lang.Throwable) -> None: ...

    def displayInfoMessage(self, errorLogger: ghidra.util.ErrorLogger, originator: object, parent: java.awt.Component, title: unicode, message: object) -> None: ...

    def displayWarningMessage(self, errorLogger: ghidra.util.ErrorLogger, originator: object, parent: java.awt.Component, title: unicode, message: object, throwable: java.lang.Throwable) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

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
