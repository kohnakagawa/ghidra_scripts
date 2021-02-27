import ghidra.feature.vt.gui.provider.matchtable
import java.lang


class NumberRangeSubFilterChecker(object):








    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def isSubFilterOf(self, __a0: ghidra.feature.vt.gui.provider.matchtable.NumberRangeProducer, __a1: ghidra.feature.vt.gui.provider.matchtable.NumberRangeProducer) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
