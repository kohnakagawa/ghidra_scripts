import java.lang


class ConsoleListener(object):
    """
    Listener that is called when a string should be written to the console.
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def put(self, message: unicode, isError: bool) -> None:
        """
        Output the message to the console.
        @param message to output
        @param isError true if this is an error message
        """
        ...

    def putln(self, message: unicode, isError: bool) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
