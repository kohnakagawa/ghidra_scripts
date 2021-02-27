import java.io
import java.lang


class Watchdog(object, java.io.Closeable):
    """
    A reusable watchdog that will execute a callback if the watchdog is not disarmed before
     it expires.
    """





    def __init__(self, defaultTimeoutMS: long, timeoutMethod: java.lang.Runnable):
        """
        Creates a watchdog (initially disarmed) that will poll for expiration every
         defaultTimeoutMS milliseconds, calling {@code timeoutMethod} when triggered.
         <p>
        @param defaultTimeoutMS number of milliseconds that the watchdog will wait after
         being armed before calling the timeout method.
        @param timeoutMethod {@link Runnable} functional callback.
        """
        ...



    def arm(self) -> None:
        """
        Enables this watchdog so that at {@link #defaultWatchdogTimeoutMS} milliseconds in the
         future the {@link #timeoutMethod} will be called.
        """
        ...

    def close(self) -> None:
        """
        Releases the background timer that this watchdog uses.
        """
        ...

    def disarm(self) -> None:
        """
        Disables this watchdog.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def finalize(self) -> None: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def isEnabled(self) -> bool:
        """
        Returns the status of the watchdog.
        @return true if the watchdog is armed, false if the watchdog is disarmed
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def enabled(self) -> bool: ...
