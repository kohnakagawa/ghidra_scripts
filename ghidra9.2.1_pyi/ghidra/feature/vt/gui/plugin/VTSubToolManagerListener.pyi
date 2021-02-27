import ghidra.feature.vt.api.main
import java.lang


class VTSubToolManagerListener(object):








    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setSelectedMatch(self, __a0: ghidra.feature.vt.api.main.VTMatch) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def selectedMatch(self) -> None: ...  # No getter available.

    @selectedMatch.setter
    def selectedMatch(self, value: ghidra.feature.vt.api.main.VTMatch) -> None: ...
