import ghidra.app.util.viewer.format
import java.lang


class CodeFormatService(object):
    """
    Service provided by a plugin that gives access to a manager for the field formats used by a
     listing.
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getFormatManager(self) -> ghidra.app.util.viewer.format.FormatManager: ...

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

    @property
    def formatManager(self) -> ghidra.app.util.viewer.format.FormatManager: ...
