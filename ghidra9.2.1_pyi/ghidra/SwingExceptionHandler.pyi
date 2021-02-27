import java.lang


class SwingExceptionHandler(object, java.lang.Thread.UncaughtExceptionHandler):
    """
    Class to handle exceptions caught within the Swing event dispatch thread.
    """





    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def handle(self, t: java.lang.Throwable) -> None:
        """
        Handle exception caught within the Swing event dispatch thread.
        @param t exception
        @throws Throwable error occurred while attempting to handle exception
        """
        ...

    @staticmethod
    def handleUncaughtException(t: java.lang.Throwable) -> None: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def registerHandler() -> None:
        """
        Register SwingExceptionHandler
        """
        ...

    def toString(self) -> unicode: ...

    def uncaughtException(self, t: java.lang.Thread, e: java.lang.Throwable) -> None: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
