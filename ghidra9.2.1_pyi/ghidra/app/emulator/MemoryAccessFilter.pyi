import java.lang


class MemoryAccessFilter(object):




    def __init__(self): ...



    def dispose(self) -> None:
        """
        Dispose this filter which will cause it to be removed from the memory state.
         If overriden, be sure to invoke super.dispose().
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def filterOnExecutionOnly(self) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setFilterOnExecutionOnly(self, filterOnExecutionOnly: bool) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...