import ghidra.app.util.html.diff
import java.lang


class DataTypeDiff(object):








    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getLeftLines(self) -> ghidra.app.util.html.diff.DiffLines: ...

    def getRightLines(self) -> ghidra.app.util.html.diff.DiffLines: ...

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
    def leftLines(self) -> ghidra.app.util.html.diff.DiffLines: ...

    @property
    def rightLines(self) -> ghidra.app.util.html.diff.DiffLines: ...