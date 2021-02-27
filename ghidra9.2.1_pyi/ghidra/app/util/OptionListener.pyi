import ghidra.app.util
import java.lang


class OptionListener(object):
    """
    Notification that an Option changed.
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def optionChanged(self, option: ghidra.app.util.Option) -> None:
        """
        Notification that the given option changed.
        @param option option that changed
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
