import java.lang


class GoToServiceListener(object):
    """
    Listener that is notified when the GOTO completes.
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def gotoCompleted(self, queryString: unicode, foundResults: bool) -> None:
        """
        Notification that the GOTO completed.
        @param queryString original query string
        @param foundResults true if at least one hit was found for the query
        """
        ...

    def gotoFailed(self, exc: java.lang.Exception) -> None:
        """
        Notification that the GOTO failed with an exception.
        @param exc the exception that occurred.
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
