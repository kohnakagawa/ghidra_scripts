import ghidra.feature.vt.gui.filters
import java.lang


class FilterChangedListener(object):








    def equals(self, __a0: object) -> bool: ...

    def filterStateChanged(self, __a0: ghidra.feature.vt.gui.filters.FilterState) -> None: ...

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
