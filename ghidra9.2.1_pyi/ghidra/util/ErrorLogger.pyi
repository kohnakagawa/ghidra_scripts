import java.lang


class ErrorLogger(object):








    @overload
    def debug(self, originator: object, message: object) -> None: ...

    @overload
    def debug(self, originator: object, message: object, throwable: java.lang.Throwable) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    @overload
    def error(self, originator: object, message: object) -> None: ...

    @overload
    def error(self, originator: object, message: object, throwable: java.lang.Throwable) -> None: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    @overload
    def info(self, originator: object, message: object) -> None: ...

    @overload
    def info(self, originator: object, message: object, throwable: java.lang.Throwable) -> None: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def trace(self, originator: object, message: object) -> None: ...

    @overload
    def trace(self, originator: object, message: object, throwable: java.lang.Throwable) -> None: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @overload
    def warn(self, originator: object, message: object) -> None: ...

    @overload
    def warn(self, originator: object, message: object, throwable: java.lang.Throwable) -> None: ...
