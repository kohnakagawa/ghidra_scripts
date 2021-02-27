import ghidra.feature.vt.gui.filters
import java.lang


class FilterStatusListener(object):








    def equals(self, __a0: object) -> bool: ...

    def filterStatusChanged(self, __a0: ghidra.feature.vt.gui.filters.Filter.FilterEditingStatus) -> None: ...

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
