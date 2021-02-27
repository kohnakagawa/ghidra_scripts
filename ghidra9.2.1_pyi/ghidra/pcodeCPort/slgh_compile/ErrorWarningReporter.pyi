import ghidra.sleigh.grammar
import java.lang


class ErrorWarningReporter(object):








    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def reportError(self, __a0: ghidra.sleigh.grammar.Location, __a1: unicode) -> None: ...

    def reportWarning(self, __a0: ghidra.sleigh.grammar.Location, __a1: unicode) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
