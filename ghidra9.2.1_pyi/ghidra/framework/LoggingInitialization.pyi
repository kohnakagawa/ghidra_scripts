import java.io
import java.lang


class LoggingInitialization(object):




    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    @staticmethod
    def getApplicationLogFile() -> java.io.File:
        """
        Returns the default file used for logging messages.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getScriptLogFile() -> java.io.File:
        """
        Returns the default file used for logging messages.
        """
        ...

    def hashCode(self) -> int: ...

    @staticmethod
    def initializeLoggingSystem() -> None: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
