import java.lang


class RemoteAdapterListener(object):
    """
    RemoteAdapterListener provides a listener interface
     which facilitates notifcation when the connection
     state of a remote server/repository adapter changes.
    """









    def connectionStateChanged(self, adapter: object) -> None:
        """
        Callback notification indicating the remote object
         connection state has changed.
        @param adapter remote interface adapter (e.g., RepositoryServerAdapter).
        """
        ...

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
