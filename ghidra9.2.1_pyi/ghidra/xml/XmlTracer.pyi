import java.lang
import org.xml.sax


class XmlTracer(object):








    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    def trace(self, locator: org.xml.sax.Locator, traceMessage: unicode, throwableIfAvailable: java.lang.Throwable) -> None:
        """
        The trace callback.  Please be quick.
        @param locator locator, or null if not available (note: locator information may be inaccurate!)
        @param traceMessage the trace message
        @param throwableIfAvailable an exception if we're encountering one (or null)
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
