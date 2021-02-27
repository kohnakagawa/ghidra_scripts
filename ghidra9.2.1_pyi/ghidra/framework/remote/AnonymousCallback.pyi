import java.io
import java.lang
import javax.security.auth.callback


class AnonymousCallback(object, javax.security.auth.callback.Callback, java.io.Serializable):
    serialVersionUID: long = 0x1L



    def __init__(self): ...



    def anonymousAccessRequested(self) -> bool:
        """
        @return true if anonymous access requested
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setAnonymousAccessRequested(self, state: bool) -> None:
        """
        If state set to true anonymous read-only access will be requested
        @param state true to request anonymous access
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
