import java.lang


class PathHighlighterWorkPauser(object):
    """
    A simple boolean supplier that signals if path highlighting work should not take place
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def isPaused(self) -> bool:
        """
        True if work should not happen; false for normal path highlighting operations
        @return if work should not happen
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
    def paused(self) -> bool: ...
