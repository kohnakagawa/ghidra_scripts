import docking.widgets
import java.lang


class DecompilerCursorPosition(docking.widgets.CursorPosition):








    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getPosition(self) -> int: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setOffset(self, __a0: int) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def offset(self) -> None: ...  # No getter available.

    @offset.setter
    def offset(self, value: int) -> None: ...
